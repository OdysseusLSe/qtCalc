# python
#
# This file is part of the qtFractals distribution
# (https://github.com/OdysseusLSe/qtFractals).
# Copyright (c) 2026 Lavrentios Servissoglou.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the Apache 2.0 license as published.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# You should have received a copy of the Apache 2.0 license
# along with this program.
# If not, see <http://www.apache.org/licenses/LICENSE-2.0>.
#

import argparse
import math
import platform
import pprint
import re
import sys
import os

import logging as pylog
import numpy as np
np.set_printoptions(precision=16)

from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QColor, QIcon
from PySide6 import QtWidgets
from PySide6.QtWidgets import QLabel, QListWidgetItem, QMainWindow, QPushButton

from MainWindow_ui import Ui_MainWindow


from MiscHelpers import Percent
from PlotWindow import PlotWindow
from Logging import Logging

import resources_rc

APP_NAME    = "qtCalc"
APP_VERSION = "1.1"
APP_L_ICON  = ""
APP_M_ICON  = ":/ui/icon.icns"
APP_W_ICON  = ":/ui/icon.ico"
APP_L_ICON  = ""
OS_NAME     = platform.system()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, path_2_icon):
        super().__init__()
        self.setupUi(self)
        self.log = Logging("MainWindow")

        self.setWindowTitle(f"{APP_NAME} {APP_VERSION}")

        self.log.write(f"--- {APP_NAME} {APP_VERSION} ---")
        self.log.entry(f"__init__({path_2_icon})")

        self.status_lbl = QLabel("Ready")
        self.status_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_bar.addWidget(self.status_lbl, 1)

        try:
            self.setWindowIcon(QIcon(path_2_icon))
        except Exception:
            self.status_lbl.setText("Cannot load window icon!")
            self.log.warning("Cannot load window icon!")

        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        all_buttons = self.findChildren(QPushButton)
        for button in all_buttons:
            if button != self.btn_RAD and button != self.btn_DEG:
                button.clicked.connect(self.on_button_clicked)

        self.advanced_operator()
        self.button_mapping()

        self.expression_line.setFocus()

        self.history_list.model().rowsInserted.connect(
            self.history_list.scrollToBottom
        )
        self.history_list.itemDoubleClicked.connect(self.on_item_double_clicked)

        self.history_item = 0
        self.memory_index = -1
        self.tokens       = []
        self.is_2nd       = False
        self.result       = None

        self.RAD = True
        self.btn_RAD.setStyleSheet("""
            background-color: lightgrey;
            color: green;
            border: 1 solid;
            padding: 3;
            """)
        self.btn_RAD.clicked.connect(self.toggle_deg_rad)

        self.DEG = False
        self.btn_DEG.setStyleSheet("""
            background-color: lightgrey;
            color: salmon;
            border: 1 solid;
            padding: 3;
            """)
        self.btn_DEG.clicked.connect(self.toggle_deg_rad)

        self.setStyleSheet("""
            QMainWindow#MainWindow {
                border-image: url(:/ui/aluminum.jpg) 0 0 0 0 stretch stretch;
            }
            """)

        # For 2D plots (see method 'plot_expression')
        self.curve = False

        # For 3D plots (see method 'plot_expression')
        self.surface = False

        self.expression_line.setFocus()

        self.log.exit("__init__")

    #
    # -----------------------------------------------
    #

    def advanced_operator(self):
        self.log.entry("advanced_operator()")

        # Operators with their precedence and associativity
        self.infix_operators = {
            '+'  : (1, True),
            '-'  : (1, True),
            '*'  : (2, True),
            '/'  : (2, True),
            '^'  : (3, False)
        }

        self.postfix_operators = {'%', '!', 'b', 'h'}

        # Functions with their corresponding implementations and # of arguments
        self.functions = {
            'abs'   : (math.fabs, 1),
            'acos'  : (math.acos, 1),
            'acosh' : (math.acosh, 1),
            'AND'   : (self.bitwise_and, 2),
            'asin'  : (math.asin, 1),
            'asinh' : (math.asinh, 1),
            'atan'  : (math.atan, 1),
            'atanh' : (math.atanh, 1),
            'bin'   : (self.dec_2_bin, 1),
            'cos'   : (math.cos, 1),
            'cosh'  : (math.cosh, 1),
            'erf'   : (math.erf, 1),
            'exp'   : (math.exp, 1),
            'gamma' : (math.gamma, 1),
            'lg2'   : (math.log2, 1),
            'ln'    : (math.log, 1),
            'log'   : (math.log10, 1),
            'LShift': (self.bitwise_lshift, 2),
            'max'   : (math.fmax, 2),
            'min'   : (math.fmin, 2),
            'mod'   : (math.fmod, 2),
            'NOT'   : (self.bitwise_not, 1),
            'OR'    : (self.bitwise_or, 2),
            'RShift': (self.bitwise_rshift, 2),
            'sin'   : (math.sin, 1),
            'sinh'  : (math.sinh, 1),
            'sqrt'  : (math.sqrt, 1),
            'sqrt3' : (math.cbrt, 1),
            'tan'   : (math.tan, 1),
            'tanh'  : (math.tanh, 1),
            'XOR'   : (self.bitwise_xor, 2),
            'YrootX': (self.yth_root_of_x, 2)
        }

        self.trig_functions = [
            'acos',
            'acosh',
            'asin',
            'asinh',
            'atan',
            'atanh',
            'cos',
            'cosh',
            'sin',
            'sinh',
            'tan',
            'tanh'
        ]

        self.powers         = ['^2', '^3']

        # Predefined constants
        self.variables = {
            'pi' : math.pi,
            'e'  : math.e,
            'x'  : 'x',
            'y'  : 'y',
        }

        self.log.exit("advanced_operator")

    #
    # -----------------------------------------------
    #

    def bitwise_and(self, a, b):
        self.log.entry(f"bitwise_and({a},{b})")

        a_fractional, a_integer = math.modf(a)
        b_fractional, b_integer = math.modf(b)

        if a_fractional == 0.0 and b_fractional == 0.0:
            self.log.exit("bitwise_and")
            return (int(a_integer) & int(b_integer))

        self.log.exit("bitwise_and")
        raise ValueError("Bitwise AND requires integers, got float(s)!")

    #
    # -----------------------------------------------
    #

    def bitwise_lshift(self, a, b):
        self.log.entry(f"bitwise_LShift({a},{b})")

        a_fractional, a_integer = math.modf(a)
        b_fractional, b_integer = math.modf(b)

        if a_fractional != 0.0 or b_fractional != 0.0:
            self.log.exit("bitwise_lshift")
            raise ValueError("Bitwise '<<' requires integers, got float(s)!")

        if b_integer <= 0.0:
            self.log.exit("bitwise_lshift")
            raise_str = "Bitwise '<<' requires positive value as 2nd argument!"
            raise ValueError(raise_str)

        self.log.exit("bitwise_lshift")
        return (int(a_integer)<< int(b_integer))

    #
    # -----------------------------------------------
    #

    def bitwise_not(self, a):
        self.log.entry(f"bitwise_not({a})")

        fractional, integer = math.modf(a)

        if fractional == 0.0:
            self.log.exit("bitwise_not")
            return (~int(integer))

        self.log.exit("bitwise_not")
        raise ValueError("Bitwise NOT requires an integer, got a float!")

    #
    # -----------------------------------------------
    #

    def bitwise_or(self, a, b):
        self.log.entry(f"bitwise_or({a},{b})")

        a_fractional, a_integer = math.modf(a)
        b_fractional, b_integer = math.modf(b)

        if a_fractional == 0.0 and b_fractional == 0.0:
            self.log.exit("bitwise_or")
            return (int(a_integer) | int(b_integer))

        self.log.exit("bitwise_or")
        raise ValueError("Bitwise OR requires integers, got float(s)!")

    #
    # -----------------------------------------------
    #

    def bitwise_rshift(self, a, b):
        self.log.entry(f"bitwise_LShift({a},{b})")

        a_fractional, a_integer = math.modf(a)
        b_fractional, b_integer = math.modf(b)

        if a_fractional != 0.0 or b_fractional != 0.0:
            self.log.exit("bitwise_rshift")
            raise ValueError("Bitwise '>>' requires integers, got float(s)!")

        if b_integer <= 0.0:
            self.log.exit("bitwise_rshift")
            raise_str = "Bitwise '>>' requires positive value as 2nd argument!"
            raise ValueError(raise_str)

        self.log.exit("bitwise_rshift")
        return (int(a_integer) >> int(b_integer))

    #
    # -----------------------------------------------
    #

    def bitwise_xor(self, a, b):
        self.log.entry(f"bitwise_xor({a},{b})")

        a_fractional, a_integer = math.modf(a)
        b_fractional, b_integer = math.modf(b)

        if a_fractional == 0.0 and b_fractional == 0.0:
            self.log.exit("bitwise_or")
            return (int(a_integer) ^ int(b_integer))

        self.log.exit("bitwise_xor")
        raise ValueError("Bitwise XOR requires integers, got float(s)!")

    #
    # -----------------------------------------------
    #

    def button_mapping(self):
        self.log.entry("button_mapping()")

        self.buttons = {
            "btn_0"             : "0",
            "btn_1"             : "1",
            "btn_2"             : "2",
            "btn_3"             : "3",
            "btn_4"             : "4",
            "btn_5"             : "5",
            "btn_6"             : "6",
            "btn_7"             : "7",
            "btn_8"             : "8",
            "btn_9"             : "9",
            "btn_10powerX"      : "10^(",
            "btn_abs"           : "abs(",
            "btn_acos"          : "acos(",
            "btn_acosh"         : "acosh(",
            "btn_AND"           : "AND(",
            "btn_asin"          : "asin(",
            "btn_asinh"         : "asinh(",
            "btn_atan"          : "atan(",
            "btn_atanh"         : "atanh(",
            "btn_bin"           : "bin(",
            "btn_bracket_left"  : "(",
            "btn_bracket_right" : ")",
            "btn_cbrt"          : "sqrt3(",
            "btn_clear"         : "C",
            "btn_comma"         : ",",
            "btn_cos"           : "cos(",
            "btn_cosh"          : "cosh(",
            "btn_cube"          : "^3",
            "btn_divide"        : "/",
            "btn_dot"           : ".",
            "btn_e"             : "e",
            "btn_equal"         : "=",
            "btn_erf"           : "erf(",
            "btn_fac"           : "!",
            "btn_gamma"         : "gamma(",
            "btn_hex"           : "hex(",
            "btn_is_bin"        : "b",
            "btn_lg2"           : "lg2(",
            "btn_ln"            : "ln(",
            "btn_log"           : "log(",
            "btn_LShift"        : "LShift(",
            "btn_max"           : "max(",
            "btn_min"           : "min(",
            "btn_minus"         : "-",
            "btn_mod"           : "mod(",
            "btn_multiply"      : "*",
            "btn_NOT"           : "NOT(",
            "btn_OR"            : "OR(",
            "btn_percent"       : "%",
            "btn_pi"            : "pi",
            "btn_plus"          : "+",
            "btn_RShift"        : "RShift(",
            "btn_unary_minus"   : "-",
            "btn_sin"           : "sin(",
            "btn_sinh"          : "sinh(",
            "btn_sqrt"          : "sqrt(",
            "btn_square"        : "^2",
            "btn_tan"           : "tan(",
            "btn_tanh"          : "tanh(",
            "btn_unary_minus"   : "-",
            "btn_x"             : "x",
            "btn_XOR"           : "XOR(",
            "btn_XpowerY"       : "^",
            "btn_y"             : "y",
            "btn_YrootX"        : "YrootX("
        }

        self.log.entry("button_mapping()")

    #
    # -----------------------------------------------
    #

    def dec_2_bin(self, value):
        self.log.entry(f"dec_2_bin({value})")

        int_value = int(value)
        raw_binary_string = str(bin(int_value))
        pos = raw_binary_string.lower().find("b") + 1
        binary_string = raw_binary_string[pos:] + "b"

        self.log.exit("dec_2_bin")
        return binary_string

    #
    # -----------------------------------------------
    #

    def evaluate_curve(self, expression, x_start, x_end, x_steps):
        log_str = f"evaluate_curve(expression='{expression}',"
        log_str += f"x_start={x_start},x_end={x_end},x_steps={x_steps})"
        self.log.entry(log_str)

        X = np.linspace(x_start, x_end, x_steps)
        raw_Y = []
        connections = []

        self.log.write(f"X=\n{pprint.pformat(X)}")

        for step, x in enumerate(X):
            y = self.evaluate_expression(expression, x=x)
            if y is None:
                self.log.error(f"x,y={x},{y}")
                raw_Y.append(0.0)
                connections.append(False)
            else:
                raw_Y.append(float(y))
                connections.append(True)
            self.log.write(f"x,y,connections[{step}]={x},{y},{connections[step]}")
        self.log.write(f"raw_Y=\n{pprint.pformat(raw_Y)}")

        Y = np.array(raw_Y, dtype=float)
        self.log.write(f"Y=\n{pprint.pformat(Y)}")

        self.plot_2d.plot_curve(X, Y, connections)

        self.log.exit("evaluate_curve")

    #
    # -----------------------------------------------
    # Handle the calculation when the "=" button is pressed
    # -----------------------------------------------
    #

    def evaluate_expression(self, expression, x=None, y=None):
        self.log.entry(f"evaluate_expression('{expression}',x={x},y={y})")

        if x is not None:
            self.variables['x'] = x
            self.log.write(f"self.variables['x']={self.variables['x']}")
        if y is not None:
            self.variables['y'] = y
            self.log.write(f"self.variables['y']={self.variables['y']}")

        try:

            token_spec = r'\d+(?:\.\d+)?(?:[eE][+-]?\d+)?|[a-zA-Z_]\w*|[\+\-\*\/\^\!\%\(\)bh,]'
            raw_tokens = re.findall(token_spec, expression)
            self.log.write(f"raw_tokens={pprint.pformat(raw_tokens)}")

            #
            # Implement implicit multiplication
            #

            num_regex = re.compile(r'^\d+(?:\.\d+)?(?:[eE][+-]?\d+)?$')

            def is_value_end(tok):
                return bool(num_regex.match(tok)) or tok in self.variables or tok == ')'

            def is_value_start(tok):
                return (
                    bool(num_regex.match(tok))
                    or tok in self.variables
                    or tok in self.functions
                    or tok == '('
                )

            tokens = []
            for i, tok in enumerate(raw_tokens):
                if i > 0 and is_value_end(raw_tokens[i - 1]) and is_value_start(tok):
                    tokens.append('*')
                tokens.append(tok)
            self.log.write(f"tokens={pprint.pformat(tokens)}")

            # Implement unary minus
            processed_tokens = []
            for i, tok in enumerate(tokens):
                if tok == '-' and (i == 0 or tokens[i-1] in self.infix_operators or tokens[i-1] in ('(', ',')):
                    processed_tokens.append('0')
                processed_tokens.append(tok)
            self.log.write(f"processed_tokens={pprint.pformat(processed_tokens)}")

            shunting_yard_output = self.shunting_yard(processed_tokens)
            self.log.write(f"shunting_yard_output={pprint.pformat(shunting_yard_output)}")

            raw_result = self.evaluate_rpn(shunting_yard_output)
            self.log.write(f"raw_result={raw_result}")

            if isinstance(raw_result, str):
                if 'b' in raw_result:
                    self.result = raw_result
                    self.log.write("Result is a binary number.")
            else:
                cleaned = float(f"{raw_result:.16g}")
                if cleaned.is_integer() and abs(cleaned) < 1e15:
                    self.result = int(cleaned)
                else:
                    self.result = cleaned
            self.log.write(f"self.result={self.result}")

            if x is None and y is None:

                self.expression_to_history(expression, "=")

                # Show result of expression
                expression = f"{self.result}"
                self.status_lbl.setText("Ready")
                self.expression_line.setText(expression)
                self.log.write(f"expression={expression}")

        except ZeroDivisionError:
            error_log = f"{expression} -> Error: Division by zero!"
            self.expression_to_history(error_log, "Error")

        except IndexError:
            error_log = f"{expression} -> Error: Insufficient operands or parentheses!"
            self.expression_to_history(error_log, "Error")

        except Exception as e:
            error_log = f"{expression} -> Error: {str(e)}"
            self.expression_to_history(error_log, "Error")

        self.log.exit("evaluate_expression")
        if self.result is None:
            return
        return self.result

    #
    # -----------------------------------------------
    #

    def evaluate_rpn(self, postfix_tokens):
        self.log.entry(f"evaluate_rpn({pprint.pformat(postfix_tokens)})")

        stack = []

        for token in postfix_tokens:

            if isinstance(token, (int, float)):

                stack.append(token)

            elif token in self.postfix_operators:

                # '%', '!', 'b', 'h'
                if len(stack) < 1:
                    raise IndexError("To few operands for operator!")
                a = stack.pop()
                if token == '%':
                    stack.append(Percent(a))
                elif token == '!':
                    stack.append(self.fac(a))
                elif token == 'b':
                    a_string = str(int(a))
                    stack.append(int(a_string, 2))

            elif token in self.infix_operators:

                # '+', '-', '*', '/', '^'

                if len(stack) < 2:
                    raise IndexError("To few operands for operator!")

                b = stack.pop()
                a = stack.pop()

                if isinstance(a, Percent):
                    a = a.value / 100.0

                if isinstance(b, Percent):
                    if token == '+':
                        # 100 + 10% -> 100 + (100 * 0.10) = 110
                        stack.append(a + (a * (b.value / 100.0)))
                    elif token == '-':
                        # 100 - 10% -> 100 - (100 * 0.10) = 90
                        stack.append(a - (a * (b.value / 100.0)))
                    elif token == '*':
                        # 100 * 10% -> 100 * 0.10 = 10
                        stack.append(a * (b.value / 100.0))
                    elif token == '/':
                        # 100 / 10% -> 100 / 0.10 = 1000
                        stack.append(a / (b.value / 100.0))

                else:

                    if token == '+':
                        stack.append(a + b)
                    elif token == '-':
                        stack.append(a - b)
                    elif token == '*':
                        stack.append(a * b)
                    elif token == '/':
                        stack.append(a / b)
                    elif token == '^':
                        stack.append(a ** b)

            elif token in self.functions:

                func, num_args = self.functions[token]

                if len(stack) < num_args:
                    raise IndexError(f"Too few operands for function {token}!")

                if num_args == 1:
                    a = stack.pop()
                    self.log.write(f"token(a)={token}({a})")
                    if token in self.trig_functions and self.DEG:
                        # Trigonometric functions need radians values
                        a = math.radians(a)
                        self.log.write(f"token(a)={token}({a})")
                    stack.append(func(a))
                elif num_args == 2:
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(func(a, b))

            self.log.write(f"stack={pprint.pformat(stack)})")

        # Check for lonesome percentage value at the beginning
        result = stack[0]
        self.log.exit("evaluate_rpn")
        return result.value / 100.0 if isinstance(result, Percent) else result

    #
    # -----------------------------------------------
    #

    def evaluate_surface(
            self,
            expression,
            x_start, x_end, x_steps,
            y_start, y_end, y_steps
        ):
        log_str = f"evaluate_surface({expression},"
        log_str += f"{x_start},{x_end},{x_steps},"
        log_str += f"{y_start},{y_end},{y_steps})"
        self.log.entry(log_str)

        x = np.linspace(x_start, x_end, x_steps)
        self.log.write(f"x=\n{pprint.pformat(x)}")

        y = np.linspace(y_start, y_end, y_steps)
        self.log.write(f"y=\n{pprint.pformat(y)}")

        X, Y = np.meshgrid(x, y)
        self.log.write(f"X=\n{pprint.pformat(X)}")
        self.log.write(f"Y=\n{pprint.pformat(Y)}")

        Z = np.zeros((len(X), len(Y)))
        for ix in range(len(X)):
            for iy in range(len(Y)):
                x_val = float(x[ix])  # NumPy float to Python float!
                y_val = float(y[iy])  # NumPy float to Python float!
                Z[ix, iy] = self.evaluate_expression(expression, x=x_val, y=y_val)
                self.log.write(f"x,y,z={x_val},{y_val},{Z[ix, iy]}")
        self.log.write(f"Z=\n{pprint.pformat(Z)}")

        self.plot_3d.plot_surface(X, Y, Z)

        self.log.exit("evaluate_surface")

    #
    # -----------------------------------------------
    # Add current expression to history list
    # -----------------------------------------------
    #

    def expression_to_history(self, history_text, appendix):
        self.log.entry(f"expression_to_history({history_text},{appendix})")

        if appendix == "Error":
            self.status_lbl.setText(history_text)
            self.log.error(history_text)
            if self.variables['x'] == 'x' or self.variables['y'] == 'y':
                item = QListWidgetItem(history_text)
                item.setBackground(QBrush(QColor("red")))
                item.setForeground(QColor("white"))
                self.history_list.addItem(item)
                self.history_item += 1
                self.expression_line.setText("")
                self.log.write("Errorneous expression stored in history.")
            self.log.exit("expression_to_history")
            return

        if appendix == "=":
            history_text += f"={self.result}"
            self.log.write("Expression and result stored in history.")
        else:
            history_text += "=Plot"
            self.log.write("Expression and plot hint stored in history.")
        final_history_text = re.sub(r'(.{78})', r'\1' + '\n', history_text)
        item = QListWidgetItem(final_history_text)
        self.log.write(f"final_history_text={final_history_text}")

        if self.history_item % 2 == 0:
            item.setBackground(QColor("white"))
            item.setForeground(QColor(94, 94, 94))
            self.log.write("Color of history line = 'white'.")
        else:
            item.setBackground(QColor(94, 94, 94))
            item.setForeground(QColor("white"))
            self.log.write("Color of history line = '94,94,94'.")
        self.history_list.addItem(item)
        self.history_item += 1

        self.log.exit("expression_to_history")

    #
    # -----------------------------------------------
    #

    def fac(self, number):
        self.log.entry(f"fac({number})")

        if number < 0:
            self.log.exit("fac")
            raise ValueError("Factorial is not defined for negative numbers!")

        fractional, integer = math.modf(number)

        if fractional == 0.0:
            self.log.exit("fac")
            return math.integer.factorial(int(integer))

        self.log.exit("fac")
        raise ValueError("Factorial requires an integer, got a float!")

    #
    # -----------------------------------------------
    # Handle the input validation
    # -----------------------------------------------
    #

    def is_input_valid(self, new_char):
        self.log.entry(f"is_input_valid('{new_char}')")

        self.status_lbl.setText(f"Validating input '{new_char}'")

        expression = self.expression_line.text()
        last_char = expression[-1] if expression else ""

        infix_list   = list(self.infix_operators.keys())
        postfix_list = list(self.postfix_operators)

        def reject(reason):
            msg = f"Validation is blocking: {reason}"
            self.status_lbl.setText(msg)
            self.log.warning(msg)
            self.log.exit("is_input_valid")
            return False

        if new_char == "=":

            if not expression:
                return reject("Empty expression!")
            if last_char in infix_list or last_char in ("(", ","):
                return reject(f"Expression cannot end with '{last_char}'!")
            if expression.count("(") != expression.count(")"):
                return reject("Unclosed parentheses!")

        else:

            if not expression:
                if (
                    new_char in self.powers
                    or new_char in postfix_list
                    or new_char in (")", ",")
                ):
                    return reject(f"Invalid start token: {new_char}!")
                if new_char in infix_list and new_char != "-":
                    return reject(f"Operator at start: {new_char}!")

            elif last_char in infix_list:
                if (
                    new_char in infix_list
                    or new_char in self.powers
                    or new_char in postfix_list
                ):
                    return reject(f"Invalid operator sequence: {last_char}{new_char}!")
                if new_char in (")", ","):
                    return reject(f"'{new_char}' after operator: {last_char}!")

            elif last_char in ("(", ","):
                if (
                    new_char in self.powers
                    or new_char in postfix_list
                    or new_char in (")", ",")
                ):
                    return reject(f"Invalid token '{new_char}' after '{last_char}'!")
                if new_char in infix_list and new_char != "-":
                    return reject(f"Operator after '{last_char}': {new_char}!")

            elif last_char == ".":
                if (
                    new_char in postfix_list
                    or new_char in infix_list
                    or new_char in self.powers
                ):
                    return reject(f"Invalid token '{new_char}' after decimal point!")

            elif last_char in postfix_list:
                if new_char in postfix_list:
                    return reject(f"Double postfix operator: {last_char}{new_char}!")
                if (
                    new_char.isdigit()
                    or new_char in (".", "(")
                    or new_char in self.variables
                ):
                    return reject(f"Missing operator between '{last_char}' and '{new_char}'!")

            if new_char == ")":
                if expression.count(")") >= expression.count("("):
                    return reject("Too many closing parentheses!")

            if new_char == ".":
                if (
                    last_char == ")"
                    or expression.endswith(tuple(self.variables.keys()))
                ):
                    return reject("Decimal point cannot follow a constant or closing parenthesis!")
                current_number = re.search(r"[\d.]+$", expression)
                if current_number and "." in current_number.group():
                    return reject("Multiple decimal points in one number!")

        self.log.exit("is_input_valid")
        return True

    #
    # -----------------------------------------------
    # Handle special buttons like clear, memory functions, cursor, etc.
    # -----------------------------------------------

    def is_special_button(self, button_name):
        self.log.entry(f"is_special_button(button_name='{button_name}')")

        self.status_lbl.setText("Checking for special button")

        if button_name == "btn_clear":
            self.log.write("Clear current expression and reset the display.")
            self.expression_line.setText("")
            value = True

        elif button_name == "btn_del":
            cursor_pos = self.expression_line.cursorPosition()
            old_text   = self.expression_line.text()
            new_text   = old_text[:cursor_pos-1] + old_text[cursor_pos:]
            self.expression_line.setText(new_text)
            self.expression_line.setCursorPosition(cursor_pos-1)
            value = True

        elif button_name == "btn_Mplus":
            self.log.write("Add current result to memory.")
            if hasattr(self, 'result') and self.result is not None:
                self.memory_list.addItem(f"{self.result}")
                self.memory_index += 1
                self.memory_list.setCurrentIndex(self.memory_index)
            value = True

        elif button_name == "btn_MC":
            self.log.write("Clear the memory.")
            self.memory_list.clear()
            self.memory_index = -1
            value = True

        elif button_name == "btn_MR":
            # Recall value from memory and
            # build it into the current expression
            self.log.write("Recall value from memory.")
            if self.memory_list.currentText() != "":
                mem_value = self.memory_list.currentText()
                cursor_pos = self.expression_line.cursorPosition()
                old_text = self.expression_line.text()
                new_text = old_text[:cursor_pos] + mem_value + old_text[cursor_pos:]
                self.expression_line.setText(new_text)
                self.expression_line.setCursorPosition(cursor_pos + len(mem_value))
            value = True

        elif button_name == "btn_left":
            self.expression_line.cursorBackward(False)
            value = True

        elif button_name == "btn_right":
            self.expression_line.cursorForward(False)
            value = True

        elif button_name == "btn_plot":
            self.plot_expression()
            value = True

        elif button_name == "btn_2nd":
            self.toggle_the_2nd()
            value = True

        else:
            value = False

        self.log.write(f"value={value}")

        self.log.exit("is_special_button")
        return value

    #
    # -----------------------------------------------
    #

    def keyPressEvent(self, event):
        self.log.entry("keyPressEvent({event})")

        key_text = event.text()
        self.log.write(f"event.text()='{event.text()}'")
        self.log.write(f"event.key()='{event.key()}'")
        self.log.write(f"Native='{event.nativeVirtualKey()}'")

        matched_btn_name = None

        if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter, Qt.Key.Key_Equal):

            self.log.write(f"Qt.Key={event.key()}")

            if self.history_list.hasFocus():

                # Item in history list selected and triggered to include it in
                # current expression.
                current_item = self.history_list.currentItem()
                self.log.write(f"current_item={current_item}")
                self.on_item_double_clicked(current_item)
                self.log.exit("keyPressEvent")
                return

            else:

                matched_btn_name = "btn_equal"
                self.log.write(f"(Qt.Key)matched_btn_name={matched_btn_name}")

                expression = self.expression_line.text()
                if "x" in expression:
                    # At least one unknown variable --> 2D/3D-plot
                    self.plot_expression()
                else:
                    self.evaluate_expression(expression)
                self.log.exit("keyPressEvent")
                return

        elif key_text:
            for button_name, character in self.buttons.items():
                if key_text == character:
                    matched_btn_name = button_name
                    break

        self.log.write(f"matched_btn_name={matched_btn_name}")
        if matched_btn_name:
            button_object = getattr(self, matched_btn_name, None)
            if button_object:
                button_object.click()
                self.log.write(f"matched_btn_name={matched_btn_name}")
                event.accept()
                self.log.exit("keyPressEvent")
                return

        super().keyPressEvent(event)

        self.log.exit("keyPressEvent")

    #
    # -----------------------------------------------
    #

    def on_button_clicked(self):
        self.log.entry("on_button_clicked()")

        button = self.sender()
        button_name = button.objectName()
        self.log.write(f"button_name='{button_name}'")
        if self.is_special_button(button_name):
            self.log.write(f"is_special_button({button_name})=True")
            self.log.exit("on_button_clicked")
            return

        new_char = self.buttons[button_name]
        self.log.write(f"new_char='{new_char}'")
        if not self.is_input_valid(new_char):
            self.log.warning(f"is_input_valid({new_char})=False")
            self.log.exit("on_button_clicked")
            return

        self.update_expression(new_char)

        if new_char == "=":
            self.result = None
            expression = self.expression_line.text()
            if "x" in expression:
                self.log.write("At least one unknown variable --> 2D/3D-plot")
                self.plot_expression()
            else:
                self.log.write("Trigger evaluation of expression.")
                self.evaluate_expression(expression)

        self.log.exit("on_button_clicked")

    #
    # -----------------------------------------------
    #

    def on_item_double_clicked(self, item):
        self.log.entry("on_item_double_clicked(item)")
        self.log.write(f"item.text()={item.text()}")

        if "=" in item.text():
            # Copy text just before "=" and attach it to the current expression.
            insert_text = item.text().split("=", 1)[0]
            self.log.write(f"insert_text={insert_text}")
        else:
            # Errorneous expression will be ignored.
            self.status_lbl.setText("Errorneous expression ignored!")
            self.log.write("Errorneous expression ignored!")
            self.log.exit("on_item_double_clicked")
            return

        cursor_pos = self.expression_line.cursorPosition()
        old_text   = self.expression_line.text()
        new_text   = old_text[:cursor_pos] + insert_text + old_text[cursor_pos:]
        self.log.write(f"cursor_pos={cursor_pos}")
        self.log.write(f"old_text={old_text}")
        self.log.write(f"new_text={new_text}")

        self.expression_line.setText(new_text)
        self.expression_line.setCursorPosition(cursor_pos + len(insert_text))

        self.log.exit("on_item_double_clicked")

    #
    # -----------------------------------------------
    #

    def plot_expression(self):
        self.log.entry("plot_expression()")

        self.curve   = False
        self.surface = False

        # Check if at least variable 'x' exists.
        expression  = self.expression_line.text()
        if "x" not in expression:
            self.status_lbl.setText("Missing primary variable 'x'")
            self.log.warning("Missing primary variable 'x'!")
            self.log.exit("plot_expression")
            return

        # Use '=' as equivalent to 'Plot' button.
        new_char = "="
        if not self.is_input_valid(new_char):
            self.status_lbl.setText("Expression is not valid!")
            self.log.warning("is_input_valid(=)=False")
            self.log.exit("plot_expression")
            return

        if "x" in expression and "y" in expression:
            self.surface = True
            self.log.write(f"self.surface={self.surface}")
            if not hasattr(self, 'plot_3d'):
                # Start new window to draw the expression: 3D
                self.log.write("Start new window to draw the expression: 3D")
                self.plot_3d = PlotWindow(expression, self.curve, self.surface)
                self.plot_3d.eval_curve.connect(self.evaluate_curve)
                self.plot_3d.eval_surface.connect(self.evaluate_surface)
                self.plot_3d.show()
            elif self.plot_3d is not None:
                if not self.plot_3d.isVisible():
                    self.plot_3d.show()
                else:
                    self.plot_3d.raise_()
                self.plot_3d.activateWindow()
                self.plot_3d.add_plot(expression)
            else:
                self.status_lbl.setText("Internal error: plotting not available!")
                self.log.error("Internal error: plotting not available!")
        else:
            self.curve = True
            self.log.write(f"self.curve={self.curve}")
            if not hasattr(self, 'plot_2d'):
                # Start new window to draw the expression: 2D
                self.log.write("Start new window to draw the expression: 2D")
                self.plot_2d = PlotWindow(expression, self.curve, self.surface)
                self.plot_2d.eval_curve.connect(self.evaluate_curve)
                self.plot_2d.eval_surface.connect(self.evaluate_surface)
                self.plot_2d.show()
            elif self.plot_2d is not None:
                if not self.plot_2d.isVisible():
                    self.plot_2d.show()
                else:
                    self.plot_2d.raise_()
                self.plot_2d.activateWindow()
                self.plot_2d.add_plot(expression)
            else:
                self.status_lbl.setText("Internal error: plotting not available!")
                self.log.error("Internal error: plotting not available!")

        self.expression_to_history(expression, "Plot")

        self.log.exit("plot_expression")

    #
    # -----------------------------------------------
    #

    def shunting_yard(self, tokens):
        self.log.entry(f"shunting_yard(tokens={pprint.pformat(tokens)})")

        output = []
        operator = []

        for token in tokens:
            if re.match(r'^\d+(?:\.\d+)?(?:[eE][+-]?\d+)?$', token):
                # Token is a number, convert it to float
                output.append(float(token))

            elif token in self.variables:
                # Token is a predefined constant or variable
                output.append(self.variables[token])

            elif token in self.functions:
                # Token is a function, push it onto the operator stack
                operator.append(token)

            elif token == ',':
                # Token is a comma, used to separate arguments in functions
                while operator and operator[-1] != '(':
                    output.append(operator.pop())

            elif token in self.infix_operators:
                # Token is an operator
                p1, a1 = self.infix_operators[token]
                while operator and operator[-1] in self.infix_operators:
                    p2, _ = self.infix_operators[operator[-1]]
                    if (a1 and p1 <= p2) or (not a1 and p1 < p2):
                        output.append(operator.pop())
                    else:
                        break
                operator.append(token)

            elif token in self.postfix_operators:
                output.append(token)

            elif token == '(':
                # Token is an opening parenthesis
                operator.append(token)

            elif token == ')':
                # Token is a closing parenthesis
                while operator and operator[-1] != '(':
                    output.append(operator.pop())
                if operator and operator[-1] == '(':
                    operator.pop()
                if operator and operator[-1] in self.functions:
                    output.append(operator.pop())

            self.log.write(f"operator={pprint.pformat(operator)})")
            self.log.write(f"output={pprint.pformat(output)})")

        while operator:
            output.append(operator.pop())
            self.log.write(f"output={pprint.pformat(output)})")

        self.log.exit("shunting_yard")
        return output

    #
    # -----------------------------------------------
    #

    def toggle_deg_rad(self):
        self.log.entry("deg_rad_toggle")

        button = self.sender()
        button_name = button.objectName()

        if button_name == "btn_DEG" and not self.DEG:
            self.log.write("Switch to degree.")
            self.DEG = True
            self.btn_DEG.setStyleSheet("""
                background-color: lightgrey;
                color: green;
                border: 1 solid;
                padding: 3;
                """)
            self.RAD = False
            self.btn_RAD.setStyleSheet("""
                background-color: lightgrey;
                color: salmon;
                border: 1 solid;
                padding: 3;
                """)

        if button_name == "btn_RAD" and not self.RAD:
            self.log.write("Switch to radiant.")
            self.RAD = True
            self.btn_RAD.setStyleSheet("""
                background-color: lightgrey;
                color: green;
                border: 1 solid;
                padding: 3;
                """)
            self.DEG = False
            self.btn_DEG.setStyleSheet("""
                background-color: lightgrey;
                color: salmon;
                border: 1 solid;
                padding: 3;
                """)

        self.log.exit("deg_rad_toggle")

    #
    # -----------------------------------------------
    #

    def toggle_the_2nd(self):
        self.log.entry("toggle_the_2nd()")

        if self.is_2nd:

            self.is_2nd = False

            self.btn_2nd.setStyleSheet("""
                QPushButton {
                    color: white;
                    background-color: rgb(66, 66, 66);
                    }
                """)

            self.btn_10powerX.setObjectName("btn_10powerX")
            self.btn_10powerX.setText("10ˣ")

            self.btn_cbrt.setObjectName("btn_cbrt")
            self.btn_cbrt.setText("∛")

            self.btn_cos.setObjectName("btn_cos")
            self.btn_cos.setText("cos")

            self.btn_cosh.setObjectName("btn_cosh")
            self.btn_cosh.setText("cosh")

            self.btn_cube.setObjectName("btn_cube")
            self.btn_cube.setText("x³")

            self.btn_lg2.setObjectName("btn_lg2")
            self.btn_lg2.setText("lg2")

            self.btn_ln.setObjectName("btn_ln")
            self.btn_ln.setText("ln")

            self.btn_log.setObjectName("btn_log")
            self.btn_log.setText("log")

            self.btn_max.setObjectName("btn_max")
            self.btn_max.setText("max")

            self.btn_min.setObjectName("btn_min")
            self.btn_min.setText("min")

            self.btn_sin.setObjectName("btn_sin")
            self.btn_sin.setText("sin")

            self.btn_sinh.setObjectName("btn_sinh")
            self.btn_sinh.setText("sinh")

            self.btn_sqrt.setObjectName("btn_sqrt")
            self.btn_sqrt.setText("√")

            self.btn_YrootX.setObjectName("btn_YrootX")
            self.btn_YrootX.setText("ʸ√x")

            self.btn_square.setObjectName("btn_square")
            self.btn_square.setText("x²")

            self.btn_tan.setObjectName("btn_tan")
            self.btn_tan.setText("tan")

            self.btn_tanh.setObjectName("btn_tanh")
            self.btn_tanh.setText("tanh")

            self.btn_XpowerY.setObjectName("btn_XpowerY")
            self.btn_XpowerY.setText("xʸ")

        else:

            self.is_2nd = True

            self.btn_2nd.setStyleSheet("""
                QPushButton {
                    color: white;
                    background-color: green;
                    }
                """)

            self.btn_10powerX.setObjectName("btn_percent")
            self.btn_10powerX.setText("%")

            self.btn_cbrt.setObjectName("btn_OR")
            self.btn_cbrt.setText("OR")

            self.btn_cos.setObjectName("btn_acos")
            self.btn_cos.setText("acos")

            self.btn_cosh.setObjectName("btn_acosh")
            self.btn_cosh.setText("acosh")

            self.btn_cube.setObjectName("btn_LShift")
            self.btn_cube.setText("<<")

            self.btn_lg2.setObjectName("btn_bin")
            self.btn_lg2.setText("bin")

            self.btn_ln.setObjectName("btn_is_bin")
            self.btn_ln.setText("is bin")

            self.btn_log.setObjectName("btn_fac")
            self.btn_log.setText("n!")

            self.btn_max.setObjectName("btn_gamma")
            self.btn_max.setText("Γ")

            self.btn_min.setObjectName("btn_erf")
            self.btn_min.setText("erf")

            self.btn_sin.setObjectName("btn_asin")
            self.btn_sin.setText("asin")

            self.btn_sinh.setObjectName("btn_asinh")
            self.btn_sinh.setText("asinh")

            self.btn_sqrt.setObjectName("btn_AND")
            self.btn_sqrt.setText("AND")

            self.btn_YrootX.setObjectName("btn_XOR")
            self.btn_YrootX.setText("XOR")

            self.btn_square.setObjectName("btn_NOT")
            self.btn_square.setText("NOT")

            self.btn_tan.setObjectName("btn_atan")
            self.btn_tan.setText("atan")

            self.btn_tanh.setObjectName("btn_atanh")
            self.btn_tanh.setText("atanh")

            self.btn_XpowerY.setObjectName("btn_RShift")
            self.btn_XpowerY.setText(">>")

        self.log.exit("toggle_the_2nd")

    #
    # -----------------------------------------------
    # If new input is valid, update the expression and display it
    # -----------------------------------------------
    #

    def update_expression(self, new_char):
        self.log.entry(f"update_expression(new_char'{new_char}')")

        cursor_pos = self.expression_line.cursorPosition()
        self.log.write(f"cursor_pos={cursor_pos}")

        if new_char != "=":
            old_text = self.expression_line.text()
            new_text = old_text[:cursor_pos] + new_char + old_text[cursor_pos:]
            self.expression_line.setText(new_text)
            self.expression_line.setCursorPosition(cursor_pos + len(new_char))
            self.log.write(f"old_text={old_text}")
            self.log.write(f"new_text={new_text}")

        expression = self.expression_line.text()
        cursor_pos = self.expression_line.cursorPosition()
        self.log.write(f"cursor_pos={cursor_pos}")
        self.log.write(f"expression={expression}")

        self.log.exit("update_expression")

#
# -----------------------------------------------
#

    def yth_root_of_x(self, x, y):
        self.log.entry(f"yth_root_of_x(x={x},y={y})")

        if x < 0 and y % 2 != 0:
            self.log.exit("yth_root_of_x")
            return (math.pow((-x), (1 / y)) * -1.0)
        self.log.exit("yth_root_of_x")
        return math.pow(x, (1 / y))


#
# -----------------------------------------------
# The application runs until the window will be closed
# -----------------------------------------------
#

if __name__ == "__main__":

    welcome_string = f"Welcome to '{APP_NAME}-{APP_VERSION}'"
    parser = argparse.ArgumentParser(description=welcome_string)
    parser.add_argument(
        "-d", "--debug", type=int, default=0,
        help="Write debug information"
    )
    args = parser.parse_args()

    if args.debug == 0:
        print("No debug information!")
        pylog.basicConfig(level=pylog.ERROR)
    else:
        print(f"Debug information is written in '{APP_NAME}-{APP_VERSION}.log'")
        pylog.basicConfig(
            filename=f"{APP_NAME}-{APP_VERSION}.log",
            filemode="w",
            level=pylog.DEBUG,
            style="{",
            format="{asctime} [{levelname:8}] {message}"
        )

    app = QtWidgets.QApplication([])

    app.setStyle('Fusion')
    app.setApplicationName(APP_NAME)

    if OS_NAME == "Darwin":
        path_2_icon = APP_M_ICON
    elif OS_NAME == "Windows":
        path_2_icon = APP_W_ICON
    elif OS_NAME == "Linux":
        path_2_icon = APP_L_ICON

    try:
        app.setWindowIcon(QIcon(path_2_icon))
    except Exception:
        print("Cannot load application icon!")

    win = MainWindow(path_2_icon)
    win.show()
    win.setFocus()

sys.exit(app.exec())

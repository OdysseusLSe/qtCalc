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

import math
import pprint
import re
import sys

import logging as pylog
import numpy as np

from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QColor
from PySide6 import QtWidgets
from PySide6.QtWidgets import QLabel, QListWidgetItem, QMainWindow, QPushButton

from MainWindow_ui import Ui_MainWindow

from PlotWindow import PlotWindow
from Logging import Logging

import resources_rc

APP_NAME    = "qtCalc"
APP_VERSION = "0.7.1"


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.log = Logging("MainWindow", True)

        self.setWindowTitle(f"{APP_NAME} {APP_VERSION}")

        self.log.write(f"--- {APP_NAME} {APP_VERSION} ---")
        self.log.entry("__init__()", False)

        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        all_buttons = self.findChildren(QPushButton)
        for button in all_buttons:
            button.clicked.connect(self.on_button_clicked)

        self.advanced_operator()
        self.button_mapping()

        self.expression_line.setFocus()
        self.expression_history = ""

        self.history_list.model().rowsInserted.connect(
            self.history_list.scrollToBottom
        )
        self.history_list.itemDoubleClicked.connect(self.on_item_double_clicked)

        self.history_item = 0
        self.memory_index = -1
        self.tokens = []

        self.RAD = True
        self.btn_RAD.setChecked(self.RAD)
        self.btn_RAD.setStyleSheet("""
            background-color: lightgrey;
            color: green;
            border: 1 solid;
            padding: 3;
            """)
        self.btn_RAD.toggled.connect(self.deg_rad_toggle)

        self.DEG = False
        self.btn_DEG.setChecked(self.DEG)
        self.btn_DEG.setStyleSheet("""
            background-color: lightgrey;
            color: salmon;
            border: 1 solid;
            padding: 3;
            """)
        self.btn_DEG.toggled.connect(self.deg_rad_toggle)

        self.status_lbl = QLabel("Ready")
        self.status_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_bar.addWidget(self.status_lbl, 1)

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

        self.log.exit("__init__", False)

    #
    # -----------------------------------------------
    #

    def advanced_operator(self):
        self.log.entry("advanced_operator()", False)

        # Operators with their precedence and associativity
        self.operators = {
            '+': (1, True),
            '-': (1, True),
            '*': (2, True),
            '/': (2, True),
            '^': (3, False)
        }

        # Functions with their corresponding implementations and # of arguments
        self.functions = {
            'abs'   : (math.fabs, 1),
            'cos'   : (math.cos, 1),
            'cosh'  : (math.cosh, 1),
            'exp'   : (math.exp, 1),
            'lg2'   : (math.log2, 1),
            'ln'    : (math.log, 1),
            'log'   : (math.log10, 1),
            'max'   : (math.fmax, 2),
            'min'   : (math.fmin, 2),
            'mod'   : (math.fmod, 2),
            'sin'   : (math.sin, 1),
            'sinh'  : (math.sinh, 1),
            'sqrt'  : (math.sqrt, 1),
            'sqrt3' : (math.cbrt, 1),
            'tan'   : (math.tan, 1),
            'tanh'  : (math.tanh, 1)
        }

        self.trig_functions = ['cos', 'cosh', 'sin', 'sinh', 'tan', 'tanh']
        self.powers         = ['^2', '^3']

        # Predefined constants
        self.variables = {
            'pi' : math.pi,
            'e'  : math.e,
            'x'  : 'x',
            'y'  : 'y',
        }

        self.log.exit("advanced_operator", False)

    #
    # -----------------------------------------------
    #

    def button_mapping(self):
        self.log.entry("button_mapping()", False)

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
            "btn_lg2"           : "lg2(",
            "btn_ln"            : "ln(",
            "btn_log"           : "log(",
            "btn_max"           : "max(",
            "btn_min"           : "min(",
            "btn_minus"         : "-",
            "btn_mod"           : "mod(",
            "btn_multiply"      : "*",
            "btn_pi"            : "pi",
            "btn_plus"          : "+",
            "btn_unary_minus"   : "-",
            "btn_sin"           : "sin(",
            "btn_sinh"          : "sinh(",
            "btn_sqrt"          : "sqrt(",
            "btn_square"        : "^2",
            "btn_tan"           : "tan(",
            "btn_tanh"          : "tanh(",
            "btn_unary_minus"   : "-",
            "btn_x"             : "x",
            "btn_XpowerY"       : "^",
            "btn_y"             : "y"
        }

        self.log.entry("button_mapping()", False)

    #
    # -----------------------------------------------
    #

    def deg_rad_toggle(self, checked):
        self.log.entry("deg_rad_toggle(checked)", False)

        if self.btn_DEG.isChecked():
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
        else:
            self.DEG = False
            self.btn_DEG.setStyleSheet("""
                background-color: lightgrey;
                color: salmon;
                border: 1 solid;
                padding: 3;
                """)
            self.RAD = True
            self.btn_RAD.setStyleSheet("""
                background-color: lightgrey;
                color: green;
                border: 1 solid;
                padding: 3;
                """)

        self.expression_line.setFocus()
        self.log.exit("deg_rad_toggle", False)

    #
    # -----------------------------------------------
    #

    def evaluate_curve(self, expression, x_start, x_end, x_steps):
        log_str = "evaluate_curve(expression, x_start, x_end, x_steps)"
        self.log.entry(log_str, True)
        self.log.write(f"expression={expression}", True)
        log_str = f"x_start,x_end,x_steps={x_start},{x_end},{x_steps}"
        self.log.write(log_str, True)

        X = np.linspace(x_start, x_end, x_steps)
        Y = []

        for x in X:
            y = self.evaluate_expression(expression, x=x)
            Y.append(y)
            self.log.write(f"x,y={x},{y}", True)

        self.log.write(f"X=\n{pprint.pformat(X)}", True)
        self.log.write(f"Y=\n{pprint.pformat(Y)}", True)

        self.plot_2d.plot_curve(X, Y)

        self.log.exit("evaluate_curve", True)

    #
    # -----------------------------------------------
    # Handle the calculation when the "=" button is pressed
    # -----------------------------------------------
    #

    def evaluate_expression(self, expression, x=None, y=None):
        self.log.entry("evaluate_expression(x, y)", True)
        self.log.write(f"expression,x,y={expression},{x},{y}", True)

        if x is not None:
            self.variables['x'] = x
            self.log.write(f"self.variables['x']={self.variables['x']}", True)
        if y is not None:
            self.variables['y'] = y
            self.log.write(f"self.variables['y']={self.variables['y']}", True)

        try:

            token_spec = r'\d+(?:\.\d+)?(?:[eE][+-]?\d+)?|[a-zA-Z_]\w*|[\+\-\*\/\^\(\),]'
            raw_tokens = re.findall(token_spec, expression)
            self.log.write(f"raw_tokens=\n{pprint.pformat(raw_tokens)}", True)

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

            # Implement unary minus
            processed_tokens = []
            for i, tok in enumerate(tokens):
                if tok == '-' and (i == 0 or tokens[i-1] in self.operators or tokens[i-1] in ('(', ',')):
                    processed_tokens.append('0')
                processed_tokens.append(tok)

            shunting_yard_output = self.shunting_yard(processed_tokens)
            self.log.write(f"shunting_yard_output={shunting_yard_output}", True)

            raw_result = self.evaluate_rpn(shunting_yard_output)

            cleaned = float(f"{raw_result:.16g}")
            if cleaned.is_integer() and abs(cleaned) < 1e15:
                self.result = int(cleaned)
            else:
                self.result = cleaned

            self.log.write(f"self.result={self.result}", True)

            if x is None and y is None:

                self.expression_to_history("=")

                # Show result of expression
                expression = f"{self.result}"
                self.status_lbl.setText("Ready")
                self.expression_line.setText(expression)
                self.log.write(f"expression={expression}", True)

        except ZeroDivisionError:
            error = "Error: Division by zero!"
            self.status_lbl.setText(error)
            self.log.error(f"{expression} --> {error}", True)
            if x is None and y is None:
                item = QListWidgetItem(f"{expression} --> {error}")
                item.setBackground(QBrush(QColor("red")))
                item.setForeground(QColor("white"))
                self.history_list.addItem(item)
                self.history_item += 1
                self.expression_line.setText("")

        except IndexError:
            error = "Error: Insufficient operands or parentheses error!"
            self.status_lbl.setText(error)
            self.log.error(f"{expression} --> {error}", True)
            if x is None and y is None:
                item = QListWidgetItem(f"{expression} --> {error}")
                item.setBackground(QBrush(QColor("red")))
                item.setForeground(QColor("white"))
                self.history_list.addItem(item)
                self.history_item += 1
                self.expression_line.setText("")

        except Exception as e:
            error = f"Error: General error: {str(e)}"
            self.status_lbl.setText(error)
            self.log.error(f"{expression} --> {error}", True)
            if x is None and y is None:
                item = QListWidgetItem(f"{expression} --> {error}")
                item.setBackground(QBrush(QColor("red")))
                item.setForeground(QColor("white"))
                self.history_list.addItem(item)
                self.history_item += 1
                self.expression_line.setText("")

        self.log.exit("evaluate_expression", True)
        return self.result

    #
    # -----------------------------------------------
    #

    def evaluate_rpn(self, postfix_tokens):
        self.log.entry("evaluate_rpn(postfix_tokens)", True)

        stack = []

        for token in postfix_tokens:
            if isinstance(token, (int, float)):

                stack.append(token)

            elif token in self.operators:

                if len(stack) < 2:
                    raise IndexError("To few operands for operator!")
                b = stack.pop()
                a = stack.pop()
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
                    self.log.write(f"token(a)={token}({a})", True)
                    if token in self.trig_functions and self.DEG:
                        # Trigonometric functions need radians values
                        a = math.radians(a)
                        self.log.write(f"token(a)={token}({a})", True)
                    stack.append(func(a))
                elif num_args == 2:
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(func(a, b))

        self.log.exit("evaluate_rpn", True)
        return stack[0]

    #
    # -----------------------------------------------
    #

    def evaluate_surface(
            self,
            expression,
            x_start, x_end, x_steps,
            y_start, y_end, y_steps
        ):
        log_str = "evaluate_surface(expressiob, x_start, x_end, x_steps,"
        log_str += "y_start, y_end, y_steps)"
        self.log.entry(log_str, True)

        self.log.write(f"expression={expression}", True)
        log_str = f"x_start,x_end,x_steps={x_start},{x_end},{x_steps}"
        self.log.write(log_str, True)
        log_str = f"y_start,y_end,y_steps={y_start},{y_end},{y_steps}"
        self.log.write(log_str, True)

        X = np.linspace(x_start, x_end, x_steps)
        Y = np.linspace(y_start, y_end, y_steps)

        Z = np.zeros((len(X), len(Y)))
        for x_val in range(len(X)):
            for y_val in range(len(Y)):
                x = float(X[x_val])  # NumPy float to Python float!
                y = float(Y[y_val])  # NumPy float to Python float!
                Z[x_val, y_val] = self.evaluate_expression(expression, x=x, y=y)
                self.log.write(f"x,y,z={x},{y},{Z[x_val, y_val]}", True)

        self.plot_3d.plot_surface(X, Y, Z)

        self.log.exit("evaluate_surface", True)

    #
    # -----------------------------------------------
    # Add current expression to history list
    # -----------------------------------------------
    #

    def expression_to_history(self, appendix):
        self.log.entry("expression_to_history(appendix)", False)
        self.log.write(f"appendix={appendix}", False)

        expression  = self.expression_line.text()

        if appendix == "=":
            expression = f"{expression}={self.result}"
        else:
            expression = f"{expression}=Plot"
        self.expression_history = re.sub(r'(.{78})', r'\1' + '\n', expression)
        item = QListWidgetItem(self.expression_history)
        self.log.write(
            f"self.expression_history={self.expression_history}",
            False
        )

        if self.history_item % 2 == 0:
            item.setBackground(QColor("white"))
            item.setForeground(QColor(94, 94, 94))
        else:
            item.setBackground(QColor(94, 94, 94))
            item.setForeground(QColor("white"))
        self.history_list.addItem(item)
        self.history_item += 1

        self.log.exit("expression_to_history", False)

    #
    # -----------------------------------------------
    # Handle the input validation
    # -----------------------------------------------
    #

    def is_input_valid(self, new_char):
        self.log.entry("is_input_valid(new_char)", False)
        self.log.write(f"new_char={new_char}", False)

        self.status_lbl.setText("Validating input")
        expression = self.expression_line.text()

        last_char = expression[-1] if expression else ""
        operators_list = list(self.operators.keys())

        def reject(reason):
            msg = f"Validation is blocking: {reason}"
            self.status_lbl.setText(msg)
            self.log.warning(msg, True)
            self.log.exit("is_input_valid", False)
            return False

        if new_char == "=":

            if not expression:
                return reject("Empty expression!")
            if last_char in operators_list or last_char in ("(", ","):
                return reject(f"Expression cannot end with '{last_char}'!")
            if expression.count("(") != expression.count(")"):
                return reject("Unclosed parentheses!")

        else:

            if not expression:
                if new_char in self.powers or new_char in (",", ")"):
                    return reject(f"Invalid start token: {new_char}!")
                if new_char in operators_list and new_char != "-":
                    return reject(f"Operator at start: {new_char}!")

            elif last_char in operators_list:
                if new_char in operators_list or new_char in self.powers:
                    return reject(f"Double operator: {last_char}{new_char}!")
                if new_char in (")", ","):
                    return reject(f"'{new_char}' after operator: {last_char}!")

            elif last_char in ("(", ","):
                if new_char in self.powers or new_char in (")", ","):
                    return reject(f"Invalid token '{new_char}' after '{last_char}'!")
                if new_char in operators_list and new_char != "-":
                    return reject(f"Operator after '{last_char}': {new_char}!")

            if new_char == ")":
                if expression.count(")") >= expression.count("("):
                    return reject("Too many closing parentheses!")

            if new_char == ".":
                if last_char == ")" or expression.endswith(tuple(self.variables.keys())):
                    return reject("Decimal point cannot follow a constant or closing parenthesis!")

                current_number = re.search(r'[\d.]+$', expression)
                if current_number and "." in current_number.group():
                    return reject("Multiple decimal points in one number!")

        self.log.exit("is_input_valid", False)
        return True

    #
    # -----------------------------------------------
    # Handle special buttons like clear, memory functions, cursor, etc.
    # -----------------------------------------------

    def is_special_button(self, button_name):
        self.log.entry("is_special_button(button_name)", False)
        self.log.write(f"button_name={button_name}", False)

        self.status_lbl.setText("Checking for special button")

        if button_name == "btn_clear":
            # Clear the current expression and reset the display
            self.expression_line.setText("")
            self.log.write("clear", False)
            self.expression_line.setFocus()
            value = True

        elif button_name == "btn_del":
            cursor_pos = self.expression_line.cursorPosition()
            old_text   = self.expression_line.text()
            new_text   = old_text[:cursor_pos-1] + old_text[cursor_pos:]
            self.expression_line.setText(new_text)
            self.expression_line.setCursorPosition(cursor_pos-1)
            self.expression_line.setFocus()
            value = True

        elif button_name == "btn_Mplus":
            # Add the current result to memory
            if hasattr(self, 'result') and self.result is not None:
                self.memory_list.addItem(f"{self.result}")
                self.memory_index += 1
                self.memory_list.setCurrentIndex(self.memory_index)
            self.expression_line.setFocus()
            value = True

        elif button_name == "btn_MC":
            # Clear the memory
            self.memory_list.clear()
            self.memory_index = -1
            self.expression_line.setFocus()
            value = True

        elif button_name == "btn_MR":
            # Recall the value from memory and
            # append it to the current expression
            if self.memory_list.currentText() != "":
                mem_value = self.memory_list.currentText()
                cursor_pos = self.expression_line.cursorPosition()
                old_text = self.expression_line.text()
                new_text = old_text[:cursor_pos] + mem_value + old_text[cursor_pos:]
                self.expression_line.setText(new_text)
                self.expression_line.setCursorPosition(cursor_pos + len(mem_value))
                self.expression_line.setFocus()
            value = True

        elif button_name == "btn_left":
            self.expression_line.setFocus()
            self.expression_line.cursorBackward(False)
            self.expression_line.setFocus()
            value = True

        elif button_name == "btn_right":
            self.expression_line.setFocus()
            self.expression_line.cursorForward(False)
            self.expression_line.setFocus()
            value = True

        elif button_name == "btn_plot":
            self.plot_expression()
            value = True

        else:
            value = False

        self.log.write(f"value={value}", False)

        self.log.exit("is_special_button", False)
        return value

    #
    # -----------------------------------------------
    #

    def keyPressEvent(self, event):
        self.log.entry("keyPressEvent(event)", False)

        key_text = event.text()
        self.log.write(f"event.text()='{event.text()}'", False)
        self.log.write(f"event.key()='{event.key()}'", False)
        self.log.write(f"Native='{event.nativeVirtualKey()}'", False)

        matched_btn_name = None

        if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            matched_btn_name = "btn_equal"
        elif key_text:
            for button_name, character in self.buttons.items():
                if key_text == character:
                    matched_btn_name = button_name
                    break

        if matched_btn_name:
            button_object = getattr(self, matched_btn_name, None)
            if button_object:
                button_object.click()
                self.log.write(f"matched_btn_name={matched_btn_name}", False)
                event.accept()
                self.log.exit("keyPressEvent(event)", False)
                return

        super().keyPressEvent(event)

        self.log.exit("keyPressEvent(event)", False)

    #
    # -----------------------------------------------
    #

    def on_button_clicked(self):
        self.log.entry("on_button_clicked()", False)

        self.expression_line.setFocus()

        button = self.sender()
        button_name = button.objectName()
        if self.is_special_button(button_name):
            self.log.write(f"is_special_button({button_name})=True", False)
            self.log.exit("on_button_clicked", False)
            return

        new_char = self.buttons[button_name]
        if not self.is_input_valid(new_char):
            self.log.write(f"is_input_valid({new_char})=False", False)
            self.log.exit("on_button_clicked", False)
            return

        self.result = None

        self.update_expression(new_char)

        if new_char == "=":
            expression = self.expression_line.text()
            if "x" in expression:
                # At least one unknown variable --> 2D/3D-plot
                self.plot_expression()
            else:
                self.evaluate_expression(expression)

        self.log.exit("on_button_clicked", False)

    #
    # -----------------------------------------------
    #

    def on_item_double_clicked(self, item):
        self.log.entry("on_item_double_clicked(self, item)", False)
        self.log.write(f"item.text()={item.text()}", False)

        if "=" in item.text():
            # Copy text just before "=" and attach it to the current expression.
            insert_text = item.text().split("=", 1)[0]
        else:
            # Errorneous expression will be ignored.
            self.status_lbl.setText("Errorneous expression ignored!")
            self.log.exit("on_item_double_clicked", False)
            return

        cursor_pos = self.expression_line.cursorPosition()
        old_text   = self.expression_line.text()
        new_text   = old_text[:cursor_pos] + insert_text + old_text[cursor_pos:]

        self.expression_line.setText(new_text)
        self.expression_line.setCursorPosition(cursor_pos + len(insert_text))
        self.log.write(f"new_text={new_text}", False)

        self.expression_line.setFocus()

        self.log.exit("on_item_double_clicked", False)

    #
    # -----------------------------------------------
    #

    def plot_expression(self):
        self.log.entry("plot_expression()", True)

        self.curve   = False
        self.surface = False

        # Check it at least variable 'x' exists.
        expression  = self.expression_line.text()
        if "x" not in expression:
            self.status_lbl.setText("Missing variable 'x'")
            self.log.warning("Missing variable 'x'!", True)
            self.log.exit("plot_expression", True)
            return

        # Use '=' as equivalent to 'Plot' button.
        new_char = "="
        if not self.is_input_valid(new_char):
            self.status_lbl.setText("Expression is not valid!")
            self.log.warning("is_input_valid(=)=False", True)
            self.log.exit("plot_expression", True)
            return

        if "x" in expression and "y" in expression:
            self.surface = True
            if not hasattr(self, 'plot_3d'):
                # Start new window to draw the expression
                self.plot_3d = PlotWindow(expression, self.curve, self.surface)
                self.plot_3d.eval_curve.connect(self.evaluate_curve)
                self.plot_3d.eval_surface.connect(self.evaluate_surface)
                self.plot_3d.show()
            elif self.plot_3d is not None:
                if not self.plot_3d.isVisible():
                    self.plot_3d.show()
                self.plot_3d.add_plot(expression)
            else:
                self.status_lbl.setText("Internal error: plotting not available!")
                self.log.error("Internal error: plotting not available!", True)
        else:
            self.curve = True
            if not hasattr(self, 'plot_2d'):
                # Start new window to draw the expression
                self.plot_2d = PlotWindow(expression, self.curve, self.surface)
                self.plot_2d.eval_curve.connect(self.evaluate_curve)
                self.plot_2d.eval_surface.connect(self.evaluate_surface)
                self.plot_2d.show()
            elif self.plot_2d is not None:
                if not self.plot_2d.isVisible():
                    self.plot_2d.show()
                self.plot_2d.add_plot(expression)
            else:
                self.status_lbl.setText("Internal error: plotting not available!")
                self.log.error("Internal error: plotting not available!", True)

        self.expression_to_history("Plot")

        self.log.exit("plot_expression", True)

    #
    # -----------------------------------------------
    #

    def shunting_yard(self, tokens):
        self.log.entry("shunting_yard(self, tokens)", True)

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

            elif token in self.operators:
                # Token is an operator
                p1, a1 = self.operators[token]
                while operator and operator[-1] in self.operators:
                    p2, _ = self.operators[operator[-1]]
                    if (a1 and p1 <= p2) or (not a1 and p1 < p2):
                        output.append(operator.pop())
                    else:
                        break
                operator.append(token)

            elif token == '(':
                # Token is an opening parenthesis
                operator.append(token)

            elif token == ')':
                # Token is a closing parenthesis
                while operator and operator[-1] != '(':
                    output.append(operator.pop())
                if operator and operator[-1] == '(':
                    operator.pop()  # Entferne '('
                if operator and operator[-1] in self.functions:
                    output.append(operator.pop())

        while operator:
            output.append(operator.pop())

        self.log.exit("shunting_yard", True)
        return output

    #
    # -----------------------------------------------
    # If the input is valid, update the expression and display it
    # -----------------------------------------------
    #

    def update_expression(self, new_char):
        self.log.entry("update_expression(new_char)", False)
        self.log.write(f"new_char={new_char}", False)

        cursor_pos = self.expression_line.cursorPosition()
        self.log.write(f"cursor_pos={cursor_pos}", False)

        if new_char != "=":
            old_text = self.expression_line.text()
            new_text = old_text[:cursor_pos] + new_char + old_text[cursor_pos:]
            self.expression_line.setText(new_text)
            self.expression_line.setCursorPosition(cursor_pos + len(new_char))

        expression = self.expression_line.text()
        cursor_pos = self.expression_line.cursorPosition()
        self.log.write(f"cursor_pos={cursor_pos}", False)
        self.log.write(f"expression={expression}", False)
        self.log.write(f"new_char={new_char}", False)

        self.log.exit("update_expression", False)


#
# -----------------------------------------------
# The application runs until the window will be closed
# -----------------------------------------------
#

app = QtWidgets.QApplication([])

app.setStyle('Fusion')

pylog.basicConfig(
    filename=f"{APP_NAME}.log",
    filemode="w",
    level=pylog.DEBUG,
    style="{",
    format="{asctime} [{levelname:8}] {message}"
)

#load_stylesheet(":/ui/style.css")

win = MainWindow()
win.show()

win.setFocus()

sys.exit(app.exec())

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
import re
import sys

import logging as pylog


from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QTextCharFormat, QTextCursor
from PySide6 import QtWidgets
from PySide6.QtWidgets import QLabel, QMainWindow, QPushButton

from MainWindow_ui import Ui_MainWindow

from Logging import Logging

#import resources_rc

APP_NAME    = "qtCalc"
APP_VERSION = "0.3"


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.log = Logging("MainWindow", True)

        self.setWindowTitle(f"{APP_NAME} {APP_VERSION}")

        self.log.write(f"--- {APP_NAME} {APP_VERSION} ---")
        self.log.entry("__init__", True)

        all_buttons = self.findChildren(QPushButton)
        for button in all_buttons:
            button.clicked.connect(self.on_button_clicked)

        self.advanced_operator()
        self.button_mapping()

        self.text = ""
        self.expression_line.setReadOnly(True)
        self.expression_history = ""

        self.history_browser.clear()
        self.history_item = 0
        self.history_browser.textChanged.connect(self.scroll_to_bottom)
        self.bg_color_lightorange = False
        self.bg_color_lightyellow = True

        self.tokens = []

        self.status_lbl = QLabel("Ready")
        self.status_lbl.setStyleSheet(
            "font-weight: bold; background-color: rgb(94, 94, 94); color: white; border: 1 solid; border-radius: 7;"
        )
        self.status_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_bar.addWidget(self.status_lbl, 1)

        self.log.exit("__init__", True)

    #
    # -----------------------------------------------
    #

    def advanced_operator(self):
        self.log.entry("advanced_operator()", True)

        # Operators with their precedence and associativity
        self.operators = {
            '+': (1, True),
            '-': (1, True),
            '*': (2, True),
            '/': (2, True),
            '^': (3, False)
        }

        # Functions with their corresponding implementations
        self.functions = {
            'cos'   : (math.cos, 1),
            'cosh'  : (math.cosh, 1),
            'exp'   : (math.exp, 1),
            'lg2'   : (math.log2, 1),
            'ln'    : (math.log, 1),
            'log'   : (math.log10, 1),
            'max'   : (math.fmax, 2),
            'min'   : (math.fmin, 2),
            'sin'   : (math.sin, 1),
            'sinh'  : (math.sinh, 1),
            'sqrt'  : (math.sqrt, 1),
            'sqrt3' : (math.cbrt, 1),
            'tan'   : (math.tan, 1),
            'tanh'  : (math.tanh, 1)
        }

        # Predefined constants
        self.variables = {
            'pi' : math.pi,
            'e'  : math.e
        }

        self.log.exit("advanced_operator", True)

    #
    # -----------------------------------------------
    #

    def button_mapping(self):
        self.log.entry("button_mapping()", True)

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
            "btn_XpowerY"       : "^"
        }

        self.log.entry("button_mapping()", True)

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
                    stack.append(func(a))
                elif num_args == 2:
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(func(a, b))

        self.log.entry("evaluate_rpn()", True)
        return stack[0]

    #
    # -----------------------------------------------
    #

    def keyPressEvent(self, event):
        self.log.entry("keyPressEvent(event)", True)

        key_text = event.text()
        self.log.write(f"event.text()='{event.text()}'", True)
        self.log.write(f"event.key()='{event.key()}'", True)
        self.log.write(f"Native='{event.nativeVirtualKey()}'", True)

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
                button_object.animateClick()
                self.log.write(f"matched_btn_name={matched_btn_name}", True)
                event.accept()
                self.log.exit("keyPressEvent(event)", True)
                return

        super().keyPressEvent(event)

        self.log.exit("keyPressEvent(event)", True)

    #
    # -----------------------------------------------
    #

    def on_button_clicked(self):
        self.log.entry("on_button_clicked()", True)

        button      = self.sender()
        button_name = button.objectName()

        #
        # First, handle special buttons like clear, memory functions, etc.
        #

        if button_name == "btn_clear":
            # Clear the current expression and reset the display
            self.text = ""
            self.expression_line.setText(self.text)
            self.log.write("clear", True)
            return
        elif button_name == "btn_Mplus":
            # Store the current result in memory
            if hasattr(self, 'result') and self.result is not None:
                self.memory_lbl.setText(f"Mem: {self.result}")
            return
        elif button_name == "btn_MC":
            # Clear the memory
            self.memory_lbl.setText("Mem: <empty>")
            return
        elif button_name == "btn_MR":
            # Recall the value from memory and
            # append it to the current expression
            if self.memory_lbl.text() != "Mem: <empty>":
                mem_value = self.memory_lbl.text().split(": ")[1]
                self.text += mem_value
                self.expression_line.setText(self.text)
            return

        self.result = None

        #
        # Second, handle the input validation
        #

        self.status_lbl.setText("Validating input...")

        new_char = self.buttons[button_name]
        self.log.write(f"new_char={new_char}", True)

        last_char = self.text[-1] if self.text else ""
        operators_list = list(self.operators.keys())

        if new_char != "=":

            log_string = f"Validation is blocking: "

            if not self.text and (new_char == "^2" or new_char == "^3"):
                log_string += f"Operator at start: {new_char}!"
                self.status_lbl.setText(log_string)
                self.log.warning(log_string, True)
                self.log.exit("on_button_clicked", True)
                return

            if not self.text and new_char in operators_list and new_char != '-':
                log_string += f"Operator at start: {new_char}!"
                self.status_lbl.setText(log_string)
                self.log.warning(log_string, True)
                self.log.exit("on_button_clicked", True)
                return

            if last_char in operators_list and new_char in operators_list:
                log_string += f"Double operator: {last_char}{new_char}!"
                self.status_lbl.setText(log_string)
                self.log.warning(log_string, True)
                self.log.exit("on_button_clicked", True)
                return

            if last_char == "(" and (new_char == "^2" or new_char == "^3"):
                log_string += f"Operator after opening parenthesis: {new_char}!"
                self.status_lbl.setText(log_string)
                self.log.warning(log_string, True)
                self.log.exit("on_button_clicked", True)
                return

            if last_char == "(" and new_char in operators_list and new_char != '-':
                log_string += f"Operator after opening parenthesis: {new_char}!"
                self.status_lbl.setText(log_string)
                self.log.warning(log_string, True)
                self.log.exit("on_button_clicked", True)
                return

            if last_char in operators_list and new_char == ")":
                log_string += f"Parenthesis after operator: {last_char}!"
                self.status_lbl.setText(log_string)
                self.log.warning(log_string, True)
                self.log.exit("on_button_clicked", True)
                return

            if new_char == ")":
                number_of_opening = self.text.count("(")
                number_of_closing = self.text.count(")")
                if number_of_closing >= number_of_opening:
                    log_string += "Too many closing parentheses!"
                    self.status_lbl.setText(log_string)
                    self.log.warning(log_string, True)
                    self.log.exit("on_button_clicked", True)
                    return

        #
        # Third, if the input is valid, update the expression and display it
        #

        self.text += new_char
        self.log.write(f"{new_char}", True)

        self.expression_line.setText(self.text)
        self.log.write(f"self.text={self.text}", True)

        #
        # Forth, handle the calculation when the "=" button is pressed
        #

        if new_char == "=":

            number_of_opening = self.text.count("(")
            number_of_closing = self.text.count(")")
            if number_of_closing < number_of_opening:
                # Remove the "=" (the last character)
                self.text = self.text[:-1]
                self.expression_line.setText(self.text)
                self.status_lbl.setText("Too few closing parentheses!")
                self.log.warning("Too few closing parentheses!", True)
                self.log.exit("on_button_clicked", True)
                return

            try:

                token_spec = r'\d+(?:\.\d+)?(?:[eE][+-]?\d+)?|[a-zA-Z_]\w*|[\+\-\*\/\^\(\),]'
                raw_tokens = re.findall(token_spec, self.text[:-1])
                self.log.write(f"raw_tokens={raw_tokens}", True)

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

                cleaned = float(f"{raw_result:.12g}")
                if cleaned.is_integer() and abs(cleaned) < 1e15:
                    self.result = int(cleaned)
                else:
                    self.result = cleaned

                self.expression_history = f"{self.text}{self.result}"
                self.history_browser.append(self.expression_history)

                # Show reuslt of expression
                self.text = f"{self.result}"
                self.status_lbl.setText("Ready")
                self.expression_line.setText(self.text)
                self.log.write(f"self.text={self.text}", True)

            except ZeroDivisionError:
                error = "Error: Division by zero!"
                self.status_lbl.setText(error)
                self.log.error(error, True)
                self.history_browser.append(
                    f"{self.text}<br><span style='color:red;'>Error: Division by zero!</span>"
                )
                self.text = ""
                self.expression_line.setText(self.text)

            except IndexError:
                error = "Error: Insufficient operands or parentheses error!"
                self.status_lbl.setText(error)
                self.log.error(error, True)
                self.history_browser.append(
                    f"{self.text}<br><span style='color:red;'>Error: Insufficient operands or parentheses error</span>"
                )
                self.text = ""
                self.expression_line.setText(self.text)

            except Exception as e:
                error = f"Error: General error: {str(e)}"
                self.status_lbl.setText(error)
                self.log.error(error, True)
                self.history_browser.append(
                    f"{self.text}<br><span style='color:red;'>Error: Calculation not possible!</span>"
                )
                self.text = ""
                self.expression_line.setText(self.text)

        self.log.exit("on_button_clicked", True)

    #
    # -----------------------------------------------
    #

    def scroll_to_bottom(self):
        scrollbar = self.history_browser.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())

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

sys.exit(app.exec())

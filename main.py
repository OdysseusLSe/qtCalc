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


from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QBrush, QColor
from PySide6 import QtWidgets
from PySide6.QtWidgets import QLabel, QListWidgetItem, QMainWindow, QPushButton

from MainWindow_ui import Ui_MainWindow

from Logging import Logging

import resources_rc

APP_NAME    = "qtCalc"
APP_VERSION = "0.5.1"


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.log = Logging("MainWindow", True)

        self.setWindowTitle(f"{APP_NAME} {APP_VERSION}")

        self.log.write(f"--- {APP_NAME} {APP_VERSION} ---")
        self.log.entry("__init__", True)

        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        all_buttons = self.findChildren(QPushButton)
        for button in all_buttons:
            button.clicked.connect(self.on_button_clicked)

        self.advanced_operator()
        self.button_mapping()

        self.text = ""
        self.expression_line.setFocus()
        self.expression_history = ""

        self.history_list.model().rowsInserted.connect(
            self.history_list.scrollToBottom
        )
        self.history_list.itemDoubleClicked.connect(self.on_item_double_clicked)

        self.history_item = 0
        self.memory_index = -1
        self.tokens = []

        self.DEG = True
        self.btn_DEG.setChecked(self.DEG)
        self.btn_DEG.setStyleSheet("color: green; border: 1 solid; padding: 3")
        self.btn_DEG.toggled.connect(self.deg_rad_toggle)
        self.RAD = False
        self.btn_RAD.setChecked(self.RAD)
        self.btn_RAD.setStyleSheet("color: salmon; border: 1 solid; padding: 3")
        self.btn_RAD.toggled.connect(self.deg_rad_toggle)

        self.status_lbl = QLabel("Ready")
        self.status_lbl.setStyleSheet(
            "font-weight: bold; background-color: rgb(94, 94, 94); color: white; border: 1 solid; border-radius: 7;"
        )
        self.status_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_bar.addWidget(self.status_lbl, 1)

        self.expression_line.setFocus()

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
            "btn_XpowerY"       : "^"
        }

        self.log.entry("button_mapping()", True)

    #
    # -----------------------------------------------
    #

    @Slot()
    def deg_rad_toggle(self, checked):
        self.log.entry("deg_rad_toggle(checked)", True)

        if self.btn_DEG.isChecked():
            self.DEG = True
            self.btn_DEG.setStyleSheet("color: green; border: 1 solid; padding: 3")
            self.RAD = False
            self.btn_RAD.setStyleSheet("color: salmon; border: 1 solid; padding: 3")
        else:
            self.DEG = False
            self.btn_DEG.setStyleSheet("color: salmon; border: 1 solid; padding: 3")
            self.RAD = True
            self.btn_RAD.setStyleSheet("color: green; border: 1 solid; padding: 3")

        self.expression_line.setFocus()
        self.log.exit("deg_rad_toggle", True)

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
    # Handle the input validation
    # -----------------------------------------------
    #

    def is_input_valid(self, new_char):
        self.log.entry("is_input_valid(new_char)", True)
        self.log.write(f"new_char={new_char}", True)

        self.status_lbl.setText("Validating input")

        last_char = self.text[-1] if self.text else ""
        operators_list = list(self.operators.keys())

        value = True

        if new_char != "=":

            log_string = f"Validation is blocking: "

            if not self.text and (new_char == "^2" or new_char == "^3"):
                log_string += f"Operator at start: {new_char}!"
                self.status_lbl.setText(log_string)
                self.log.warning(log_string, True)
                value = False

            if not self.text and new_char in operators_list and new_char != '-':
                log_string += f"Operator at start: {new_char}!"
                self.status_lbl.setText(log_string)
                self.log.warning(log_string, True)
                value = False

            if last_char in operators_list and new_char in operators_list:
                log_string += f"Double operator: {last_char}{new_char}!"
                self.status_lbl.setText(log_string)
                self.log.warning(log_string, True)
                value = False

            if last_char == "(" and (new_char == "^2" or new_char == "^3"):
                log_string += f"Operator after opening parenthesis: {new_char}!"
                self.status_lbl.setText(log_string)
                self.log.warning(log_string, True)
                value = False

            if last_char == "(" and new_char in operators_list and new_char != '-':
                log_string += f"Operator after opening parenthesis: {new_char}!"
                self.status_lbl.setText(log_string)
                self.log.warning(log_string, True)
                value = False

            if last_char in operators_list and new_char == ")":
                log_string += f"Parenthesis after operator: {last_char}!"
                self.status_lbl.setText(log_string)
                self.log.warning(log_string, True)
                value = False

            if new_char == ")":
                number_of_opening = self.text.count("(")
                number_of_closing = self.text.count(")")
                if number_of_closing >= number_of_opening:
                    log_string += "Too many closing parentheses!"
                    self.status_lbl.setText(log_string)
                    self.log.warning(log_string, True)
                    value = False

        self.log.exit("is_input_valid", True)
        return value

    #
    # -----------------------------------------------
    # Handle special buttons like clear, memory functions, cursor, etc.
    # -----------------------------------------------

    def is_special_button(self, button_name):
        self.log.entry("is_special_button(button_name)", True)
        self.log.write(f"button_name={button_name}", True)

        self.status_lbl.setText("Checking for special button")

        if button_name == "btn_clear":
            # Clear the current expression and reset the display
            self.text = ""
            self.expression_line.setText(self.text)
            self.log.write("clear", True)
            self.expression_line.setFocus()
            value = True

        elif button_name == "btn_del":
            cursor_pos = self.expression_line.cursorPosition()
            old_text   = self.expression_line.text()
            new_text   = old_text[:cursor_pos-1] + old_text[cursor_pos:]
            self.text  = new_text
            self.expression_line.setText(self.text)
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
                self.text = new_text
                self.expression_line.setText(self.text)
                self.text += mem_value
                self.expression_line.setText(self.text)
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

        else:
            value = False

        self.log.write(f"value={value}", True)

        self.log.exit("is_special_button", True)
        return value

    #
    # -----------------------------------------------
    #

    @Slot()
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
                button_object.click()
                self.log.write(f"matched_btn_name={matched_btn_name}", True)
                event.accept()
                self.log.exit("keyPressEvent(event)", True)
                return

        super().keyPressEvent(event)

        self.log.exit("keyPressEvent(event)", True)

    #
    # -----------------------------------------------
    #

    @Slot()
    def on_button_clicked(self):
        self.log.entry("on_button_clicked()", True)

        self.expression_line.setFocus()

        button = self.sender()
        button_name = button.objectName()
        if self.is_special_button(button_name):
            return

        new_char = self.buttons[button_name]
        if not self.is_input_valid(new_char):
            return

        self.result = None

        self.update_expression(new_char)

        #
        # Forth, handle the calculation when the "=" button is pressed
        #

        if new_char == "=":

            number_of_opening = self.text.count("(")
            number_of_closing = self.text.count(")")
            if number_of_closing < number_of_opening:
                self.expression_line.setText(self.text)
                self.status_lbl.setText("Too few closing parentheses!")
                self.log.warning("Too few closing parentheses!", True)
                self.log.exit("on_button_clicked", True)
                return

            try:

                token_spec = r'\d+(?:\.\d+)?(?:[eE][+-]?\d+)?|[a-zA-Z_]\w*|[\+\-\*\/\^\(\),]'
                raw_tokens = re.findall(token_spec, self.text)
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

                cleaned = float(f"{raw_result:.16g}")
                if cleaned.is_integer() and abs(cleaned) < 1e15:
                    self.result = int(cleaned)
                else:
                    self.result = cleaned

                # Add current expression to history list
                expression = f"{self.text}={self.result}"
                self.expression_history = re.sub(r'(.{78})', r'\1' + '\n', expression)
                item = QListWidgetItem(self.expression_history)
                self.log.write(
                    f"self.expression_history={self.expression_history}",
                    True
                )

                if self.history_item % 2 == 0:
                    item.setBackground(QBrush(QColor("white")))
                self.history_list.addItem(item)
                self.history_item += 1

                # Show result of expression
                self.text = f"{self.result}"
                self.status_lbl.setText("Ready")
                self.expression_line.setText(self.text)
                self.log.write(f"self.text={self.text}", True)

            except ZeroDivisionError:
                error = "Error: Division by zero!"
                self.status_lbl.setText(error)
                self.log.error(error, True)
                item = QListWidgetItem(f"{self.text} --> {error}")
                item.setBackground(QBrush(QColor("red")))
                item.setForeground(QColor("white"))
                self.history_list.addItem(item)
                self.history_item += 1
                self.text = ""
                self.expression_line.setText(self.text)

            except IndexError:
                error = "Error: Insufficient operands or parentheses error!"
                self.status_lbl.setText(error)
                self.log.error(error, True)
                item = QListWidgetItem(f"{self.text} --> {error}")
                item.setBackground(QBrush(QColor("red")))
                item.setForeground(QColor("white"))
                self.history_list.addItem(item)
                self.history_item += 1
                self.text = ""
                self.expression_line.setText(self.text)

            except Exception as e:
                error = f"Error: General error: {str(e)}"
                self.status_lbl.setText(error)
                item = QListWidgetItem(f"{self.text} --> {error}")
                item.setBackground(QBrush(QColor("red")))
                item.setForeground(QColor("white"))
                self.history_list.addItem(item)
                self.history_item += 1
                self.text = ""
                self.expression_line.setText(self.text)

        self.log.exit("on_button_clicked", True)

    #
    # -----------------------------------------------
    #

    @Slot()
    def on_item_double_clicked(self, item):
        self.log.entry("on_item_double_clicked(self, item)", True)

        self.log.write(f"item.text()={item.text()}", True)

        self.text = self.expression_line.text()

        cursor_pos = self.expression_line.cursorPosition()
        old_text = self.expression_line.text()

        if "=" in item.text():
            # Copy text just before "=" and attach it to the current expression
            insert_text = item.text().split("=", 1)[0]
        else:
            # Check for errorneous expression
            insert_text = item.text().split(" --> ", 1)[0]

        new_text = old_text[:cursor_pos] + insert_text + old_text[cursor_pos:]
        self.expression_line.setText(new_text)
        self.expression_line.setCursorPosition(cursor_pos + len(insert_text))
        self.log.write(f"new_text={new_text}", True)

        self.expression_line.setFocus()

        self.log.exit("on_item_double_clicked", True)

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
    # Third, if the input is valid, update the expression and display it
    # -----------------------------------------------
    #

    def update_expression(self, new_char):
        self.log.entry("update_expression(new_char)", True)
        self.log.write(f"new_char={new_char}", True)

        cursor_pos = self.expression_line.cursorPosition()
        self.log.write(f"cursor_pos={cursor_pos}", True)
        if new_char != "=":
            old_text = self.expression_line.text()
            new_text = old_text[:cursor_pos] + new_char + old_text[cursor_pos:]
            self.text = new_text
            self.expression_line.setText(self.text)
            self.expression_line.setCursorPosition(cursor_pos + len(new_char))
        else:
            self.text = self.expression_line.text()
        cursor_pos = self.expression_line.cursorPosition()
        self.log.write(f"cursor_pos={cursor_pos}", True)
        self.log.write(f"self.text={self.text}", True)
        self.log.write(f"new_char={new_char}", True)

        self.log.exit("update_expression", True)

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

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


import copy
import pprint
import math
import re
import sys
import time

import logging as pylog

from PySide6 import QtWidgets
from PySide6.QtWidgets import (
    QComboBox,
    QColorDialog,
    QDialog,
    QDialogButtonBox,
    QDoubleSpinBox,
    QFileDialog,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMenu,
    QMessageBox,
    QPushButton,
    QSizePolicy,
    QStatusBar,
    QVBoxLayout,
    QWidget
)

from MainWindow_ui import Ui_MainWindow

from Logging import Logging

#import resources_rc

APP_NAME    = "qtCalc"
APP_VERSION = "0.1"


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

        self.textBrowser.clear()
        self.text = ""

        self.tokens = []

        self.log.exit("__init__", True)

    #
    # -----------------------------------------------
    #

    def advanced_operator(self):

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
            'cos'   : math.cos,
            'exp'   : math.exp,
            'ln'    : math.log1p,
            'lg2'   : math.log2,
            'log'   : math.log,
            'sin'   : math.sin,
            'sqrt'  : math.sqrt,
            'sqrt3' : math.cbrt,
            'tan'   : math.tan
        }

        # Predefined constants
        self.variables = {
            'pi' : math.pi,
            'e'  : math.e
        }

    #
    # -----------------------------------------------
    #

    def button_mapping(self):

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
            "btn_bracket_left"  : "(",
            "btn_bracket_right" : ")",
            "btn_cbrt"          : "sqrt3(",
            "btn_clear"         : "C",
            "btn_cos"           : "cos(",
            "btn_cube"          : "^3",
            "btn_divide"        : "/",
            "btn_e"             : "e",
            "btn_equal"         : "=",
            "btn_lg2"           : "lg2(",
            "btn_ln"            : "ln(",
            "btn_log"           : "log(",
            "btn_max"           : "max(",
            "btn_min"           : "min( ",
            "btn_minus"         : "-",
            "btn_multiply"      : "*",
            "btn_pi"            : "pi",
            "btn_plus"          : "+",
            "btn_sin"           : "sin(",
            "btn_sqrt"          : "sqrt(",
            "btn_square"        : "^2",
            "btn_tan"           : "tan(",
            "btn_XpowerY"       : "^"
        }

    #
    # -----------------------------------------------
    #

    def evaluate_rpn(self, postfix_tokens):

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
                if len(stack) < 1:
                    raise IndexError("To few operands for function")
                a = stack.pop()
                stack.append(self.functions[token](a))

        return stack[0]

    #
    # -----------------------------------------------
    #

    def on_button_clicked(self):
        self.log.entry("on_button_clicked", True)

        button = self.sender()

        if button.objectName() == "btn_clear":
            self.text = ""
            self.textBrowser.clear()
            self.log.write("clear", True)
            return

        self.text += self.buttons[button.objectName()]
        self.log.write(f"{self.buttons[button.objectName()]}", True)

        self.textBrowser.clear()
        self.textBrowser.setPlainText(self.text)
        self.log.write(f"self.text={self.text}", True)

        if button.objectName() == "btn_equal":

            try:

                token_spec = r'\d+(?:\.\d+)?|[a-zA-Z_]\w*|[\+\-\*\/\^\(\),]'
                tokens = re.findall(token_spec, self.text[:-1])
                self.log.write(f"tokens={tokens}", True)

                shunting_yard_output = self.shunting_yard(tokens)
                self.log.write(f"shunting_yard_output={shunting_yard_output}", True)

                result = self.evaluate_rpn(shunting_yard_output)

                self.text += f"<br>{result}"
                self.log.write(f"self.text={self.text}", True)
                self.textBrowser.setHtml(self.text)
                self.text = str(result)

            except ZeroDivisionError:
                self.log.error("Division by zero!", True)
                self.textBrowser.setHtml(
                    f"{self.text}<br><span style='color:red;'>Error: Division by zero!</span>"
                )
                self.text = ""

            except IndexError:
                self.log.error("Index error: Insufficient operands or parentheses error", True)
                self.textBrowser.setHtml(
                    f"{self.text}<br><span style='color:red;'>Error: Insufficient operands or parentheses error</span>"
                )
                self.text = ""

            except Exception as e:
                self.log.error(f"General error: {str(e)}", True)
                self.textBrowser.setHtml(
                    f"{self.text}<br><span style='color:red;'>Error: Calculation not possible!</span>"
                )
                self.text = ""

        self.log.exit("on_button_clicked", True)

    #
    # -----------------------------------------------
    #

    def shunting_yard(self, tokens):

        output = []
        operator = []

        for token in tokens:
            if re.match(r'^\d+(?:\.\d+)?$', token):
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

        return output


#
# -----------------------------------------------
# The application runs until the window will be closed
# -----------------------------------------------
#

app = QtWidgets.QApplication([])

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

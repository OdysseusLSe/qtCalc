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

#
# -----------------------------------------------
#

# The application runs until the window will be closed

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

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

import pprint

import pyqtgraph as pg

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets import QLabel, QMainWindow, QVBoxLayout

from PlotWindow_ui import Ui_PlotWindow
from Logging import Logging

#
# -----------------------------------------------
#


class PlotWindow(QMainWindow, Ui_PlotWindow):

    # Signal to start evaluation of expression
    eval_curve   = Signal(float, float, int)
    eval_surface = Signal(float, float, int, float, float, int)

    def __init__(self, expression):
        super().__init__()
        self.setupUi(self)
        self.log = Logging("PlotWindow", True)

        self.setWindowTitle("Plot Window")

        self.log.entry("__init__(expression)", True)
        self.log.write(f"expression={expression}", True)

        self.plot_title = expression

        self.status_lbl = QLabel("Ready")
        self.status_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_bar.addWidget(self.status_lbl, 1)

        self.x_start.setValidator(QDoubleValidator(-1000, 1000, 15))
        self.x_end.setValidator(QDoubleValidator(-1000, 1000, 15))

        self.y_start.setValidator(QDoubleValidator(-1000, 1000, 15))
        self.y_end.setValidator(QDoubleValidator(-1000, 1000, 15))

        self.start_btn.clicked.connect(self.start)

        self.curve   = True
        self.surface = False

        self.curve_number = -1
        self.curve_colors = ["white", "black", "red", "green", "blue"]

        plot_layout = QVBoxLayout()
        self.plot_widget = pg.PlotWidget()
        plot_layout.addWidget(self.plot_widget)
        self.bottom.setLayout(plot_layout)

        self.plot_widget.setBackground("gray")
        self.plot_widget.setLabel("left", "y", color="white")
        self.plot_widget.setLabel("bottom", "x", color="white")
        self.plot_widget.showGrid(x=True, y=True)

        if "y" not in expression:
            self.status_lbl.setText("Missing variable 'y' --> curve")
            self.y_start.setEnabled(False)
            self.y_end.setEnabled(False)
            self.y_steps.setEnabled(False)
        else:
            self.status_lbl.setText("Existing variable 'y' --> surface")
            self.surface = True

        status_str = "Define parameters for expression '" + expression + "'"
        self.status_lbl.setText(status_str)

        self.log.entry("__init__", True)

    #
    # -----------------------------------------------
    #

    def add_plot(self, expression):
        self.log.entry("add_plot(self, expression)", True)

        if "y" in expression and self.surface is False:
            self.status_lbl.setText("3D plot not available in 2D plot!")
            self.log.warning("3D plot not available in 2D plot!", True)
            return

        self.x_start.setText("")
        self.x_end.setText("")
        self.x_steps.setValue(1)

        self.y_start.setText("")
        self.y_end.setText("")
        self.y_steps.setValue(1)

        self.plot_title += "  ]|[  " + expression

        status_str = "Define parameters for expression '" + expression + "'"
        self.status_lbl.setText(status_str)

        self.log.exit("add_plot", True)

    #
    # -----------------------------------------------
    #

    def plot_curve(self, X, Y):
        self.log.entry("plot_curve(X, Y)", True)

        self.plot_widget.setTitle(self.plot_title, size="14pt")

        self.curve_number += 1

        self.status_lbl.setText("Plotting curve")
        pen = pg.mkPen(color=self.curve_colors[self.curve_number], width=2)
        self.plot_widget.plot(X, Y, pen=pen)
        self.status_lbl.setText("Finished")

        self.log.exit("plot_curve", True)

    #
    # -----------------------------------------------
    #

    def start(self):
        self.log.entry("start()", True)

        try:
            x_start = float(self.x_start.text())
            x_end   = float(self.x_end.text())
            x_steps = float(self.x_steps.text())
        except (ValueError, TypeError):
            self.status_lbl.setText("No valid x values")

        if self.curve:
            self.eval_curve.emit(x_start, x_end, x_steps)
            self.log.exit("start", True)
            return

        try:
            y_start = float(self.y_start.text())
            y_end   = float(self.y_end.text())
            y_steps = float(self.y_steps.text())
            self.eval_surface.emit(
                x_start, x_end, x_steps,
                y_start, y_end, y_steps
            )
        except (ValueError, TypeError):
            self.status_lbl.setText("No valid y values")

        self.log.exit("start", True)

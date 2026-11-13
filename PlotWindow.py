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

import pyqtgraph as pg
import pyqtgraph.opengl as gl

from pyqtgraph.Qt import QtGui

from PySide6 import QtWidgets

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
    eval_curve   = Signal(str, float, float, int)
    eval_surface = Signal(str, float, float, int, float, float, int)

    def __init__(self, expression, curve, surface):
        super().__init__()
        self.setupUi(self)
        self.log = Logging("PlotWindow", True)

        self.expression       = expression
        self.done             = False
        self.curve_number     = -1
        self.max_curves       = 6
        self.list_of_curves   = []
        self.surface_number   = -1
        self.list_of_surfaces = []

        self.log.entry("__init__(expression)")
        self.log.write(f"expression={expression}")

        self.curve   = curve
        self.surface = surface

        self.status_lbl = QLabel("Ready")
        self.status_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_bar.addWidget(self.status_lbl, 1)

        self.x_start.setValidator(QDoubleValidator(-1000, 1000, 15))
        self.x_end.setValidator(QDoubleValidator(-1000, 1000, 15))

        self.y_start.setValidator(QDoubleValidator(-1000, 1000, 15))
        self.y_end.setValidator(QDoubleValidator(-1000, 1000, 15))

        self.start_btn.clicked.connect(self.start)

        self.save_btn.clicked.connect(self.save)
        self.save_btn.setEnabled(False)

        self.clear_btn.clicked.connect(self.clear)
        self.clear_btn.setEnabled(False)

        status_str = "Define parameters for expression '" + expression + "'"
        self.status_lbl.setText(status_str)

        self.colors = ["white", "black", "red", "green", "blue", "yellow"]

        pg.setConfigOption('background', 'grey')
        pg.setConfigOption('foreground', 'white')

        plot_layout = QVBoxLayout()

        if not self.surface:

            self.setWindowTitle("2D-Plot")
            self.log.write(self.expression)

            self.y_start.setEnabled(False)
            self.y_end.setEnabled(False)
            self.y_steps.setEnabled(False)

            self.plot_widget = pg.PlotWidget()
            plot_layout.addWidget(self.plot_widget)
            self.bottom.setLayout(plot_layout)

            self.plot_widget.addLegend(labelTextSize='15pt')
            self.plot_widget.setLabel("left", "y", color="white")
            self.plot_widget.setLabel("bottom", "x", color="white")
            self.plot_widget.showGrid(x=True, y=True)

        else:

            self.setWindowTitle("3D-Plot")
            self.log.write(self.expression)

            self.plot_widget = gl.GLViewWidget()
            plot_layout.addWidget(self.plot_widget)
            self.bottom.setLayout(plot_layout)

            xgrid = gl.GLGridItem()
            self.plot_widget.addItem(xgrid)

        status_str = "Define parameters for expression '" + expression + "'"
        self.status_lbl.setText(status_str)

        self.log.exit("__init__")

    #
    # -----------------------------------------------
    #

    def add_plot(self, expression):
        self.log.entry("add_plot(self, expression)")

        if "y" in expression and self.surface is False:
            self.status_lbl.setText("3D plot not available in 2D plot!")
            self.log.warning("3D plot not available in 2D plot!")
            return

        if not self.done:
            self.status_lbl.setText("Previous plot not finished!")
            self.log.warning("Previous plot not finished!")
            return

        if self.curve and self.curve_number == (self.max_curves - 1):
            self.status_lbl.setText("Limit of curves reached!")
            self.log.warning("Limit of curves reached!")
            return

        self.expression   = expression
        self.done         = False

        self.x_start.setText("")
        self.x_end.setText("")
        self.x_steps.setValue(1)

        self.y_start.setText("")
        self.y_end.setText("")
        self.y_steps.setValue(1)

        status_str = "Define parameters for expression '" + expression + "'"
        self.status_lbl.setText(status_str)

        self.log.exit("add_plot")

    #
    # -----------------------------------------------
    #

    def clear(self):
        self.log.entry("clear()")

        self.plot_widget.clear()

        self.expression       = ""
        self.done             = True
        self.curve_number     = -1
        self.list_of_curves   = []
        self.surface_number   = -1
        self.list_of_surfaces = []

        self.x_start.setText("")
        self.x_end.setText("")
        self.x_steps.setValue(1)

        self.y_start.setText("")
        self.y_end.setText("")
        self.y_steps.setValue(1)

        self.X = None
        self.Y = None
        self.Z = None
        self.save_btn.setEnabled(False)
        self.clear_btn.setEnabled(False)

        if self.surface:
            self.setWindowTitle("3D-Plot")

        self.status_lbl.setText("Cleared!")

        self.log.exit("clear")

    #
    # -----------------------------------------------
    #

    def plot_curve(self, X, Y):
        self.log.entry("plot_curve(X, Y)")

        self.curve_number += 1

        self.status_lbl.setText("Plotting curve")
        pen = pg.mkPen(color=self.colors[self.curve_number], width=4)
        self.plot_widget.plot(X, Y, pen=pen, name=self.expression)
        self.status_lbl.setText("Finished")

        curve = {
            'number'     : self.curve_number,
            'expression' : self.expression,
            'color'      : self.colors[self.curve_number],
            'X'          : X,
            'Y'          : Y
        }
        self.list_of_curves.append(curve)

        self.expression = ""
        self.done = True

        self.save_btn.setEnabled(True)
        self.clear_btn.setEnabled(True)

        self.log.exit("plot_curve")

    #
    # -----------------------------------------------
    #

    def plot_surface(self, X, Y, Z):
        self.log.entry("plot_surface(X, Y, Z)")

        self.surface_number += 1

        self.status_lbl.setText("Plotting surface")
        surface = gl.GLSurfacePlotItem(
            x=X,
            y=Y,
            z=Z,
            shader='heightColor',
            computeNormals=False,
            smooth=True
        )
        self.plot_widget.addItem(surface)
        self.status_lbl.setText("Finished")

        surface = {
            'number'     : self.surface_number,
            'expression' : self.expression,
            'color'      : self.colors[self.curve_number],
            'X'          : X,
            'Y'          : Y,
            'Z'          : Z
        }
        self.list_of_surfaces.append(surface)

        self.setWindowTitle(f"3D-Plot: {self.expression}")

        self.expression = ""
        self.done = True

        self.save_btn.setEnabled(True)
        self.clear_btn.setEnabled(True)

        self.log.exit("plot_surface")

    #
    # -----------------------------------------------
    #

    def save(self):
        self.log.entry("save()")

        self.log.exit("save")

    #
    # -----------------------------------------------
    #

    def start(self):
        self.log.entry("start()")

        try:
            x_start = float(self.x_start.text())
            x_end   = float(self.x_end.text())
            x_steps = float(self.x_steps.text())
        except (ValueError, TypeError):
            self.status_lbl.setText("No valid x values")
            return

        if self.curve:
            self.eval_curve.emit(self.expression, x_start, x_end, x_steps)
            self.log.exit("start")
            return

        try:
            y_start = float(self.y_start.text())
            y_end   = float(self.y_end.text())
            y_steps = float(self.y_steps.text())
            self.eval_surface.emit(
                self.expression,
                x_start, x_end, x_steps,
                y_start, y_end, y_steps
            )
        except (ValueError, TypeError):
            self.status_lbl.setText("No valid y values")
            return

        self.log.exit("start")

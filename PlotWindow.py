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

import csv
import matplotlib
import pprint
import time

matplotlib.use('QtAgg')

import numpy as np

from pathlib import Path

from PySide6.QtCore import QLocale, QSize, Qt, Signal
from PySide6.QtGui import QDoubleValidator, QIcon
from PySide6.QtWidgets import (
    QColorDialog,
    QComboBox,
    QFileDialog,
    QInputDialog,
    QLabel,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout
)
from MiscHelpers import CustomToolbar, MplCanvas
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
        self.log = Logging("PlotWindow")
        self.log.entry(f"__init__(expression, {curve}, {surface})")
        self.log.write(f"expression='{expression}'")

        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        self.expression       = expression
        self.done             = False

        self.log.entry("__init__(expression)")
        self.log.write(f"expression={expression}")

        self.curve   = curve
        self.surface = surface

        self.status_lbl = QLabel("Ready")
        self.status_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_bar.addWidget(self.status_lbl, 1)

        validator = QDoubleValidator(-1000.0, 1000.0, 15, self)
        validator.setLocale(QLocale("en_US"))

        self.x_start.setValidator(validator)
        self.x_end.setValidator(validator)

        self.y_start.setValidator(validator)
        self.y_end.setValidator(validator)

        self.start_btn.clicked.connect(self.start)
        self.start_btn.setStyleSheet("""
            QPushButton:focus {
                color: white;
                background-color: green;
            }
            QPushButton:hover {
                color: white;
                background-color: green;
            }
        """)

        if self.curve:
            self.export_btn.clicked.connect(self.save_curve)
        else:
            self.export_btn.clicked.connect(self.save_surface)
        self.export_btn.setEnabled(False)
        self.export_btn.setStyleSheet("""
            QPushButton:focus {
                color: black;
                background-color: lightgray;
            }
            QPushButton:hover {
                color: black;
                background-color: lightgray;
            }
        """)

        self.clear_btn.clicked.connect(self.clear)
        self.clear_btn.setEnabled(False)
        self.clear_btn.setStyleSheet("""
            QPushButton:focus {
                color: white;
                background-color: red;
            }
            QPushButton:hover {
                color: white;
                background-color: red;
            }
        """)

        status_str = "Define parameters for expression '" + expression + "'"
        self.status_lbl.setText(status_str)

        plot_layout = QVBoxLayout()
        plot_layout.setContentsMargins(0, 0, 0, 0)

        while self.stack.count() > 0:
            widget = self.stack.widget(0)
            self.stack.removeWidget(widget)
            widget.deleteLater()

        self.color_dialog = QPushButton("Select color")
        self.stack.addWidget(self.color_dialog)
        self.color_dialog.clicked.connect(self.select_line_color)

        self.color_box = QComboBox()
        self.stack.addWidget(self.color_box)

        #from PySide6.QtWidgets import QSizePolicy
        #self.stack.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        #self.stack.setMinimumHeight(30)

        self.stack.setCurrentIndex(0)

        if not self.surface:

            self.setWindowTitle("Curve (2D) Plot")

            self.stack.setCurrentWidget(self.color_dialog)

            self.curve_number     = -1
            self.max_curves       = 10
            self.list_of_curves   = []
            self.list_of_c_expr   = []

            self.y_start.setEnabled(False)
            self.y_end.setEnabled(False)
            self.y_steps.setEnabled(False)

        else:

            self.setWindowTitle("Surface (3D) Plot")

            self.stack.setCurrentWidget(self.color_box)

            self.sequentials = {
                "viridis" : QIcon(":/ui/viridis.png"),
                "plasma"  : QIcon(":/ui/plasma.png"),
                "cividis" : QIcon(":/ui/cividis.png"),
                "Reds"    : QIcon(":/ui/Reds.png"),
                "Greens"  : QIcon(":/ui/Greens.png"),
                "Blues"   : QIcon(":/ui/Blues.png"),
                "Purples" : QIcon(":/ui/Purples.png"),
                "Greys"   : QIcon(":/ui/Greys.png")
            }

            self.color_box.setIconSize(QSize(425, 25))
            for text, icon in self.sequentials.items():
                self.color_box.addItem(icon, f"({text})")

            self.surface_number   = -1
            self.max_surfaces     = len(self.sequentials)
            self.list_of_surfaces = []
            self.list_of_s_expr   = []

        self.log.write(self.expression)

        self.plot_widget = MplCanvas(
            self,
            width=6, height=4, dpi=100,
            curve=self.curve, surface=self.surface
        )

        self.toolbar = CustomToolbar(self.plot_widget, self)
        self.toolbar.setStyleSheet("""
            QToolBar {
                background-color: lightgray;
                border: none;
                spacing: 4px;
            }
            QLabel {
                color: black;
            }
        """)

        plot_layout.addWidget(self.toolbar)
        plot_layout.addWidget(self.plot_widget)
        self.bottom.setLayout(plot_layout)

        self.plot_widget.axes.set_xlabel("x")
        self.plot_widget.axes.set_ylabel("y")
        if self.surface:
            self.plot_widget.axes.set_zlabel("z")

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
            self.log.exit("add_plot")
            return

        if not self.done:
            self.status_lbl.setText("Previous plot not finished!")
            self.log.warning("Previous plot not finished!")
            self.log.exit("add_plot")
            return

        if self.curve and self.curve_number == (self.max_curves - 1):
            self.status_lbl.setText("Limit of curves reached!")
            self.log.warning("Limit of curves reached!")
            self.log.exit("add_plot")
            return

        if self.surface and self.surface_number == (self.max_surfaces - 1):
            self.status_lbl.setText("Limit of surfaces reached!")
            self.log.warning("Limit of surfaces reached!")
            self.log.exit("add_plot")
            return

        self.expression   = expression
        self.done         = False

        self.x_start.setEnabled(True)
        self.x_end.setEnabled(True)
        self.x_steps.setEnabled(True)

        if self.surface:
            self.y_start.setEnabled(True)
            self.y_end.setEnabled(True)
            self.y_steps.setEnabled(True)

        self.x_start.setText("")
        self.x_end.setText("")
        self.x_steps.setValue(1)

        self.y_start.setText("")
        self.y_end.setText("")
        self.y_steps.setValue(1)

        self.start_btn.setEnabled(True)

        status_str = "Define parameters for expression '" + expression + "'"
        self.status_lbl.setText(status_str)

        self.log.exit("add_plot")

    #
    # -----------------------------------------------
    #

    def clear(self):
        self.log.entry("clear()")

        self.plot_widget.axes.clear()
        self.plot_widget.setup_axes()

        self.plot_widget.axes.set_xlabel("x")
        self.plot_widget.axes.set_ylabel("y")
        if self.surface:
            self.plot_widget.axes.set_zlabel("z")
        self.plot_widget.draw()

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
        self.start_btn.setEnabled(False)
        self.export_btn.setEnabled(False)
        self.clear_btn.setEnabled(False)

        self.x_start.setEnabled(False)
        self.x_end.setEnabled(False)
        self.x_steps.setEnabled(False)

        self.y_start.setEnabled(False)
        self.y_end.setEnabled(False)
        self.y_steps.setEnabled(False)

        self.status_lbl.setText("Cleared!")

        self.log.exit("clear")

    #
    # -----------------------------------------------
    #

    def keyPressEvent(self, event):
        self.log.entry("keyPressEvent(event)")

        key = event.key()

        if key in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            if self.start_btn.hasFocus():
                self.start()
                event.accept()
                self.log.exit("keyPressEvent")
                return
            elif self.export_btn.hasFocus():
                if self.curve:
                    self.save_curve()
                else:
                    self.save_surface()
                event.accept()
                self.log.exit("keyPressEvent")
                return
            elif self.clear_btn.hasFocus():
                self.clear()
                event.accept()
                self.log.exit("keyPressEvent")
                return

        if key == Qt.Key.Key_Escape:
            self.close()
            event.accept()
            self.log.exit("keyPressEvent")
            return

        super().keyPressEvent(event)

        self.log.exit("keyPressEvent")

    #
    # -----------------------------------------------
    #

    def plot_curve(self, X, Y, connections):
        self.log.entry("plot_curve(X, Y)")

        self.curve_number += 1

        self.status_lbl.setText("Plotting curve")
        self.plot_widget.axes.plot(
            X, Y,
            color=self.line_color.name(),
            label=self.expression
        )
        self.plot_widget.axes.legend()
        self.plot_widget.draw()

        self.status_lbl.setText("Finished")

        curve = {
            'number'     : self.curve_number,
            'expression' : self.expression,
            'color'      : self.line_color,
            'X'          : X,
            'Y'          : Y
        }
        self.list_of_curves.append(curve)
        self.list_of_c_expr.append(curve['expression'])

        self.expression = ""
        self.done = True

        self.export_btn.setEnabled(True)
        self.clear_btn.setEnabled(True)

        self.log.exit("plot_curve")

    #
    # -----------------------------------------------
    #

    def plot_surface(self, X, Y, Z):
        self.log.entry("plot_surface(X, Y, Z)")

        self.surface_number += 1

        self.status_lbl.setText("Plotting surface")

        selected_color = self.color_box.currentText()
        color_text     = selected_color.replace("(", "").replace(")", "")
        self.plot_widget.axes.plot_surface(
            X, Y, Z,
            cmap=color_text, edgecolor='none',
            label=self.expression
        )
        self.plot_widget.axes.legend()
        self.plot_widget.draw()

        self.status_lbl.setText("Finished")

        surface_item = {
            'number'     : self.surface_number,
            'expression' : self.expression,
            'color'      : color_text,
            'X'          : X,
            'Y'          : Y,
            'Z'          : Z
        }
        self.list_of_surfaces.append(surface_item)
        self.list_of_s_expr.append(surface_item['expression'])

        self.expression = ""
        self.done = True

        self.export_btn.setEnabled(True)
        self.clear_btn.setEnabled(True)

        self.log.exit("plot_surface")

    #
    # -----------------------------------------------
    #

    def save_curve(self):
        self.log.entry("save_curve()")

        selected_expression, ok = QInputDialog.getItem(
            self,
            "Select a curve",
            "Select a curve from the list:",
            self.list_of_c_expr,
            current=0,
            editable=False,
        )

        if not ok:
            self.log.exit("save_curve")
            return

        # Choose selected item from list of curves
        for element in self.list_of_curves:
            if selected_expression == element['expression']:
                self.selected_curve = element
                break

        #
        # Select directory where to save the data of the curve
        #

        folder_path = QFileDialog.getExistingDirectory(
            self,
            caption="Select folder to save data of the curve",
            dir=str(Path.home()),
            options=QFileDialog.ShowDirsOnly
        )

        if folder_path:

            dir_time = time.time()
            csv_file_name = f"qtCalc-X_Y-data_{dir_time}.csv"
            full_path_name = folder_path + "/" + csv_file_name

            try:
                with open(full_path_name, "w", newline="", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow(["X", self.selected_curve['expression']])  # Header
                    writer.writerows(zip(
                        self.selected_curve['X'],
                        self.selected_curve['Y']
                    ))
            except FileExistsError:
                msg = "File already exists!"
                QMessageBox.warning(self, "Warning!", msg)
                self.log.warning(msg)
                self.log.exit("save_curve")
                return
            except PermissionError:
                msg = "No permission to create file!"
                QMessageBox.warning(self, "Warning!", msg)
                self.log.warning(msg)
                self.log.exit("save_curve")
                return
            except OSError as e:
                msg = f"General file system error: {e}"
                QMessageBox.warning(self, "Warning!", msg)
                self.log.warning(msg)
                self.log.exit("save_curve")
                return

            msg = f"Curve data file\n {csv_file_name}\n successful saved."
            QMessageBox.information(self, "Data saved", msg)

        self.log.exit("save_curve")

    #
    # -----------------------------------------------
    #

    def save_surface(self):
        self.log.entry("save_surface()")

        selected_expression, ok = QInputDialog.getItem(
            self,
            "Select a surface",
            "Select a surface from the list:",
            self.list_of_s_expr,
            current=0,
            editable=False,
        )

        if not ok:
            self.log.exit("save_surface")
            return

        # Choose selected item from list of surfaces
        for element in self.list_of_surfaces:
            if selected_expression == element['expression']:
                self.selected_surface = element
                break

        #
        # Select directory where to save the data of the curve
        #

        folder_path = QFileDialog.getExistingDirectory(
            self,
            caption="Select folder to save data of the curve",
            dir=str(Path.home()),
            options=QFileDialog.ShowDirsOnly
        )

        if folder_path:

            dir_time = time.time()
            csv_file_name = f"qtCalc-X_Y_Z-data_{dir_time}.csv"
            full_path_name = folder_path + "/" + csv_file_name

            X = self.selected_surface['X']
            Y = self.selected_surface['Y']
            Z = self.selected_surface['Z']

            grid_with_y = np.column_stack((Y, Z))

            try:
                with open(full_path_name, "x") as f:
                    np.savetxt(
                        f,
                        grid_with_y,
                        footer=self.selected_surface['expression'],
                        delimiter=",", fmt="%.20g", encoding="utf-8",
                        header="y\\x," + ",".join(map(str, X))
                    )
            except FileExistsError:
                msg = "File already exists!"
                QMessageBox.warning(self, "Warning!", msg)
                self.log.warning(msg)
                self.log.exit("save_surface")
                return
            except PermissionError:
                msg = "No permission to create file!"
                QMessageBox.warning(self, "Warning!", msg)
                self.log.warning(msg)
                self.log.exit("save_surface")
                return
            except OSError as e:
                msg = f"General file system error: {e}"
                QMessageBox.warning(self, "Warning!", msg)
                self.log.warning(msg)
                self.log.exit("save_surface")
                return

            msg = f"Surface data file\n {csv_file_name}\n successful saved."
            QMessageBox.information(self, "Data saved", msg)

        self.log.exit("save_surface")

    #
    # -----------------------------------------------
    #

    def select_line_color(self):
        new_bg_color = QColorDialog.getColor(
            parent=self,
            title="Select curve color"
        )
        if new_bg_color.isValid():
            self.line_color = new_bg_color

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

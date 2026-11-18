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

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from Logging import Logging


#
# -----------------------------------------------
#

class MplCanvas(FigureCanvas):
    def __init__(
            self, parent=None,
            width=5, height=4, dpi=100,
            curve=False, surface=False
        ):

        self.fig = Figure(
            figsize=(width, height),
            dpi=dpi,
            facecolor="darkgray",
            layout="constrained"
        )

        super().__init__(self.fig)

        self.curve   = curve
        self.surface = surface

        if curve:
            self.axes = self.fig.add_subplot()
        else:
            self.axes = self.fig.add_subplot(projection='3d')

        self.axes.set_facecolor("gray")

        self.setup_axes()

        for spine in self.axes.spines.values():
            spine.set_edgecolor("white")

        self.axes.grid(True, color="white", linestyle="--", linewidth=0.5)

    #
    # -----------------------------------------------
    #

    def setup_axes(self):

        self.axes.tick_params(colors="white", which="both")
        self.axes.xaxis.label.set_color("white")
        self.axes.yaxis.label.set_color("white")
        if self.surface:
            self.axes.zaxis.label.set_color("white")
        self.axes.title.set_color("white")
        self.axes.grid(True)


#
# -----------------------------------------------
#

class CustomToolbar(NavigationToolbar):

    # (name, tooltip, icon name, method)
    toolitems = [
        ("Home", "Reset original view", "home", "home"),
        ("Back", "Back to previous view", "back", "back"),
        ("Forward", "Forward to next view", "forward", "forward"),
        (None, None, None, None),
        ("Pan", "Pan / Scale", "move", "pan"),
        ("Zoom", "Zoom", "zoom_to_rect", "zoom"),
        # ("Subplots", "Configure axes", "subplots", "configure_subplots"),
        # (None, None, None, None),
        ("Save", "Save plot as image", "filesave", "save_figure"),
    ]

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PlotWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_PlotWindow(object):
    def setupUi(self, PlotWindow):
        if not PlotWindow.objectName():
            PlotWindow.setObjectName(u"PlotWindow")
        PlotWindow.resize(600, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PlotWindow.sizePolicy().hasHeightForWidth())
        PlotWindow.setSizePolicy(sizePolicy)
        PlotWindow.setMinimumSize(QSize(600, 600))
        self.centralwidget = QWidget(PlotWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 5, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 0, 3, 1, 1)

        self.y_end = QLineEdit(self.centralwidget)
        self.y_end.setObjectName(u"y_end")
        self.y_end.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.y_end, 1, 4, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 2, 3, 1, 1)

        self.x_start = QLineEdit(self.centralwidget)
        self.x_start.setObjectName(u"x_start")
        self.x_start.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.x_start, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.x_end = QLineEdit(self.centralwidget)
        self.x_end.setObjectName(u"x_end")
        self.x_end.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.x_end, 1, 1, 1, 1)

        self.y_start = QLineEdit(self.centralwidget)
        self.y_start.setObjectName(u"y_start")
        self.y_start.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.y_start, 0, 4, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 3, 1, 1)

        self.x_steps = QSpinBox(self.centralwidget)
        self.x_steps.setObjectName(u"x_steps")
        self.x_steps.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.x_steps.setMinimum(1)
        self.x_steps.setMaximum(10000)

        self.gridLayout_2.addWidget(self.x_steps, 2, 1, 1, 1)

        self.y_steps = QSpinBox(self.centralwidget)
        self.y_steps.setObjectName(u"y_steps")
        self.y_steps.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.y_steps.setMinimum(1)
        self.y_steps.setMaximum(10000)

        self.gridLayout_2.addWidget(self.y_steps, 2, 4, 1, 1)

        self.start_btn = QPushButton(self.centralwidget)
        self.start_btn.setObjectName(u"start_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.start_btn.sizePolicy().hasHeightForWidth())
        self.start_btn.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(20)
        font.setWeight(QFont.DemiBold)
        self.start_btn.setFont(font)
        self.start_btn.setStyleSheet(u"background-color: green;\n"
"color: white;")

        self.gridLayout_2.addWidget(self.start_btn, 0, 6, 1, 1)

        self.clear_btn = QPushButton(self.centralwidget)
        self.clear_btn.setObjectName(u"clear_btn")
        sizePolicy1.setHeightForWidth(self.clear_btn.sizePolicy().hasHeightForWidth())
        self.clear_btn.setSizePolicy(sizePolicy1)
        self.clear_btn.setFont(font)

        self.gridLayout_2.addWidget(self.clear_btn, 2, 6, 1, 1)

        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 1)
        self.gridLayout_2.setRowStretch(2, 1)
        self.gridLayout_2.setColumnStretch(5, 1)

        self.verticalLayout.addLayout(self.gridLayout_2)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        font1 = QFont()
        font1.setBold(False)
        self.line.setFont(font1)
        self.line.setFrameShadow(QFrame.Shadow.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout.addWidget(self.line)

        self.bottom = QWidget(self.centralwidget)
        self.bottom.setObjectName(u"bottom")

        self.verticalLayout.addWidget(self.bottom)

        self.verticalLayout.setStretch(2, 5)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        PlotWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(PlotWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 600, 30))
        PlotWindow.setMenuBar(self.menubar)
        self.status_bar = QStatusBar(PlotWindow)
        self.status_bar.setObjectName(u"status_bar")
        PlotWindow.setStatusBar(self.status_bar)

        self.retranslateUi(PlotWindow)

        QMetaObject.connectSlotsByName(PlotWindow)
    # setupUi

    def retranslateUi(self, PlotWindow):
        PlotWindow.setWindowTitle(QCoreApplication.translate("PlotWindow", u"MainWindow", None))
        self.label_4.setText(QCoreApplication.translate("PlotWindow", u"y-Start:", None))
        self.label_5.setText(QCoreApplication.translate("PlotWindow", u"y-Steps:", None))
        self.label_2.setText(QCoreApplication.translate("PlotWindow", u"x-End:", None))
        self.label_6.setText(QCoreApplication.translate("PlotWindow", u"x-Steps:", None))
        self.label.setText(QCoreApplication.translate("PlotWindow", u"x-Start:", None))
        self.label_3.setText(QCoreApplication.translate("PlotWindow", u"y-End:", None))
        self.start_btn.setText(QCoreApplication.translate("PlotWindow", u"Start", None))
        self.clear_btn.setText(QCoreApplication.translate("PlotWindow", u"Clear", None))
    # retranslateUi


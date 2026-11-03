# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(750, 600)
        MainWindow.setMinimumSize(QSize(750, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout.addWidget(self.textBrowser)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushButton_20 = QPushButton(self.centralwidget)
        self.pushButton_20.setObjectName(u"pushButton_20")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_20.sizePolicy().hasHeightForWidth())
        self.pushButton_20.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.pushButton_20, 0, 0, 1, 1)

        self.pushButton_47 = QPushButton(self.centralwidget)
        self.pushButton_47.setObjectName(u"pushButton_47")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_47.sizePolicy().hasHeightForWidth())
        self.pushButton_47.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(25)
        font.setWeight(QFont.ExtraBold)
        self.pushButton_47.setFont(font)

        self.gridLayout_3.addWidget(self.pushButton_47, 1, 7, 1, 1)

        self.pushButton_10 = QPushButton(self.centralwidget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy1.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.pushButton_10, 5, 0, 1, 1)

        self.pushButton_13 = QPushButton(self.centralwidget)
        self.pushButton_13.setObjectName(u"pushButton_13")
        sizePolicy1.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.pushButton_13, 4, 2, 1, 1)

        self.btn_3 = QPushButton(self.centralwidget)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy1.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy1)
        self.btn_3.setFont(font)

        self.gridLayout_3.addWidget(self.btn_3, 4, 8, 1, 1)

        self.pushButton_32 = QPushButton(self.centralwidget)
        self.pushButton_32.setObjectName(u"pushButton_32")
        sizePolicy1.setHeightForWidth(self.pushButton_32.sizePolicy().hasHeightForWidth())
        self.pushButton_32.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.pushButton_32, 2, 1, 1, 1)

        self.btn_8 = QPushButton(self.centralwidget)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy1.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy1)
        self.btn_8.setFont(font)

        self.gridLayout_3.addWidget(self.btn_8, 2, 7, 1, 1)

        self.btn_0 = QPushButton(self.centralwidget)
        self.btn_0.setObjectName(u"btn_0")
        sizePolicy1.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy1)
        self.btn_0.setFont(font)

        self.gridLayout_3.addWidget(self.btn_0, 5, 6, 1, 1)

        self.pushButton_42 = QPushButton(self.centralwidget)
        self.pushButton_42.setObjectName(u"pushButton_42")
        sizePolicy1.setHeightForWidth(self.pushButton_42.sizePolicy().hasHeightForWidth())
        self.pushButton_42.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.pushButton_42, 1, 1, 1, 1)

        self.btn_4 = QPushButton(self.centralwidget)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy1.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy1)
        self.btn_4.setFont(font)

        self.gridLayout_3.addWidget(self.btn_4, 3, 6, 1, 1)

        self.btn_log = QPushButton(self.centralwidget)
        self.btn_log.setObjectName(u"btn_log")
        sizePolicy1.setHeightForWidth(self.btn_log.sizePolicy().hasHeightForWidth())
        self.btn_log.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(25)
        font1.setWeight(QFont.DemiBold)
        self.btn_log.setFont(font1)

        self.gridLayout_3.addWidget(self.btn_log, 5, 3, 1, 1)

        self.pushButton_21 = QPushButton(self.centralwidget)
        self.pushButton_21.setObjectName(u"pushButton_21")
        sizePolicy1.setHeightForWidth(self.pushButton_21.sizePolicy().hasHeightForWidth())
        self.pushButton_21.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.pushButton_21, 3, 0, 1, 1)

        self.pushButton_44 = QPushButton(self.centralwidget)
        self.pushButton_44.setObjectName(u"pushButton_44")
        sizePolicy1.setHeightForWidth(self.pushButton_44.sizePolicy().hasHeightForWidth())
        self.pushButton_44.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.pushButton_44, 1, 3, 1, 1)

        self.pushButton_30 = QPushButton(self.centralwidget)
        self.pushButton_30.setObjectName(u"pushButton_30")
        sizePolicy.setHeightForWidth(self.pushButton_30.sizePolicy().hasHeightForWidth())
        self.pushButton_30.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.pushButton_30, 0, 10, 1, 1)

        self.pushButton_15 = QPushButton(self.centralwidget)
        self.pushButton_15.setObjectName(u"pushButton_15")
        sizePolicy1.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy1)
        self.pushButton_15.setFont(font1)

        self.gridLayout_3.addWidget(self.pushButton_15, 4, 4, 1, 1)

        self.pushButton_23 = QPushButton(self.centralwidget)
        self.pushButton_23.setObjectName(u"pushButton_23")
        sizePolicy1.setHeightForWidth(self.pushButton_23.sizePolicy().hasHeightForWidth())
        self.pushButton_23.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.pushButton_23, 3, 2, 1, 1)

        self.btn_6 = QPushButton(self.centralwidget)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy1.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy1)
        self.btn_6.setFont(font)

        self.gridLayout_3.addWidget(self.btn_6, 3, 8, 1, 1)

        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy1.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy1)
        self.pushButton_6.setFont(font1)

        self.gridLayout_3.addWidget(self.pushButton_6, 5, 4, 1, 1)

        self.btn_div_by = QPushButton(self.centralwidget)
        self.btn_div_by.setObjectName(u"btn_div_by")
        sizePolicy1.setHeightForWidth(self.btn_div_by.sizePolicy().hasHeightForWidth())
        self.btn_div_by.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(25)
        font2.setBold(True)
        self.btn_div_by.setFont(font2)

        self.gridLayout_3.addWidget(self.btn_div_by, 2, 9, 1, 1)

        self.pushButton_14 = QPushButton(self.centralwidget)
        self.pushButton_14.setObjectName(u"pushButton_14")
        sizePolicy1.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy1)
        self.pushButton_14.setFont(font1)

        self.gridLayout_3.addWidget(self.pushButton_14, 4, 3, 1, 1)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy1.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy1)
        self.pushButton_4.setFont(font2)

        self.gridLayout_3.addWidget(self.pushButton_4, 5, 7, 1, 1)

        self.pushButton_22 = QPushButton(self.centralwidget)
        self.pushButton_22.setObjectName(u"pushButton_22")
        sizePolicy1.setHeightForWidth(self.pushButton_22.sizePolicy().hasHeightForWidth())
        self.pushButton_22.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.pushButton_22, 3, 1, 1, 1)

        self.btn_5 = QPushButton(self.centralwidget)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy1.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy1)
        self.btn_5.setFont(font)

        self.gridLayout_3.addWidget(self.btn_5, 3, 7, 1, 1)

        self.btn_times = QPushButton(self.centralwidget)
        self.btn_times.setObjectName(u"btn_times")
        sizePolicy1.setHeightForWidth(self.btn_times.sizePolicy().hasHeightForWidth())
        self.btn_times.setSizePolicy(sizePolicy1)
        self.btn_times.setFont(font)

        self.gridLayout_3.addWidget(self.btn_times, 3, 9, 1, 1)

        self.pushButton_40 = QPushButton(self.centralwidget)
        self.pushButton_40.setObjectName(u"pushButton_40")
        sizePolicy1.setHeightForWidth(self.pushButton_40.sizePolicy().hasHeightForWidth())
        self.pushButton_40.setSizePolicy(sizePolicy1)
        self.pushButton_40.setFont(font)

        self.gridLayout_3.addWidget(self.pushButton_40, 2, 10, 1, 1)

        self.pushButton_33 = QPushButton(self.centralwidget)
        self.pushButton_33.setObjectName(u"pushButton_33")
        sizePolicy1.setHeightForWidth(self.pushButton_33.sizePolicy().hasHeightForWidth())
        self.pushButton_33.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.pushButton_33, 2, 2, 1, 1)

        self.pushButton_35 = QPushButton(self.centralwidget)
        self.pushButton_35.setObjectName(u"pushButton_35")
        sizePolicy1.setHeightForWidth(self.pushButton_35.sizePolicy().hasHeightForWidth())
        self.pushButton_35.setSizePolicy(sizePolicy1)
        self.pushButton_35.setFont(font1)

        self.gridLayout_3.addWidget(self.pushButton_35, 2, 4, 1, 1)

        self.btn_plus = QPushButton(self.centralwidget)
        self.btn_plus.setObjectName(u"btn_plus")
        sizePolicy1.setHeightForWidth(self.btn_plus.sizePolicy().hasHeightForWidth())
        self.btn_plus.setSizePolicy(sizePolicy1)
        self.btn_plus.setFont(font)

        self.gridLayout_3.addWidget(self.btn_plus, 5, 9, 1, 1)

        self.btn_7 = QPushButton(self.centralwidget)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy1.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy1)
        self.btn_7.setFont(font)

        self.gridLayout_3.addWidget(self.btn_7, 2, 6, 1, 1)

        self.pushButton_31 = QPushButton(self.centralwidget)
        self.pushButton_31.setObjectName(u"pushButton_31")
        sizePolicy1.setHeightForWidth(self.pushButton_31.sizePolicy().hasHeightForWidth())
        self.pushButton_31.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.pushButton_31, 2, 0, 1, 1)

        self.pushButton_41 = QPushButton(self.centralwidget)
        self.pushButton_41.setObjectName(u"pushButton_41")
        sizePolicy1.setHeightForWidth(self.pushButton_41.sizePolicy().hasHeightForWidth())
        self.pushButton_41.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.pushButton_41, 1, 0, 1, 1)

        self.btn_minus = QPushButton(self.centralwidget)
        self.btn_minus.setObjectName(u"btn_minus")
        sizePolicy1.setHeightForWidth(self.btn_minus.sizePolicy().hasHeightForWidth())
        self.btn_minus.setSizePolicy(sizePolicy1)
        self.btn_minus.setFont(font)

        self.gridLayout_3.addWidget(self.btn_minus, 4, 9, 1, 1)

        self.pushButton_43 = QPushButton(self.centralwidget)
        self.pushButton_43.setObjectName(u"pushButton_43")
        sizePolicy1.setHeightForWidth(self.pushButton_43.sizePolicy().hasHeightForWidth())
        self.pushButton_43.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.pushButton_43, 1, 2, 1, 1)

        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy1.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.pushButton_8, 5, 2, 1, 1)

        self.btn_9 = QPushButton(self.centralwidget)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy1.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy1)
        self.btn_9.setFont(font)

        self.gridLayout_3.addWidget(self.btn_9, 2, 8, 1, 1)

        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy1.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.pushButton_9, 5, 1, 1, 1)

        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy1.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy1)
        self.btn_2.setFont(font)

        self.gridLayout_3.addWidget(self.btn_2, 4, 7, 1, 1)

        self.pushButton_48 = QPushButton(self.centralwidget)
        self.pushButton_48.setObjectName(u"pushButton_48")
        sizePolicy1.setHeightForWidth(self.pushButton_48.sizePolicy().hasHeightForWidth())
        self.pushButton_48.setSizePolicy(sizePolicy1)
        self.pushButton_48.setFont(font)

        self.gridLayout_3.addWidget(self.pushButton_48, 1, 8, 1, 1)

        self.pushButton_11 = QPushButton(self.centralwidget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy1.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.pushButton_11, 4, 0, 1, 1)

        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy1.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy1)
        self.btn_1.setFont(font)

        self.gridLayout_3.addWidget(self.btn_1, 4, 6, 1, 1)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy1.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy1)
        self.pushButton_3.setFont(font)

        self.gridLayout_3.addWidget(self.pushButton_3, 5, 8, 1, 1)

        self.pushButton_24 = QPushButton(self.centralwidget)
        self.pushButton_24.setObjectName(u"pushButton_24")
        sizePolicy1.setHeightForWidth(self.pushButton_24.sizePolicy().hasHeightForWidth())
        self.pushButton_24.setSizePolicy(sizePolicy1)
        self.pushButton_24.setFont(font1)

        self.gridLayout_3.addWidget(self.pushButton_24, 3, 3, 1, 1)

        self.pushButton_25 = QPushButton(self.centralwidget)
        self.pushButton_25.setObjectName(u"pushButton_25")
        sizePolicy1.setHeightForWidth(self.pushButton_25.sizePolicy().hasHeightForWidth())
        self.pushButton_25.setSizePolicy(sizePolicy1)
        self.pushButton_25.setFont(font1)

        self.gridLayout_3.addWidget(self.pushButton_25, 3, 4, 1, 1)

        self.pushButton_34 = QPushButton(self.centralwidget)
        self.pushButton_34.setObjectName(u"pushButton_34")
        sizePolicy1.setHeightForWidth(self.pushButton_34.sizePolicy().hasHeightForWidth())
        self.pushButton_34.setSizePolicy(sizePolicy1)
        self.pushButton_34.setFont(font1)

        self.gridLayout_3.addWidget(self.pushButton_34, 2, 3, 1, 1)

        self.pushButton_46 = QPushButton(self.centralwidget)
        self.pushButton_46.setObjectName(u"pushButton_46")
        sizePolicy1.setHeightForWidth(self.pushButton_46.sizePolicy().hasHeightForWidth())
        self.pushButton_46.setSizePolicy(sizePolicy1)
        self.pushButton_46.setFont(font)

        self.gridLayout_3.addWidget(self.pushButton_46, 1, 6, 1, 1)

        self.pushButton_45 = QPushButton(self.centralwidget)
        self.pushButton_45.setObjectName(u"pushButton_45")
        sizePolicy1.setHeightForWidth(self.pushButton_45.sizePolicy().hasHeightForWidth())
        self.pushButton_45.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.pushButton_45, 1, 4, 1, 1)

        self.btn_equals = QPushButton(self.centralwidget)
        self.btn_equals.setObjectName(u"btn_equals")
        sizePolicy1.setHeightForWidth(self.btn_equals.sizePolicy().hasHeightForWidth())
        self.btn_equals.setSizePolicy(sizePolicy1)
        self.btn_equals.setFont(font)

        self.gridLayout_3.addWidget(self.btn_equals, 3, 10, 3, 1)

        self.pushButton_12 = QPushButton(self.centralwidget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy1.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.pushButton_12, 4, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 3, 5, 1, 1)

        self.btn_forward = QPushButton(self.centralwidget)
        self.btn_forward.setObjectName(u"btn_forward")
        sizePolicy1.setHeightForWidth(self.btn_forward.sizePolicy().hasHeightForWidth())
        self.btn_forward.setSizePolicy(sizePolicy1)
        self.btn_forward.setFont(font)

        self.gridLayout_3.addWidget(self.btn_forward, 1, 9, 1, 1)

        self.btn_backward = QPushButton(self.centralwidget)
        self.btn_backward.setObjectName(u"btn_backward")
        sizePolicy1.setHeightForWidth(self.btn_backward.sizePolicy().hasHeightForWidth())
        self.btn_backward.setSizePolicy(sizePolicy1)
        self.btn_backward.setFont(font)

        self.gridLayout_3.addWidget(self.btn_backward, 1, 10, 1, 1)

        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 1)
        self.gridLayout_3.setColumnStretch(2, 1)
        self.gridLayout_3.setColumnStretch(3, 1)
        self.gridLayout_3.setColumnStretch(4, 1)
        self.gridLayout_3.setColumnStretch(6, 1)
        self.gridLayout_3.setColumnStretch(7, 1)
        self.gridLayout_3.setColumnStretch(8, 1)
        self.gridLayout_3.setColumnStretch(9, 1)
        self.gridLayout_3.setColumnStretch(10, 1)

        self.verticalLayout.addLayout(self.gridLayout_3)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 3)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 750, 30))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_47.setText(QCoreApplication.translate("MainWindow", u",", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_32.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_42.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_log.setText(QCoreApplication.translate("MainWindow", u"log", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_44.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"x\u00b2", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"10\u02e3", None))
        self.btn_div_by.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"\u221a", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u00b1", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_times.setText(QCoreApplication.translate("MainWindow", u"\u2716\ufe0f", None))
        self.pushButton_40.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"x\u02b8", None))
        self.btn_plus.setText(QCoreApplication.translate("MainWindow", u"\u271a", None))
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_41.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_minus.setText(QCoreApplication.translate("MainWindow", u"\u2796", None))
        self.pushButton_43.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_48.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"\u221b", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"x\u00b3", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"\u02b8\u221ax", None))
        self.pushButton_46.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.pushButton_45.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_equals.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_forward.setText(QCoreApplication.translate("MainWindow", u"\u2190", None))
        self.btn_backward.setText(QCoreApplication.translate("MainWindow", u"\u2192", None))
    # retranslateUi


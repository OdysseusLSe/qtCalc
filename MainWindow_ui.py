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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTextBrowser, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(750, 500)
        MainWindow.setMinimumSize(QSize(750, 500))
        MainWindow.setMaximumSize(QSize(750, 500))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        font = QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet(u"background-color: palegoldenrod;\n"
"color: black;\n"
"border: 5px solid;")
        self.textBrowser.setFrameShadow(QFrame.Shadow.Sunken)
        self.textBrowser.setLineWidth(1)

        self.verticalLayout.addWidget(self.textBrowser)

        self.gridLayout_3 = QGridLayout()
#ifndef Q_OS_MACOS
        self.gridLayout_3.setSpacing(-1)
#endif
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushButton_20 = QPushButton(self.centralwidget)
        self.pushButton_20.setObjectName(u"pushButton_20")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_20.sizePolicy().hasHeightForWidth())
        self.pushButton_20.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.pushButton_20, 0, 0, 1, 1)

        self.btn_comma = QPushButton(self.centralwidget)
        self.btn_comma.setObjectName(u"btn_comma")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_comma.sizePolicy().hasHeightForWidth())
        self.btn_comma.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(25)
        font1.setWeight(QFont.ExtraBold)
        self.btn_comma.setFont(font1)
        self.btn_comma.setStyleSheet(u"background-color: rgb(128, 128, 128);\n"
"color: white;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.btn_comma, 1, 7, 1, 1)

        self.btn_max = QPushButton(self.centralwidget)
        self.btn_max.setObjectName(u"btn_max")
        sizePolicy1.setHeightForWidth(self.btn_max.sizePolicy().hasHeightForWidth())
        self.btn_max.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(25)
        font2.setWeight(QFont.DemiBold)
        self.btn_max.setFont(font2)
        self.btn_max.setStyleSheet(u"background-color: lightgrey;\n"
"color: black;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.btn_max, 5, 0, 1, 1)

        self.btn_cos = QPushButton(self.centralwidget)
        self.btn_cos.setObjectName(u"btn_cos")
        sizePolicy1.setHeightForWidth(self.btn_cos.sizePolicy().hasHeightForWidth())
        self.btn_cos.setSizePolicy(sizePolicy1)
        self.btn_cos.setFont(font2)
        self.btn_cos.setStyleSheet(u"background-color: lightgrey;\n"
"color: black;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.btn_cos, 4, 2, 1, 1)

        self.btn_3 = QPushButton(self.centralwidget)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy1.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy1)
        self.btn_3.setFont(font1)
        self.btn_3.setStyleSheet(u"background-color: black;\n"
"color: white;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.btn_3, 4, 8, 1, 1)

        self.pushButton_32 = QPushButton(self.centralwidget)
        self.pushButton_32.setObjectName(u"pushButton_32")
        sizePolicy1.setHeightForWidth(self.pushButton_32.sizePolicy().hasHeightForWidth())
        self.pushButton_32.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setPointSize(25)
        self.pushButton_32.setFont(font3)
        self.pushButton_32.setStyleSheet(u"background-color: lightgrey;\n"
"color: black;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.pushButton_32, 2, 1, 1, 1)

        self.btn_8 = QPushButton(self.centralwidget)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy1.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy1)
        self.btn_8.setFont(font1)
        self.btn_8.setStyleSheet(u"background-color: black;\n"
"color: white;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.btn_8, 2, 7, 1, 1)

        self.btn_0 = QPushButton(self.centralwidget)
        self.btn_0.setObjectName(u"btn_0")
        sizePolicy1.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy1)
        self.btn_0.setFont(font1)
        self.btn_0.setStyleSheet(u"background-color: black;\n"
"color: white;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.btn_0, 5, 6, 1, 1)

        self.btn_pi = QPushButton(self.centralwidget)
        self.btn_pi.setObjectName(u"btn_pi")
        sizePolicy1.setHeightForWidth(self.btn_pi.sizePolicy().hasHeightForWidth())
        self.btn_pi.setSizePolicy(sizePolicy1)
        self.btn_pi.setFont(font3)
        self.btn_pi.setStyleSheet(u"background-color: lightgrey;\n"
"color: black;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.btn_pi, 1, 1, 1, 1)

        self.btn_4 = QPushButton(self.centralwidget)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy1.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy1)
        self.btn_4.setFont(font1)
        self.btn_4.setStyleSheet(u"background-color: black;\n"
"color: white;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.btn_4, 3, 6, 1, 1)

        self.btn_log = QPushButton(self.centralwidget)
        self.btn_log.setObjectName(u"btn_log")
        sizePolicy1.setHeightForWidth(self.btn_log.sizePolicy().hasHeightForWidth())
        self.btn_log.setSizePolicy(sizePolicy1)
        self.btn_log.setFont(font2)
        self.btn_log.setStyleSheet(u"background-color: lightgrey;\n"
"color: black;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.btn_log, 5, 3, 1, 1)

        self.btn__MC = QPushButton(self.centralwidget)
        self.btn__MC.setObjectName(u"btn__MC")
        sizePolicy1.setHeightForWidth(self.btn__MC.sizePolicy().hasHeightForWidth())
        self.btn__MC.setSizePolicy(sizePolicy1)
        self.btn__MC.setFont(font2)
        self.btn__MC.setStyleSheet(u"background-color: blue;\n"
"color: white;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.btn__MC, 3, 0, 1, 1)

        self.btn_ln = QPushButton(self.centralwidget)
        self.btn_ln.setObjectName(u"btn_ln")
        sizePolicy1.setHeightForWidth(self.btn_ln.sizePolicy().hasHeightForWidth())
        self.btn_ln.setSizePolicy(sizePolicy1)
        self.btn_ln.setFont(font2)
        self.btn_ln.setStyleSheet(u"background-color: lightgrey;\n"
"color: black;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.btn_ln, 1, 3, 1, 1)

        self.pushButton_30 = QPushButton(self.centralwidget)
        self.pushButton_30.setObjectName(u"pushButton_30")
        sizePolicy.setHeightForWidth(self.pushButton_30.sizePolicy().hasHeightForWidth())
        self.pushButton_30.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.pushButton_30, 0, 10, 1, 1)

        self.btn_square = QPushButton(self.centralwidget)
        self.btn_square.setObjectName(u"btn_square")
        sizePolicy1.setHeightForWidth(self.btn_square.sizePolicy().hasHeightForWidth())
        self.btn_square.setSizePolicy(sizePolicy1)
        self.btn_square.setFont(font2)
        self.btn_square.setStyleSheet(u"background-color: lightgrey;\n"
"color: black;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.btn_square, 4, 4, 1, 1)

        self.btn_tan = QPushButton(self.centralwidget)
        self.btn_tan.setObjectName(u"btn_tan")
        sizePolicy1.setHeightForWidth(self.btn_tan.sizePolicy().hasHeightForWidth())
        self.btn_tan.setSizePolicy(sizePolicy1)
        self.btn_tan.setFont(font2)
        self.btn_tan.setStyleSheet(u"background-color: lightgrey;\n"
"color: black;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.btn_tan, 3, 2, 1, 1)

        self.btn_6 = QPushButton(self.centralwidget)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy1.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy1)
        self.btn_6.setFont(font1)
        self.btn_6.setStyleSheet(u"background-color: black;\n"
"color: white;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.btn_6, 3, 8, 1, 1)

        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy1.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy1)
        self.pushButton_6.setFont(font2)
        self.pushButton_6.setStyleSheet(u"background-color: lightgrey;\n"
"color: black;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.pushButton_6, 5, 4, 1, 1)

        self.btn_divide = QPushButton(self.centralwidget)
        self.btn_divide.setObjectName(u"btn_divide")
        sizePolicy1.setHeightForWidth(self.btn_divide.sizePolicy().hasHeightForWidth())
        self.btn_divide.setSizePolicy(sizePolicy1)
        self.btn_divide.setFont(font)
        self.btn_divide.setStyleSheet(u"background-color: orange;\n"
"color: black;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.btn_divide, 2, 9, 1, 1)

        self.btn_sqrt = QPushButton(self.centralwidget)
        self.btn_sqrt.setObjectName(u"btn_sqrt")
        sizePolicy1.setHeightForWidth(self.btn_sqrt.sizePolicy().hasHeightForWidth())
        self.btn_sqrt.setSizePolicy(sizePolicy1)
        self.btn_sqrt.setFont(font2)
        self.btn_sqrt.setStyleSheet(u"background-color: lightgrey;\n"
"color: black;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.btn_sqrt, 4, 3, 1, 1)

        self.btn_plus_minus = QPushButton(self.centralwidget)
        self.btn_plus_minus.setObjectName(u"btn_plus_minus")
        sizePolicy1.setHeightForWidth(self.btn_plus_minus.sizePolicy().hasHeightForWidth())
        self.btn_plus_minus.setSizePolicy(sizePolicy1)
        self.btn_plus_minus.setFont(font)
        self.btn_plus_minus.setStyleSheet(u"background-color: rgb(128, 128, 128);\n"
"color: white;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.btn_plus_minus, 5, 7, 1, 1)

        self.pushButton_22 = QPushButton(self.centralwidget)
        self.pushButton_22.setObjectName(u"pushButton_22")
        sizePolicy1.setHeightForWidth(self.pushButton_22.sizePolicy().hasHeightForWidth())
        self.pushButton_22.setSizePolicy(sizePolicy1)
        self.pushButton_22.setFont(font3)
        self.pushButton_22.setStyleSheet(u"background-color: lightgrey;\n"
"color: black;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.pushButton_22, 3, 1, 1, 1)

        self.btn_5 = QPushButton(self.centralwidget)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy1.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy1)
        self.btn_5.setFont(font1)
        self.btn_5.setStyleSheet(u"background-color: black;\n"
"color: white;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.btn_5, 3, 7, 1, 1)

        self.btn_multiply = QPushButton(self.centralwidget)
        self.btn_multiply.setObjectName(u"btn_multiply")
        sizePolicy1.setHeightForWidth(self.btn_multiply.sizePolicy().hasHeightForWidth())
        self.btn_multiply.setSizePolicy(sizePolicy1)
        self.btn_multiply.setFont(font)
        self.btn_multiply.setStyleSheet(u"background-color: orange;\n"
"color: black;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.btn_multiply, 3, 9, 1, 1)

        self.btn_clear = QPushButton(self.centralwidget)
        self.btn_clear.setObjectName(u"btn_clear")
        sizePolicy1.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy1)
        self.btn_clear.setFont(font1)
        self.btn_clear.setStyleSheet(u"background-color: red;\n"
"color: white;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.btn_clear, 2, 10, 1, 1)

        self.pushButton_33 = QPushButton(self.centralwidget)
        self.pushButton_33.setObjectName(u"pushButton_33")
        sizePolicy1.setHeightForWidth(self.pushButton_33.sizePolicy().hasHeightForWidth())
        self.pushButton_33.setSizePolicy(sizePolicy1)
        self.pushButton_33.setFont(font3)
        self.pushButton_33.setStyleSheet(u"background-color: lightgrey;\n"
"color: black;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.pushButton_33, 2, 2, 1, 1)

        self.btn_XpowerY = QPushButton(self.centralwidget)
        self.btn_XpowerY.setObjectName(u"btn_XpowerY")
        sizePolicy1.setHeightForWidth(self.btn_XpowerY.sizePolicy().hasHeightForWidth())
        self.btn_XpowerY.setSizePolicy(sizePolicy1)
        self.btn_XpowerY.setFont(font2)
        self.btn_XpowerY.setStyleSheet(u"background-color: lightgrey;\n"
"color: black;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.btn_XpowerY, 2, 4, 1, 1)

        self.btn_plus = QPushButton(self.centralwidget)
        self.btn_plus.setObjectName(u"btn_plus")
        sizePolicy1.setHeightForWidth(self.btn_plus.sizePolicy().hasHeightForWidth())
        self.btn_plus.setSizePolicy(sizePolicy1)
        self.btn_plus.setFont(font1)
        self.btn_plus.setStyleSheet(u"background-color: orange;\n"
"color: black;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.btn_plus, 5, 9, 1, 1)

        self.btn_7 = QPushButton(self.centralwidget)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy1.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy1)
        self.btn_7.setFont(font1)
        self.btn_7.setStyleSheet(u"background-color: black;\n"
"color: white;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.btn_7, 2, 6, 1, 1)

        self.btn_MR = QPushButton(self.centralwidget)
        self.btn_MR.setObjectName(u"btn_MR")
        sizePolicy1.setHeightForWidth(self.btn_MR.sizePolicy().hasHeightForWidth())
        self.btn_MR.setSizePolicy(sizePolicy1)
        self.btn_MR.setFont(font2)
        self.btn_MR.setStyleSheet(u"background-color: blue;\n"
"color: white;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.btn_MR, 2, 0, 1, 1)

        self.btn_Mplus = QPushButton(self.centralwidget)
        self.btn_Mplus.setObjectName(u"btn_Mplus")
        sizePolicy1.setHeightForWidth(self.btn_Mplus.sizePolicy().hasHeightForWidth())
        self.btn_Mplus.setSizePolicy(sizePolicy1)
        self.btn_Mplus.setFont(font2)
        self.btn_Mplus.setStyleSheet(u"background-color: blue;\n"
"color: white;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.btn_Mplus, 1, 0, 1, 1)

        self.btn_minus = QPushButton(self.centralwidget)
        self.btn_minus.setObjectName(u"btn_minus")
        sizePolicy1.setHeightForWidth(self.btn_minus.sizePolicy().hasHeightForWidth())
        self.btn_minus.setSizePolicy(sizePolicy1)
        self.btn_minus.setFont(font1)
        self.btn_minus.setStyleSheet(u"background-color: orange;\n"
"color: white;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.btn_minus, 4, 9, 1, 1)

        self.btn_e = QPushButton(self.centralwidget)
        self.btn_e.setObjectName(u"btn_e")
        sizePolicy1.setHeightForWidth(self.btn_e.sizePolicy().hasHeightForWidth())
        self.btn_e.setSizePolicy(sizePolicy1)
        self.btn_e.setFont(font2)
        self.btn_e.setStyleSheet(u"background-color: lightgrey;\n"
"color: black;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.btn_e, 1, 2, 1, 1)

        self.btn_sin = QPushButton(self.centralwidget)
        self.btn_sin.setObjectName(u"btn_sin")
        sizePolicy1.setHeightForWidth(self.btn_sin.sizePolicy().hasHeightForWidth())
        self.btn_sin.setSizePolicy(sizePolicy1)
        self.btn_sin.setFont(font2)
        self.btn_sin.setStyleSheet(u"background-color: lightgrey;\n"
"color: black;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.btn_sin, 5, 2, 1, 1)

        self.btn_9 = QPushButton(self.centralwidget)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy1.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy1)
        self.btn_9.setFont(font1)
        self.btn_9.setStyleSheet(u"background-color: black;\n"
"color: white;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.btn_9, 2, 8, 1, 1)

        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy1.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy1)
        self.pushButton_9.setFont(font3)
        self.pushButton_9.setStyleSheet(u"background-color: lightgrey;\n"
"color: black;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.pushButton_9, 5, 1, 1, 1)

        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy1.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy1)
        self.btn_2.setFont(font1)
        self.btn_2.setStyleSheet(u"background-color: black;\n"
"color: white;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.btn_2, 4, 7, 1, 1)

        self.btn_bracket_right = QPushButton(self.centralwidget)
        self.btn_bracket_right.setObjectName(u"btn_bracket_right")
        sizePolicy1.setHeightForWidth(self.btn_bracket_right.sizePolicy().hasHeightForWidth())
        self.btn_bracket_right.setSizePolicy(sizePolicy1)
        self.btn_bracket_right.setFont(font1)
        self.btn_bracket_right.setStyleSheet(u"background-color: rgb(128, 128, 128);\n"
"color: white;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.btn_bracket_right, 1, 8, 1, 1)

        self.btn_min = QPushButton(self.centralwidget)
        self.btn_min.setObjectName(u"btn_min")
        sizePolicy1.setHeightForWidth(self.btn_min.sizePolicy().hasHeightForWidth())
        self.btn_min.setSizePolicy(sizePolicy1)
        self.btn_min.setFont(font2)
        self.btn_min.setStyleSheet(u"background-color: lightgrey;\n"
"color: black;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.btn_min, 4, 0, 1, 1)

        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy1.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy1)
        self.btn_1.setFont(font1)
        self.btn_1.setStyleSheet(u"background-color: black;\n"
"color: white;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.btn_1, 4, 6, 1, 1)

        self.btn_dot = QPushButton(self.centralwidget)
        self.btn_dot.setObjectName(u"btn_dot")
        sizePolicy1.setHeightForWidth(self.btn_dot.sizePolicy().hasHeightForWidth())
        self.btn_dot.setSizePolicy(sizePolicy1)
        self.btn_dot.setFont(font1)
        self.btn_dot.setStyleSheet(u"background-color: rgb(128, 128, 128);\n"
"color: white;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.btn_dot, 5, 8, 1, 1)

        self.btn_cbrt = QPushButton(self.centralwidget)
        self.btn_cbrt.setObjectName(u"btn_cbrt")
        sizePolicy1.setHeightForWidth(self.btn_cbrt.sizePolicy().hasHeightForWidth())
        self.btn_cbrt.setSizePolicy(sizePolicy1)
        self.btn_cbrt.setFont(font2)
        self.btn_cbrt.setStyleSheet(u"background-color: lightgrey;\n"
"color: black;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.btn_cbrt, 3, 3, 1, 1)

        self.btn_cube = QPushButton(self.centralwidget)
        self.btn_cube.setObjectName(u"btn_cube")
        sizePolicy1.setHeightForWidth(self.btn_cube.sizePolicy().hasHeightForWidth())
        self.btn_cube.setSizePolicy(sizePolicy1)
        self.btn_cube.setFont(font2)
        self.btn_cube.setStyleSheet(u"background-color: lightgrey;\n"
"color: black;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.btn_cube, 3, 4, 1, 1)

        self.pushButton_34 = QPushButton(self.centralwidget)
        self.pushButton_34.setObjectName(u"pushButton_34")
        sizePolicy1.setHeightForWidth(self.pushButton_34.sizePolicy().hasHeightForWidth())
        self.pushButton_34.setSizePolicy(sizePolicy1)
        self.pushButton_34.setFont(font2)
        self.pushButton_34.setStyleSheet(u"background-color: lightgrey;\n"
"color: black;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.pushButton_34, 2, 3, 1, 1)

        self.btn_bracket_left = QPushButton(self.centralwidget)
        self.btn_bracket_left.setObjectName(u"btn_bracket_left")
        sizePolicy1.setHeightForWidth(self.btn_bracket_left.sizePolicy().hasHeightForWidth())
        self.btn_bracket_left.setSizePolicy(sizePolicy1)
        self.btn_bracket_left.setFont(font1)
        self.btn_bracket_left.setStyleSheet(u"background-color: rgb(128, 128, 128);\n"
"color: white;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.btn_bracket_left, 1, 6, 1, 1)

        self.btn_lg2 = QPushButton(self.centralwidget)
        self.btn_lg2.setObjectName(u"btn_lg2")
        sizePolicy1.setHeightForWidth(self.btn_lg2.sizePolicy().hasHeightForWidth())
        self.btn_lg2.setSizePolicy(sizePolicy1)
        self.btn_lg2.setFont(font2)
        self.btn_lg2.setStyleSheet(u"background-color: lightgrey;\n"
"color: black;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.btn_lg2, 1, 4, 1, 1)

        self.btn_equal = QPushButton(self.centralwidget)
        self.btn_equal.setObjectName(u"btn_equal")
        sizePolicy1.setHeightForWidth(self.btn_equal.sizePolicy().hasHeightForWidth())
        self.btn_equal.setSizePolicy(sizePolicy1)
        self.btn_equal.setFont(font1)
        self.btn_equal.setStyleSheet(u"background-color: green;\n"
"color: white;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.btn_equal, 3, 10, 3, 1)

        self.pushButton_12 = QPushButton(self.centralwidget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy1.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy1)
        self.pushButton_12.setFont(font3)
        self.pushButton_12.setStyleSheet(u"background-color: lightgrey;\n"
"color: black;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.pushButton_12, 4, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 3, 5, 1, 1)

        self.btn_forward = QPushButton(self.centralwidget)
        self.btn_forward.setObjectName(u"btn_forward")
        sizePolicy1.setHeightForWidth(self.btn_forward.sizePolicy().hasHeightForWidth())
        self.btn_forward.setSizePolicy(sizePolicy1)
        self.btn_forward.setFont(font1)
        self.btn_forward.setStyleSheet(u"background-color: rgb(128, 128, 128);\n"
"color: white;\n"
"border: 1px solid;\n"
"padding: 5px;")

        self.gridLayout_3.addWidget(self.btn_forward, 1, 9, 1, 1)

        self.btn_backward = QPushButton(self.centralwidget)
        self.btn_backward.setObjectName(u"btn_backward")
        sizePolicy1.setHeightForWidth(self.btn_backward.sizePolicy().hasHeightForWidth())
        self.btn_backward.setSizePolicy(sizePolicy1)
        self.btn_backward.setFont(font1)
        self.btn_backward.setStyleSheet(u"background-color: rgb(128, 128, 128);\n"
"color: white;\n"
"border: 1px solid;\n"
"padding: 5px;")

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
        self.btn_comma.setText(QCoreApplication.translate("MainWindow", u",", None))
        self.btn_max.setText(QCoreApplication.translate("MainWindow", u"max", None))
        self.btn_cos.setText(QCoreApplication.translate("MainWindow", u"cos", None))
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_32.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_pi.setText(QCoreApplication.translate("MainWindow", u"\u03c0", None))
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_log.setText(QCoreApplication.translate("MainWindow", u"log", None))
        self.btn__MC.setText(QCoreApplication.translate("MainWindow", u"MC", None))
        self.btn_ln.setText(QCoreApplication.translate("MainWindow", u"ln", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_square.setText(QCoreApplication.translate("MainWindow", u"x\u00b2", None))
        self.btn_tan.setText(QCoreApplication.translate("MainWindow", u"tan", None))
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"10\u02e3", None))
        self.btn_divide.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.btn_sqrt.setText(QCoreApplication.translate("MainWindow", u"\u221a", None))
        self.btn_plus_minus.setText(QCoreApplication.translate("MainWindow", u"\u00b1", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_multiply.setText(QCoreApplication.translate("MainWindow", u"\u2716\ufe0f", None))
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_XpowerY.setText(QCoreApplication.translate("MainWindow", u"x\u02b8", None))
        self.btn_plus.setText(QCoreApplication.translate("MainWindow", u"\u271a", None))
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_MR.setText(QCoreApplication.translate("MainWindow", u"MR", None))
        self.btn_Mplus.setText(QCoreApplication.translate("MainWindow", u"M+", None))
        self.btn_minus.setText(QCoreApplication.translate("MainWindow", u"\u2796", None))
        self.btn_e.setText(QCoreApplication.translate("MainWindow", u"e", None))
        self.btn_sin.setText(QCoreApplication.translate("MainWindow", u"sin", None))
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_bracket_right.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.btn_min.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_dot.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.btn_cbrt.setText(QCoreApplication.translate("MainWindow", u"\u221b", None))
        self.btn_cube.setText(QCoreApplication.translate("MainWindow", u"x\u00b3", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"\u02b8\u221ax", None))
        self.btn_bracket_left.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.btn_lg2.setText(QCoreApplication.translate("MainWindow", u"lg2", None))
        self.btn_equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_forward.setText(QCoreApplication.translate("MainWindow", u"\u2190", None))
        self.btn_backward.setText(QCoreApplication.translate("MainWindow", u"\u2192", None))
    # retranslateUi


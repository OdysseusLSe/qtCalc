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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLayout,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(750, 500)
        MainWindow.setMinimumSize(QSize(750, 500))
        MainWindow.setMaximumSize(QSize(750, 500))
        font = QFont()
        font.setFamilies([u"Courier New"])
        font.setWeight(QFont.DemiBold)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color : rgb(169, 169, 169);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.history_list = QListWidget(self.centralwidget)
        self.history_list.setObjectName(u"history_list")
        font1 = QFont()
        font1.setFamilies([u"Courier New"])
        font1.setPointSize(15)
        font1.setWeight(QFont.DemiBold)
        self.history_list.setFont(font1)
        self.history_list.setStyleSheet(u"background-color: rgb(214, 214, 214);\n"
"color: rgb(94, 94, 94);\n"
"border: 3px solid;")
        self.history_list.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.history_list.setAlternatingRowColors(True)
        self.history_list.setTextElideMode(Qt.TextElideMode.ElideNone)
        self.history_list.setWordWrap(True)

        self.verticalLayout.addWidget(self.history_list)

        self.expression_line = QLineEdit(self.centralwidget)
        self.expression_line.setObjectName(u"expression_line")
        font2 = QFont()
        font2.setFamilies([u"Courier New"])
        font2.setPointSize(25)
        font2.setWeight(QFont.ExtraBold)
        self.expression_line.setFont(font2)
        self.expression_line.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.expression_line.setStyleSheet(u"background-color : rgb(214, 214, 214);\n"
"color: black;\n"
"border: 3px solid;")
        self.expression_line.setReadOnly(False)

        self.verticalLayout.addWidget(self.expression_line)

        self.gridLayout_3 = QGridLayout()
#ifndef Q_OS_MACOS
        self.gridLayout_3.setSpacing(-1)
#endif
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.btn_comma = QPushButton(self.centralwidget)
        self.btn_comma.setObjectName(u"btn_comma")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_comma.sizePolicy().hasHeightForWidth())
        self.btn_comma.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setPointSize(25)
        font3.setWeight(QFont.ExtraBold)
        self.btn_comma.setFont(font3)
        self.btn_comma.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_comma.setStyleSheet(u"background-color: rgb(128, 128, 128);\n"
"color: white;")

        self.gridLayout_3.addWidget(self.btn_comma, 1, 7, 1, 1)

        self.btn_max = QPushButton(self.centralwidget)
        self.btn_max.setObjectName(u"btn_max")
        sizePolicy.setHeightForWidth(self.btn_max.sizePolicy().hasHeightForWidth())
        self.btn_max.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setPointSize(20)
        font4.setBold(True)
        self.btn_max.setFont(font4)
        self.btn_max.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_max.setStyleSheet(u"background-color: lightgrey;\n"
"color: black;")

        self.gridLayout_3.addWidget(self.btn_max, 5, 0, 1, 1)

        self.btn_cos = QPushButton(self.centralwidget)
        self.btn_cos.setObjectName(u"btn_cos")
        sizePolicy.setHeightForWidth(self.btn_cos.sizePolicy().hasHeightForWidth())
        self.btn_cos.setSizePolicy(sizePolicy)
        self.btn_cos.setFont(font4)
        self.btn_cos.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_cos.setStyleSheet(u"background-color: lightgrey;\n"
"color: black;")

        self.gridLayout_3.addWidget(self.btn_cos, 4, 2, 1, 1)

        self.btn_3 = QPushButton(self.centralwidget)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)
        self.btn_3.setFont(font3)
        self.btn_3.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_3.setStyleSheet(u"background-color: black;\n"
"color: white;")

        self.gridLayout_3.addWidget(self.btn_3, 4, 8, 1, 1)

        self.pushButton_32 = QPushButton(self.centralwidget)
        self.pushButton_32.setObjectName(u"pushButton_32")
        sizePolicy.setHeightForWidth(self.pushButton_32.sizePolicy().hasHeightForWidth())
        self.pushButton_32.setSizePolicy(sizePolicy)
        self.pushButton_32.setFont(font4)
        self.pushButton_32.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_32.setStyleSheet(u"background-color: lightgrey;\n"
"color: black;")

        self.gridLayout_3.addWidget(self.pushButton_32, 2, 1, 1, 1)

        self.btn_8 = QPushButton(self.centralwidget)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy)
        self.btn_8.setFont(font3)
        self.btn_8.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_8.setStyleSheet(u"background-color: black;\n"
"color: white;")

        self.gridLayout_3.addWidget(self.btn_8, 2, 7, 1, 1)

        self.btn_0 = QPushButton(self.centralwidget)
        self.btn_0.setObjectName(u"btn_0")
        sizePolicy.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy)
        self.btn_0.setFont(font3)
        self.btn_0.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_0.setStyleSheet(u"background-color: black;\n"
"color: white;")

        self.gridLayout_3.addWidget(self.btn_0, 5, 6, 1, 1)

        self.btn_pi = QPushButton(self.centralwidget)
        self.btn_pi.setObjectName(u"btn_pi")
        sizePolicy.setHeightForWidth(self.btn_pi.sizePolicy().hasHeightForWidth())
        self.btn_pi.setSizePolicy(sizePolicy)
        self.btn_pi.setFont(font4)
        self.btn_pi.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_pi.setStyleSheet(u"background-color: lightgrey;\n"
"color: black;")

        self.gridLayout_3.addWidget(self.btn_pi, 1, 1, 1, 1)

        self.btn_4 = QPushButton(self.centralwidget)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy)
        self.btn_4.setFont(font3)
        self.btn_4.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_4.setStyleSheet(u"background-color: black;\n"
"color: white;")

        self.gridLayout_3.addWidget(self.btn_4, 3, 6, 1, 1)

        self.btn_log = QPushButton(self.centralwidget)
        self.btn_log.setObjectName(u"btn_log")
        sizePolicy.setHeightForWidth(self.btn_log.sizePolicy().hasHeightForWidth())
        self.btn_log.setSizePolicy(sizePolicy)
        self.btn_log.setFont(font4)
        self.btn_log.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_log.setStyleSheet(u"background-color: lightgrey;\n"
"color: black;")

        self.gridLayout_3.addWidget(self.btn_log, 5, 3, 1, 1)

        self.btn_MC = QPushButton(self.centralwidget)
        self.btn_MC.setObjectName(u"btn_MC")
        sizePolicy.setHeightForWidth(self.btn_MC.sizePolicy().hasHeightForWidth())
        self.btn_MC.setSizePolicy(sizePolicy)
        font5 = QFont()
        font5.setPointSize(25)
        font5.setWeight(QFont.DemiBold)
        self.btn_MC.setFont(font5)
        self.btn_MC.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_MC.setStyleSheet(u"background-color: blue;\n"
"color: white;")

        self.gridLayout_3.addWidget(self.btn_MC, 3, 0, 1, 1)

        self.btn_ln = QPushButton(self.centralwidget)
        self.btn_ln.setObjectName(u"btn_ln")
        sizePolicy.setHeightForWidth(self.btn_ln.sizePolicy().hasHeightForWidth())
        self.btn_ln.setSizePolicy(sizePolicy)
        self.btn_ln.setFont(font4)
        self.btn_ln.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_ln.setStyleSheet(u"background-color: lightgrey;\n"
"color: black;")

        self.gridLayout_3.addWidget(self.btn_ln, 1, 3, 1, 1)

        self.btn_2nd = QPushButton(self.centralwidget)
        self.btn_2nd.setObjectName(u"btn_2nd")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_2nd.sizePolicy().hasHeightForWidth())
        self.btn_2nd.setSizePolicy(sizePolicy1)
        self.btn_2nd.setFont(font3)
        self.btn_2nd.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_2nd.setStyleSheet(u"background-color : rgb(66, 66, 66);\n"
"color : white;")

        self.gridLayout_3.addWidget(self.btn_2nd, 0, 10, 1, 1)

        self.btn_square = QPushButton(self.centralwidget)
        self.btn_square.setObjectName(u"btn_square")
        sizePolicy.setHeightForWidth(self.btn_square.sizePolicy().hasHeightForWidth())
        self.btn_square.setSizePolicy(sizePolicy)
        self.btn_square.setFont(font4)
        self.btn_square.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_square.setStyleSheet(u"background-color: lightgrey;\n"
"color: black;\n"
"")

        self.gridLayout_3.addWidget(self.btn_square, 4, 4, 1, 1)

        self.btn_tan = QPushButton(self.centralwidget)
        self.btn_tan.setObjectName(u"btn_tan")
        sizePolicy.setHeightForWidth(self.btn_tan.sizePolicy().hasHeightForWidth())
        self.btn_tan.setSizePolicy(sizePolicy)
        self.btn_tan.setFont(font4)
        self.btn_tan.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_tan.setStyleSheet(u"background-color: lightgrey;\n"
"color: black;")

        self.gridLayout_3.addWidget(self.btn_tan, 3, 2, 1, 1)

        self.btn_6 = QPushButton(self.centralwidget)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy)
        self.btn_6.setFont(font3)
        self.btn_6.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_6.setStyleSheet(u"background-color: black;\n"
"color: white;")

        self.gridLayout_3.addWidget(self.btn_6, 3, 8, 1, 1)

        self.btn_10powerX = QPushButton(self.centralwidget)
        self.btn_10powerX.setObjectName(u"btn_10powerX")
        sizePolicy.setHeightForWidth(self.btn_10powerX.sizePolicy().hasHeightForWidth())
        self.btn_10powerX.setSizePolicy(sizePolicy)
        self.btn_10powerX.setFont(font4)
        self.btn_10powerX.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_10powerX.setStyleSheet(u"background-color: lightgrey;\n"
"color: black;")

        self.gridLayout_3.addWidget(self.btn_10powerX, 5, 4, 1, 1)

        self.btn_divide = QPushButton(self.centralwidget)
        self.btn_divide.setObjectName(u"btn_divide")
        sizePolicy.setHeightForWidth(self.btn_divide.sizePolicy().hasHeightForWidth())
        self.btn_divide.setSizePolicy(sizePolicy)
        font6 = QFont()
        font6.setPointSize(25)
        font6.setBold(True)
        self.btn_divide.setFont(font6)
        self.btn_divide.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_divide.setStyleSheet(u"background-color: orange;\n"
"color: black;")

        self.gridLayout_3.addWidget(self.btn_divide, 2, 9, 1, 1)

        self.btn_sqrt = QPushButton(self.centralwidget)
        self.btn_sqrt.setObjectName(u"btn_sqrt")
        sizePolicy.setHeightForWidth(self.btn_sqrt.sizePolicy().hasHeightForWidth())
        self.btn_sqrt.setSizePolicy(sizePolicy)
        self.btn_sqrt.setFont(font4)
        self.btn_sqrt.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_sqrt.setStyleSheet(u"background-color: lightgrey;\n"
"color: black;")

        self.gridLayout_3.addWidget(self.btn_sqrt, 4, 3, 1, 1)

        self.btn_unary_minus = QPushButton(self.centralwidget)
        self.btn_unary_minus.setObjectName(u"btn_unary_minus")
        sizePolicy.setHeightForWidth(self.btn_unary_minus.sizePolicy().hasHeightForWidth())
        self.btn_unary_minus.setSizePolicy(sizePolicy)
        self.btn_unary_minus.setFont(font6)
        self.btn_unary_minus.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_unary_minus.setStyleSheet(u"background-color: rgb(128, 128, 128);\n"
"color: white;")

        self.gridLayout_3.addWidget(self.btn_unary_minus, 5, 7, 1, 1)

        self.btn_tanh = QPushButton(self.centralwidget)
        self.btn_tanh.setObjectName(u"btn_tanh")
        sizePolicy.setHeightForWidth(self.btn_tanh.sizePolicy().hasHeightForWidth())
        self.btn_tanh.setSizePolicy(sizePolicy)
        self.btn_tanh.setFont(font4)
        self.btn_tanh.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_tanh.setStyleSheet(u"background-color: lightgrey;\n"
"color: black;")

        self.gridLayout_3.addWidget(self.btn_tanh, 3, 1, 1, 1)

        self.btn_5 = QPushButton(self.centralwidget)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy)
        self.btn_5.setFont(font3)
        self.btn_5.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_5.setStyleSheet(u"background-color: black;\n"
"color: white;")

        self.gridLayout_3.addWidget(self.btn_5, 3, 7, 1, 1)

        self.btn_multiply = QPushButton(self.centralwidget)
        self.btn_multiply.setObjectName(u"btn_multiply")
        sizePolicy.setHeightForWidth(self.btn_multiply.sizePolicy().hasHeightForWidth())
        self.btn_multiply.setSizePolicy(sizePolicy)
        self.btn_multiply.setFont(font6)
        self.btn_multiply.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_multiply.setStyleSheet(u"background-color: orange;\n"
"color: black;")

        self.gridLayout_3.addWidget(self.btn_multiply, 3, 9, 1, 1)

        self.btn_clear = QPushButton(self.centralwidget)
        self.btn_clear.setObjectName(u"btn_clear")
        sizePolicy.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy)
        self.btn_clear.setFont(font3)
        self.btn_clear.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_clear.setStyleSheet(u"background-color: red;\n"
"color: white;")

        self.gridLayout_3.addWidget(self.btn_clear, 2, 10, 1, 1)

        self.pushButton_33 = QPushButton(self.centralwidget)
        self.pushButton_33.setObjectName(u"pushButton_33")
        sizePolicy.setHeightForWidth(self.pushButton_33.sizePolicy().hasHeightForWidth())
        self.pushButton_33.setSizePolicy(sizePolicy)
        self.pushButton_33.setFont(font4)
        self.pushButton_33.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_33.setStyleSheet(u"background-color: lightgrey;\n"
"color: black;")

        self.gridLayout_3.addWidget(self.pushButton_33, 2, 2, 1, 1)

        self.btn_XpowerY = QPushButton(self.centralwidget)
        self.btn_XpowerY.setObjectName(u"btn_XpowerY")
        sizePolicy.setHeightForWidth(self.btn_XpowerY.sizePolicy().hasHeightForWidth())
        self.btn_XpowerY.setSizePolicy(sizePolicy)
        self.btn_XpowerY.setFont(font4)
        self.btn_XpowerY.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_XpowerY.setStyleSheet(u"background-color: lightgrey;\n"
"color: black;")

        self.gridLayout_3.addWidget(self.btn_XpowerY, 2, 4, 1, 1)

        self.btn_plus = QPushButton(self.centralwidget)
        self.btn_plus.setObjectName(u"btn_plus")
        sizePolicy.setHeightForWidth(self.btn_plus.sizePolicy().hasHeightForWidth())
        self.btn_plus.setSizePolicy(sizePolicy)
        self.btn_plus.setFont(font3)
        self.btn_plus.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_plus.setStyleSheet(u"background-color: orange;\n"
"color: black;")

        self.gridLayout_3.addWidget(self.btn_plus, 5, 9, 1, 1)

        self.btn_7 = QPushButton(self.centralwidget)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)
        self.btn_7.setFont(font3)
        self.btn_7.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_7.setStyleSheet(u"background-color: black;\n"
"color: white;")

        self.gridLayout_3.addWidget(self.btn_7, 2, 6, 1, 1)

        self.btn_MR = QPushButton(self.centralwidget)
        self.btn_MR.setObjectName(u"btn_MR")
        sizePolicy.setHeightForWidth(self.btn_MR.sizePolicy().hasHeightForWidth())
        self.btn_MR.setSizePolicy(sizePolicy)
        self.btn_MR.setFont(font5)
        self.btn_MR.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_MR.setStyleSheet(u"background-color: blue;\n"
"color: white;")

        self.gridLayout_3.addWidget(self.btn_MR, 2, 0, 1, 1)

        self.btn_Mplus = QPushButton(self.centralwidget)
        self.btn_Mplus.setObjectName(u"btn_Mplus")
        sizePolicy.setHeightForWidth(self.btn_Mplus.sizePolicy().hasHeightForWidth())
        self.btn_Mplus.setSizePolicy(sizePolicy)
        self.btn_Mplus.setFont(font5)
        self.btn_Mplus.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_Mplus.setStyleSheet(u"background-color: blue;\n"
"color: white;")

        self.gridLayout_3.addWidget(self.btn_Mplus, 1, 0, 1, 1)

        self.btn_minus = QPushButton(self.centralwidget)
        self.btn_minus.setObjectName(u"btn_minus")
        sizePolicy.setHeightForWidth(self.btn_minus.sizePolicy().hasHeightForWidth())
        self.btn_minus.setSizePolicy(sizePolicy)
        self.btn_minus.setFont(font3)
        self.btn_minus.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_minus.setStyleSheet(u"background-color: orange;\n"
"color: white;")

        self.gridLayout_3.addWidget(self.btn_minus, 4, 9, 1, 1)

        self.btn_e = QPushButton(self.centralwidget)
        self.btn_e.setObjectName(u"btn_e")
        sizePolicy.setHeightForWidth(self.btn_e.sizePolicy().hasHeightForWidth())
        self.btn_e.setSizePolicy(sizePolicy)
        self.btn_e.setFont(font4)
        self.btn_e.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_e.setStyleSheet(u"background-color: lightgrey;\n"
"color: black;")

        self.gridLayout_3.addWidget(self.btn_e, 1, 2, 1, 1)

        self.btn_sin = QPushButton(self.centralwidget)
        self.btn_sin.setObjectName(u"btn_sin")
        sizePolicy.setHeightForWidth(self.btn_sin.sizePolicy().hasHeightForWidth())
        self.btn_sin.setSizePolicy(sizePolicy)
        self.btn_sin.setFont(font4)
        self.btn_sin.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_sin.setStyleSheet(u"background-color: lightgrey;\n"
"color: black;")

        self.gridLayout_3.addWidget(self.btn_sin, 5, 2, 1, 1)

        self.btn_9 = QPushButton(self.centralwidget)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy)
        self.btn_9.setFont(font3)
        self.btn_9.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_9.setStyleSheet(u"background-color: black;\n"
"color: white;")

        self.gridLayout_3.addWidget(self.btn_9, 2, 8, 1, 1)

        self.btn_sinh = QPushButton(self.centralwidget)
        self.btn_sinh.setObjectName(u"btn_sinh")
        sizePolicy.setHeightForWidth(self.btn_sinh.sizePolicy().hasHeightForWidth())
        self.btn_sinh.setSizePolicy(sizePolicy)
        self.btn_sinh.setFont(font4)
        self.btn_sinh.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_sinh.setStyleSheet(u"background-color: lightgrey;\n"
"color: black;")

        self.gridLayout_3.addWidget(self.btn_sinh, 5, 1, 1, 1)

        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)
        self.btn_2.setFont(font3)
        self.btn_2.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_2.setStyleSheet(u"background-color: black;\n"
"color: white;")

        self.gridLayout_3.addWidget(self.btn_2, 4, 7, 1, 1)

        self.btn_bracket_right = QPushButton(self.centralwidget)
        self.btn_bracket_right.setObjectName(u"btn_bracket_right")
        sizePolicy.setHeightForWidth(self.btn_bracket_right.sizePolicy().hasHeightForWidth())
        self.btn_bracket_right.setSizePolicy(sizePolicy)
        self.btn_bracket_right.setFont(font3)
        self.btn_bracket_right.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_bracket_right.setStyleSheet(u"background-color: rgb(128, 128, 128);\n"
"color: white;")

        self.gridLayout_3.addWidget(self.btn_bracket_right, 1, 8, 1, 1)

        self.btn_min = QPushButton(self.centralwidget)
        self.btn_min.setObjectName(u"btn_min")
        sizePolicy.setHeightForWidth(self.btn_min.sizePolicy().hasHeightForWidth())
        self.btn_min.setSizePolicy(sizePolicy)
        self.btn_min.setFont(font4)
        self.btn_min.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_min.setStyleSheet(u"background-color: lightgrey;\n"
"color: black;")

        self.gridLayout_3.addWidget(self.btn_min, 4, 0, 1, 1)

        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)
        self.btn_1.setFont(font3)
        self.btn_1.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_1.setStyleSheet(u"background-color: black;\n"
"color: white;")

        self.gridLayout_3.addWidget(self.btn_1, 4, 6, 1, 1)

        self.btn_dot = QPushButton(self.centralwidget)
        self.btn_dot.setObjectName(u"btn_dot")
        sizePolicy.setHeightForWidth(self.btn_dot.sizePolicy().hasHeightForWidth())
        self.btn_dot.setSizePolicy(sizePolicy)
        self.btn_dot.setFont(font3)
        self.btn_dot.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_dot.setStyleSheet(u"background-color: rgb(128, 128, 128);\n"
"color: white;")

        self.gridLayout_3.addWidget(self.btn_dot, 5, 8, 1, 1)

        self.btn_cbrt = QPushButton(self.centralwidget)
        self.btn_cbrt.setObjectName(u"btn_cbrt")
        sizePolicy.setHeightForWidth(self.btn_cbrt.sizePolicy().hasHeightForWidth())
        self.btn_cbrt.setSizePolicy(sizePolicy)
        self.btn_cbrt.setFont(font4)
        self.btn_cbrt.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_cbrt.setStyleSheet(u"background-color: lightgrey;\n"
"color: black;")

        self.gridLayout_3.addWidget(self.btn_cbrt, 3, 3, 1, 1)

        self.btn_cube = QPushButton(self.centralwidget)
        self.btn_cube.setObjectName(u"btn_cube")
        sizePolicy.setHeightForWidth(self.btn_cube.sizePolicy().hasHeightForWidth())
        self.btn_cube.setSizePolicy(sizePolicy)
        self.btn_cube.setFont(font4)
        self.btn_cube.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_cube.setStyleSheet(u"background-color: lightgrey;\n"
"color: black;")

        self.gridLayout_3.addWidget(self.btn_cube, 3, 4, 1, 1)

        self.pushButton_34 = QPushButton(self.centralwidget)
        self.pushButton_34.setObjectName(u"pushButton_34")
        sizePolicy.setHeightForWidth(self.pushButton_34.sizePolicy().hasHeightForWidth())
        self.pushButton_34.setSizePolicy(sizePolicy)
        self.pushButton_34.setFont(font4)
        self.pushButton_34.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_34.setStyleSheet(u"background-color: lightgrey;\n"
"color: black;")

        self.gridLayout_3.addWidget(self.pushButton_34, 2, 3, 1, 1)

        self.btn_bracket_left = QPushButton(self.centralwidget)
        self.btn_bracket_left.setObjectName(u"btn_bracket_left")
        sizePolicy.setHeightForWidth(self.btn_bracket_left.sizePolicy().hasHeightForWidth())
        self.btn_bracket_left.setSizePolicy(sizePolicy)
        self.btn_bracket_left.setFont(font3)
        self.btn_bracket_left.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_bracket_left.setStyleSheet(u"background-color: rgb(128, 128, 128);\n"
"color: white;")

        self.gridLayout_3.addWidget(self.btn_bracket_left, 1, 6, 1, 1)

        self.btn_lg2 = QPushButton(self.centralwidget)
        self.btn_lg2.setObjectName(u"btn_lg2")
        sizePolicy.setHeightForWidth(self.btn_lg2.sizePolicy().hasHeightForWidth())
        self.btn_lg2.setSizePolicy(sizePolicy)
        self.btn_lg2.setFont(font4)
        self.btn_lg2.setStyleSheet(u"background-color: lightgrey;\n"
"color: black;")

        self.gridLayout_3.addWidget(self.btn_lg2, 1, 4, 1, 1)

        self.btn_equal = QPushButton(self.centralwidget)
        self.btn_equal.setObjectName(u"btn_equal")
        sizePolicy.setHeightForWidth(self.btn_equal.sizePolicy().hasHeightForWidth())
        self.btn_equal.setSizePolicy(sizePolicy)
        self.btn_equal.setFont(font3)
        self.btn_equal.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_equal.setStyleSheet(u"background-color: green;\n"
"color: white;")

        self.gridLayout_3.addWidget(self.btn_equal, 3, 10, 3, 1)

        self.btn_cosh = QPushButton(self.centralwidget)
        self.btn_cosh.setObjectName(u"btn_cosh")
        sizePolicy.setHeightForWidth(self.btn_cosh.sizePolicy().hasHeightForWidth())
        self.btn_cosh.setSizePolicy(sizePolicy)
        self.btn_cosh.setFont(font4)
        self.btn_cosh.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_cosh.setStyleSheet(u"background-color: lightgrey;\n"
"color: black;")

        self.gridLayout_3.addWidget(self.btn_cosh, 4, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 3, 5, 1, 1)

        self.btn_left = QPushButton(self.centralwidget)
        self.btn_left.setObjectName(u"btn_left")
        sizePolicy.setHeightForWidth(self.btn_left.sizePolicy().hasHeightForWidth())
        self.btn_left.setSizePolicy(sizePolicy)
        self.btn_left.setFont(font3)
        self.btn_left.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_left.setStyleSheet(u"background-color: rgb(128, 128, 128);\n"
"color: white;")

        self.gridLayout_3.addWidget(self.btn_left, 1, 9, 1, 1)

        self.btn_right = QPushButton(self.centralwidget)
        self.btn_right.setObjectName(u"btn_right")
        sizePolicy.setHeightForWidth(self.btn_right.sizePolicy().hasHeightForWidth())
        self.btn_right.setSizePolicy(sizePolicy)
        self.btn_right.setFont(font3)
        self.btn_right.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_right.setStyleSheet(u"background-color: rgb(128, 128, 128);\n"
"color: white;")

        self.gridLayout_3.addWidget(self.btn_right, 1, 10, 1, 1)

        self.btn_del = QPushButton(self.centralwidget)
        self.btn_del.setObjectName(u"btn_del")
        sizePolicy1.setHeightForWidth(self.btn_del.sizePolicy().hasHeightForWidth())
        self.btn_del.setSizePolicy(sizePolicy1)
        self.btn_del.setFont(font3)
        self.btn_del.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.btn_del.setStyleSheet(u"background-color : red;\n"
"color : white;")

        self.gridLayout_3.addWidget(self.btn_del, 0, 9, 1, 1)

        self.memory_list = QComboBox(self.centralwidget)
        self.memory_list.setObjectName(u"memory_list")
        sizePolicy1.setHeightForWidth(self.memory_list.sizePolicy().hasHeightForWidth())
        self.memory_list.setSizePolicy(sizePolicy1)
        font7 = QFont()
        font7.setFamilies([u"Courier New"])
        font7.setPointSize(17)
        font7.setWeight(QFont.DemiBold)
        self.memory_list.setFont(font7)
        self.memory_list.setStyleSheet(u"background-color: rgb(214, 214, 214);\n"
"color: rgb(94, 94, 94);")
        self.memory_list.setMaxVisibleItems(3)

        self.gridLayout_3.addWidget(self.memory_list, 0, 0, 1, 3)

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
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 3)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menu_bar = QMenuBar(MainWindow)
        self.menu_bar.setObjectName(u"menu_bar")
        self.menu_bar.setGeometry(QRect(0, 0, 750, 30))
        MainWindow.setMenuBar(self.menu_bar)
        self.status_bar = QStatusBar(MainWindow)
        self.status_bar.setObjectName(u"status_bar")
        MainWindow.setStatusBar(self.status_bar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
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
        self.btn_MC.setText(QCoreApplication.translate("MainWindow", u"MC", None))
        self.btn_ln.setText(QCoreApplication.translate("MainWindow", u"ln", None))
        self.btn_2nd.setText(QCoreApplication.translate("MainWindow", u"2nd", None))
        self.btn_square.setText(QCoreApplication.translate("MainWindow", u"x\u00b2", None))
        self.btn_tan.setText(QCoreApplication.translate("MainWindow", u"tan", None))
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_10powerX.setText(QCoreApplication.translate("MainWindow", u"10\u02e3", None))
        self.btn_divide.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.btn_sqrt.setText(QCoreApplication.translate("MainWindow", u"\u221a", None))
        self.btn_unary_minus.setText(QCoreApplication.translate("MainWindow", u"\u00b1", None))
        self.btn_tanh.setText(QCoreApplication.translate("MainWindow", u"tanh", None))
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
        self.btn_sinh.setText(QCoreApplication.translate("MainWindow", u"sinh", None))
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
        self.btn_cosh.setText(QCoreApplication.translate("MainWindow", u"cosh", None))
        self.btn_left.setText(QCoreApplication.translate("MainWindow", u"\u2190", None))
        self.btn_right.setText(QCoreApplication.translate("MainWindow", u"\u2192", None))
        self.btn_del.setText(QCoreApplication.translate("MainWindow", u"\u232b", None))
    # retranslateUi


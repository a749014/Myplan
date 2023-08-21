# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'countdown.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class Ui_Countdown(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(466, 408)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 40))
        self.label_4.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)

        self.verticalLayout.addWidget(self.label_4)

        self.label_picture = QLabel(self.centralwidget)
        self.label_picture.setObjectName(u"label_picture")
        self.label_picture.setMinimumSize(QSize(0, 300))
        self.label_picture.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_picture)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(80, 30))
        self.label.setMaximumSize(QSize(80, 30))

        self.horizontalLayout.addWidget(self.label)

        self.lcdNumber_min = QLCDNumber(self.centralwidget)
        self.lcdNumber_min.setObjectName(u"lcdNumber_min")
        self.lcdNumber_min.setMinimumSize(QSize(90, 30))
        self.lcdNumber_min.setMaximumSize(QSize(90, 30))

        self.horizontalLayout.addWidget(self.lcdNumber_min)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(30, 30))
        self.label_2.setMaximumSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.label_2)

        self.lcdNumber_second = QLCDNumber(self.centralwidget)
        self.lcdNumber_second.setObjectName(u"lcdNumber_second")
        self.lcdNumber_second.setMinimumSize(QSize(90, 30))
        self.lcdNumber_second.setMaximumSize(QSize(90, 30))

        self.horizontalLayout.addWidget(self.lcdNumber_second)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(30, 30))
        self.label_3.setMaximumSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.label_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_stop = QPushButton(self.centralwidget)
        self.pushButton_stop.setObjectName(u"pushButton_stop")
        self.pushButton_stop.setMinimumSize(QSize(80, 30))
        self.pushButton_stop.setMaximumSize(QSize(80, 30))

        self.horizontalLayout.addWidget(self.pushButton_stop)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u8ba1\u5212\u8fdb\u884c\u4e2d", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u8ba1\u5212\u540d\uff1a", None))
        self.label_picture.setText(QCoreApplication.translate("MainWindow", u"picture", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5269\u4f59\u65f6\u957f\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5206", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u79d2", None))
        self.pushButton_stop.setText(QCoreApplication.translate("MainWindow", u"\u653e\u5f03\u5b8c\u6210", None))
    # retranslateUi


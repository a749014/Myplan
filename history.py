# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'history.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_History(object):
    def setupUi(self, History):
        History.setObjectName("History")
        History.resize(497, 307)
        self.centralwidget = QtWidgets.QWidget(History)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(100, 40))
        self.label.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMinimumSize(QtCore.QSize(400, 200))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 477, 241))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(400, 200))
        self.scrollAreaWidgetContents.setMaximumSize(QtCore.QSize(114514, 16777215))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.history1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.history1.setMinimumSize(QtCore.QSize(400, 25))
        self.history1.setMaximumSize(QtCore.QSize(16777215, 25))
        self.history1.setObjectName("history1")
        self.verticalLayout.addWidget(self.history1)
        self.history_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.history_2.setMinimumSize(QtCore.QSize(400, 25))
        self.history_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.history_2.setObjectName("history_2")
        self.verticalLayout.addWidget(self.history_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        History.setCentralWidget(self.centralwidget)

        self.retranslateUi(History)
        QtCore.QMetaObject.connectSlotsByName(History)

    def retranslateUi(self, History):
        _translate = QtCore.QCoreApplication.translate
        History.setWindowTitle(_translate("History", "MainWindow"))
        self.label.setText(_translate("History", "History"))
        self.history1.setText(_translate("History", "Date:{}Finish progress:{}{}"))
        self.history_2.setText(_translate("History", "Date:{}Finish progress:{}{}"))
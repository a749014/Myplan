# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PySide2 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(674, 533)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(100, 40))
        self.label.setMaximumSize(QtCore.QSize(114514, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.pbtn_about = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn_about.setMinimumSize(QtCore.QSize(60, 30))
        self.pbtn_about.setMaximumSize(QtCore.QSize(60, 30))
        self.pbtn_about.setObjectName("pbtn_about")
        self.horizontalLayout_3.addWidget(self.pbtn_about)

        self.pbtn_new = QtWidgets.QPushButton(self.centralwidget)
        self.pbtn_new.setMinimumSize(QtCore.QSize(60, 30))
        self.pbtn_new.setMaximumSize(QtCore.QSize(60, 30))
        self.pbtn_new.setObjectName("pbtn_new")
        self.horizontalLayout_3.addWidget(self.pbtn_new)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMinimumSize(QtCore.QSize(650, 450))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.planWindow = QtWidgets.QWidget()
        self.planWindow.setGeometry(QtCore.QRect(0, 0, 654, 465))
        self.planWindow.setMinimumSize(QtCore.QSize(600, 400))
        self.planWindow.setObjectName("planWindow")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.planWindow)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        # self.horizontalLayout = QtWidgets.QHBoxLayout()
        # self.horizontalLayout.setObjectName("horizontalLayout")
        # self.cbox_plan1 = QtWidgets.QCheckBox(self.planWindow)
        # self.cbox_plan1.setMinimumSize(QtCore.QSize(550, 30))
        # self.cbox_plan1.setMaximumSize(QtCore.QSize(16777215, 30))
        # self.cbox_plan1.setObjectName("cbox_plan1")
        # self.horizontalLayout.addWidget(self.cbox_plan1)
        # self.pbtn_delete_1 = QtWidgets.QPushButton(self.planWindow)
        # self.pbtn_delete_1.setMinimumSize(QtCore.QSize(55, 25))
        # self.pbtn_delete_1.setMaximumSize(QtCore.QSize(55, 25))
        # self.pbtn_delete_1.setObjectName("pbtn_delete_1")
        # self.horizontalLayout.addWidget(self.pbtn_delete_1)
        # self.verticalLayout_2.addLayout(self.horizontalLayout)
        # self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        # self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        # self.cbox_plan2 = QtWidgets.QCheckBox(self.planWindow)
        # self.cbox_plan2.setMinimumSize(QtCore.QSize(550, 30))
        # self.cbox_plan2.setMaximumSize(QtCore.QSize(16777215, 30))
        # self.cbox_plan2.setObjectName("cbox_plan2")
        # self.horizontalLayout_2.addWidget(self.cbox_plan2)
        # self.pbtn_delete_2 = QtWidgets.QPushButton(self.planWindow)
        # self.pbtn_delete_2.setMinimumSize(QtCore.QSize(55, 25))
        # self.pbtn_delete_2.setMaximumSize(QtCore.QSize(55, 25))
        # self.pbtn_delete_2.setObjectName("pbtn_delete_2")
        # self.horizontalLayout_2.addWidget(self.pbtn_delete_2)
        # self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(self.spacerItem)
        self.label_2 = QtWidgets.QLabel(self.planWindow)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.scrollArea.setWidget(self.planWindow)
        self.verticalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "我的计划"))
        self.label.setText(_translate("MainWindow", "我的计划"))
        self.pbtn_new.setText(_translate("MainWindow", "添加"))
        self.pbtn_about.setText(_translate("MainWindow","关于"))
        # self.cbox_plan1.setText(_translate("MainWindow", "起床"))
        # self.pbtn_delete_1.setText(_translate("MainWindow", "delete"))
        # self.cbox_plan2.setText(_translate("MainWindow", "跑步"))
        # self.pbtn_delete_2.setText(_translate("MainWindow", "delete"))
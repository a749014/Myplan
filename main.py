from PySide2 import QtGui
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from mainwindow import Ui_MainWindow
from addplan import Ui_Addplan
import sys
import time
import json
import os
import re
path=os.path.dirname(os.path.abspath(__file__))
class main(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup()
        self.show()
    def setup(self):
        self.setWindowTitle('MyPlan')
        self.setWindowIcon(QIcon(path+'/icons/hutao.jpeg'))
        self.plans={}
        self.checkboxs={}
        self.planNum=0
        self.addplanWindow=addPlanWindow()
        self.pbtn_new.clicked.connect(self.addplanWindow.show)
        self.pbtn_about.clicked.connect(self.about)
        self.addplanWindow.pbtn_OK.clicked.connect(self.getNewPlan)
        self.addplanWindow.pbtn_import.clicked.connect(self.ImportfromLocalFiles)
        try:
            with open(path+'/plan_data/plans.json','r')as f:
                self.plans=json.load(f)
                for i in list(self.plans.values()):
                    self.planNum+=1
                    self.addNewPlan(i['plan_content'],ischeck=i['finish'])
                    
        except:
            pass
    def about(self):
        QMessageBox.information(self,'关于','软件名：我的计划\n介绍：一款帮助你安排计划的日用小工具')
    def getNewPlan(self):
        self.planNum+=1
        self.plans[str(self.planNum)]={'add_time':time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime()),'plan_content':self.addplanWindow.lineEdit.text(),'finish':False}
        self.addplanWindow.lineEdit.clear()
        self.addplanWindow.hide()
        self.addNewPlan(self.plans[str(self.planNum)]['plan_content'])
    def addNewPlan(self,planname,ischeck=False):
        '''添加新计划到ui,变量中'''
        if self.planNum>11:
            self.planWindow.setMinimumSize(QSize(600, 400+40*(self.planNum-11)))
        self.verticalLayout_2.removeItem(self.spacerItem)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(f"horizontalLayout_{self.planNum}")
        self.cbox_plan2 = QCheckBox(self.planWindow)
        self.cbox_plan2.setMinimumSize(QSize(550, 30))
        self.cbox_plan2.setMaximumSize(QSize(16777215, 30))
        self.cbox_plan2.setObjectName(planname)
        self.cbox_plan2.setText(planname)
        if ischeck:
            self.cbox_plan2.setChecked(True)
        self.checkboxs[self.cbox_plan2]=str(self.planNum)
        self.cbox_plan2.destroyed.connect(self.updateplans)
        #bug
        self.horizontalLayout_2.addWidget(self.cbox_plan2)
        self.horizontalLayout_2.destroyed.connect(self.cbox_plan2.deleteLater)
        self.pbtn_delete_2 = QPushButton(self.planWindow)
        self.pbtn_delete_2.setMinimumSize(QSize(55, 25))
        self.pbtn_delete_2.setMaximumSize(QSize(55, 25))
        self.pbtn_delete_2.setObjectName(f"pbtn_delete_{self.planNum}")
        self.pbtn_delete_2.setText('删除')
        self.pbtn_delete_2.clicked.connect(self.pbtn_delete_2.deleteLater)
        self.pbtn_delete_2.destroyed.connect(self.horizontalLayout_2.deleteLater)
        self.horizontalLayout_2.addWidget(self.pbtn_delete_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addItem(self.spacerItem)
    def updateplans(self):
        new_plans={}
        new_checkboxs={}
        num=0
        for i in self.findChildren(QCheckBox):
            num+=1
            new_plans[str(num)]=self.plans[self.checkboxs[i]]
            new_checkboxs[i]=str(num)
        self.checkboxs=new_checkboxs
        self.plans=new_plans
        self.planNum=num
    
    def closeEvent(self, a0: QCloseEvent):
        children=self.findChildren(QCheckBox)
        for i in range(len(children)):
            if children[i].isChecked():
                self.plans[str(i+1)]['finish']=True
        
        with open(path+'/plan_data/plans.json','w')as f:
            json.dump(self.plans,f)
        sys.exit()
    def keyPressEvent(self, a0: QKeyEvent):
        if a0.key()==Qt.Key_Control and a0.key()==Qt.Key_N:
            self.pbtn_new.click()
    def ImportfromLocalFiles(self):
        filepath,_=QFileDialog.getOpenFileName(caption='选择文件',filter='(*.txt)')
        with open(filepath,'r',encoding='utf-8') as f:
            contents=re.split('\W',f.read(),flags=re.M)
        for i in contents:
            if len(i)>0:
                self.planNum+=1
                self.plans[str(self.planNum)]={'add_time':time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime()),'plan_content':i,'finish':False}
                self.addNewPlan(i)
        self.addplanWindow.hide()
        
class addPlanWindow(QMainWindow,Ui_Addplan):
    def __init__(self):
        super().__init__()
        self.addtime=0
        self.setupUi(self)
        self.setWindowIcon(QIcon(path+'/icons/hutao2.jpeg'))
        self.setWindowTitle('New')
    def keyPressEvent(self, a0: QKeyEvent):
        if a0.key()==Qt.Key_Return:
            self.pbtn_OK.click()


if __name__=='__main__':
    app=QApplication(sys.argv)
    m=main()
    sys.exit(app.exec_())

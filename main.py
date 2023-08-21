from PySide2 import QtGui
import PySide2.QtGui
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from mainwindow import Ui_MainWindow
from addplan import Ui_Addplan
from ui_countdown import Ui_Countdown
import sys
import time
import json
import os
import re
import random
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
        self.pbtn_limits={}
        self.planNum=0
        self.addplanWindow=addPlanWindow()
        self.countdownui=countdownUi()
        self.pbtn_new.clicked.connect(self.addplanWindow.show)
        self.pbtn_about.clicked.connect(self.about)
        self.addplanWindow.pbtn_OK.clicked.connect(self.getNewPlan)
        self.addplanWindow.pbtn_import.clicked.connect(self.ImportfromLocalFiles)
        try:
            with open(path+'/plan_data/plans.json','r')as f:
                self.plans=json.load(f)
                for i in list(self.plans.values()):
                    self.planNum+=1
                    self.addNewPlan(i['plan_content'],i['limit_time'],ischeck=i['finish'])
                    
        except:
            raise
    def about(self):
        QMessageBox.information(self,'关于','软件名：我的计划\n介绍：一款帮助你安排计划的日用小工具')
    def getNewPlan(self):
        if self.addplanWindow.lineEdit_limit.text():
            try:
                limit_time=float(self.addplanWindow.lineEdit_limit.text())
            except:
                QMessageBox.critical(self,'错误','请输入正确的时间')
                return
        else:
            limit_time=0.0
        self.planNum+=1
        self.plans[str(self.planNum)]={'add_time':time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime()),'plan_content':self.addplanWindow.lineEdit.text(),\
                                       'finish':False,'limit_time':limit_time}
        self.addplanWindow.lineEdit.clear()
        self.addplanWindow.hide()
        self.addNewPlan(self.plans[str(self.planNum)]['plan_content'],self.plans[str(self.planNum)]['limit_time'])
    def addNewPlan(self,planname:str,limit_time:float,ischeck=False):
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
        self.checkboxs[self.cbox_plan2]=str(self.planNum)
        self.cbox_plan2.destroyed.connect(self.updateplans)
        self.horizontalLayout_2.addWidget(self.cbox_plan2)
        self.horizontalLayout_2.destroyed.connect(self.cbox_plan2.deleteLater)
        if ischeck:
            self.cbox_plan2.setChecked(True)
        elif limit_time>0.0:
            self.cbox_plan2.setCheckable(False)
            self.cbox_plan2.setText(planname+f'（限时{limit_time}分钟）')
            self.pbtn_start = QPushButton(self.planWindow)
            self.pbtn_start.setMinimumSize(QSize(55, 25))
            self.pbtn_start.setMaximumSize(QSize(55, 25))
            self.pbtn_start.setObjectName(f"pbtn_start_{self.planNum}")
            self.pbtn_start.setText('开始')
            self.pbtn_start.destroyed.connect(self.cbox_plan2.deleteLater)
            self.pbtn_limits[self.pbtn_start]=str(self.planNum)
            self.horizontalLayout_2.addWidget(self.pbtn_start)
            self.horizontalLayout_2.destroyed.connect(self.pbtn_start.deleteLater)
            self.connectLimitItems()
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
        
    def connectLimitItems(self):
        pbtn=list(self.pbtn_limits.keys())[-1]
        pbtn.clicked.connect(lambda:self.countdownui.beginCount(self.plans,str(self.pbtn_limits[pbtn]),\
                                                                [k for k, v in self.checkboxs.items() if v == str(self.pbtn_limits[pbtn])][0]))
                                                                # list(self.checkboxs.keys())[self.pbtn_limits[pbtn]]))
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
            else:
                self.plans[str(i+1)]['finish']=False
        
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
        if self.checkbox_limit.isChecked():
            self.limit=True
        else:
            self.limit=False
        self.lineEdit_limit.setReadOnly(not self.limit)
        self.checkbox_limit.clicked.connect(self.changelimit)
    def keyPressEvent(self, a0: QKeyEvent):
        if a0.key()==Qt.Key_Return:
            self.pbtn_OK.click()
    def changelimit(self):
        self.limit=not self.limit
        self.lineEdit_limit.setReadOnly(not self.limit)
        self.lineEdit_limit.clear()
class countdownUi(QMainWindow,Ui_Countdown):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def beginCount(self,plandict:dict,planindex:str,checkbox:QCheckBox):
        '''plandict格式：{'1':{'add_time': '', 'plan_content': '', 'finish': False, 'limit_time': 0},'2':{}}'''
        if not checkbox.isChecked():
            self.show()
            self.showFullScreen()
            self.pictures=[QPixmap(path+'/backgrounds/'+i) for i in os.listdir(path+'/backgrounds')]
            self.label_picture.setPixmap(random.choice(self.pictures))
            self.label_picture.setScaledContents(True)
            self.content=plandict[planindex]['plan_content']
            self.Time_second=plandict[planindex]['limit_time']*60
            self.label_4.setText(f'计划名：{self.content}')
            self.lcdNumber_min.display(self.Time_second//60)
            self.lcdNumber_second.display(self.Time_second%60)
            self.pushButton_stop.clicked.connect(lambda:self.over(checkbox))
            self.timer=QTimer()
            self.timer.start(1000)
            self.timer.timeout.connect(lambda:self.timeoutEvent(checkbox))
        else:
            QMessageBox.information(self,'','已完成该计划')
    def timeoutEvent(self,checkbox:QCheckBox):
        self.Time_second-=1
        self.lcdNumber_min.display(self.Time_second//60)
        self.lcdNumber_second.display(self.Time_second%60)
        if self.Time_second<=0:
            self.over(checkbox,status=True)
    def over(self,checkbox:QCheckBox,status=False):
        self.timer.stop()
        checkbox.setCheckable(True)
        checkbox.setChecked(status)
        if status==True:
            QMessageBox.information(self,'恭喜',f'完成计划：{self.content}')
        self.close()


if __name__=='__main__':
    app=QApplication(sys.argv)
    m=main()
    sys.exit(app.exec_())

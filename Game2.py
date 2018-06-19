# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Game.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Game import Ui_Dialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(949, 818)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.Bat_No = QtWidgets.QLabel(self.centralwidget)
        self.Bat_No.setAutoFillBackground(False)
        self.Bat_No.setObjectName("Bat_No")
        self.horizontalLayout.addWidget(self.Bat_No)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.Bowl_No = QtWidgets.QLabel(self.centralwidget)
        self.Bowl_No.setObjectName("Bowl_No")
        self.horizontalLayout.addWidget(self.Bowl_No)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.All_No = QtWidgets.QLabel(self.centralwidget)
        self.All_No.setObjectName("All_No")
        self.horizontalLayout.addWidget(self.All_No)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.Wk_No = QtWidgets.QLabel(self.centralwidget)
        self.Wk_No.setObjectName("Wk_No")
        self.horizontalLayout.addWidget(self.Wk_No)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.lcdNumber = QtWidgets.QLabel(self.centralwidget)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout_4.addWidget(self.lcdNumber)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.lcdNumber_2 = QtWidgets.QLabel(self.centralwidget)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.horizontalLayout_4.addWidget(self.lcdNumber_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Bat_Btn = QtWidgets.QRadioButton(self.centralwidget)
        self.Bat_Btn.setEnabled(False)
        self.Bat_Btn.setObjectName("Bat_Btn")
        self.horizontalLayout_2.addWidget(self.Bat_Btn)
        self.Bowl_Btn = QtWidgets.QRadioButton(self.centralwidget)
        self.Bowl_Btn.setEnabled(False)
        self.Bowl_Btn.setObjectName("Bowl_Btn")
        self.horizontalLayout_2.addWidget(self.Bowl_Btn)
        self.All_Btn = QtWidgets.QRadioButton(self.centralwidget)
        self.All_Btn.setEnabled(False)
        self.All_Btn.setObjectName("All_Btn")
        self.horizontalLayout_2.addWidget(self.All_Btn)
        self.Wk_Btn = QtWidgets.QRadioButton(self.centralwidget)
        self.Wk_Btn.setEnabled(False)
        self.Wk_Btn.setObjectName("Wk_Btn")
        self.horizontalLayout_2.addWidget(self.Wk_Btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.list1 = QtWidgets.QListWidget(self.centralwidget)
        self.list1.setEnabled(False)
        self.list1.setObjectName("list1")
        self.verticalLayout.addWidget(self.list1)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Name_Label = QtWidgets.QLabel(self.centralwidget)
        self.Name_Label.setObjectName("Name_Label")
        self.horizontalLayout_3.addWidget(self.Name_Label)
        self.SetName = QtWidgets.QLineEdit(self.centralwidget)
        self.SetName.setEnabled(False)
        self.SetName.setObjectName("SetName")
        self.horizontalLayout_3.addWidget(self.SetName)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.list2 = QtWidgets.QListWidget(self.centralwidget)
        self.list2.setEnabled(False)
        self.list2.setObjectName("list2")
        self.verticalLayout_2.addWidget(self.list2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout_4, 4, 0, 1, 1)
        self.label_3.raise_()
        self.list1.raise_()
        self.label_8.raise_()
        self.label_7.raise_()
        self.label_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 949, 31))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Team = QtWidgets.QAction(MainWindow)
        self.actionNew_Team.setCheckable(False)
        self.actionNew_Team.setMenuRole(QtWidgets.QAction.TextHeuristicRole)
        self.actionNew_Team.setObjectName("actionNew_Team")
        self.actionEdit_Team = QtWidgets.QAction(MainWindow)
        self.actionEdit_Team.setObjectName("actionEdit_Team")
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.menuFile.addAction(self.actionNew_Team)
        self.menuFile.addAction(self.actionEdit_Team)
        self.menuFile.addAction(self.actionSAVE_Team)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionEVALUATE_Team)
        self.menubar.addAction(self.menuFile.menuAction())
        self.team=[]
        self.data1=[]
        self.bt_no=0
        self.bwl_no=0
        self.al_no=0
        self.w_no=0
        self.points_available=1000
        self.points_used=0
        self.count=0
        self.list1.itemDoubleClicked.connect(self.remove_listPlayers)
        self.list2.itemDoubleClicked.connect(self.remove_listTeam)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.menuFile.triggered[QtWidgets.QAction].connect(self.New)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Your Selections"))
        self.label_6.setText(_translate("MainWindow", "Batsmen(BAT)"))
        self.Bat_No.setText(_translate("MainWindow", "####"))
        self.label_8.setText(_translate("MainWindow", "Bowlers(BOWL)"))
        self.Bowl_No.setText(_translate("MainWindow", "####"))
        self.label_7.setText(_translate("MainWindow", "All-Rounders(ALL)"))
        self.All_No.setText(_translate("MainWindow", "####"))
        self.label_5.setText(_translate("MainWindow", "Wicket-Keeper(WK)"))
        self.Wk_No.setText(_translate("MainWindow", "####"))
        self.label_2.setText(_translate("MainWindow", "Points Available"))
        self.label.setText(_translate("MainWindow", "Points Used"))
        self.Bat_Btn.setText(_translate("MainWindow", "BAT"))
        self.Bowl_Btn.setText(_translate("MainWindow", "BOWL"))
        self.All_Btn.setText(_translate("MainWindow", "ALL"))
        self.Wk_Btn.setText(_translate("MainWindow", "WK"))
        self.Name_Label.setText(_translate("MainWindow", "Team Name:"))
        self.menuFile.setTitle(_translate("MainWindow", "ManageTeams"))
        self.actionNew_Team.setText(_translate("MainWindow", "New Team"))
        self.actionNew_Team.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionEdit_Team.setText(_translate("MainWindow", "Edit Team"))
        self.actionEdit_Team.setShortcut(_translate("MainWindow","Ctrl+E"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))

    def New(self,action):
        txt=action.text()
        if(txt=='New Team'):
            self.SetName.setEnabled(True)
            self.SetName.setText("")
            self.Bat_Btn.setEnabled(True)
            self.Bowl_Btn.setEnabled(True)
            self.Wk_Btn.setEnabled(True)
            self.All_Btn.setEnabled(True)
            self.lcdNumber.setEnabled(True)
            self.lcdNumber.setText("1000")
            self.lcdNumber_2.setEnabled(True)
            self.lcdNumber_2.setText("0")
            self.Bat_No.setText("0")
            self.Bowl_No.setText("0")
            self.All_No.setText("0")
            self.Wk_No.setText("0")
            self.lcdNumber_2.setText("0")
            self.list1.setEnabled(True)
            self.list2.setEnabled(True)
            # self.list2.addItem("Shubham:")
            self.Bat_Btn.toggled.connect(self.New_ListPopulate)
            self.Bowl_Btn.toggled.connect(self.New_ListPopulate)
            self.All_Btn.toggled.connect(self.New_ListPopulate)
            self.Wk_Btn.toggled.connect(self.New_ListPopulate)
        elif(txt=='Edit Team'):
            self.my_dialogue=QtWidgets.QDialog()
            self.my_ui=Ui_Dialog()
            self.my_ui.setupUi(self.my_dialogue)
            self.my_dialogue.show()

        elif(txt=='SAVE Team'):
            all_info=[self.bt_no,self.bwl_no,self.al_no,self.w_no,self.points_used]
            if(self.SetName.text() !=""):
                print(self.SetName.text)
                
                # print(str(self.SetName.text))

            else:
                print("Stop")
                self.my_dialogue=QtWidgets.QDialog()
                self.my_ui=Ui_Dialog()
                self.my_ui.setupUi(self.my_dialogue)
                self.my_dialogue.show()
                self.my_ui.label.setText("Enter the name of the team")
                # self.wen=Warning_Name()
                # self.wen.pop_up(self.my_warning)
                # self.my_warning.show()
                pass
            # My_Data=sqlite3.connect("D:\\SQLite studios\\Fantasy_PL")
            # csr=My_Data.cursor()



    def New_ListPopulate(self):
        # (points_available,points_used)=(1000,0)
        items=""
        i=0
        import sqlite3
        My_Data=sqlite3.connect("D:\\SQLite studios\\Fantasy_PL")
        csr=My_Data.cursor()
        if(self.Bat_Btn.isChecked()):
            self.list1.clear()
            i=0
            csr.execute('''SELECT PLAYER_NAME,VALUE,ctg FROM Stats WHERE ctg="BAT";''')
            record=csr.fetchall()
            for result in record:
                if result[0] not in self.team:
                    if result not in self.data1:
                        self.data1.append(result)
                    item=QtWidgets.QListWidgetItem()
                    self.list1.addItem(item)
                    item1=self.list1.item(i)
                    i+=1
                    item1.setText("%s"%result[0])
                elif(result in self.data1):
                    self.data1.remove(result)



        elif(self.Bowl_Btn.isChecked()):
            self.list1.clear()
            i=0
            csr.execute('''SELECT PLAYER_NAME,VALUE,ctg FROM Stats WHERE ctg="BOWL";''')
            record=csr.fetchall()
            for result in record:
                if result[0] not in self.team:
                    if result not in self.data1:
                        self.data1.append(result)
                    item1=QtWidgets.QListWidgetItem()
                    self.list1.addItem(item1)
                    items1=self.list1.item(i)
                    i+=1
                    items1.setText("%s"%result[0])
                elif(result in self.data1):
                    self.data1.remove(result)

            # self.list1.itemDoubleClicked.connect(self.remove_listPlayers)
        elif(self.All_Btn.isChecked()):
            self.list1.clear()
            i=0
            csr.execute('''SELECT PLAYER_NAME,VALUE,ctg FROM Stats WHERE ctg="ALL";''')
            record=csr.fetchall()
            for result in record:
                if result[0] not in self.team:
                    if result not in self.data1:
                        self.data1.append(result)
                    item1=QtWidgets.QListWidgetItem()
                    self.list1.addItem(item1)
                    items1=self.list1.item(i)
                    i+=1
                    items1.setText("%s"%result[0])
                elif(result in self.data1):
                    self.data1.remove(result)
            # self.list1.itemDoubleClicked.connect(self.remove_listPlayers)
        elif(self.Wk_Btn.isChecked()):
            self.list1.clear()
            i=0
            csr.execute('''SELECT PLAYER_NAME,VALUE,ctg FROM Stats WHERE ctg="WK";''')
            record=csr.fetchall()
            for result in record:
                if result[0] not in self.team:
                    if result not in self.data1:
                        self.data1.append(result)
                    item1=QtWidgets.QListWidgetItem()
                    self.list1.addItem(item1)
                    items1=self.list1.item(i)
                    i+=1
                    items1.setText("%s"%result[0])
                elif(result in self.data1):
                    self.data1.remove(result)
            # self.list1.itemDoubleClicked.connect(self.remove_listPlayers)
        
            
        My_Data.close()

    def remove_listPlayers(self,item):   
        self.list1.takeItem(self.list1.row(item))
        name=item.text()
        # print(name)
        # print((name,self.data1))
        for i in self.data1:
            # print('Etered')
            if(name==i[0]):
                # Points_Calc(self,i[1])
                # print("Enter")
                self.points_used+=i[1]
                # print(self.points_used)
                self.points_available-=i[1]
                # print(self.points_availabl
                if(i[2]=="BAT"):
                    self.bt_no+=1
                    print("Enet")
                    self.Bat_No.setText("%s"%str(self.bt_no))
                elif(i[2]=="BOWL"):
                    self.bwl_no+=1
                    self.Bowl_No.setText("%s"%str(self.bwl_no))
                elif(i[2]=="ALL"):
                    self.al_no+=1
                    self.All_No.setText("%s"%str(self.al_no))
                elif(i[2]=="WK"):
                    self.w_no+=1
                    self.Wk_No.setText("%s"%str(self.w_no))
                print("Etered")
                
                if(self.points_available<0):
                    self.points_available+=i[1]
                    self.points_used-=i[1]
                    self.lcdNumber.setText("%s"%str(self.points_available))
                    self.lcdNumber_2.setText("%s"%str(self.points_used))
                    print((self.data1,self.team))

                    # self.points_used-=i[1]
                    # self.points_available-=i[1]
                elif(self.points_available==0):
                    self.list1.setEnabled(False)
                    self.count=0
                    # print((self.data1,self.team))
                    # self.list2.addItems(self.team)
                elif(self.points_available>0):
                    self.lcdNumber.setText("%s"%str(self.points_available))
                    self.lcdNumber_2.setText("%s"%str(self.points_used))
                    # print("Bro")
                    self.team.append(name)
                    # print("Bro")
                    obj=QtWidgets.QListWidgetItem()
                    self.list2.addItem(obj)
                    it=self.list2.item(self.count)
                    self.count+=1
                    it.setText("%s"%self.team[-1])
                break        
           
    def remove_listTeam(self,item):
        self.list2.takeItem(self.list2.row(item))
        name=item.text()
        print((self.data1,self.team))
        for i in self.data1:
            # print("En")
            if(i[0]==name):
                # print("Yo")
                self.points_available+=i[1]
                self.points_used-=i[1]
                # print((self.points_available,self.points_used))
                self.lcdNumber_2.setText("%s"%str(self.points_used))
                self.lcdNumber.setText("%s"%str(self.points_available))
                if(i[2]=="BAT"):
                    self.bt_no-=1
                    self.Bat_No.setText("%s"%str(self.bt_no))
                elif(i[2]=="BOWL"):
                    self.bwl_no-=1
                    self.Bowl_No.setText("%s"%str(self.bwl_no))
                elif(i[2]=="ALL"):
                    self.al_no-=1
                    self.All_No.setText("%s"%str(self.al_no))
                elif(i[2]=="WK"):
                    self.w_no-=1
                    self.Wk_No.setText("%s"%str(self.w_no))

                self.team.remove(i[0])
                self.count-=1
                self.list1.addItem(name)
                # print((self.team,self.data1))
                break




        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


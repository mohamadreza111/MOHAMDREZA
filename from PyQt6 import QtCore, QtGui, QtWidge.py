from PyQt6 import QtCore, QtGui, QtWidgets
import json

class Ui_loginMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(290, 40, 251, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 70, 251, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(370, 120, 75, 24))
        self.pushButton.setObjectName("pushButton")

        self.pushButton2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(370, 180, 75, 24))
        self.pushButton2.setObjectName("singup")
        self.pushButton2.setHidden(True)
        self.pushButton2.setText("signup")


       
        self.setCentralWidget(self.centralwidget)
        self.w=None
        self.x=None
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar()
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        
        self.pushButton.clicked.connect(self.login)
        self.pushButton2.clicked.connect(self.signup)
        
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.lineEdit.setPlaceholderText( "UserName:")
        self.lineEdit_2.setPlaceholderText( "Password:")
        self.pushButton.setText( "login")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
     
    def login(self):
        name=self.lineEdit.text()
        password=self.lineEdit_2.text()
    
        file=open(r"C:\Users\Hp\Desktop\test311\result.json" , mode='r')
        save_data=json.load(file)
         
        file.close()

         
        for i in save_data:
             if i["Username"]== name and    i["password"]== password:
                if self.x is None:
                    self.x =dashbord()
                    self.x.show()
                
             else:
              
    
                self.pushButton2.setHidden(False)

    def signup(self):
       if self.w is None:
           self.w= Ui_singupMainWindow()
       self.w.show()


class Ui_singupMainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        #MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QVBoxLayout()
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit()
        self.lineEdit.setGeometry(QtCore.QRect(200, 50, 331, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit()
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 70, 331, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit()
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 90, 331, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setGeometry(QtCore.QRect(300, 150, 75, 24))
        self.pushButton.setObjectName("pushButton")
        
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        
        self.statusbar = QtWidgets.QStatusBar()
        self.statusbar.setObjectName("statusbar")
    
       # self.retranslateUi(MainWindow)
        #QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.save_data) 
    #def retranslateUi(self, MainWindow):
       # _translate = QtCore.QCoreApplication.translate
        #MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText( "Username:")
        self.lineEdit_2.setPlaceholderText( "Password:")
        self.lineEdit_3.setPlaceholderText ("re Password")
        self.pushButton.setText("Submit")

        self.centralwidget.addWidget(self.lineEdit)
        self.centralwidget.addWidget(self.lineEdit_2)
        self.centralwidget.addWidget(self.lineEdit_3)
        self.centralwidget.addWidget(self.pushButton)

        self.setLayout(self.centralwidget)
       
    def save_data(self):
        name=self.lineEdit.text()
        password=self.lineEdit_2.text()
        repassword=self.lineEdit_3.text()
        if password==repassword:
            file=open(r"C:\Users\Hp\Desktop\test311\result.json" , mode='r' )
            a=json.load(file)
            file.close()




            data={"Username":name,
                "password":password
                
            }
            a.append(data)

            with open( r"C:\Users\Hp\Desktop\test311\result.json",'w') as file:
                json.dump(a,file)

        


class dashbord(QtWidgets.QWidget):
    pass

import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
w=Ui_loginMainWindow()
w.show()




sys.exit(app.exec())

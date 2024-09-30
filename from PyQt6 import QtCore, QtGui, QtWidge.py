from PyQt6 import QtCore, QtGui, QtWidgets
import json
import hashlib
login_user=None
class Ui_loginMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.resize(900,600)
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
    
        file=open(r"C:\Users\Hp\Desktop\Mohamadrez\result.json" , mode='r')
        save_data=json.load(file)
         
        file.close()

         
        for i in save_data:
             if i["Username"]== name and    i["password"]==hashlib.sha256(password.encode("utf-8")).hexdigest():

                global login_user
                login_user=name

                if self.x is None:
                    self.x =dashbord()
                    self.x.show()
                self.x.change_user_label()
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



        if name!="" and password!="":

            if len(password)>=8:
                if'@' in password and '!' in password and '#' in password:
                
                    if password==repassword:
                
                       file=open(r"C:\Users\Hp\Desktop\Mohamadrez\result.json" , mode='r' )

                    a=json.load(file)
                
                    file.close()
                
                is_find=False
                for i in a:
                    if name==i["Username"]:
                        is_find=True
                        break

                if is_find==False:
                    




                    data={"Username":name,
                        "password":hashlib.sha256(password.encode("utf-8")).hexdigest()
                        
                    }
                    a.append(data)

                    with open( r"C:\Users\Hp\Desktop\Mohamadrez\result.json",'w') as file:
                        json.dump(a,file)
                        self.close()
                



                


class dashbord(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        centralwidget=QtWidgets.QVBoxLayout()
        self.lineEdit = QtWidgets.QLineEdit()
        self.lineEdit.setGeometry(QtCore.QRect(200, 50, 331, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit()
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 50, 331, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.btn_password=QtWidgets.QPushButton()
        self.show_pass=QtWidgets.QPushButton()
        self.btn_password.setObjectName("btn_password")
        self.show_pass.setObjectName("show_pass")
        self.btn_password.clicked.connect(self.save_password)
        self.show_pass.clicked.connect(self.show_password)
        self.btn_password.setText("password")
        centralwidget.addWidget(self.lineEdit)
        centralwidget.addWidget(self.lineEdit_2)
        centralwidget.addWidget(self.btn_password)
        centralwidget.addWidget(self.show_pass)
        
        

        self.lbl_username=QtWidgets.QLabel()
        self.lbl_username.setObjectName("lbl_username")
        self.change_user_label()
        self.resetpassword=QtWidgets.QPushButton()
        self.resetpassword.setObjectName("resetpassword")
        self.resetpassword.clicked.connect(self.reset_password_open)

        self.resetpassword.setText("resetpassword")
        centralwidget.addWidget(self.resetpassword)



        centralwidget.addWidget(self.lbl_username)

        self.setLayout(centralwidget)
        self.y=None

        self.show_reset_pass_page=None
    def change_user_label(self):
        global login_user
        self.lbl_username.setText("welcome"+login_user)
    
    def show_password(self):
       if self.y is None:
           self.y= list_password()
       self.y.show()

    def reset_password_open(self):
        if self.show_reset_pass_page is None:
            self.show_reset_pass_page=Reset_Password()

        self.show_reset_pass_page.show()

    def save_password(self):
                    global login_user
                    name=self.lineEdit.text()
                    password=self.lineEdit_2.text()
                    if len(name)>0 and len(password)>0:
                            file=open(r"C:\Users\Hp\Desktop\Mohamadrez\password.json" , mode='r' )

                            a=json.load(file)
                        
                            file.close()

                
                            data={"Username":login_user,
                                    "name":name,
                                "password":hashlib.sha256(password.encode("utf-8")).hexdigest()
                                
                                }
                            a.append(data)

                            with open( r"C:\Users\Hp\Desktop\Mohamadrez\password.json",'w') as file:
                                    json.dump(a,file)
                                #self.close()
                



class Reset_Password(QtWidgets.QWidget): 
    def __init__(self): 
        super().__init__() 
        centeralwidget = QtWidgets.QVBoxLayout() 
        self.pushButton = QtWidgets.QPushButton() 
        self.pushButton.setGeometry(QtCore.QRect(100, 270, 151, 51)) 
        self.pushButton.setObjectName("pushButton") 
        self.UserName = QtWidgets.QLineEdit() 
        self.UserName.setEnabled(True) 
        self.UserName.setGeometry(QtCore.QRect(10, 60, 321, 31)) 
        self.UserName.setObjectName("UserName") 
        self.UserName.setPlaceholderText("Write Your User Name") 
        self.label = QtWidgets.QLabel() 
        self.label.setGeometry(QtCore.QRect(60, 9, 221, 31)) 
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
        self.label.setObjectName("label") 
        self.Password = QtWidgets.QLineEdit() 
        self.Password.setEnabled(True) 
        self.Password.setGeometry(QtCore.QRect(10, 130, 321, 31)) 
        self.Password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal) 
        self.Password.setObjectName("Password") 
        self.Password.setPlaceholderText("Write Password") 
        self.RePassword = QtWidgets.QLineEdit() 
        self.RePassword.setEnabled(True) 
        self.RePassword.setGeometry(QtCore.QRect(10, 200, 321, 31)) 
        self.RePassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password) 
        self.RePassword.setObjectName("RePassword") 
        self.RePassword.setPlaceholderText("Write Password Again") 
        self.label = QtWidgets.QLabel() 
        self.label.setGeometry(QtCore.QRect(60, 9, 221, 31)) 
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
        self.label.setObjectName("label") 
        self.pushButton.clicked.connect(self.reset_password)
        self.pushButton.setText("Sign-Up") 
        self.label.setText( "WELLCOME") 
        centeralwidget.addWidget(self.label) 
        centeralwidget.addWidget(self.UserName) 
        centeralwidget.addWidget(self.Password) 
        centeralwidget.addWidget(self.RePassword) 
        centeralwidget.addWidget(self.pushButton) 
        self.setLayout(centeralwidget) 

    def reset_password(self):
        global login_user
        old_passwd=self.txt_old_passwd.text()
        new_passwd=self.txt_new_passwd.text()
        new_repasswd=self.txt.new_repasswd.text()
        if "@" in new_passwd and '!' in new_passwd and "#" in new_passwd:
            if old_passwd !="" and new_passwd != "":
                if new_passwd==new_repasswd:

                    file=open(r"C:\Users\Hp\Desktop\Mohamadrez\result.json" , mode='r' )

                    a=json.load(file)
                    file.close()

            for i in a:
                if hashlib.sha256(old_passwd.encode("utf-8")).hexdigest()==i["password"] and login_user==i["username"]:
                    i["password"]=hashlib.sha256(new_passwd.encode("utf-8")).hexdigest()
                    break

            file=open(r"C:\Users\Hp\Desktop\Mohamadrez\result.json" , mode="w" )
            
            json.dump(a,file)
            file.close()


class list_password(QtWidgets.QWidget):
     def __init__(self): 
        super().__init__() 
        centeralwidget = QtWidgets.QVBoxLayout() 
        self.lbl.all_passw=QtWidgets.QLabel()
        

    

import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
w=Ui_loginMainWindow()
w.show()




sys.exit(app.exec())

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color red")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 10, 113, 22))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        self.lineEdit.setFont(font)
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(170, 150, 160, 356))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.calender = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.calender.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.calender.setContentsMargins(1, 0, 0, 0)
        self.calender.setObjectName("calender")
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.calender.addWidget(self.pushButton_9, 1, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.calender.addWidget(self.pushButton_3, 6, 0, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.pushButton_11.setObjectName("pushButton_11")
        self.calender.addWidget(self.pushButton_11, 11, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.calender.addWidget(self.pushButton_6, 3, 0, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.pushButton_12.setObjectName("pushButton_12")
        self.calender.addWidget(self.pushButton_12, 10, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.calender.addWidget(self.pushButton, 2, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.calender.addWidget(self.pushButton_7, 5, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.calender.addWidget(self.pushButton_4, 7, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.calender.addWidget(self.pushButton_8, 8, 0, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.calender.addWidget(self.pushButton_10, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.calender.addWidget(self.pushButton_2, 4, 0, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(330, 150, 160, 146))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_13 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout.addWidget(self.pushButton_13)
        self.pushButton_14 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_14.setObjectName("pushButton_14")
        self.verticalLayout.addWidget(self.pushButton_14)
        self.pushButton_16 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_16.setObjectName("pushButton_16")
        self.verticalLayout.addWidget(self.pushButton_16)
        self.pushButton_15 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_15.setObjectName("pushButton_15")
        self.verticalLayout.addWidget(self.pushButton_15)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setText(_translate("MainWindow", "asa"))
        self.pushButton_9.setText(_translate("MainWindow", "1"))
        self.pushButton_3.setText(_translate("MainWindow", "6"))
        self.pushButton_11.setText(_translate("MainWindow", "10"))
        self.pushButton_6.setText(_translate("MainWindow", "3"))
        self.pushButton_12.setText(_translate("MainWindow", "9"))
        self.pushButton.setText(_translate("MainWindow", "2"))
        self.pushButton_7.setText(_translate("MainWindow", "5"))
        self.pushButton_4.setText(_translate("MainWindow", "7"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_10.setText(_translate("MainWindow", "0"))
        self.pushButton_2.setText(_translate("MainWindow", "4"))
        self.pushButton_5.setText(_translate("MainWindow", "+"))
        self.pushButton_13.setText(_translate("MainWindow", "="))
        self.pushButton_14.setText(_translate("MainWindow", "*"))
        self.pushButton_16.setText(_translate("MainWindow", "/"))
        self.pushButton_15.setText(_translate("MainWindow", "-"))

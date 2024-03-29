# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registerUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class registerForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(508, 448)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(-20, 0, 521, 441))
        self.widget.setStyleSheet("QPushButton#pushButtonRegister{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#pushButtonRegister:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton#pushButtonRegister:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}\n"
"\n"
"QPushButton#pushButtonCancel{\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color:rgba(85, 98, 112, 255);\n"
"}\n"
"\n"
"QPushButton#pushButtonCancel:hover{\n"
"    color: rgba(131, 96, 53, 255);\n"
"}\n"
"\n"
"QPushButton#pushButtonCancel:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    color:rgba(91, 88, 53, 255);\n"
"}\n"
"\n"
"")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(32, 7, 280, 430))
        self.label.setStyleSheet("border-image: url(:/images/background.jpg);\n"
"border-top-left-radius: 50px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(32, 7, 280, 430))
        self.label_2.setStyleSheet("background-color:rgba(0, 0, 0, 80);\n"
"border-top-left-radius: 50px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(262, 7, 251, 431))
        self.label_3.setStyleSheet("background-color:rgba(255, 255, 255, 255);\n"
"border-bottom-right-radius: 50px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(330, 10, 121, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(0, 0, 0, 200);")
        self.label_4.setObjectName("label_4")
        self.editEmail = QtWidgets.QLineEdit(self.widget)
        self.editEmail.setGeometry(QtCore.QRect(290, 60, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.editEmail.setFont(font)
        self.editEmail.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.editEmail.setObjectName("editEmail")
        self.editPassword = QtWidgets.QLineEdit(self.widget)
        self.editPassword.setGeometry(QtCore.QRect(290, 110, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.editPassword.setFont(font)
        self.editPassword.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.editPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.editPassword.setObjectName("editPassword")
        self.pushButtonRegister = QtWidgets.QPushButton(self.widget)
        self.pushButtonRegister.setGeometry(QtCore.QRect(290, 340, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonRegister.setFont(font)
        self.pushButtonRegister.setObjectName("pushButtonRegister")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(30, 60, 230, 81))
        self.label_6.setStyleSheet("background-color:rgba(0, 0, 0, 75);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(42, 57, 201, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgba(255, 255, 255, 200);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(110, 90, 131, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:rgba(0, 50, 160, 200);")
        self.label_8.setObjectName("label_8")
        self.editFirstName = QtWidgets.QLineEdit(self.widget)
        self.editFirstName.setGeometry(QtCore.QRect(290, 160, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.editFirstName.setFont(font)
        self.editFirstName.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.editFirstName.setObjectName("editFirstName")
        self.editLastName = QtWidgets.QLineEdit(self.widget)
        self.editLastName.setGeometry(QtCore.QRect(290, 210, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.editLastName.setFont(font)
        self.editLastName.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.editLastName.setObjectName("editLastName")
        self.editPhoneNumber = QtWidgets.QLineEdit(self.widget)
        self.editPhoneNumber.setGeometry(QtCore.QRect(290, 270, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.editPhoneNumber.setFont(font)
        self.editPhoneNumber.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.editPhoneNumber.setObjectName("editPhoneNumber")
        self.pushButtonCancel = QtWidgets.QPushButton(self.widget)
        self.pushButtonCancel.setGeometry(QtCore.QRect(330, 400, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonCancel.setFont(font)
        self.pushButtonCancel.setObjectName("pushButtonCancel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Register an account"))
        self.label_4.setText(_translate("Form", "Register"))
        self.editEmail.setPlaceholderText(_translate("Form", "  Email"))
        self.editPassword.setPlaceholderText(_translate("Form", "  Password"))
        self.pushButtonRegister.setText(_translate("Form", "Register"))
        self.label_7.setText(_translate("Form", "Object Detection"))
        self.label_8.setText(_translate("Form", "Application"))
        self.editFirstName.setPlaceholderText(_translate("Form", "  First Name"))
        self.editLastName.setPlaceholderText(_translate("Form", "  Last Name"))
        self.editPhoneNumber.setPlaceholderText(_translate("Form", "  Phone Number"))
        self.pushButtonCancel.setText(_translate("Form", "Cancel"))
import res_rc

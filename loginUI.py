from PyQt5 import QtCore, QtGui, QtWidgets
class loginForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(508, 448)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(-20, 0, 521, 441))
        self.widget.setStyleSheet("QPushButton#buttonLogin{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#buttonLogin:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton#buttonLogin:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}\n"
"\n"
"QPushButton#buttonRegister{\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color:rgba(85, 98, 112, 255);\n"
"}\n"
"\n"
"QPushButton#buttonRegister:hover{\n"
"    color: rgba(131, 96, 53, 255);\n"
"}\n"
"\n"
"QPushButton#buttonRegister:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    color:rgba(91, 88, 53, 255);\n"
"}\n"
"\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("python-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
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
        self.label_3.setGeometry(QtCore.QRect(262, 7, 251, 430))
        self.label_3.setStyleSheet("background-color:rgba(255, 255, 255, 255);\n"
"border-bottom-right-radius: 50px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(332, 57, 111, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(0, 0, 0, 200);")
        self.label_4.setObjectName("label_4")
        self.editEmail = QtWidgets.QLineEdit(self.widget)
        self.editEmail.setGeometry(QtCore.QRect(287, 127, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.editEmail.setFont(font)
        self.editEmail.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.editEmail.setObjectName("editUsername")
        self.editPassword = QtWidgets.QLineEdit(self.widget)
        self.editPassword.setGeometry(QtCore.QRect(287, 192, 190, 40))
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
        self.buttonLogin = QtWidgets.QPushButton(self.widget)
        self.buttonLogin.setGeometry(QtCore.QRect(287, 272, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.buttonLogin.setFont(font)
        self.buttonLogin.setObjectName("buttonLogin")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(320, 320, 131, 16))
        self.label_5.setStyleSheet("color:rgba(0, 0, 0, 210);")
        self.label_5.setObjectName("label_5")
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
        self.buttonRegister = QtWidgets.QPushButton(self.widget)
        self.buttonRegister.setGeometry(QtCore.QRect(330, 390, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.buttonRegister.setFont(font)
        self.buttonRegister.setObjectName("buttonRegister")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Log In"))
        self.label_4.setText(_translate("Form", "Log In"))
        self.editEmail.setPlaceholderText(_translate("Form", "  Email"))
        self.editPassword.setPlaceholderText(_translate("Form", "  Password"))
        self.buttonLogin.setText(_translate("Form", "L o g  I n"))
        self.label_5.setText(_translate("Form", "Forgot your password?"))
        self.label_7.setText(_translate("Form", "Object Detection"))
        self.label_8.setText(_translate("Form", "Application"))
        self.buttonRegister.setText(_translate("Form", "Register"))
import res_rc
# -*- coding: utf-8 -*-

# Form implementation generated from reading
# ui file 'insert.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file
# will be lost when pyuic5 is
# run again.  Do not edit this file unless you know
# what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mc

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(507, 224)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEditEmail = QtWidgets.QLineEdit(Form)
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.horizontalLayout.addWidget(self.lineEditEmail)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEditPassword = QtWidgets.QLineEdit(Form)
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.horizontalLayout_2.addWidget(self.lineEditPassword)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40,
        QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        
        #connected the pushbutton in here 
        self.pushButton.clicked.connect(self.insert_data)
        self.verticalLayout.addWidget(self.pushButton)
        self.labelResult = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelResult.setFont(font)
        self.labelResult.setText("")
        self.labelResult.setObjectName("labelResult")
        self.verticalLayout.addWidget(self.labelResult)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def insert_data(self):
        try:
            mydb = mc.connect(
                                host= "localhost",
                                user = "usersobjectdetection",
                                password = "manofsuccess1303",
                                database = "pyqt5")

            mycursor = mydb.cursor()

            email = self.lineEditEmail.text()
            password = self.lineEditPassword.text()

            query = "INSERT INTO users (email, password) VALUES (%s, %s)"
            value = (email, password)

            mycursor.execute(query, value)

            mydb.commit()
            self.labelResult.setText("Data Inserted ")

        except mc.Error as e:
            self.labelResult.setText("Error Inserting Data")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Email:"))
        self.label_2.setText(_translate("Form", "Password:"))
        self.pushButton.setText(_translate("Form", "Insert Data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
import re
import sys
from PyQt5.QtWidgets import *
from loginUI import loginForm
from registerUI import registerForm
from GUI import Ui_MainWindow
import mysql.connector

# Public password account


class skipWindow:
    windowMain = None
    windowLogin = None
    windowRegister = None

# This class is login interface


class windowLogin(QMainWindow):
    def __init__(self, parent=None):
        super(windowLogin, self).__init__(parent)
        self.loginUI = loginForm()
        self.loginUI.setupUi(self)
        self.initSlots()

    def initSlots(self):
        # Using login button and enter key
        self.loginUI.buttonLogin.clicked.connect(self.logIn)
        self.loginUI.editPassword.returnPressed.connect(self.logIn)
        self.loginUI.buttonRegister.clicked.connect(self.createID)

    # Skip to register UI
    def createID(self):
        skipWindow.windowRegister = windowRegister()
        skipWindow.windowRegister.show()

    # This function is to login using login button or press enter
    def logIn(self):
        # Get username and password from login GUI
        newEmail = self.loginUI.editEmail.text()
        newPassword = self.loginUI.editPassword.text()
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="yolov5")
            # Check password is match with database
            myCursor = mydb.cursor()
            query = "SELECT email, password from users where email " \
                    "like '" + newEmail + "'and password like '" \
                    + newPassword + "'"
            myCursor.execute(query)
            result = myCursor.fetchone()

            if result == None:
                replay = QMessageBox.warning(self, "Abort", "Incorrect login or password!", QMessageBox.Ok)
                return
            else:
                print("\nSkipping to main window\n\n")
                print('Logged In!')
                
                skipWindow.windowMain = Ui_MainWindow()
                skipWindow.windowMain.show()
        except mysql.exceptions.Error as e:
            replay = QMessageBox.warning(
                self, "Abort", "Unsuccessful login!", QMessageBox.Ok)
        self.close()

# Register GUI


class windowRegister(QDialog):
    def __init__(self, parent=None):
        super(windowRegister, self).__init__(parent)
        self.registerUI = registerForm()
        self.registerUI.setupUi(self)
        self.initSlots()

    # Click to register new account or cancel
    def initSlots(self):
        self.registerUI.pushButtonRegister.clicked.connect(self.newAccount)
        self.registerUI.pushButtonCancel.clicked.connect(self.cancel)

    # Create new account
    def newAccount(self):
        # Get all informations from register GUI
        newEmail = self.registerUI.editEmail.text()
        newPassword = self.registerUI.editPassword.text()
        newFirstName = self.registerUI.editFirstName.text()
        newLastName = self.registerUI.editLastName.text()
        newPhoneNumber = self.registerUI.editPhoneNumber.text()

        # make a pattern
        patternMain = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        pattern = "^[A-Za-z0-9_-]*$"

        if newEmail == "" or newPassword == "":
            replay = QMessageBox.warning(self, "Abort", "Invalid email or password!", QMessageBox.Ok)
        # elif bool(re.match(pattern, newEmail)) != True or bool(re.match(pattern, newPassword)) != True:
        #     replay = QMessageBox.warning(
        #         self, "Abort", "Invalid email or password!\nThose should be in latin!", QMessageBox.Ok)
        else:
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="yolov5")

                myCursor = mydb.cursor()
                # query = "SELECT count(*) FROM users WHERE email=%s"
                # myCursor.execute(query, newEmail)
                # if next(myCursor, None) is None:
                #     replay = QMessageBox.warning(self, "Abort", "The email address is exist!", QMessageBox.Ok)
                #     return

                queryAllInformations = "INSERT INTO users (firstName, lastName, email, password, phoneNumber) VALUES (%s, %s, %s, %s, %s)"
                value = (newFirstName, newLastName, newEmail, newPassword, newPhoneNumber)
                myCursor.execute(queryAllInformations, value)

                mydb.commit()
                replay = QMessageBox.warning(self, "Abort", "Successful register!", QMessageBox.Ok)

            except mysql.connector.Error as e:
                replay = QMessageBox.warning(
                    self, "Abort", "Unsuccessful register!", QMessageBox.Ok)
                mydb.close()
                return
            self.close()
    def cancel(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Choose Log In GUI is main GUI
    skipWindow.windowLogin = windowLogin()
    skipWindow.windowLogin.show()
    sys.exit(app.exec_())

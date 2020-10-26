from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from RegisterWin import Ui_RegisterWindow
import sqlite3
class QLabelClickable(QtWidgets.QLabel):
    clicked = QtCore.pyqtSignal(str)
    def __init__(self,parent=None):
        super(QLabelClickable,self).__init__(parent)
    def mousePressEvent(self,event):
        self.action = "click"
    def mouseReleaseEvent(self,event):
        if self.action == "click":
            self.clicked.emit(self.action)
class Ui_LoginWindow(object):
    def __init__(self,objWindow,MainWindow):
        self.loginWindow = objWindow
        self.MainWindow = MainWindow
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(800, 600)
        self.centralWidget = QtWidgets.QWidget(LoginWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.centralWidget.setStyleSheet("*{background-color:#f8ce58;}")
        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(140, 150, 521, 281))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(1)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet('QFrame {background-color: white}')
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(50, 30, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setFamily("Century Gothic")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(50, 120, 181, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setFamily("Century Gothic")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.btn_login = QtWidgets.QPushButton(self.frame)
        self.btn_login.setGeometry(QtCore.QRect(380, 190, 111, 31))
        self.btn_login.setAutoFillBackground(False)
        self.btn_login.setObjectName("btn_login")
        self.btn_login.clicked.connect(self.login)
        self.btn_login.setStyleSheet("QPushButton {background-color:darkgrey;border-width:2px;border-radius:10px}"
            "QPushButton:pressed {background-color:grey;border-width:2px;border-style:outset;border-radius:10px}")

        self.lbl_reg = QLabelClickable(self.frame)
        self.lbl_reg.setGeometry(QtCore.QRect(400, 230, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.lbl_reg.setFont(font)
        self.lbl_reg.setObjectName("lbl_reg")
        self.lbl_reg.clicked.connect(self.register)
        self.lbl_reg.setStyleSheet('QLabel {color: blue;}')
        self.lbl_reg.setCursor(QCursor(Qt.PointingHandCursor))

        self.line_email = QtWidgets.QLineEdit(self.frame)
        self.line_email.setGeometry(QtCore.QRect(240, 50, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_email.setFont(font)
        self.line_email.setObjectName("line_email")
        self.line_email.setPlaceholderText("Enter Email")
        self.line_email.setStyleSheet("QLineEdit{background-color:#8d98a1; border-style:outset ;border-radius:10px}")

        self.line_pass = QtWidgets.QLineEdit(self.frame)
        self.line_pass.setGeometry(QtCore.QRect(240, 140, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_pass.setFont(font)
        self.line_pass.setObjectName("line_pass")
        self.line_pass.setPlaceholderText("Enter Password")        
        self.line_pass.setEchoMode(QtWidgets.QLineEdit.Password)

        self.line_pass.setStyleSheet("QLineEdit{background-color:#8d98a1; border-style:outset ;border-radius:10px}")


        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(140, 70, 350, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setFamily("Century Gothic")
        self.label.setFont(font)
        self.label.setObjectName("label")
        LoginWindow.setCentralWidget(self.centralWidget)

        self.menuBar = QtWidgets.QMenuBar(LoginWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 17))
        self.menuBar.setObjectName("menuBar")
        LoginWindow.setMenuBar(self.menuBar)

        self.mainToolBar = QtWidgets.QToolBar(LoginWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        LoginWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)

        self.statusBar = QtWidgets.QStatusBar(LoginWindow)
        self.statusBar.setObjectName("statusBar")
        LoginWindow.setStatusBar(self.statusBar)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Parking Sure"))
        self.label_2.setText(_translate("LoginWindow", "Email:"))
        self.label_3.setText(_translate("LoginWindow", "Password:"))
        self.btn_login.setText(_translate("LoginWindow", "Login"))
        self.lbl_reg.setText(_translate("LoginWindow", "Register"))
        self.label.setText(_translate("LoginWindow", "Parking Sure"))

    def login(self):
        self.username = self.line_email.text()
        self.password = self.line_pass.text()
        if self.checkAccount() == True:
            self.loginWindow.close()
            self.MainWindow.show()
            self.check = True
        else:
            self.show_login_popup()
            self.check= False

    def checkAccount(self):
        try:
            with sqlite3.connect('userinfo.db') as conn:
                c = conn.cursor()
                c.execute("SELECT * FROM acc WHERE username=:username",{'username':self.username})
                listA = c.fetchall()
        except Exception as e:
            self.testTable()
            print(e)
        for a in listA:
            if a[3] == self.password:
                c.execute("UPDATE acc SET isactive = 1 WHERE username = :name AND password = :pass",
                    {'name':self.username,'pass':self.password})
                conn.commit()  
                conn.close()
                return True
            conn.close()
    def testTable(self):
        try:
            with sqlite3.connect('userinfo.db') as conn:
                conn.execute("""CREATE TABLE acc(
                          name text,
                          gender text,
                          username text,
                          password text,
                          phone text,
                          isactive integer
                          )""")
                conn.commit()
        except Exception as e:
                print(e)
        finally:
            conn.close()
    def show_login_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Fail to Login")
        msg.setText("Incorrect Username or Password!")
        msg.setIcon(QMessageBox.Warning)
        x = msg.exec_()

    def register(self):
        self.registerWindow = QtWidgets.QMainWindow()
        self.ui = Ui_RegisterWindow(self.registerWindow)
        self.ui.setupUi(self.registerWindow)
        self.registerWindow.show()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow(LoginWindow,LoginWindow)
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())

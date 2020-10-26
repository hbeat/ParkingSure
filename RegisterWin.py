from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
import abc
import sqlite3

class RegInfo(metaclass = abc.ABCMeta):
    def __init__(self,info):
        self.info = info
    @abc.abstractmethod
    def get(self):
        pass
class fullName(RegInfo):
    def __init__(self,name):
        super().__init__(name)
    def get(self):
        return self.info
class gender(RegInfo):
    def __init__(self,g):
        super().__init__(g)
    def get(self):
        return self.info   
class emailAddr(RegInfo):
    def __init__(self,email):
        super().__init__(email)
    def get(self):
        return self.info
class userPass(RegInfo):
    def __init__(self,password):
        super().__init__(password)
    def get(self):
        return self.info
class phone(RegInfo):
    def __init__(self,phone):
        super().__init__(phone)
    def get(self):
        return self.info

class Ui_RegisterWindow(object):
    def __init__(self,window):
        self.registerWin = window 
    def setupUi(self, RegisterWindow):
        RegisterWindow.setObjectName("RegisterWindow")
        RegisterWindow.resize(500, 450)
        RegisterWindow.setMinimumSize(QtCore.QSize(650, 430))
        RegisterWindow.setMaximumSize(QtCore.QSize(650, 430))
        
        RegisterWindow.setStyleSheet("*{background-color:#bdbdbd}")
        self.centralwidget = QtWidgets.QWidget(RegisterWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(70, 90, 189, 240))
        self.frame.setStyleSheet('QFrame {background-color: white}')
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")


        self.lbl_name = QtWidgets.QLabel(self.frame)
        self.lbl_name.setGeometry(QtCore.QRect(10, 0, 169, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_name.setFont(font)
        self.lbl_name.setObjectName("lbl_name")
        self.lbl_gender = QtWidgets.QLabel(self.frame)
        self.lbl_gender.setGeometry(QtCore.QRect(10, 50, 169, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_gender.setFont(font)
        self.lbl_gender.setObjectName("lbl_gender")
        self.lbl_email = QtWidgets.QLabel(self.frame)
        self.lbl_email.setGeometry(QtCore.QRect(10, 100, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_email.setFont(font)
        self.lbl_email.setObjectName("lbl_email")

        self.lbl_password = QtWidgets.QLabel(self.frame)
        self.lbl_password.setGeometry(QtCore.QRect(10, 150, 169, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_password.setFont(font)
        self.lbl_password.setObjectName("lbl_password")

        self.lbl_phone = QtWidgets.QLabel(self.frame)
        self.lbl_phone.setGeometry(QtCore.QRect(10, 200, 160, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_phone.setFont(font)
        self.lbl_phone.setObjectName("lbl_phone")

        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(250, 90, 300, 240))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setStyleSheet('QFrame {background-color: white}')
        self.line_name = QtWidgets.QLineEdit(self.frame_2)
        self.line_name.setGeometry(QtCore.QRect(10, 3, 200, 31))
        self.line_name.setText("")
        self.line_name.setPlaceholderText("")
        self.line_name.setObjectName("line_name")
        self.line_name.setStyleSheet("QLineEdit{background-color:#fada5e;; border-style:outset ;border-radius:10px}")

        self.combo_gender = QtWidgets.QComboBox(self.frame_2)
        self.combo_gender.setGeometry(QtCore.QRect(10, 50, 81, 31))
        self.combo_gender.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.combo_gender.setObjectName("combo_gender")
        self.combo_gender.addItem("")
        self.combo_gender.addItem("")
        self.combo_gender.setStyleSheet("QComboBox{background-color:#f6f6f6;}")
        self.line_email = QtWidgets.QLineEdit(self.frame_2)
        self.line_email.setGeometry(QtCore.QRect(10, 100, 181, 31))
        self.line_email.setText("")
        self.line_email.setObjectName("line_email")
        self.line_email.setStyleSheet("QLineEdit{background-color:#fada5e;; border-style:outset ;border-radius:10px}")

        self.line_pass = QtWidgets.QLineEdit(self.frame_2)
        self.line_pass.setGeometry(QtCore.QRect(10, 150, 181, 31))
        self.line_pass.setText("")
        self.line_pass.setObjectName("line_pass")
        self.line_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_pass.setStyleSheet("QLineEdit{background-color:#fada5e;; border-style:outset ;border-radius:10px}")

        self.line_phone = QtWidgets.QLineEdit(self.frame_2)
        self.line_phone.setGeometry(QtCore.QRect(10, 200, 140, 31))
        self.line_phone.setText("")
        self.line_phone.setObjectName("line_phone")
        self.line_phone.setMaxLength(10)
        self.line_phone.setStyleSheet("QLineEdit{background-color:#fada5e;; border-style:outset ;border-radius:10px}")
        self.onlyInt = QIntValidator()
        self.line_phone.setValidator(self.onlyInt)


        self.lbl_Title = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Title.setGeometry(QtCore.QRect(70, 30, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.lbl_Title.setFont(font)
        self.lbl_Title.setObjectName("lbl_Title")
        self.lbl_Title.setStyleSheet("QLabel{color:#00007f;}")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(270, 340, 191, 51))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")

        self.btn_register = QtWidgets.QPushButton(self.frame_3)
        self.btn_register.setGeometry(QtCore.QRect(100, 10, 71, 31))
        self.btn_register.setObjectName("btn_register")
        self.btn_register.clicked.connect(self.click_reg)
        self.btn_register.setStyleSheet("QPushButton {background-color:#878787;border-width:2px;border-radius:10px}"
            "QPushButton:pressed {background-color:lightgrey;border-width:2px;border-style:outset;border-radius:10px}")


        self.btn_cancel = QtWidgets.QPushButton(self.frame_3)
        self.btn_cancel.setGeometry(QtCore.QRect(20, 10, 71, 31))
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_cancel.clicked.connect(self.click_cancel)
        self.btn_cancel.setStyleSheet("QPushButton {background-color:#878787;border-width:2px;border-radius:10px}"
            "QPushButton:pressed {background-color:lightgrey;border-width:2px;border-style:outset;border-radius:10px}")


        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        RegisterWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RegisterWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 17))
        self.menubar.setObjectName("menubar")
        RegisterWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RegisterWindow)
        self.statusbar.setObjectName("statusbar")
        RegisterWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RegisterWindow)
        QtCore.QMetaObject.connectSlotsByName(RegisterWindow)

    def retranslateUi(self, RegisterWindow):
        _translate = QtCore.QCoreApplication.translate
        RegisterWindow.setWindowTitle(_translate("RegisterWindow", "Parking Sure"))
        self.lbl_name.setText(_translate("RegisterWindow", "Full Name"))
        self.lbl_gender.setText(_translate("RegisterWindow", "Gender"))
        self.lbl_email.setText(_translate("RegisterWindow", "Email Adress"))
        self.lbl_phone.setText(_translate("RegisterWindow", "Phone number"))
        self.lbl_password.setText(_translate("RegisterWindow", "Password"))
        self.line_name.setAccessibleDescription(_translate("RegisterWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.combo_gender.setItemText(0, _translate("RegisterWindow", "Male"))
        self.combo_gender.setItemText(1, _translate("RegisterWindow", "Female"))
        self.lbl_Title.setText(_translate("RegisterWindow", "Register"))
        self.btn_register.setText(_translate("RegisterWindow", "Register"))
        self.btn_cancel.setText(_translate("RegisterWindow", "Cancel"))

    def click_reg(self,info):
        self.n=fullName(self.line_name.text()) 
        self.g=gender(self.combo_gender.currentText())
        self.e=emailAddr(self.line_email.text()) 
        self.p=userPass(self.line_pass.text())
        self.t=phone(self.line_phone.text())
        self.save()
        self.registerWin.close()

    def click_cancel(self):
        self.registerWin.close()

    def save(self):
        try:
            with sqlite3.connect('userinfo.db') as conn:
                c = conn.cursor()
                c.execute("INSERT INTO acc VALUES (:name,:gender,:username,:password,:phone,0)"
                    ,{'name':self.n.get(),'gender':self.g.get(),'username':self.e.get(),'password':self.p.get(),'phone':self.t.get()})
                conn.commit()
        except Exception as e:
            print("Error no database file",e)       



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RegisterWindow = QtWidgets.QMainWindow()
    ui = Ui_RegisterWindow(RegisterWindow)
    ui.setupUi(RegisterWindow)
    RegisterWindow.show()
    sys.exit(app.exec_())

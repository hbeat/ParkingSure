from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import sqlite3
from datetime import datetime
from datetime import timedelta
from bookingWindow import Ui_BookWindow
from loginWindow import Ui_LoginWindow

class Ui_MainWindow(object):
    def __init__(self,main):
        self.main = main
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1400, 800)

        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1270, 20, 111, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.logOut)


        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 291, 71))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 131, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.viewParking)

        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 10, 141, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.viewLog)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1260, 670, 121, 71))
        self.pushButton_3.setObjectName("Book_Button")
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.clicked.connect(self.OpenBookWindow)

        self.frame_2 = QtWidgets.QFrame(self.centralWidget)
        self.frame_2.setGeometry(QtCore.QRect(20, 90, 1221, 651))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.Cartop_btn_10 = QtWidgets.QPushButton(self.frame_2)
        self.Cartop_btn_10.setGeometry(QtCore.QRect(1100, 30, 85, 140))
        self.Cartop_btn_10.setText("")
        self.Cartop_btn_10.setCheckable(True)
        self.Cartop_btn_10.setChecked(False)
        self.Cartop_btn_10.setObjectName("Cartop_btn_10")

        self.Car_btn_4 = QtWidgets.QPushButton(self.frame_2)
        self.Car_btn_4.setGeometry(QtCore.QRect(410, 480, 85, 140))
        self.Car_btn_4.setText("")
        self.Car_btn_4.setCheckable(True)
        self.Car_btn_4.setObjectName("Car_btn_4")

        self.Cartop_btn_1 = QtWidgets.QPushButton(self.frame_2)
        self.Cartop_btn_1.setGeometry(QtCore.QRect(40, 30, 85, 140))
        self.Cartop_btn_1.setText("")
        self.Cartop_btn_1.setCheckable(True)
        self.Cartop_btn_1.setObjectName("Cartop_btn_1")

        self.Cartop_btn_2 = QtWidgets.QPushButton(self.frame_2)
        self.Cartop_btn_2.setGeometry(QtCore.QRect(150, 30, 85, 140))
        self.Cartop_btn_2.setText("")
        self.Cartop_btn_2.setCheckable(True)
        self.Cartop_btn_2.setObjectName("Cartop_btn_2")

        self.Car_btn_8 = QtWidgets.QPushButton(self.frame_2)
        self.Car_btn_8.setGeometry(QtCore.QRect(880, 480, 85, 140))
        self.Car_btn_8.setText("")
        self.Car_btn_8.setCheckable(True)
        self.Car_btn_8.setObjectName("Car_btn_8")

        self.Car_btn_10 = QtWidgets.QPushButton(self.frame_2)
        self.Car_btn_10.setGeometry(QtCore.QRect(1100, 480, 85, 140))
        self.Car_btn_10.setText("")
        self.Car_btn_10.setCheckable(True)
        self.Car_btn_10.setObjectName("Car_btn_10")

        self.Car_btn_7 = QtWidgets.QPushButton(self.frame_2)
        self.Car_btn_7.setGeometry(QtCore.QRect(730, 480, 85, 140))
        self.Car_btn_7.setText("")
        self.Car_btn_7.setCheckable(True)
        self.Car_btn_7.setObjectName("Car_btn_7")

        self.Cartop_btn_8 = QtWidgets.QPushButton(self.frame_2)
        self.Cartop_btn_8.setGeometry(QtCore.QRect(880, 30, 85, 140))
        self.Cartop_btn_8.setText("")
        self.Cartop_btn_8.setCheckable(True)
        self.Cartop_btn_8.setObjectName("Cartop_btn_8")

        self.Car_btn_6 = QtWidgets.QPushButton(self.frame_2)
        self.Car_btn_6.setGeometry(QtCore.QRect(620, 480, 85, 140))
        self.Car_btn_6.setText("")
        self.Car_btn_6.setCheckable(True)
        self.Car_btn_6.setObjectName("Car_btn_6")

        self.Cartop_btn_6 = QtWidgets.QPushButton(self.frame_2)
        self.Cartop_btn_6.setGeometry(QtCore.QRect(620, 30, 85, 140))
        self.Cartop_btn_6.setText("")
        self.Cartop_btn_6.setCheckable(True)
        self.Cartop_btn_6.setObjectName("Cartop_btn_6")

        self.Car_btn_3 = QtWidgets.QPushButton(self.frame_2)
        self.Car_btn_3.setGeometry(QtCore.QRect(260, 480, 85, 140))
        self.Car_btn_3.setText("")
        self.Car_btn_3.setCheckable(True)
        self.Car_btn_3.setObjectName("Car_btn_3")

        self.Cartop_btn_7 = QtWidgets.QPushButton(self.frame_2)
        self.Cartop_btn_7.setGeometry(QtCore.QRect(720, 30, 85, 140))
        self.Cartop_btn_7.setText("")
        self.Cartop_btn_7.setCheckable(True)
        self.Cartop_btn_7.setObjectName("Cartop_btn_7")

        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(10, 10, 1201, 631))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Parking-Artwork.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.setScaledContents(True)

        self.Cartop_btn_3 = QtWidgets.QPushButton(self.frame_2)
        self.Cartop_btn_3.setGeometry(QtCore.QRect(260, 30, 85, 140))
        self.Cartop_btn_3.setText("")
        self.Cartop_btn_3.setCheckable(True)
        self.Cartop_btn_3.setObjectName("Cartop_btn_3")

        self.Car_btn_9 = QtWidgets.QPushButton(self.frame_2)
        self.Car_btn_9.setGeometry(QtCore.QRect(990, 480, 85, 140))
        self.Car_btn_9.setText("")
        self.Car_btn_9.setCheckable(True)
        self.Car_btn_9.setObjectName("Car_btn_9")

        self.Car_btn_2 = QtWidgets.QPushButton(self.frame_2)
        self.Car_btn_2.setGeometry(QtCore.QRect(150, 480, 85, 140))
        self.Car_btn_2.setText("")
        self.Car_btn_2.setCheckable(True)
        self.Car_btn_2.setObjectName("Car_btn_2")

        self.Car_btn_5 = QtWidgets.QPushButton(self.frame_2)
        self.Car_btn_5.setGeometry(QtCore.QRect(520, 480, 85, 140))
        self.Car_btn_5.setText("")
        self.Car_btn_5.setCheckable(True)
        self.Car_btn_5.setObjectName("Car_btn_5")

        self.Cartop_btn_4 = QtWidgets.QPushButton(self.frame_2)
        self.Cartop_btn_4.setGeometry(QtCore.QRect(410, 30, 85, 140))
        self.Cartop_btn_4.setText("")
        self.Cartop_btn_4.setCheckable(True)
        self.Cartop_btn_4.setObjectName("Cartop_btn_4")

        self.Cartop_btn_5 = QtWidgets.QPushButton(self.frame_2)
        self.Cartop_btn_5.setGeometry(QtCore.QRect(520, 30, 85, 140))
        self.Cartop_btn_5.setText("")
        self.Cartop_btn_5.setCheckable(True)
        self.Cartop_btn_5.setObjectName("Cartop_btn_5")

        self.Cartop_btn_9 = QtWidgets.QPushButton(self.frame_2)
        self.Cartop_btn_9.setGeometry(QtCore.QRect(990, 30, 85, 140))
        self.Cartop_btn_9.setText("")
        self.Cartop_btn_9.setCheckable(True)
        self.Cartop_btn_9.setObjectName("Cartop_btn_9")


        self.Car_btn_1 = QtWidgets.QPushButton(self.frame_2)
        self.Car_btn_1.setGeometry(QtCore.QRect(40, 480, 85, 140))
        self.Car_btn_1.setText("")
        self.Car_btn_1.setCheckable(True)
        self.Car_btn_1.setObjectName("Car_btn_1")


        self.check = 1
        self.Cartop_btn_1.clicked.connect(lambda: self.selectSlot(self.Cartop_btn_1))
        self.Cartop_btn_2.clicked.connect(lambda: self.selectSlot(self.Cartop_btn_2))
        self.Cartop_btn_3.clicked.connect(lambda: self.selectSlot(self.Cartop_btn_3))
        self.Cartop_btn_4.clicked.connect(lambda: self.selectSlot(self.Cartop_btn_4))
        self.Cartop_btn_5.clicked.connect(lambda: self.selectSlot(self.Cartop_btn_5))
        self.Cartop_btn_6.clicked.connect(lambda: self.selectSlot(self.Cartop_btn_6))
        self.Cartop_btn_7.clicked.connect(lambda: self.selectSlot(self.Cartop_btn_7))
        self.Cartop_btn_8.clicked.connect(lambda: self.selectSlot(self.Cartop_btn_8))
        self.Cartop_btn_9.clicked.connect(lambda: self.selectSlot(self.Cartop_btn_9))
        self.Cartop_btn_10.clicked.connect(lambda: self.selectSlot(self.Cartop_btn_10))

        self.Car_btn_1.clicked.connect(lambda: self.selectSlot(self.Car_btn_1))
        self.Car_btn_2.clicked.connect(lambda: self.selectSlot(self.Car_btn_2))
        self.Car_btn_3.clicked.connect(lambda: self.selectSlot(self.Car_btn_3))
        self.Car_btn_4.clicked.connect(lambda: self.selectSlot(self.Car_btn_4))
        self.Car_btn_5.clicked.connect(lambda: self.selectSlot(self.Car_btn_5))
        self.Car_btn_6.clicked.connect(lambda: self.selectSlot(self.Car_btn_6))
        self.Car_btn_7.clicked.connect(lambda: self.selectSlot(self.Car_btn_7))
        self.Car_btn_8.clicked.connect(lambda: self.selectSlot(self.Car_btn_8))
        self.Car_btn_9.clicked.connect(lambda: self.selectSlot(self.Car_btn_9))
        self.Car_btn_10.clicked.connect(lambda: self.selectSlot(self.Car_btn_10))

        self.frame_3 = QtWidgets.QFrame(self.centralWidget)
        self.frame_3.setGeometry(QtCore.QRect(20, 90, 1221, 651))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")

        self.table = QtWidgets.QTableWidget(self.frame_3)
        self.table.setGeometry(QtCore.QRect(10, 10, 935, 631))
        self.table.setObjectName("tableLogs")
        self.table.setColumnCount(6)
        self.table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.table.setHorizontalHeaderLabels(['User','phone number','Start Date', 'Start Time','Total Hours','Slot'])

        self.label.raise_()
        self.Cartop_btn_10.raise_()
        self.Car_btn_4.raise_()
        self.Cartop_btn_1.raise_()
        self.Cartop_btn_2.raise_()
        self.Car_btn_8.raise_()
        self.Car_btn_10.raise_()
        self.Car_btn_7.raise_()
        self.Cartop_btn_8.raise_()
        self.Car_btn_6.raise_()
        self.Cartop_btn_6.raise_()
        self.Car_btn_3.raise_()
        self.Cartop_btn_7.raise_()
        self.Cartop_btn_3.raise_()
        self.Car_btn_9.raise_()
        self.Car_btn_2.raise_()
        self.Car_btn_5.raise_()
        self.Cartop_btn_4.raise_()
        self.Cartop_btn_5.raise_()
        self.Cartop_btn_9.raise_()
        self.Car_btn_1.raise_()
        self.frame_2.raise_()
        self.pushButton_4.raise_()
        self.frame.raise_()
        self.pushButton_3.raise_()
        MainWindow.setCentralWidget(self.centralWidget)

        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1400, 17))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)

        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Parking Sure"))
        self.pushButton_4.setText(_translate("MainWindow", "Log Out"))
        self.pushButton.setText(_translate("MainWindow", "View Parking"))
        self.pushButton_2.setText(_translate("MainWindow", "View Booking Log"))
        self.pushButton_3.setText(_translate("MainWindow", "Book"))

        self.Cartop_btn_1.setText(_translate("MainWindow","1"))
        self.Cartop_btn_2.setText(_translate("MainWindow","2"))
        self.Cartop_btn_3.setText(_translate("MainWindow","3"))
        self.Cartop_btn_4.setText(_translate("MainWindow","4"))
        self.Cartop_btn_5.setText(_translate("MainWindow","5"))
        self.Cartop_btn_6.setText(_translate("MainWindow","6"))
        self.Cartop_btn_7.setText(_translate("MainWindow","7"))
        self.Cartop_btn_8.setText(_translate("MainWindow","8"))
        self.Cartop_btn_9.setText(_translate("MainWindow","9"))
        self.Cartop_btn_10.setText(_translate("MainWindow","10"))

        self.Car_btn_1.setText(_translate("MainWindow","11"))
        self.Car_btn_2.setText(_translate("MainWindow","12"))
        self.Car_btn_3.setText(_translate("MainWindow","13"))
        self.Car_btn_4.setText(_translate("MainWindow","14"))
        self.Car_btn_5.setText(_translate("MainWindow","15"))
        self.Car_btn_6.setText(_translate("MainWindow","16"))
        self.Car_btn_7.setText(_translate("MainWindow","17"))        
        self.Car_btn_8.setText(_translate("MainWindow","18"))
        self.Car_btn_9.setText(_translate("MainWindow","19"))
        self.Car_btn_10.setText(_translate("MainWindow","20"))

    def OpenBookWindow(self):
        self.time = 0
        self.Bookwindow = QtWidgets.QMainWindow()
        self.ui = Ui_BookWindow(self,self.Bookwindow,self.slot,self.selectbtn)
        self.ui.setupUi(self.Bookwindow)
        self.Bookwindow.show()
    def HideWindow(self):
        MainWindow.hide()

    def logOut(self):
        self.main.close()
        try:
            with sqlite3.connect('userinfo.db') as conn:
                c = conn.cursor()
                c.execute("""UPDATE acc SET isactive = 0
                            Where isactive = :status""",{'status':1})
                conn.commit()
        except Exception as e:
            print(e)

        newMainWindow = QtWidgets.QMainWindow()
        newui = Ui_MainWindow(newMainWindow)
        newui.setupUi(newMainWindow)

        self.check = 1
        self.Loginwindow = QtWidgets.QMainWindow()
        self.ui = Ui_LoginWindow(self.Loginwindow,newMainWindow)
        self.ui.setupUi(self.Loginwindow)
        self.Loginwindow.show()

    def viewParking(self):
        self.frame_2.hide()
        self.frame_2.show()

    def viewLog(self):
        self.frame_2.hide()
        self.frame_3.show()
        self.showLog()

    def showLog(self):
        try:
            with sqlite3.connect('userinfo.db') as con:
                c = con.cursor()
                c.execute("SELECT * FROM acc")
                user = c.fetchall()
                con.commit()
            with sqlite3.connect('carlog.db') as conn:
                logs=conn.execute("SELECT * FROM logs")
                conn.commit()
                self.table.setRowCount(0)
                for row_number,row_data in enumerate(logs):
                    self.table.insertRow(row_number)
                    for row in user:     
                        if row[2]==row_data[4]:
                            self.table.setItem(row_number,0,QtWidgets.QTableWidgetItem(str(row[0])))
                            self.table.setItem(row_number,1,QtWidgets.QTableWidgetItem(str(row[4])))
                    for column_number,data in enumerate(row_data):
                        self.table.setItem(row_number,column_number+2,QtWidgets.QTableWidgetItem(str(data)))
        except Exception as e:
            print(e)
        finally:
            conn.close()
            con.close()

    def selectSlot(self,btn):
        if btn.isChecked():
            btn.setStyleSheet('QPushButton {background-image: url(Car-Artwork1.png)}')
            self.slot = str(btn.text())
            self.pushButton_3.setEnabled(True)
            if self.check == 0:
                btn.setStyleSheet('QPushButton {background-image: none}')
                btn.setChecked(False)
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("You already select a slot!")
                msg.setIcon(QMessageBox.Critical)
                self.pushButton_3.setEnabled(False)
                x = msg.exec_()
            self.check = 0
            self.selectbtn = btn
        else:
            btn.setStyleSheet('QPushButton {background-image: none}')
            self.slot = ""
            self.pushButton_3.setEnabled(False)
            self.check = 1

    def showBookedSlot(self,selectTime=0):
        btnDic = {"1":self.Cartop_btn_1,"2":self.Cartop_btn_2,"3":self.Cartop_btn_3,"4":self.Cartop_btn_4,"5":self.Cartop_btn_5,
        "6":self.Cartop_btn_6,"7":self.Cartop_btn_7,"8":self.Cartop_btn_8,"9":self.Cartop_btn_9,"10":self.Cartop_btn_10,
        "11":self.Car_btn_1,"12":self.Car_btn_2,"13":self.Car_btn_3,"14":self.Car_btn_4,"15":self.Car_btn_5,"16":self.Car_btn_6,
        "17":self.Car_btn_7,"18":self.Car_btn_8,"19":self.Car_btn_9,"20":self.Car_btn_10}
        try:
            with sqlite3.connect('carlog.db') as conn:
                c = conn.cursor()
                c.execute("SELECT * FROM logs")
                logs = c.fetchall()
                conn.commit()
                base = datetime(2019,12,23)
                for log in logs:
                    date = log[0].split('-')
                    time = log[1].split(':')
                    d = datetime(int(date[0]),int(date[1]),int(date[2]),int(time[0]))
                    dayhour = abs(d-base).days*24
                    hour = abs(d-base).seconds//3600
                    start_offset = dayhour+hour
                    end_offset = start_offset+ log[2]
                    if(start_offset<=selectTime<end_offset or start_offset<selectTime<=end_offset):
                        btn = btnDic[log[3]]
                        btn.setStyleSheet('QPushButton {background-image: url(Car-Artwork1.png)}')
                        btn.setChecked(True)
                        btn.setEnabled(False)
                self.check = 1
        except Exception as e:
          print(e)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    ui.setupUi(MainWindow)

    Loginwindow = QtWidgets.QMainWindow()
    logui= Ui_LoginWindow(Loginwindow,MainWindow)
    logui.setupUi(Loginwindow)
    Loginwindow.show()
    sys.exit(app.exec_())

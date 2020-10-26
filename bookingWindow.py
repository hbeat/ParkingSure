import sqlite3
from datetime import datetime
from datetime import timedelta
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BookWindow(object):
    def __init__(self,parent,qWindow,slot,btn):
        self.BookWindow = qWindow
        self.slot = slot
        self.selectbtn = btn
        self.parent = parent
    def setupUi(self, BookWindow):
        self.testTable()
        BookWindow.setObjectName("BookWindow")
        BookWindow.resize(1200, 827)
        self.centralWidget = QtWidgets.QWidget(BookWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.lbl_title = QtWidgets.QLabel(self.centralWidget)
        self.lbl_title.setGeometry(QtCore.QRect(-110, 50, 1431, 81))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.lbl_title.setFont(font)
        self.lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_title.setObjectName("lbl_title")
        self.timeEditStart = QtWidgets.QTimeEdit(self.centralWidget)
        self.timeEditStart.setEnabled(True)
        self.timeEditStart.setGeometry(QtCore.QRect(390, 550, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setKerning(True)
        self.timeEditStart.setFont(font)
        self.timeEditStart.setAccessibleDescription("")
        self.timeEditStart.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.timeEditStart.setWrapping(False)
        self.timeEditStart.setAlignment(QtCore.Qt.AlignCenter)
        self.timeEditStart.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 12, 23), QtCore.QTime(16,0,0)))
        self.timeEditStart.setDate(QtCore.QDate(2019, 12, 23))
        self.timeEditStart.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.timeEditStart.setObjectName("timeEditStart")


        self.dateEditStart = QtWidgets.QDateEdit(self.centralWidget)
        self.dateEditStart.setGeometry(QtCore.QRect(610, 180, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateEditStart.setFont(font)
        self.dateEditStart.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.dateEditStart.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEditStart.setReadOnly(True)
        self.dateEditStart.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateEditStart.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 12, 23), QtCore.QTime(0, 0, 0)))
        self.dateEditStart.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2019, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEditStart.setMinimumDate(QtCore.QDate(2019, 1, 1))
        self.dateEditStart.setObjectName("dateEditStart")
        self.dateEditStart.setStyleSheet("QDateEdit{border-style:solid;border:0.5px solid;border-radius:20px;}")

        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(450, 180, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(230, 550, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(700, 550, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.lbl_slot = QtWidgets.QLabel(self.centralWidget)
        self.lbl_slot.setGeometry(QtCore.QRect(230, 150, 140, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_slot.setFont(font)
        self.lbl_slot.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_slot.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lbl_slot.setObjectName("lbl_slot")
        self.lbl_slot.setStyleSheet("QLabel{background-color:#fada5e;}")

        self.comboBoxDuration = QtWidgets.QComboBox(self.centralWidget)
        self.comboBoxDuration.setEnabled(True)
        self.comboBoxDuration.setGeometry(QtCore.QRect(910, 550, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBoxDuration.setFont(font)
        self.comboBoxDuration.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.comboBoxDuration.setAcceptDrops(False)
        self.comboBoxDuration.setAccessibleDescription("")
        self.comboBoxDuration.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBoxDuration.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.comboBoxDuration.setEditable(True)
        self.comboBoxDuration.setMinimumContentsLength(0)
        self.comboBoxDuration.setObjectName("comboBoxDuration")
        self.comboBoxDuration.addItem("")
        self.comboBoxDuration.addItem("")
        self.comboBoxDuration.addItem("")
        self.comboBoxDuration.addItem("")
        self.comboBoxDuration.addItem("")
        self.comboBoxDuration.addItem("")
        self.comboBoxDuration.addItem("")
        self.comboBoxDuration.addItem("")
        self.comboBoxDuration.addItem("")
        self.comboBoxDuration.addItem("")

        self.btn_confirm = QtWidgets.QPushButton(self.centralWidget)
        self.btn_confirm.setGeometry(QtCore.QRect(510, 670, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_confirm.setFont(font)
        self.btn_confirm.setObjectName("btn_confirm")
        self.btn_confirm.clicked.connect(self.pressed)
        self.btn_confirm.setStyleSheet("QPushButton{border-radius:20px;border-width:2px;border-style:inset;background-color:rgb(220, 220, 220);}"
"QPushButton:Pressed{border-radius:20px;border-width:2px;border-style:outset;background-color:rgb(200, 200, 200);}")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralWidget)
        self.calendarWidget.setGeometry(QtCore.QRect(460, 250, 352, 250))
        self.calendarWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.calendarWidget.setSelectedDate(QtCore.QDate(2019, 12, 23))
        self.calendarWidget.setMinimumDate(QtCore.QDate(2019, 12, 23))
        self.calendarWidget.setFirstDayOfWeek(QtCore.Qt.Sunday)
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setSelectionMode(QtWidgets.QCalendarWidget.SingleSelection)
        self.calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.SingleLetterDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setObjectName("calendarWidget")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(1030, 550, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        BookWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(BookWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1200, 30))
        self.menuBar.setObjectName("menuBar")
        BookWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(BookWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        BookWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(BookWindow)
        self.statusBar.setObjectName("statusBar")
        BookWindow.setStatusBar(self.statusBar)

        self.retranslateUi(BookWindow)
        self.comboBoxDuration.setCurrentIndex(0)
        self.calendarWidget.clicked['QDate'].connect(self.dateEditStart.setDate)
        QtCore.QMetaObject.connectSlotsByName(BookWindow)

    def retranslateUi(self, BookWindow):
        _translate = QtCore.QCoreApplication.translate
        BookWindow.setWindowTitle(_translate("BookWindow", "Parking Sure"))
        self.lbl_title.setText(_translate("BookWindow", "Book Slot"))
        self.timeEditStart.setDisplayFormat(_translate("BookWindow", "hh:mm"))
        self.label_2.setText(_translate("BookWindow", "Select Date:"))
        self.label_3.setText(_translate("BookWindow", "Start Time:"))
        self.label_4.setText(_translate("BookWindow", "Select Duration:"))
        self.comboBoxDuration.setCurrentText(_translate("BookWindow", "1"))
        self.comboBoxDuration.setItemText(0, _translate("BookWindow", "1"))
        self.comboBoxDuration.setItemText(1, _translate("BookWindow", "2"))
        self.comboBoxDuration.setItemText(2, _translate("BookWindow", "3"))
        self.comboBoxDuration.setItemText(3, _translate("BookWindow", "4"))
        self.comboBoxDuration.setItemText(4, _translate("BookWindow", "5"))
        self.comboBoxDuration.setItemText(5, _translate("BookWindow", "6"))
        self.comboBoxDuration.setItemText(6, _translate("BookWindow", "7"))
        self.comboBoxDuration.setItemText(7, _translate("BookWindow", "8"))
        self.comboBoxDuration.setItemText(8, _translate("BookWindow", "9"))
        self.comboBoxDuration.setItemText(9, _translate("BookWindow", "10"))
        self.btn_confirm.setText(_translate("BookWindow", "Confirm"))
        self.label_5.setText(_translate("BookWindow", "hours"))
        self.lbl_slot.setText(_translate("BookWindow", "Slot "+str(self.slot)))



    def pressed(self):
        self.duration =int(self.comboBoxDuration.currentText())
        self.timeValue = self.timeEditStart.time().toString()
        self.dateValue = self.dateEditStart.date().toPyDate()
        self.add()
        self.selectbtn.setEnabled(False)
        self.BookWindow.close()
    def testTable(self):
        try:
            with sqlite3.connect('carlog.db') as conn:
                conn.execute("""CREATE TABLE logs (
                startDate text,
                startTime text,
                duration integer,
                slot text,
                user_id int
                )""")
                conn.commit()
        except Exception as e:
                print(e)
        finally:
            conn.close()

    def add(self):
        if(self.checktime()!=False):
            try:
                with sqlite3.connect('userinfo.db') as con:
                    curs = con.cursor()
                    curs.execute("SELECT * FROM acc WHERE isactive=1")                 
                    user = curs.fetchone()
                    con.commit()
                with sqlite3.connect('carlog.db') as conn:
                    c = conn.cursor()
                    c.execute("INSERT INTO logs VALUES  (:startDate, :startTime, :duration ,:slot ,:user_id)",
                        {'startDate':self.dateValue,'startTime':self.timeValue,'duration':self.duration,
                        'slot':self.slot,'user_id':str(user[2])})
                    conn.commit()
                    con.close()
                self.show_book_popup()
                self.parent.pushButton_3.setEnabled(False)
            except Exception as e:
                print(e)
        return
    def checktime(self):
        base = datetime(2019,12,23)
        s_date = str(self.dateValue).split('-')
        s_time = str(self.timeValue).split(':')
        self.select_d = datetime(int(s_date[0]),int(s_date[1]),int(s_date[2]),int(s_time[0]))
        d_offset = (abs((self.select_d - base).days)*24)+(abs((self.select_d-base).seconds)//3600)
        d_end_offset= d_offset+self.duration
        try:
            with sqlite3.connect('carlog.db') as conn:
                c = conn.cursor()
                c.execute("SELECT * FROM logs")
                logs = c.fetchall()
                conn.commit()
                for log in logs:
                    date = log[0].split('-')
                    time = log[1].split(':')
                    d = datetime(int(date[0]),int(date[1]),int(date[2]),int(time[0]))
                    dayhour = abs(d-base).days*24
                    hour = abs(d-base).seconds//3600
                    start_offset = dayhour+hour
                    end_offset = start_offset+ log[2]
                    if((self.slot == log[3]) and (start_offset<=d_offset<end_offset or start_offset<d_end_offset<=end_offset)):
                        self.parent.time = d_offset
                        self.show_slot_warning()
                        self.parent.showBookedSlot(d_offset)
                        self.parent.pushButton_3.setEnabled(False)
                        self.parent.check = 1
                        return False
            return True
        except Exception as e:
          print(e)

    def show_slot_warning(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Fails to Book")
        msg.setText("This slot is already booked\nPlease select other slot")
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        x = msg.exec_()

    def show_book_popup(self):
        msg1 = QtWidgets.QMessageBox()
        msg1.setWindowTitle("Booking Information")
        msg1.setText("Complete Booked\t\t\t\t")
        msg1.setIcon(QtWidgets.QMessageBox.Information)
        msg1.setStandardButtons(QtWidgets.QMessageBox.Ok)
        d = timedelta(hours =self.duration)
        end = str(self.select_d +d)
        msg1.setInformativeText("Booking details:\nSlot number "+str(self.slot)+'\nDate: '+str(self.dateValue)+" Time: "+
            str(self.timeValue)+'\nBook hours:'+str(self.duration)+" Hrs.\nEnd: "+end)
        x = msg1.exec_()
if __name__ == "__main__":
    import sys
    a = 0
    app = QtWidgets.QApplication(sys.argv)
    BookWindow = QtWidgets.QMainWindow()
    btn = QtWidgets.QPushButton()
    ui = Ui_BookWindow(a,BookWindow,0,btn)
    ui.setupUi(BookWindow)
    BookWindow.show()
    sys.exit(app.exec_())

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QLabel, QLineEdit, QWidget, QApplication, QPushButton, QDateTimeEdit
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from function import zoom_access, convert_second
from datetime import datetime as dt

import sys
import sip
import subprocess
import datetime
import time


#from .apps import MainWindow

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.resize(500, 400)
        self.move(400, 300)

        #layout=QVBoxLayout()
        
        #title
        self.setWindowTitle('Zoom_Auto_Attendance')
        

        #zoom idの設定
        self.zoomIdLabel  =QLabel(self)
        self.zoomIdLabel.setText('Zoom_id:')
        self.zoom_id = QLineEdit(self)
        self.zoom_id.move(100,20)
        self.zoom_id.resize(200, 20)
        self.zoomIdLabel.move(20,20)
        #self.zoom_id.setGeometry(100, 50, 200, 20)

        #zoom passwordの設定
        self.zoomPassLabel  =QLabel(self)
        self.zoomPassLabel.setText('Zoom_pass:')
        self.zoom_pass = QLineEdit(self)
        self.zoom_pass.move(100,50)
        self.zoom_pass.resize(200, 20)
        self.zoomPassLabel.move(20,50)

        #時刻の設定
        self.datetimelabel = QLabel(self)
        self.datetimelabel.setText('Zoom start time')
        self.datetime_setting = QDateTimeEdit(QDateTime.currentDateTime(), self)
        self.datetimelabel.setWordWrap(True)
        self.datetime_setting.move(100,70)
        self.datetimelabel.move(20, 70)

        #buttonの設定
        pybutton = QPushButton('Send', self)
        pybutton.clicked.connect(self.ZoomclickMethod)
        pybutton.resize(pybutton.sizeHint())
        pybutton.move(70,100)

    #Zoomにアクセスするする関数
    def ZoomclickMethod(self):
        #datetimeで扱いやすいように変換
        tmp = self.datetime_setting.dateTime().toString('yyyy-MM-dd hh:mm:ss')
        zoom_start_datetime = dt.strptime(tmp, '%Y-%m-%d %H:%M:%S')
        wait_time  =int(convert_second(zoom_start_datetime))
        print(wait_time)

        if wait_time > 0:
            loop = QEventLoop()
            QTimer.singleShot(wait_time*1000, loop.quit)
            loop.exec_()
            #zoom_access(self.zoom_id.text(), self.zoom_pass.text())
        else:
            print('error')

        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
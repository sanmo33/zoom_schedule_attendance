from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QLabel, QLineEdit, QWidget, QApplication, QPushButton, QDateTimeEdit
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtGui

from function import zoom_access, convert_second, convert_second_to_hms
from datetime import datetime as dt

import sys
#import sip
import subprocess
import datetime
import time

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.resize(430, 190)
        self.move(400, 300)
        
        #title
        self.setWindowTitle('Zoom_Auto_Attendance')
        
        #zoom idの設定
        self.zoomIdLabel = QLabel(self)
        self.zoomIdLabel.setText('Zoom_id:')
        self.zoomIdLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.zoomIdLabel.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Black))
        self.zoomIdLabel.resize(100, 20)
        self.zoom_id = QLineEdit(self)
        self.zoom_id.resize(200, 20)
        self.zoom_id.move(150,20)
        self.zoomIdLabel.move(20,20)

        #zoom passwordの設定
        self.zoomPassLabel  =QLabel(self)
        self.zoomPassLabel.setText('Zoom_pass:')
        self.zoomPassLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.zoomPassLabel.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Black))
        self.zoomPassLabel.resize(100, 20)
        self.zoom_pass = QLineEdit(self)
        self.zoom_pass.resize(200, 20)
        self.zoom_pass.move(150,50)
        self.zoomPassLabel.move(20,50)

        #時刻の設定
        self.datetimelabel = QLabel(self)
        self.datetimelabel.setText('Start time:')
        self.datetimelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.datetimelabel.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Black))
        self.datetimelabel.resize(100, 20)
        self.datetime_setting = QDateTimeEdit(QDateTime.currentDateTime(), self)
        self.datetimelabel.setWordWrap(True)
        self.datetime_setting.move(150,80)
        self.datetimelabel.move(20,80)

        #buttonの設定
        self.pybutton = QPushButton('Send', self)
        self.pybutton.clicked.connect(self.ZoomclickMethod)
        self.pybutton.resize(self.pybutton.sizeHint())
        self.pybutton.move(150,110)

        self.lefttime = QLabel(self)
        self.lefttime.move(20, 140)
        self.lefttime.resize(200, 20)
        self.lefttime.setAlignment(QtCore.Qt.AlignLeft)
        self.lefttime.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Black))
        self.lefttime.setText('Wait:')


    #Zoomにアクセスするする関数
    def ZoomclickMethod(self):
        #datetimeで扱いやすいように変換
        tmp = self.datetime_setting.dateTime().toString('yyyy-MM-dd hh:mm:ss')
        zoom_start_datetime = dt.strptime(tmp, '%Y-%m-%d %H:%M:%S')
        wait_time  =int(convert_second(zoom_start_datetime))

        #どれくらい待つのか変換
        h,m,s = convert_second_to_hms(wait_time)
        str_hms = h+'H'+m+'M'+s+'S'

        
        if wait_time > 0:
            self.lefttime.setText('Wait:'+str_hms)
            loop = QEventLoop()
            QTimer.singleShot(wait_time*1000, loop.quit)
            loop.exec_()
            zoom_access(self.zoom_id.text(), self.zoom_pass.text())
        else:
            print('error')

        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
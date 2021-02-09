import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QLabel, QLineEdit, QWidget, QApplication, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui
import sip
import subprocess

#from .apps import MainWindow

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.resize(500, 400)
        self.move(400, 300)
        
        #title
        self.setWindowTitle('QChexkBox')
        self.setWindowIcon(QtGui.QIcon('./notepc.jpeg'))

        #zoom id
        self.zoomIdLabel  =QLabel(self)
        self.zoomIdLabel.setText('Zoom_id:')
        self.zoom_id = QLineEdit(self)
        self.zoom_id.move(100,20)
        self.zoom_id.resize(200, 20)
        self.zoomIdLabel.move(20,20)
        #self.zoom_id.setGeometry(100, 50, 200, 20)

        #zoom password
        self.zooPassLabel  =QLabel(self)
        self.zooPassLabel.setText('Zoom_pass:')
        self.zoom_pass = QLineEdit(self)
        self.zoom_pass.move(100,50)
        self.zoom_pass.resize(200, 20)
        self.zooPassLabel.move(20,50)

        #button setting
        pybutton = QPushButton('Send', self)
        pybutton.clicked.connect(self.ZoomclickMethod)
        pybutton.resize(pybutton.sizeHint())
        pybutton.move(70,70)

    #Zoomにアクセスするする関数
    def ZoomclickMethod(self):
        id = self.zoom_id.text().replace(' ', '')
        password = self.zoom_pass.text().replace(' ', '')
        url = 'zoommtg:"//zoom.us/join?confno=' + id + '&pwd=' + password + '"'
        cmd = "open %s" %url
        subprocess.check_output(cmd, shell=True)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
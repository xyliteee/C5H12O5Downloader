from PyQt5.QtCore import QObject
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import *
from PyQt5 import QtGui
from PyQt5.QtGui import *
from multiprocessing import *
from qfluentwidgets import *
from Window_Def import *
from qframelesswindow import FramelessMainWindow

class Basewindow(FramelessMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window")
        self.setGeometry(360,240,720,480)
        self.setMinimumSize(720,480)
        self.setMaximumSize(720,480)

        self.StackedWidget = QStackedWidget(self)
        self.Loadingwindow = LoadingWindow(self)
        self.Errorwindow = ErrorWindow(self)
        self.Mainwindow = MainWindow(self)
        self.Downloadingwindow = DownloadingWindow(self)

        self.StackedWidget.addWidget(self.Loadingwindow)
        self.StackedWidget.addWidget(self.Mainwindow)
        self.StackedWidget.addWidget(self.Errorwindow)
        self.StackedWidget.addWidget(self.Downloadingwindow)

        self.StackedWidget.setCurrentWidget(self.Mainwindow)
        self.setCentralWidget(self.StackedWidget) 

        self.Mainwindow.Minwindow.clicked.connect(self.showMinimized)

    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.m_flag=True
            self.m_Position=event.globalPos()-self.pos() 
            event.accept()
            self.s = str(self.m_Position)
            self.s = self.s.replace("PyQt5.QtCore.QPoint(", "")
            self.s = self.s.replace(")", "")
            self.s = self.s.replace(",", "")
            self.numbers = self.s.split()
            self.numbers = [int(num) for num in self.numbers]
            
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            if self.numbers[1] <= 40:
                self.move(QMouseEvent.globalPos()-self.m_Position)
                QMouseEvent.accept()
            
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag=False
        self.setCursor(QCursor(Qt.ArrowCursor))  
        



if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    window = Basewindow()
    window.show()
    app.exec_()
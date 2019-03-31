import sys
import cv2 as cv
import numpy as np
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import (QApplication, QDialog, QFileDialog, QGridLayout,
                             QLabel, QPushButton)


class win(QDialog):
    def __init__(self):

        # Initialize an array from image
        self.img = np.ndarray(())

        super().__init__()
        self.title = 'Ryota Katayose'
        self.initUI()

    def initUI(self):
        self.resize(600, 800)
        self.setWindowTitle(self.title)
        self.btnOpen = QPushButton('片片小天使', self)
        self.btnQuit = QPushButton('溜了溜了', self)
        self.btnProcess = QPushButton('我可以！', self)
        self.label = QLabel()

        # Setting layout
        layout = QGridLayout(self)
        layout.addWidget(self.label, 0, 1, 4, 5)
        layout.addWidget(self.btnOpen, 4, 2, 1, 1)
        layout.addWidget(self.btnProcess, 4, 3, 1, 1)
        layout.addWidget(self.btnQuit, 4, 4, 1, 1)

        #Connect signals to slots
        self.btnOpen.clicked.connect(self.openSlot)
        self.btnQuit.clicked.connect(self.close)

        
 
    def openSlot(self):
        # 调用打开文件diglog
        fileName, tmp = QFileDialog.getOpenFileName(
            self, 'Open Image', './__data', '*.png *.jpg *.bmp')

        if fileName is '':
            return

        # Use cv to get image
        self.img = cv.imread(fileName, -1)

        if self.img.size == 1:
            return
        
        r = 600.0 / self.img.shape[1]
        dim = (600, int(self.img.shape[0] * r))
        self.img = cv.resize(self.img, dim, interpolation=cv.INTER_AREA)
        
        self.refreshShow()

    def refreshShow(self):
        #Extract image
        height, width, channel = self.img.shape
        bytesPerLine = 3 * width
        self.qImg = QImage(self.img.data, width, height, bytesPerLine,
                           QImage.Format_RGB888).rgbSwapped()
        #Show images
        self.label.setPixmap(QPixmap.fromImage(self.qImg))

class childwindow(QDialog):
    
    def __init__(self):
        super().__init__()
        self.title = 'Detail Information'
        self.initUI()
    
    def initUI(self):
        self.resize(400, 500)
        self.setWindowTitle(self.title)
        self.btnQuit = QPushButton('溜了溜了', self)
        self.label = QLabel()
        
        #setting layout
        layout = QGridLayout(self)
        layout.addWidget(self.label, 0, 1, 4, 5)
        layout.addWidget(self.btnQuit, 4, 3, 1, 1)
        
        self.img = cv.imread('C:/Users/dell/Desktop/MCL/2019-2/Python/Assignment/Detail.jpg', -1)
        r = 500.0 / self.img.shape[1]
        dim = (500, int(self.img.shape[0] * r))
        self.img = cv.resize(self.img, dim, interpolation=cv.INTER_AREA)
        
        height, width, channel = self.img.shape
        bytesPerLine = 3 * width
        self.qImg = QImage(self.img.data, width, height, bytesPerLine,
                           QImage.Format_RGB888).rgbSwapped()
        
        #Show Images
        self.label.setPixmap(QPixmap.fromImage(self.qImg))
        
        #Connect signal to slots
        self.btnQuit.clicked.connect(self.close)
    
    def handle_click(self):
        if not self.isVisible():
            self.show()


if __name__ == '__main__':
    a = QApplication(sys.argv)
    w = win()
    child = childwindow()
    w.btnProcess.clicked.connect(child.handle_click)
    w.btnProcess.clicked.connect(w.hide)
    w.show()
    
    sys.exit(a.exec_())
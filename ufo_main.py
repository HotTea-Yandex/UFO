import random
import sys

from PIL import Image
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('НЛО')
        self.l = QLabel(self)
        self.l.setGeometry(150, 150, 96, 96)
        self.im = 'ufo.png'
        self.img = Image.open(self.im)
        pix = QPixmap(self.im)
        self.l.setPixmap(pix)
        self.x = 150
        self.y = 150
        self.show()

    def car_draw(self):
        self.x = self.x % 504
        self.y = self.y % 504
        self.l.setGeometry(self.x, self.y, 96, 96)

    def keyPressEvent(self, event):
        if event.key() == 16777236:
            self.x += 10
        if event.key() == 16777234:
            self.x -=10
        if event.key() == 16777235:
            self.y-=10
        if event.key() == 16777237:
            self.y +=10
        self.car_draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

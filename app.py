import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt, QPropertyAnimation, QPoint


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.position = [100]
        self.resize(900, 850)
        self.setWindowTitle("TgoesWrum")
        self.setWindowIcon(QIcon('./static/images/train.png'))

        self.label = QLabel(self)
        pixmap = QPixmap('./static/images/train.png')
        pixmap = pixmap.scaled(300, 300)
        self.label.setPixmap(pixmap)
        self.label.move(self.position[0], 200)
        
        self.right_button()
        self.left_button()
        

    def right_button(self):
        button = QPushButton("Right", self)
        button.move(200, 100)
        button.clicked.connect(self.go_right)

    def left_button(self):
        button = QPushButton("Left", self)
        button.move(100, 100)
        button.clicked.connect(self.go_left)

    def go_right(self):
        self.change_right(self.position)
        self.anim = QPropertyAnimation(self.label, b"pos")
        self.anim.setEndValue(QPoint(self.position[0], 200))
        self.anim.setDuration(150)
        self.anim.start()
        if self.position[0] > 400:
            self.change_limit_right(self.position)

    def go_left(self):
        self.change_left(self.position)
        self.anim = QPropertyAnimation(self.label, b"pos")
        self.anim.setEndValue(QPoint(self.position[0], 200))
        self.anim.setDuration(150)
        self.anim.start()
        if self.position[0] < 100:
            self.change_limit_left(self.position)

    def change_right(self, var):
        var[0] = var[0] + 10

    def change_left(self, var):
        var[0] = var[0] - 10

    def change_limit_right(self, var):
        var[0] = 400

    def change_limit_left(self, var):
        var[0] = 100
        

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
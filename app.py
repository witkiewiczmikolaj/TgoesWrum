import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt

class Window(QWidget):
    def __init__(self):
        super().__init__()
 
        self.resize(900, 850)
        self.setWindowTitle("TgoesWrum")
        self.setWindowIcon(QIcon('./static/images/train.png'))

        self.train()
        self.right_button()
        self.left_button()


    def right_button(self):
        button = QPushButton("Right", self)
        button.move(100, 100)
        button.clicked.connect(self.go_right)

    def left_button(self):
        button = QPushButton("Left", self)
        button.move(200, 100)
        button.clicked.connect(self.go_left)

    def train(self):
        label = QLabel(self)
        pixmap = QPixmap('./static/images/train.png')
        pixmap = pixmap.scaled(300, 300)
        label.setPixmap(pixmap)
        label.move(100, 200)

    def go_right(self):
        pass

    def go_left(self):
        pass
        

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
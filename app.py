import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtGui import QPixmap, QIcon, QPainter
from PyQt6.QtCore import Qt, QPropertyAnimation, QPoint, QTimer


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
        self.go_button()
        self.draw_floor()
        self.draw_sensor(100, 'X1')
        self.draw_sensor(320, 'X2')
        self.draw_sensor(540, 'X3')
        self.draw_sensor(760, 'X4')

    def draw_sensor(self, position, text):
        self.sensor = QWidget(self)
        self.sensor.setStyleSheet("background-color:red;border-radius:20px;")
        self.sensor.resize(40, 40)
        self.sensor.move(position, 505)
        self.name = QLabel(self)
        self.name.setText(text)
        self.name.move(position + 10, 510)

    def draw_floor(self):
        self.floor = QWidget(self)
        self.floor.setStyleSheet("background-color:black;")
        self.floor.resize(700, 5)
        self.floor.move(100, 500)

    def go_button(self):
        self.button = QPushButton("GO!", self)
        self.button.move(300, 100)
        self.button.clicked.connect(self.execute)

    def right_button(self):
        self.rbutton = QPushButton("Right", self)
        self.rbutton.setCheckable(True)
        self.rbutton.move(200, 100)

    def left_button(self):
        self.lbutton = QPushButton("Left", self)
        self.lbutton.setCheckable(True)
        self.lbutton.move(100, 100)

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

    def execute(self):
        if self.rbutton.isChecked() and not self.lbutton.isChecked():
            self.go_right()
        elif self.lbutton.isChecked() and not self.rbutton.isChecked():
            self.go_left()
        elif self.rbutton.isChecked() and self.lbutton.isChecked():
            pass
    
        
app = QApplication(sys.argv)
app.setStyleSheet("QLabel{font-size: 14pt;}")
window = Window()
window.show()
sys.exit(app.exec())
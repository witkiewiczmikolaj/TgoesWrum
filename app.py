import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget
from PyQt6.QtGui import QPixmap, QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
 
        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("TgoesWrum")
        self.setWindowIcon(QIcon('./static/images/train.png'))
 
        label = QLabel(self)
        pixmap = QPixmap('./static/images/train.png')
        pixmap = pixmap.scaled(300, 300)
        label.setPixmap(pixmap)
 
 
 
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
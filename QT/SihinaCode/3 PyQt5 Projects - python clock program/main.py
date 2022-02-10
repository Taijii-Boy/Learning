from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from clock import *

import sys


class MyWin(QMainWindow):
    """Главное окно приложения"""

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.label.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=15, xOffset=0, yOffset=0))
        self.ui.label_2.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5, xOffset=5, yOffset=5))

        timer = QTimer(self)
        timer.timeout.connect(self.set_time)
        timer.start(1000)

        gif1 = QMovie(':/img/icons/butterflies.gif')
        gif1.setScaledSize(QSize().scaled(120, 60, Qt.KeepAspectRatio))
        self.ui.label_4.setMovie(gif1)
        gif1.start()

    def set_time(self):
        time = QtCore.QTime.currentTime()
        text = time.toString('HH:mm')
        self.ui.label_2.setText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = MyWin()
    my_app.show()

    sys.exit(app.exec_())

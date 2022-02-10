from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from login import *

import sys


class MyWin(QMainWindow):
    """Главное окно приложения"""

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = MyWin()
    my_app.show()

    sys.exit(app.exec_())

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from interface import *

import sys

# ---------------------------------------------------------

# Form, Window = uic.loadUiType("ui/PassManager2.ui")
#
# app = QApplication([])
# window = Window()
# form = Form()
# form.setupUi(window)
# window.show()
# app.exec()

# ---------------------------------------------------------


class MyWin(QtWidgets.QMainWindow):
    """Главное окно приложения"""

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_app = MyWin()
    my_app.show()

    sys.exit(app.exec_())

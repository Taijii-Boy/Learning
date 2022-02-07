from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from interface import *
import sys


class MyWin(QtWidgets.QMainWindow):
    """Главное окно приложения"""

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # Remove window title bar

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Shadow effect
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QtGui.QColor(0, 92, 157, 550))

        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        self.setWindowIcon(QtGui.QIcon(":/icons/icons/github.svg"))
        self.setWindowTitle("ModernUI")

        QtWidgets.QSizeGrip(self.ui.size_qrip)

        # Buttons
        self.ui.minimize_window_button.clicked.connect(lambda: self.showMinimized())
        self.ui.close_window_button.clicked.connect(lambda: self.close())
        self.ui.exit_button.clicked.connect(lambda: self.close())
        self.ui.restore_window_button.clicked.connect(lambda: self.restore_or_maximize_window())

        def move_window(e):
            if self.isMaximized() == False:
                if e.buttons() == QtCore.Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        self.ui.header_frame.mouseMoveEvent = move_window
        self.ui.open_close_side_bar_btn.clicked.connect(lambda: self.slideLeftMenu())

    def restore_or_maximize_window(self):
        # if window is maximized
        if self.isMaximized():
            self.showNormal()
            # change Icon
            self.ui.restore_window_button.setIcon(QtGui.QIcon(u':/icons/icons/maximize-2.svg'))
        else:
            self.showMaximized()
            # change Icon
            self.ui.restore_window_button.setIcon(QtGui.QIcon(u':/icons/icons/minimize-2.svg'))

    def mousePressEvent(self, event):
        # Get the current position of the mouse
        self.clickPosition = event.globalPos()
        # We will use this value to move the window

    def slideLeftMenu(self):
        # Get current left menu width
        width = self.ui.slide_menu_container.width()

        # If minimized
        if width == 0:
            # Expand menu
            newWidth = 200
            self.ui.open_close_side_bar_btn.setIcon(QtGui.QIcon(u":/icons/icons/chevron-left.svg"))
        # If maximized
        else:
            # Restore menu
            newWidth = 0
            self.ui.open_close_side_bar_btn.setIcon(QtGui.QIcon(u":/icons/icons/align-left.svg"))

        # Animate the transition
        self.animation = QtCore.QPropertyAnimation(self.ui.slide_menu_container,
                                                   b"maximumWidth")  # Animate minimumWidth
        self.animation.setDuration(250)
        self.animation.setStartValue(width)  # Start value is the current menu width
        self.animation.setEndValue(newWidth)  # end value is the new menu width
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_app = MyWin()
    my_app.show()

    sys.exit(app.exec_())

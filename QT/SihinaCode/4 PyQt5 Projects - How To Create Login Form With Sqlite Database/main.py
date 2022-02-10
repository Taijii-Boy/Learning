from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtSql
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
        self.ui.label.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.ui.label_2.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.ui.pushButton.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.open_db()
        self.ui.pushButton.clicked.connect(self.check_user)

    def open_db(self):
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('data.sqlite')

        if not self.db.open():
            print('Error. Db is not exists')
        self.query = QtSql.QSqlQuery()

    def check_user(self):
        username1 = self.ui.lineEdit.text()
        password1 = self.ui.lineEdit_2.text()
        print(username1, password1)
        self.query.exec_(f'SELECT * FROM userdata WHERE username = {username1} AND password = {password1};')
        self.query.first()
        if self.query.value('username') != None and self.query.value('password') != None:
            print('Login successful!')
        else:
            print('Login failed')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = MyWin()
    my_app.show()

    sys.exit(app.exec_())

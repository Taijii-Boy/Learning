from PyQt5 import QtSql

db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
db.setDatabaseName('data.sqlite')

if not db.open():
    print('Error. Db is not exists')

query = QtSql.QSqlQuery()
query.exec_('CREATE TABLE userdata (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username VARCHAR(100) NOT NULL,\
            password VARCHAR(100) NOT NULL);')
query.exec_('INSERT INTO userdata (username, password) VALUES("DaoCODE", "12345");')
query.exec_('SELECT * FROM userdata WHERE id=1;')
query.first()
print(query.value('username'), query.value('password'))

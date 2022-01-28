import sqlite3 as sq

# Полный вариант, но не самый лучший:
# con = sq.connect('saper.db')
# cur = con.cursor()
#
# cur.execute('''
# ''')
# con.close()


# Более удобный и безопасный вариант:
with sq.connect('saper.db') as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS users") # Удалить таблицу с именем users
    cur.execute('''CREATE TABLE IF NOT EXISTS users (
        name TEXT NOT NULL,
        sex INTEGER NOT NULL DEFAULT 1,
        old INTEGER,
        score INTEGER
        )''')

    cur.execute("DROP TABLE IF EXISTS games")
    cur.execute('''CREATE TABLE IF NOT EXISTS games (
        user_id INTEGER NOT NULL,
        score INTEGER NOT NULL, 
        time INTEGER NOT NULL
        )''')

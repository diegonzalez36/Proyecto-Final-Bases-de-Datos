import sqlite3


class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS Productos (id INTEGER PRIMARY KEY, producto text, cliente text, tipo text, precio text)")
        self.con.commit() 
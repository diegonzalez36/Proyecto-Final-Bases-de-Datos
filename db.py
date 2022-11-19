import sqlite3


class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS Productos (id INTEGER PRIMARY KEY, producto text, cliente text, tipo text, precio text)")
        self.con.commit()

    def capturar(self):
        self.cur.execute("SELECT * FROM Productos")
        filas = self.cur.fetchall()
        return filas

    def insertar(self, producto, cliente, tipo, precio):
        self.cur.execute("INSERT INTO Productos VALUES (NULL, ?, ?, ?, ?)", (producto, cliente, tipo, precio))    
        self.con.commit()

    def remover(self, id):
        self.cur.execute("DELETE FROM Productos WHERE id=?", (id,))
        self.con.commit()
    
    def actualizar(self, id, producto, cliente, tipo, precio):
        self.cur.execute("UPDATE Productos SET producto = ?, cliente=?, tipo=?, precio=? WHERE id =?", (producto, cliente, tipo, precio, id))
        self.con.commit()

    def __del__(self):
        self.con.close()
        
""""
db = Database('tienda.db')
db.insertar("Sopa", "Diego", "Fuerte", "20000")
db.insertar("Arroz", "Andres", "Entrada", "9000")
db.insertar("Pollo", "Carlos", "Entrada", "7000")
"""
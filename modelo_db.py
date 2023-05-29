import sqlite3
from tkinter import messagebox

class ConexionDB:
    def __init__(self):
        self.con = sqlite3.connect("db_proyect.db")
        self.cursor = self.con.cursor()
        self.create_db()

    def create_db(self):
        sql = """CREATE TABLE IF NOT EXISTS tickets
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                ticket varchar(20) NOT NULL,
                estado varchar(64) NOT NULL,
                fecha real)
        """
        self.cursor.execute(sql)
        self.con.commit()

    def read_tickets(self):
        sql = "SELECT * FROM tickets ORDER BY id ASC"
        cursor = self.con.cursor()
        cursor.execute(sql)
        datos = cursor.fetchall()
        return datos
    
    def create_ticket(self, ticket, estado, fecha):
        try:
            data = (ticket, estado, fecha)
            sql = "INSERT INTO tickets(ticket, estado, fecha) VALUES(?, ?, ?)"
            self.cursor.execute(sql, data)
            self.con.commit()
        except IndexError:
            messagebox.showinfo("Base de datos", "Crear ticket...")

    def delete_ticket(self, id):
        try:
            data = (id,)
            sql = "DELETE FROM tickets WHERE id = ?;"
            self.cursor.execute(sql, data)
            self.con.commit()
        except IndexError:
            messagebox.showinfo("DELETE DB", "No se pudo borrar")

    def update_ticket(self, id, ticket, estado, fecha):
        try:
            data = (id, ticket, estado, fecha)
            sql = "UPDATE tickets SET ticket=?, estado=?, fecha=? WHERE id=?"
            self.cursor.execute(sql, data)
            self.con.commit()
        except IndexError:
            messagebox.showinfo("UPDATE ITEM", "No se pudo actualizar")


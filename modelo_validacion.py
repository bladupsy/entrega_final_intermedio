from tkinter import messagebox
from modelo_db import ConexionDB
import re

class Validations:
    def __init__(self): 
        self.conexion = ConexionDB()
        self.conexion.create_db()

    def create_ticket(self, ticket, estado, fecha, tree):
        patron_regex = "^[A-Za-záéíóú]*$"
        if re.match(patron_regex, ticket):
            print(ticket, estado, fecha)
            self.conexion.create_ticket(ticket, estado, fecha)
            self.actualizar_treeview(tree)
            messagebox.showinfo("Validacion", "Registro creado correctamente")
        else: 
            messagebox.showinfo("Validacion", "Error")

    def delete_ticket(self, id):
        try:
            self.conexion.delete_ticket(id)
            messagebox.showinfo("Validacion", "Ticket borrado correctamente")
        except:
            messagebox.showinfo("Validacion", "Error")
#TO-DO: modificar
    def update(self, id, ticket, estado, fecha, tree):
        patron_regex = "^[A-Za-záéíóú]*$"
        if re.match(patron_regex, ticket):
            print(id, ticket, estado, fecha)
            self.conexion.update_ticket(id, ticket, estado, fecha)  # Agregar el argumento 'id' en la llamada
            self.actualizar_treeview(tree)
            print("UPDATE, todo ok")
        else:
            print("error en update")
    
    def actualizar_treeview(self, tree):
        try:
            records = tree.get_children()
            for element in records:
                tree.delete(element)
                
            datos = self.conexion.read_tickets()
            for fila in datos:
                tree.insert("", 0, text=fila[0],
                            values=(fila[1], fila[2], fila[3]))
        except IndexError:
            messagebox.showinfo("Validacion", "Error")


from tkinter import StringVar, Entry, Tk, ttk, Button, Label
from tkcalendar import DateEntry
from modelo_validacion import Validations

class Vista:
    def __init__(self, root):
        self.root = root
        self.valid_modelo = Validations()
        self.root.title("Registro de tickets")

        titulo = Label(self.root, text="Registre los tickets", bg="blue", fg="thistle1", height=1, width=60)
        titulo.grid(row=0, column=0, columnspan=8, padx=1, pady=1, sticky="w")

        ticket = Label(self.root, text="Ticket")
        ticket.grid(row=1, column=0, sticky="w")
        estado = Label(self.root, text="Estado")
        estado.grid(row=2, column=0, sticky="w")
        fecha = Label(self.root, text="Fecha")
        fecha.grid(row=3, column=0, sticky="w")

        a_val, b_val, c_val = StringVar(), StringVar(), StringVar()
        w_ancho = 20

        entrada1 = Entry(self.root, textvariable=a_val, width=w_ancho)
        entrada1.grid(row=1, column=1)
        entrada2 = ttk.Combobox(root, values=["Aprobado", "En proceso", "Cerrado", "Terminado"], textvariable=b_val, width=w_ancho)
        entrada2.grid(row=2, column=1)
        entrada3 = DateEntry(self.root, selectmode='day', textvariable=c_val, width=w_ancho)
        entrada3.grid(row=3, column=1)

        self.tree = ttk.Treeview(self.root)
        self.tree["columns"] = ("col1", "col2", "col3")
        self.tree.column("#0", width=90, minwidth=50, anchor="w")
        self.tree.column("col1", width=200, minwidth=80)
        self.tree.column("col2", width=200, minwidth=80)
        self.tree.column("col3", width=200, minwidth=80)
        self.tree.heading("#0", text="ID")
        self.tree.heading("col1", text="ticket")
        self.tree.heading("col2", text="estado")
        self.tree.heading("col3", text="fecha")
        self.tree.grid(row=10, column=0, columnspan=4)

        boton_alta = Button(self.root, text="Crear registro", command=lambda: self.alta(a_val.get(), b_val.get(), c_val.get(), self.tree))
        boton_alta.grid(row=6, column=1)

        boton_modificar = Button(self.root, text="Modificar", command=lambda: self.modificar(a_val.get(), b_val.get(), c_val.get(), self.tree))
        boton_modificar.grid(row=7, column=1)

        boton_borrar = Button(self.root, text="Borrar", command=lambda: self.borrar(self.tree))
        boton_borrar.grid(row=8, column=1)


    def alta(self, ticket, estado, fecha, tree):
        self.valid_modelo.create_ticket(ticket, estado, fecha, tree)
    #TO-DO: modificar
    def modificar(self, ticket, estado, fecha, tree):
        item_select = tree.selection()
        item = tree.item(item_select)
        mi_id = item['text']
        self.valid_modelo.update(str(ticket), str(mi_id), estado, fecha, tree)

    def borrar(self, tree):
        item_select = tree.selection()
        item = tree.item(item_select)
        mi_id = item['text']
        self.valid_modelo.delete_ticket(mi_id)
        tree.delete(item_select)


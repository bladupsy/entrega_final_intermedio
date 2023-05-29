

from tkinter import Tk
from vista import Vista


if __name__ == "__main__":
    root = Tk()
    view = Vista(root)
    view.valid_modelo.actualizar_treeview(view.tree)
    root.mainloop()
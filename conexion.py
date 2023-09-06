import mysql.connector
import tkinter as tk
from tkinter import ttk


conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin1234",
    database = "almacen"
)



ventana = tk.Tk()
ventana.title("Tabla de Productos")


tree = ttk.Treeview(ventana)
tree["columns"] = ("ID", "Nombre", "Categoría", "Marca", "Stock")


tree.column("#0", width=0, stretch=tk.NO)
tree.column("ID", anchor=tk.W, width=50)
tree.column("Nombre", anchor=tk.W, width=150)
tree.column("Categoría", anchor=tk.W, width=100)
tree.column("Marca", anchor=tk.W, width=100)
tree.column("Stock", anchor=tk.W, width=100)

tree.heading("#0", text="", anchor=tk.W)
tree.heading("ID", text="ID", anchor=tk.W)
tree.heading("Nombre", text="Nombre", anchor=tk.W)
tree.heading("Categoría", text="Categoría", anchor=tk.W)
tree.heading("Marca", text="Marca", anchor=tk.W)
tree.heading("Stock", text="Stock", anchor=tk.W)

cursor = conexion.cursor()
cursor.execute("SELECT producto.id, producto.nombre, categoria.nombre, marca.nombre FROM producto INNER JOIN categoria ON producto.categoria_id = categoria.id INNER JOIN marca ON producto.marca_id = marca.id")

for row in cursor.fetchall():
    tree.insert("", "end", values=row)

cursor.close()


tree.pack()


ventana.mainloop()


conexion.close()

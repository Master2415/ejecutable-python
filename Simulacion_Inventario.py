import tkinter as tk
from tkinter import ttk

# Simulación de inventario con diferentes productos
inventario = {
    "Producto A": [10, 5, 3],  # Entradas iniciales para Producto A
    "Producto B": [7, 8],      # Entradas iniciales para Producto B
    "Producto C": [2, 4, 6]    # Entradas iniciales para Producto C
}

# Función para calcular el total del stock de un producto
def calcular_total_stock(producto):
    return sum(inventario[producto])

# Función para actualizar el stock con entrada de productos
def actualizar_stock_entrada():
    try:
        producto_seleccionado = combobox_producto.get()
        nueva_entrada = int(entry_stock.get())
        inventario[producto_seleccionado].append(nueva_entrada)
        actualizar_tabla()
        label_status.config(text=f"Entrada añadida para {producto_seleccionado}")
        entry_stock.delete(0, tk.END)  # Limpiar el entry después de agregar la nueva entrada
    except ValueError:
        label_status.config(text="Por favor, ingrese un número válido")
    except KeyError:
        label_status.config(text="Seleccione un producto válido")

# Función para actualizar el stock con salida de productos
def actualizar_stock_salida():
    try:
        producto_seleccionado = combobox_producto.get()
        salida = int(entry_stock.get())
        if salida > calcular_total_stock(producto_seleccionado):
            label_status.config(text="Stock insuficiente para la salida")
            return
        inventario[producto_seleccionado].append(-salida)
        actualizar_tabla()
        label_status.config(text=f"Salida registrada para {producto_seleccionado}")
        entry_stock.delete(0, tk.END)  # Limpiar el entry después de registrar la salida
    except ValueError:
        label_status.config(text="Por favor, ingrese un número válido")
    except KeyError:
        label_status.config(text="Seleccione un producto válido")

# Función para actualizar el contenido de la tabla
def actualizar_tabla():
    for item in tree.get_children():
        tree.delete(item)
    for producto, entradas in inventario.items():
        total = calcular_total_stock(producto)
        tree.insert("", tk.END, values=(producto, total))

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Inventario")

# Crear un frame para la tabla y añadir el Treeview
frame_tabla = tk.Frame(ventana)
frame_tabla.pack()

tree = ttk.Treeview(frame_tabla, columns=("producto", "stock"), show="headings")
tree.heading("producto", text="Producto")
tree.heading("stock", text="Stock Disponible")
tree.pack()

# Crear un combobox para seleccionar el producto
combobox_producto = ttk.Combobox(ventana, values=list(inventario.keys()))
combobox_producto.current(0)  # Seleccionar el primer producto por defecto
combobox_producto.pack()

# Crear un entry para ingresar una nueva entrada o salida
entry_stock = tk.Entry(ventana)
entry_stock.pack()

# Crear un botón para actualizar el stock con entrada
boton_entrada = tk.Button(ventana, text="Añadir entrada", command=actualizar_stock_entrada)
boton_entrada.pack()

# Crear un botón para actualizar el stock con salida
boton_salida = tk.Button(ventana, text="Registrar salida", command=actualizar_stock_salida)
boton_salida.pack()

# Crear un label para mostrar mensajes de estado
label_status = tk.Label(ventana, text="")
label_status.pack()

# Inicializar la tabla con los datos actuales
actualizar_tabla()

# Ejecutar la aplicación
ventana.mainloop()

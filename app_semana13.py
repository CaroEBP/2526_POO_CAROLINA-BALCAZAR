#Alumna:Carolina Elizabeth Balcazar Pardo 

import tkinter as tk
from tkinter import messagebox

# Crear ventana principal con título
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica")

# Etiqueta para indicar al usuario qué debe ingresar
label = tk.Label(ventana, text="Ingrese un dato:")
label.pack(pady=5)

# Campo de texto donde el usuario escribe el dato
entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=5)

# Lista para mostrar los datos ingresados
lista = tk.Listbox(ventana, width=40, height=10)
lista.pack(pady=5)

# Función para agregar datos desde el campo de texto a la lista
def agregar_dato():
    dato = entrada.get()
    if dato.strip() != "":
        lista.insert(tk.END, dato)
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "El campo está vacío")

# Función para limpiar todos los datos de la lista
def limpiar_lista():
    lista.delete(0, tk.END)

# Botón para agregar datos
btn_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
btn_agregar.pack(pady=5)

# Botón para limpiar la lista
btn_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
btn_limpiar.pack(pady=5)

# Mantener la ventana abierta y esperando eventos
ventana.mainloop()

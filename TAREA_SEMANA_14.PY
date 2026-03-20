#ALUMNO:CAROLINA BALCAZAR

import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Necesario para el DatePicker

# Crear ventana principal
root = tk.Tk()
root.title("Gestor de Eventos")
root.geometry("600x400")

# ---------------- FRAME PRINCIPAL ----------------
frame_lista = tk.Frame(root)
frame_lista.pack(fill="both", expand=True, padx=10, pady=10)

# Treeview para mostrar eventos
columnas = ("Fecha", "Hora", "Descripción")
tree = ttk.Treeview(frame_lista, columns=columnas, show="headings")
for col in columnas:
    tree.heading(col, text=col)
    tree.column(col, width=150)
tree.pack(fill="both", expand=True)

# ---------------- FRAME DE ENTRADA ----------------
frame_entrada = tk.Frame(root)
frame_entrada.pack(fill="x", padx=10, pady=10)

# Etiquetas y campos
tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
fecha_entry = DateEntry(frame_entrada, width=12, background="darkblue",
                        foreground="white", borderwidth=2)
fecha_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_entrada, text="Hora:").grid(row=0, column=2, padx=5, pady=5)
hora_entry = tk.Entry(frame_entrada)
hora_entry.grid(row=0, column=3, padx=5, pady=5)

tk.Label(frame_entrada, text="Descripción:").grid(row=1, column=0, padx=5, pady=5)
desc_entry = tk.Entry(frame_entrada, width=40)
desc_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

# ---------------- FRAME DE BOTONES ----------------
frame_botones = tk.Frame(root)
frame_botones.pack(fill="x", padx=10, pady=10)

def agregar_evento():
    fecha = fecha_entry.get()
    hora = hora_entry.get()
    desc = desc_entry.get()
    if fecha and hora and desc:
        tree.insert("", "end", values=(fecha, hora, desc))
        hora_entry.delete(0, tk.END)
        desc_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Campos vacíos", "Por favor completa todos los campos.")

def eliminar_evento():
    seleccionado = tree.selection()
    if seleccionado:
        confirmar = messagebox.askyesno("Confirmar", "¿Eliminar evento seleccionado?")
        if confirmar:
            tree.delete(seleccionado)
    else:
        messagebox.showwarning("Selección vacía", "No hay evento seleccionado.")

# Botones
tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento).pack(side="left", padx=5)
tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=eliminar_evento).pack(side="left", padx=5)
tk.Button(frame_botones, text="Salir", command=root.quit).pack(side="right", padx=5)

# ---------------- EJECUCIÓN ----------------
root.mainloop()
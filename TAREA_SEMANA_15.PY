# ALUMNO: BALCAZAR PARDO CAROLINA ELIZABETH
# ASIGNATURA: PROGRAMACION ORIENTADA A OBJETOS 

import tkinter as tk
from tkinter import messagebox

def add_task(event=None):
    task = entry.get()
    if task:
        listbox.insert(tk.END, f" {task}")
        entry.delete(0, tk.END)

def mark_completed():
    try:
        index = listbox.curselection()[0]
        task = listbox.get(index)
        listbox.delete(index)
        listbox.insert(tk.END, f" {task[2:]}")  # reemplaza el ícono
    except IndexError:
        messagebox.showwarning("Atención", "Selecciona una tarea primero.")

def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
        status_label.config(text="¡Tarea eliminada con éxito!")
    except IndexError:
        messagebox.showwarning("Atención", "Selecciona una tarea primero.")

root = tk.Tk()
root.title("Lista de Tareas")

entry = tk.Entry(root, width=40)
entry.pack(pady=5)
entry.bind("<Return>", add_task)

add_button = tk.Button(root, text="Añadir Tarea", command=add_task)
add_button.pack(pady=2)

complete_button = tk.Button(root, text="Marcar como Completada", command=mark_completed)
complete_button.pack(pady=2)

delete_button = tk.Button(root, text="Eliminar Tarea", command=delete_task)
delete_button.pack(pady=2)

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=5)

status_label = tk.Label(root, text="", fg="red")
status_label.pack()

root.mainloop()

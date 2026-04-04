#ALUMNO: BALCAZAR PARDO CAROLINA ELIZABETH
import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        # Campo de entrada
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.add_task)  # Atajo Enter

        # Botones
        tk.Button(root, text="Añadir", command=self.add_task).pack(pady=5)
        tk.Button(root, text="Completar", command=self.complete_task).pack(pady=5)
        tk.Button(root, text="Eliminar", command=self.delete_task).pack(pady=5)

        # Lista de tareas
        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.pack(pady=10)

        # Atajos de teclado
        root.bind("<c>", self.complete_task)   # tecla C
        root.bind("<d>", self.delete_task)     # tecla D
        root.bind("<Delete>", self.delete_task)
        root.bind("<Escape>", lambda e: root.quit())

    # Métodos
    def add_task(self, event=None):
        task = self.entry.get()
        if task:
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Escribe una tarea antes de añadir.")

    def complete_task(self, event=None):
        try:
            index = self.listbox.curselection()[0]
            task = self.listbox.get(index)
            # Feedback visual: añadir prefijo ✔
            self.listbox.delete(index)
            self.listbox.insert(index, f"✔ {task}")
        except IndexError:
            messagebox.showwarning("Aviso", "Selecciona una tarea para completar.")

    def delete_task(self, event=None):
        try:
            index = self.listbox.curselection()[0]
            self.listbox.delete(index)
        except IndexError:
            messagebox.showwarning("Aviso", "Selecciona una tarea para eliminar.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
    
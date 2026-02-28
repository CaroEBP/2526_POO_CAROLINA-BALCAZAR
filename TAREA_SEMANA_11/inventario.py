from producto import Producto
import json

class Inventario:
    def __init__(self):
        # Diccionario: clave = ID del producto, valor = objeto Producto
        self.productos = {}
        self.cargar_desde_archivo()

    def guardar_en_archivo(self):
        try:
            with open("inventario.json", "w") as f:
                # Serializamos el diccionario en JSON
                data = {id_p: {"nombre": p.get_nombre(),
                               "cantidad": p.get_cantidad(),
                               "precio": p.get_precio()}
                        for id_p, p in self.productos.items()}
                json.dump(data, f, indent=4)
        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")

    def cargar_desde_archivo(self):
        try:
            with open("inventario.json", "r") as f:
                data = json.load(f)
                for id_p, info in data.items():
                    producto = Producto(int(id_p), info["nombre"], info["cantidad"], info["precio"])
                    self.productos[int(id_p)] = producto
        except FileNotFoundError:
            print("Archivo inventario.json no encontrado. Se creará al guardar.")
        except PermissionError:
            print("Error: No tienes permisos para leer el archivo.")
        except json.JSONDecodeError:
            print("Error: Archivo corrupto, no se pudo cargar el inventario.")

    def agregar_producto(self, producto: Producto):
        if producto.get_id() in self.productos:
            print("Error: Ya existe un producto con ese ID.")
        else:
            self.productos[producto.get_id()] = producto
            self.guardar_en_archivo()
            print("Producto agregado y guardado en inventario.json.")

    def eliminar_producto(self, id_producto: int):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()
            print("Producto eliminado y cambios guardados en inventario.json.")
        else:
            print("No se encontró el producto con ese ID.")

    def actualizar_producto(self, id_producto: int, nueva_cantidad=None, nuevo_precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if nueva_cantidad is not None:
                producto.set_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                producto.set_precio(nuevo_precio)
            self.guardar_en_archivo()
            print("Producto actualizado y cambios guardados en inventario.json.")
        else:
            print("No se encontró el producto con ese ID.")

    def buscar_por_nombre(self, nombre: str):
        resultados = [p for p in self.productos.values() if nombre.lower() in p.get_nombre().lower()]
        return resultados

    def mostrar_todos(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            for p in self.productos.values():
                print(p)
                
from producto import Producto

class Inventario:
    def __init__(self):
        self.productos = []
        self.cargar_desde_archivo()

    def guardar_en_archivo(self):
        try:
            with open("inventario.txt", "w") as f:
                for p in self.productos:
                    f.write(f"{p.get_id()},{p.get_nombre()},{p.get_cantidad()},{p.get_precio()}\n")
        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")

    def cargar_desde_archivo(self):
        try:
            with open("inventario.txt", "r") as f:
                for linea in f:
                    try:
                        id_p, nombre, cantidad, precio = linea.strip().split(",")
                        producto = Producto(int(id_p), nombre, int(cantidad), float(precio))
                        self.productos.append(producto)
                    except ValueError:
                        print("Error: Datos corruptos en el archivo, línea ignorada.")
        except FileNotFoundError:
            print("Archivo inventario.txt no encontrado. Se creará al guardar.")
        except PermissionError:
            print("Error: No tienes permisos para leer el archivo.")

    def agregar_producto(self, producto: Producto):
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: Ya existe un producto con ese ID.")
        else:
            self.productos.append(producto)
            self.guardar_en_archivo()
            print("Producto agregado y guardado en inventario.txt.")

    def eliminar_producto(self, id_producto: int):
        self.productos = [p for p in self.productos if p.get_id() != id_producto]
        self.guardar_en_archivo()
        print("Producto eliminado y cambios guardados en inventario.txt.")

    def actualizar_producto(self, id_producto: int, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                self.guardar_en_archivo()
                print("Producto actualizado y cambios guardados en inventario.txt.")
                return
        print("No se encontró el producto con ese ID.")

    def buscar_por_nombre(self, nombre: str):
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        return resultados

    def mostrar_todos(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            for p in self.productos:
                print(p)
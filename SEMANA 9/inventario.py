from producto import Producto

class Inventario:
    """
    Clase que gestiona una lista de productos.
    Permite añadir, eliminar, actualizar y buscar productos.
    """

    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto: Producto):
        # Verificar que el ID sea único
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: Ya existe un producto con ese ID.")
        else:
            self.productos.append(producto)
            print("Producto agregado correctamente.")

    def eliminar_producto(self, id_producto: int):
        self.productos = [p for p in self.productos if p.get_id() != id_producto]
        print("Producto eliminado (si existía).")

    def actualizar_producto(self, id_producto: int, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                print("Producto actualizado.")
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
                
class Producto:
    """
    Clase que representa un producto dentro del inventario.
    Cada producto tiene un ID único, un nombre, una cantidad y un precio.
    """

    def __init__(self, id_producto: int, nombre: str, cantidad: int, precio: float):
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # Setters
    def set_nombre(self, nuevo_nombre: str):
        self._nombre = nuevo_nombre

    def set_cantidad(self, nueva_cantidad: int):
        self._cantidad = nueva_cantidad

    def set_precio(self, nuevo_precio: float):
        self._precio = nuevo_precio

    def __str__(self):
        return f"ID: {self._id} | Nombre: {self._nombre} | Cantidad: {self._cantidad} | Precio: ${self._precio:.2f}"
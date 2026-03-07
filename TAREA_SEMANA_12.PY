# -------------------------------
# Sistema de Gestión de Biblioteca Digital
# -------------------------------

class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Autor y título como tupla inmutable
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[0]} por {self.info[1]} (ISBN: {self.isbn}, Categoría: {self.categoria})"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # lista de libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"


class Biblioteca:
    def __init__(self):
        self.libros = {}        # diccionario ISBN -> Libro
        self.usuarios = set()   # conjunto de IDs únicos
        self.registro_usuarios = {}  # ID -> Usuario

    # -------------------------------
    # Gestión de usuarios
    # -------------------------------
    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios:
            self.usuarios.add(usuario.id_usuario)
            self.registro_usuarios[usuario.id_usuario] = usuario
            print(f"Usuario {usuario.nombre} registrado con éxito.")
        else:
            print("ID de usuario ya registrado.")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            self.usuarios.remove(id_usuario)
            del self.registro_usuarios[id_usuario]
            print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print("Usuario no encontrado.")

    # -------------------------------
    # Gestión de libros
    # -------------------------------
    def añadir_libro(self, libro):
        self.libros[libro.isbn] = libro
        print(f"Libro '{libro.info[0]}' añadido a la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print("Libro no encontrado.")

    # -------------------------------
    # Préstamos
    # -------------------------------
    def prestar_libro(self, id_usuario, isbn):
        usuario = self.registro_usuarios.get(id_usuario)
        libro = self.libros.get(isbn)
        if usuario and libro:
            usuario.libros_prestados.append(libro)
            del self.libros[isbn]
            print(f"Libro '{libro.info[0]}' prestado a {usuario.nombre}.")
        else:
            print("Usuario o libro no disponible.")

    def devolver_libro(self, id_usuario, isbn):
        usuario = self.registro_usuarios.get(id_usuario)
        if usuario:
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros[isbn] = libro
                    print(f"Libro '{libro.info[0]}' devuelto por {usuario.nombre}.")
                    break
        else:
            print("Usuario no encontrado.")

    # -------------------------------
    # Búsqueda y listados
    # -------------------------------
    def buscar_libro(self, criterio, valor):
        resultados = []
        for libro in self.libros.values():
            if criterio == "titulo" and libro.info[0] == valor:
                resultados.append(libro)
            elif criterio == "autor" and libro.info[1] == valor:
                resultados.append(libro)
            elif criterio == "categoria" and libro.categoria == valor:
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, id_usuario):
        usuario = self.registro_usuarios.get(id_usuario)
        if usuario:
            return usuario.libros_prestados
        return []


# -------------------------------
# Bloque de pruebas
# -------------------------------
if __name__ == "__main__":
    # Crear biblioteca
    biblioteca = Biblioteca()

    # Crear libros
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "12345")
    libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", "Infantil", "67890")
    libro3 = Libro("Python para todos", "Charles Severance", "Tecnología", "11111")

    # Añadir libros
    biblioteca.añadir_libro(libro1)
    biblioteca.añadir_libro(libro2)
    biblioteca.añadir_libro(libro3)

    # Crear usuarios
    usuario1 = Usuario("Carolina", "U001")
    usuario2 = Usuario("Juan", "U002")

    # Registrar usuarios
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Prestar libros
    biblioteca.prestar_libro("U001", "12345")
    biblioteca.prestar_libro("U002", "67890")

    # Listar libros prestados
    print("Libros prestados a Carolina:", [str(libro) for libro in biblioteca.listar_libros_prestados("U001")])
    print("Libros prestados a Juan:", [str(libro) for libro in biblioteca.listar_libros_prestados("U002")])

    # Devolver libro
    biblioteca.devolver_libro("U001", "12345")

    # Buscar libro por categoría
    resultados = biblioteca.buscar_libro("categoria", "Tecnología")
    print("Libros encontrados en categoría Tecnología:", [str(libro) for libro in resultados])

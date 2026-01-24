
"""
#Programa en Python para demostrar el uso de
constructores (__init__) y destructores (__del__).
Alumno: Carolina Elizabeth Balcázar Pardo
"""
class Estudiante:
    def __init__(self, nombre, carrera):
        """
        Constructor de la clase.
        Se ejecuta automáticamente al crear un objeto.
        Inicializa los atributos y abre un archivo para registrar datos.
        """
        self.nombre = nombre
        self.carrera = carrera
        self.archivo = open("registro.txt", "a", encoding="utf-8")
        self.archivo.write(f"Estudiante creado: {self.nombre}, Carrera: {self.carrera}\n")
        print(f"[INIT] Objeto Estudiante inicializado para {self.nombre}")

    def mostrar_info(self):
        """Método para mostrar la información del estudiante."""
        print(f"Nombre: {self.nombre}, Carrera: {self.carrera}")

    def __del__(self):
        """
        Destructor de la clase.
        Se ejecuta automáticamente cuando el objeto es eliminado.
        Aquí cerramos el archivo para liberar recursos.
        """
        if self.archivo:
            self.archivo.write(f"Estudiante eliminado: {self.nombre}\n")
            self.archivo.close()
        print(f"[DEL] Objeto Estudiante destruido para {self.nombre}")


# Ejemplo de uso
if __name__ == "__main__":
    estudiante1 = Estudiante("Ana Pérez", "Ingeniería en Sistemas")
    estudiante1.mostrar_info()

    estudiante2 = Estudiante("Luis Gómez", "Matemáticas Aplicadas")
    estudiante2.mostrar_info()

    # Al finalizar el programa, los destructores se ejecutan automáticamente
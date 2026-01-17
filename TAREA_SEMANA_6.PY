# Ejemplo de POO en Python
# ALUMNO: Carolina Balcázar
# Objetivo: Demostrar Clase, Objeto, Herencia, Encapsulación y Polimorfismo

# Clase base
class Animal:
    def __init__(self, nombre, edad):
        # Encapsulación: atributo privado
        self.__nombre = nombre
        self.edad = edad

    # Método getter para acceder al atributo privado
    def get_nombre(self):
        return self.__nombre

    # Método que será sobrescrito (polimorfismo)
    def hablar(self):
        return "El animal hace un sonido."

# Clase derivada (Herencia)
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    # Polimorfismo: sobrescribir método hablar
    def hablar(self):
        return "El perro ladra: ¡Guau Guau!"

# Otra clase derivada
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color

    # Polimorfismo: sobrescribir método hablar
    def hablar(self):
        return "El gato maúlla: ¡Miau!"

# Programa principal
if __name__ == "__main__":
    perro = Perro("Rex", 5, "shih tzu")
    gato = Gato("Manchita", 3, "Blanco y negro")

    # Demostración de encapsulación
    print(f"Nombre del perro: {perro.get_nombre()}")
    print(f"Nombre del gato: {gato.get_nombre()}")

    # Demostración de polimorfismo
    animales = [perro, gato]
    for animal in animales:
        print(animal.hablar())
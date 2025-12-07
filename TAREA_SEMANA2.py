# TAREA SEMANA 2
#ESTUDIANTE Carolina Elizabeth Balcazar Pardo
#asignatura_ Programaion Orientada a OBJETOS 

from abc import ABC, abstractmethod

# Abstracción: clase base con métodos obligatorios
class Persona(ABC):
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Encapsulación
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    @abstractmethod
    def presentarse(self):
        pass


# Herencia: Estudiante hereda de Persona
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    # Polimorfismo: comportamiento personalizado
    def presentarse(self):
        print(f"Hola, soy {self.get_nombre()}, tengo {self.get_edad()} años y estudio {self.carrera}.")


# Uso del programa
carolina = Estudiante("Carolina Balcázar", 34, "Tecnologías de la Información")
carolina.presentarse()
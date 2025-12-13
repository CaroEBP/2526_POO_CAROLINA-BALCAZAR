# Clase que representa el clima de un día específico
# Aplica encapsulamiento usando atributos privados
class DiaClima:
    def __init__(self, dia, temperatura):
        self.__dia = dia  # Atributo privado: día de la semana
        self.__temperatura = temperatura  # Atributo privado: temperatura registrada

    def mostrar_info(self):
        """Muestra la información del día y su temperatura"""
        print(f"{self.__dia}: {self.__temperatura}°C")

    def obtener_temperatura(self):
        """Devuelve la temperatura del día (acceso controlado)"""
        return self.__temperatura

# Clase que representa el clima de toda la semana
class SemanaClima:
    def __init__(self):
        self.dias = []  # Lista para almacenar objetos DiaClima

    def agregar_dia(self, dia, temperatura):
        """Agrega un objeto DiaClima a la semana"""
        self.dias.append(DiaClima(dia, temperatura))

    def calcular_promedio(self):
        """Calcula el promedio de temperaturas usando acceso controlado"""
        total = sum(dia.obtener_temperatura() for dia in self.dias)
        return total / len(self.dias)

    def mostrar_semana(self):
        """Muestra la información de todos los días"""
        for dia in self.dias:
            dia.mostrar_info()

# Función principal del programa
def main():
    print("POO con Encapsulamiento: Promedio Semanal de Temperaturas")
    semana = SemanaClima()
    for i in range(1, 8):
        temp = float(input(f"Ingrese la temperatura del día {i}: "))
        semana.agregar_dia(f"Día {i}", temp)
    print("\nTemperaturas registradas:")
    semana.mostrar_semana()
    promedio = semana.calcular_promedio()
    print(f"\nEl promedio semanal de temperaturas es: {promedio:.2f}°C")

# Ejecuta el programa
main()
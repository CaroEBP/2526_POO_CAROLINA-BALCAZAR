# Clase que representa el clima de un día específico
class DiaClima:
    def __init__(self, dia, temperatura):
        self.dia = dia  # Día de la semana (1 a 7)
        self.temperatura = temperatura  # Temperatura registrada

# Clase que representa el clima de toda la semana
class SemanaClima:
    def __init__(self):
        self.dias = []  # Lista para almacenar objetos DiaClima

    # Método para agregar un día con su temperatura
    def agregar_dia(self, dia, temperatura):
        self.dias.append(DiaClima(dia, temperatura))  # Crea y agrega un objeto DiaClima

    # Método para calcular el promedio semanal
    def calcular_promedio(self):
        total = sum(dia.temperatura for dia in self.dias)  # Suma las temperaturas de todos los días
        return total / len(self.dias)  # Divide por el número de días

# Función principal del programa
def main():
    print("POO: Promedio Semanal de Temperaturas")
    semana = SemanaClima()  # Crea una instancia de SemanaClima
    for i in range(1, 8):  # Itera del día 1 al 7
        temp = float(input(f"Ingrese la temperatura del día {i}: "))
        semana.agregar_dia(i, temp)  # Agrega el día y su temperatura
    promedio = semana.calcular_promedio()  # Calcula el promedio
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}°C")  # Muestra el resultado

# Ejecuta el programa
main()
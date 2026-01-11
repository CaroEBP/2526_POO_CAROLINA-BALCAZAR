# Programa: cálculo del área de un rectángulo
# Autor: Carolina Balcázar
# Descripción: Este programa solicita al usuario la base y la altura de un rectángulo,
# calcula su área y muestra el resultado en pantalla.
# Se utilizan diferentes tipos de datos y convenciones de nomenclatura.

# Función principal para calcular el área
def calcular_area_rectangulo(base: float, altura: float) -> float:
    """
    Calcula el área de un rectángulo.
    Parámetros:
        base (float): longitud de la base
        altura (float): longitud de la altura
    Retorna:
        float: área del rectángulo
    """
    return base * altura

# Entrada de datos
base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))

# Procesamiento
area = calcular_area_rectangulo(base, altura)

# Salida de datos
print(f"El área del rectángulo es: {area}")

# Ejemplo de uso de booleano
es_area_positiva = area > 0
print(f"¿El área calculada es positiva? {es_area_positiva}")

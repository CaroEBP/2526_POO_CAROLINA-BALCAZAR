# Clase Cliente
class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def __str__(self):
        return f"Cliente: {self.nombre}, Email: {self.email}"


# Clase Habitación
class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True

    def __str__(self):
        estado = "Disponible" if self.disponible else "Ocupada"
        return f"Habitación {self.numero} ({self.tipo}) - {estado}, Precio: ${self.precio}"


# Clase Reserva
class Reserva:
    def __init__(self, cliente, habitacion, fecha):
        self.cliente = cliente
        self.habitacion = habitacion
        self.fecha = fecha
        habitacion.disponible = False  # Al reservar, la habitación deja de estar disponible

    def __str__(self):
        return f"Reserva: {self.cliente.nombre} - Habitación {self.habitacion.numero} en {self.fecha}"


# Clase Hotel
class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []
        self.reservas = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones(self):
        for h in self.habitaciones:
            print(h)

    def reservar(self, cliente, numero_habitacion, fecha):
        for h in self.habitaciones:
            if h.numero == numero_habitacion and h.disponible:
                reserva = Reserva(cliente, h, fecha)
                self.reservas.append(reserva)
                print(f" Reserva realizada: {reserva}")
                return
        print(" No se pudo realizar la reserva. Habitación no disponible.")


# Ejemplo de uso
hotel = Hotel("Hotel Paraíso")

# Agregar habitaciones
hotel.agregar_habitacion(Habitacion(101, "Simple", 50))
hotel.agregar_habitacion(Habitacion(102, "Doble", 80))
hotel.agregar_habitacion(Habitacion(201, "Suite", 150))

# Mostrar habitaciones
hotel.mostrar_habitaciones()

# Crear cliente
cliente1 = Cliente("Carolina Balcázar", "carolina@email.com")

# Realizar reserva
hotel.reservar(cliente1, 102, "21-12-2025")

# Mostrar habitaciones después de la reserva
hotel.mostrar_habitaciones()


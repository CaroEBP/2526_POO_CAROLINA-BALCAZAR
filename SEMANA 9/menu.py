from inventario import Inventario
from producto import Producto

def menu():
    inventario = Inventario()

    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_p = int(input("Ingrese ID: "))
            nombre = input("Ingrese nombre: ")
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio: "))
            nuevo = Producto(id_p, nombre, cantidad, precio)
            inventario.agregar_producto(nuevo)

        elif opcion == "2":
            id_p = int(input("Ingrese ID del producto a eliminar: "))
            inventario.eliminar_producto(id_p)

        elif opcion == "3":
            id_p = int(input("Ingrese ID del producto a actualizar: "))
            cantidad = input("Nueva cantidad (deje vacío si no cambia): ")
            precio = input("Nuevo precio (deje vacío si no cambia): ")

            inventario.actualizar_producto(
                id_p,
                nueva_cantidad=int(cantidad) if cantidad else None,
                nuevo_precio=float(precio) if precio else None
            )

        elif opcion == "4":
            nombre = input("Ingrese nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)
            if resultados:
                print("Resultados:")
                for r in resultados:
                    print(r)
            else:
                print("No se encontraron coincidencias.")

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()

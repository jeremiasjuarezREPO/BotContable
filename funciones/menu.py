from funciones.opciones_menu import cargar_factura, registrar_proveedor, salir


def iniciar_sistema():
    estado = "MENU_PRINCIPAL"

    while estado == "MENU_PRINCIPAL":
        print("\n--- FacturasBot ---")
        print("1. Cargar factura")
        print("2. Registrar proveedor")
        print("3. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                cargar_factura()

            elif opcion == 2:
                registrar_proveedor()

            elif opcion == 3:
                estado = "SALIENDO"

            else:
                print("Opción incorrecta. Debe ingresar un número entre 1 y 3.")

        except ValueError:
            print("Opción incorrecta. Debe ingresar un número entero entre 1 y 3.")

    print("Saliendo del sistema...")
    salir()

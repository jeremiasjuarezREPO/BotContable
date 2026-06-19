
import csv
import os
from datetime import datetime

RUTA_PROVEEDORES = "proveedores.csv"
RUTA_FACTURAS = os.path.join("facturas", "facturas.csv")


#!! ---------------------------------Cargar Factura

def cargar_factura():
    estado = "ESPERANDO_NOMBRE_PROVEEDOR"

    # ---------- Solicitar proveedor ----------
    proveedor = input("Ingrese el nombre del proveedor: ").strip().lower()

    if proveedor == "":
        print("Error: el nombre del proveedor no puede estar vacío.")
        return

    # ---------- VERIFICANDO_PROVEEDOR ----------
    estado = "VERIFICANDO_PROVEEDOR"

    id_proveedor = None

    try:
        with open(RUTA_PROVEEDORES, "r", newline="", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            next(lector, None)

            for fila in lector:
                if len(fila) >= 2 and fila[1].strip().lower() == proveedor:
                    id_proveedor = int(fila[0])
                    break

    except FileNotFoundError:
        print("Error: no existe el archivo de proveedores.")
        return

    if id_proveedor is None:
        print("El proveedor no existe, debe cargarlo primero.")
        return

    # ---------- ESPERANDO_NUMERO_FACTURA ----------
    estado = "ESPERANDO_NUMERO_FACTURA"

    while True:
        try:
            numero_factura = int(input("Ingrese el número de factura: "))

            if numero_factura <= 0:
                print("Error: el número debe ser mayor que cero.")
                continue

            break

        except ValueError:
            print("Error: debe ingresar un número entero.")

    # ---------- VERIFICANDO_FACTURA ----------
    estado = "VERIFICANDO_FACTURA"

    if os.path.exists(RUTA_FACTURAS):
        with open(RUTA_FACTURAS, "r", newline="", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            next(lector, None)

            for fila in lector:
                if fila and int(fila[0]) == numero_factura:
                    print("Error: ya existe una factura con ese número.")
                    return

    # ---------- ESPERANDO_IMPORTE ----------
    estado = "ESPERANDO_IMPORTE"

    while True:
        try:
            importe = float(input("Ingrese el importe de la factura: "))

            if importe <= 0:
                print("Error: el importe debe ser mayor que cero.")
                continue

            break

        except ValueError:
            print("Error: debe ingresar un importe válido.")

    # ---------- ESPERANDO_FECHA ----------
    estado = "ESPERANDO_FECHA"

    while True:
        fecha = input("Ingrese la fecha (DD/MM/AAAA): ").strip()

        try:
            datetime.strptime(fecha, "%d/%m/%Y")
            break

        except ValueError:
            print("Error: la fecha debe tener formato DD/MM/AAAA.")

    # ---------- GUARDANDO_FACTURA ----------
    estado = "GUARDANDO_FACTURA"

    archivo_existe = os.path.exists(RUTA_FACTURAS)

    with open(RUTA_FACTURAS, "a", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)

        if not archivo_existe:
            escritor.writerow(["NumeroFactura", "Fecha", "Importe", "IdProveedor"])

        escritor.writerow([numero_factura, fecha, f"{importe:.2f}", id_proveedor])

    # ---------- FINALIZADO ----------
    estado = "FINALIZADO"

    print("Factura registrada correctamente.")


#!! ---------------------------------Registrar proveedor

def registrar_proveedor():
    estado = "INICIALIZANDO"

    # Crear el archivo con cabecera si no existe
    estado = "VERIFICANDO_ARCHIVO_PROVEEDORES"

    if not os.path.exists(RUTA_PROVEEDORES):
        estado = "CREANDO_ARCHIVO_PROVEEDORES"

        with open(RUTA_PROVEEDORES, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["ID", "Nombre"])

    # Leer proveedores existentes
    estado = "LEYENDO_PROVEEDORES_EXISTENTES"

    ids_existentes = set()

    with open(RUTA_PROVEEDORES, "r", newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        next(lector, None)

        for fila in lector:
            if fila:
                ids_existentes.add(int(fila[0]))

    # Estado: esperando ID
    estado = "ESPERANDO_ID_PROVEEDOR"

    while True:
        try:
            id_proveedor = int(input("Ingrese el ID del proveedor: "))

            if id_proveedor <= 0:
                print("Error: el ID debe ser un número mayor que cero.")
                continue

            if id_proveedor in ids_existentes:
                print("Error: ese ID ya está registrado.")
                continue

            break

        except ValueError:
            print("Error: el ID debe ser un número entero.")

    # Estado: esperando nombre
    estado = "ESPERANDO_NOMBRE_PROVEEDOR"

    while True:
        nombre = input("Ingrese el nombre del proveedor: ").strip().lower()

        if nombre == "":
            print("Error: el nombre no puede estar vacío.")
            continue

        if nombre.isdigit():
            print("Error: el nombre no puede contener solo números.")
            continue

        if len(nombre) > 20:
            print("Error: el nombre no puede superar los 20 caracteres.")
            continue

        break

    # Guardar proveedor
    estado = "GUARDANDO_PROVEEDOR"

    with open(RUTA_PROVEEDORES, "a", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([id_proveedor, nombre])

    estado = "FINALIZADO"

    print("Proveedor registrado correctamente.")


#!! ----------------------------- Salir
def salir():
    estado = "SALIENDO"

    print("Se cerró el programa")

    estado = "FINALIZADO"

import csv
import os
from datetime import datetime

import csv
import os
from datetime import datetime

# Ruta absoluta basada en la ubicacion de este archivo
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RUTA_PROVEEDORES = os.path.join(BASE_DIR, "proveedores.csv")
RUTA_FACTURAS = os.path.join(BASE_DIR, "facturas", "facturas.csv")


#?? Funcion que busca duplicado en los id del csv de proveedores

def existe_proveedor_en_base_datos(id_proveedor):

    existe_proveedor = False

    try:
        with open(RUTA_PROVEEDORES, "r", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                if int(fila["ID"]) == id_proveedor:
                    existe_proveedor = True
                    break

    except FileNotFoundError:
        existe_proveedor = False  # Si no existe el archivo, no hay duplicados

    return existe_proveedor



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
    print("A continuación deberá ingresar el ID y nombre del proveedor que desea añadir.\n")

    # ---------- Validar ID ----------
    while True:
        try:
            id_nuevo_proveedor = int(input("Ingrese el ID del proveedor: "))

            if id_nuevo_proveedor <= 0:
                print("Error: el ID debe ser un número mayor que cero.")
                continue

            if existe_proveedor_en_base_datos(id_nuevo_proveedor):
                print("Error: ese ID ya está registrado.")
                continue

            break

        except ValueError:
            print("Error: el ID debe ser un número entero.")

    # ---------- Validar Nombre ----------
    while True:
        nombre_nuevo_proveedor = input("Ingrese el nombre del proveedor: ").strip().lower()

        if nombre_nuevo_proveedor == "":
            print("Error: el nombre no puede estar vacío.")
            continue

        if nombre_nuevo_proveedor.isdigit():
            print("Error: el nombre no puede contener solo números.")
            continue

        if len(nombre_nuevo_proveedor) > 20:
            print("Error: el nombre no puede superar los 20 caracteres.")
            continue

        break

    # Verificar si el archivo existe para saber si hay que escribir el encabezado
    archivo_existe = os.path.exists(RUTA_PROVEEDORES) and os.path.getsize(RUTA_PROVEEDORES) > 0

    # Bloque try/except. Almacena la logica para la escritura del archivo y manejo de posibles errores
    try:
        with open(RUTA_PROVEEDORES, "a", newline="", encoding="utf-8") as archivo:

            escritor = csv.DictWriter(archivo, fieldnames=["ID", "Nombre"])

            # Si el archivo no existia, escribe el encabezado primero
            if not archivo_existe:
                escritor.writeheader()

            # Definicion de diccionario con los datos del proveedor a guardar
            nuevo_proveedor = {
                "ID": id_nuevo_proveedor,
                "Nombre": nombre_nuevo_proveedor
            }

            # Añade una fila al final del archivo con los datos del nuevo proveedor
            escritor.writerow(nuevo_proveedor)

    except FileNotFoundError:
        print("Error: no se encontró el archivo en la ruta especificada.")
        return

    except PermissionError:
        print("Error: no posee permisos para la escritura del archivo. Verifique que no esté siendo utilizado por otra aplicación.")
        return

    except UnicodeDecodeError:
        print("Error: el formato de codificación de caracteres no es compatible.")
        return

    except Exception as error:
        print(f"Ocurrió un error inesperado: {type(error).__name__} = {error}")
        return

    # Mensaje de exito
    print("")
    print(f"Se añadió con éxito el proveedor '{nombre_nuevo_proveedor}' con la siguiente información:\n")
    print(f"ID: {id_nuevo_proveedor}")
    print(f"Nombre: {nombre_nuevo_proveedor}\n")


#!! ----------------------------- Salir
def salir():
    estado = "SALIENDO"

    print("Se cerró el programa")

    estado = "FINALIZADO"
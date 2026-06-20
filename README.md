# FacturasBot

Aplicación de consola desarrollada en Python para la gestión de facturas y proveedores. Permite registrar proveedores y cargar facturas, almacenando los datos de forma persistente en archivos CSV.

---

## Requisitos

- Python 3.x instalado

---

## Estructura del proyecto

```text
Bot Contable/
├── docs/
│   ├── TPI Organizacion Empresarial 2026 Juarez Jeremias - Elias Ceballos Rey.pdf
│   ├── BPMN AS IS Diagrama de proceso.bpm
│   └── BPMN TO BE Diagrama de proceso.bpm
├── facturas/
│   └── facturas.csv
├── funciones/
├── menu.py
├── opciones_menu.py
├── main.py
├── proveedores.csv
└── README.md


---

## Instalación y ejecución

1. Clonar o descargar el repositorio
2. Desde la raíz del proyecto ejecutar:

```bash
python main.py
```

---

## Funcionalidades

- **Registrar proveedor**: permite dar de alta un nuevo proveedor ingresando un ID único y un nombre.
- **Cargar factura**: permite registrar una factura asociada a un proveedor existente, ingresando número de factura, importe y fecha.

---

## Almacenamiento de datos

Los datos se guardan en archivos CSV:

- `proveedores.csv`: almacena los proveedores registrados con sus campos ID y Nombre.
- `facturas/facturas.csv`: almacena las facturas cargadas con sus campos NumeroFactura, Fecha, Importe e IdProveedor.

Ambos archivos se crean automáticamente la primera vez que se registra un dato.

---

## Autores

Jeremias Juarez - Comision 6
Elias Ceballos Rey - Comison 14

Desarrollado como Trabajo Práctico Integrador para la materia Organización Empresarial — UTN San Nicolás.
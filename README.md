# Restaurante App - Semana 15

Este proyecto mantiene la evolución de la aplicación de restaurante desarrollada en semanas anteriores y añade la nueva operación de ventas siguiendo los fundamentos de manejo de eventos con Tkinter.

## Objetivo de la semana

La funcionalidad principal consiste en registrar una venta como una acción iniciada por el usuario desde la interfaz. El flujo es:

- Usuario selecciona un cliente y un producto
- Presiona el botón Registrar venta
- El botón ejecuta un callback mediante `command=`
- El callback solicita la operación al servicio
- `RestauranteServicio` valida la información y persiste la venta
- La interfaz actualiza la tabla de ventas mostrando el resultado

## Estructura del proyecto

```text
restaurante_app/
├── __init__.py
├── main.py
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── assets/
│   ├── logo.ppm
│   └── icono.ppm
└── README.md
```

## Funcionalidades

- Inicio de sesión con usuarios registrados
- Consulta de usuarios
- Gestión básica de productos
- Registro de ventas con selección interactiva
- Persistencia en archivos JSON
- Actualización de la información mostrada en la interfaz
- Uso explícito de callbacks con `command=` en el botón de venta

## Ejecutar la aplicación

Desde la raíz del proyecto:

```bash
python restaurante_app/main.py
```

Si se trabaja en un entorno sin interfaz gráfica disponible, puede ejecutarse con un servidor virtual de X:

```bash
xvfb-run -a python restaurante_app/main.py
```

## Notas

La lógica de validaciones y persistencia se mantiene en `RestauranteServicio`, evitando que la interfaz manipule directamente los archivos JSON.

La venta refleja el dominio del restaurante: usuario + producto + fecha, con respuesta visual inmediata en la tabla de ventas.

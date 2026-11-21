# Software FJ - Sistema Integral de Gestion

Proyecto academico en Python para administrar clientes, servicios y reservas sin utilizar bases de datos.

La informacion operativa se mantiene en objetos y listas durante la ejecucion; los archivos se utilizan para registrar eventos y errores.

## Requisitos

- Python 3.10 o superior.
- No requiere instalar paquetes externos.

## Estructura

- `clases/entidad.py`: clase abstracta general.
- `clases/cliente.py`: clientes, encapsulacion y validaciones.
- `clases/servicio.py`: clase abstracta Servicio y calculo general.
- `clases/reserva_sala.py`: servicio de salas.
- `clases/alquiler_equipos.py`: servicio de alquiler de equipos.
- `clases/asesoria.py`: servicio de asesoria.
- `clases/reserva.py`: confirmacion, cancelacion y procesamiento.
- `clases/excepciones.py`: excepciones personalizadas.
- `clases/logs.py`: configuracion del registro.
- `registros/`: archivo de eventos y errores generado al ejecutar.
- `evidencias/`: documentacion y resultados del proyecto.

## Ejecutar

Desde la carpeta principal:

```bash
python main.py

# Reto Técnico: Procesamiento de Transacciones Bancarias (CLI)

## Introducción

Este proyecto consiste en una aplicación de línea de comandos (CLI) que permite procesar un archivo CSV con transacciones bancarias. El objetivo es generar un reporte que contenga:

- Balance Final: Total de créditos menos total de débitos.
- Transacción de Mayor Monto: ID y monto de la transacción más alta.
- Conteo de Transacciones: Total de transacciones por tipo ("Crédito" y "Débito").

La aplicación ha sido desarrollada en Python por su versatilidad, facilidad de escritura y su amplio ecosistema de bibliotecas, que lo hacen ideal para el procesamiento de datos bancarios.

Se utilizaron dos bibliotecas clave:

- pandas: permite trabajar de manera eficiente con archivos CSV y grandes volúmenes de datos estructurados. Su sintaxis intuitiva y rendimiento lo convierten en la opción ideal para sumarizar transacciones, realizar filtros por tipo y detectar valores máximos. Además, es escalable y ampliamente usado en entornos reales como banca, fintech y análisis financiero.

- tkinter: ofrece una forma simple y multiplataforma de abrir un explorador de archivos, lo que mejora significativamente la experiencia de usuario al evitar la necesidad de ingresar rutas manualmente en la terminal. Esto facilita el uso de la herramienta por parte de usuarios no técnicos o en entornos corporativos.


## Instrucciones de Ejecución

### 1. Requisitos Previos

Asegúrate de tener instalado Python 3, pip y las bibliotecas necesarias para ejecutar el programa.

En sistemas Windows (CMD), puedes instalar los paquetes necesarios con:

python -m pip install --upgrade pip
pip install pandas

tkinter ya viene preinstalado con la mayoría de versiones oficiales de Python en Windows. Si recibes un error, asegúrate de estar usando Python descargado desde python.org.

### 2. Ejecutar la aplicación

1. Abre una terminal o CMD.
2. Navega a la carpeta donde se encuentra el archivo procesador_transacciones.py.
3. Ejecuta el siguiente comando:   python procesador_transacciones.py

4. Se abrirá una ventana para que selecciones el archivo .csv desde tu computadora.
5. El reporte se mostrará directamente en la consola.


## Enfoque y Solución

Esta sección describe brevemente la lógica implementada y las decisiones de diseño tomadas para resolver el reto técnico de forma eficiente y escalable.

- Se usó una estructura modular que separa claramente la lógica de procesamiento (procesar_transacciones_pandas) de la interacción con el usuario (seleccionar_archivo), facilitando la mantenibilidad y posibles mejoras futuras.
- Se utilizó tkinter para facilitar la selección del archivo .csv mediante una interfaz gráfica simple, evitando que el usuario tenga que escribir rutas manualmente.
- El script valida que el archivo CSV contenga las columnas requeridas (id, tipo, monto) y convierte los montos a tipo numérico, eliminando automáticamente los datos inválidos.
- Se calculan tres indicadores principales:
  - El total de montos por tipo de transacción ("Crédito" y "Débito")
  - El balance final (Créditos - Débitos)
  - La transacción con el monto más alto

Estas decisiones permiten que la solución sea ligera, rápida, robusta y escalable en entornos con grandes volúmenes de datos como los que se manejan en el sector bancario.

## Estructura del Proyecto

retotecnico-cobol/
|- procesador_transacciones.py   # Script principal de la aplicación
|- README.md                     # Documentación del proyecto

El archivo .csv de entrada debe ser seleccionado por el usuario mediante el explorador de archivos que se abre automáticamente.

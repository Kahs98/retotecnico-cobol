# retotecnico-cobol
# Reto Técnico: Procesamiento de Transacciones Bancarias (CLI)

## Introducción

Este proyecto consiste en una aplicación de línea de comandos (CLI) que permite procesar un archivo CSV con transacciones bancarias. El objetivo es generar un reporte que contenga:

- Balance Final: Total de créditos menos total de débitos.
- Transacción de Mayor Monto: ID y monto de la transacción más alta.
- Conteo de Transacciones: Total de transacciones por tipo ("Crédito" y "Débito").

La aplicación ha sido desarrollada en **Python** por su versatilidad, facilidad de escritura, y gran ecosistema de bibliotecas que lo hacen ideal para el procesamiento de datos bancarios.

Se utilizaron dos bibliotecas clave:

- pandas: porque permite trabajar de manera eficiente con archivos CSV y grandes volúmenes de datos estructurados. Su sintaxis intuitiva y rendimiento lo convierten en la opción ideal para sumarizar transacciones, realizar filtros por tipo y detectar valores máximos sin necesidad de estructuras manuales. Además, es escalable y ampliamente usado en entornos reales como banca, fintech y análisis financiero.

- tkinter: porque ofrece una forma simple y multiplataforma de abrir un explorador de archivos, lo que mejora significativamente la experiencia de usuario al evitar tener que ingresar rutas manualmente en la terminal. Esto facilita el uso de la herramienta por parte de usuarios no técnicos o en entornos corporativos.

Esta combinación permite construir una aplicación ligera pero robusta, con buen rendimiento, facilidad de mantenimiento y adaptable a entornos reales con volúmenes de datos crecientes.
---

## Instrucciones de Ejecución

### Requisitos Previos

Asegúrate de tener instalado Python 3, pip y las bibliotecas necesarias para ejecutar el programa.

En sistemas Windows, puedes instalar los paquetes necesarios desde CMD con:

python -m pip install --upgrade pip
pip install pandas

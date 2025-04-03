import pandas as pd
import tkinter as tk
from tkinter import filedialog

def procesar_transacciones_pandas(nombre_archivo):
    try:
        df = pd.read_csv(nombre_archivo, encoding='latin1') 

        columnas_esperadas = {'id', 'tipo', 'monto'}
        if not columnas_esperadas.issubset(df.columns):
            raise ValueError("El archivo no contiene las columnas necesarias: id, tipo, monto.")

        df = df.dropna(subset=['id', 'tipo', 'monto'])
        df['monto'] = pd.to_numeric(df['monto'], errors='coerce')
        df = df.dropna(subset=['monto'])

        credito_total = df[df['tipo'] == 'Crédito']['monto'].sum()
        debito_total = df[df['tipo'] == 'Débito']['monto'].sum()
        balance_final = credito_total - debito_total

        transaccion_mayor = df.loc[df['monto'].idxmax()]
        conteo = df['tipo'].value_counts()

        print("\nReporte de Transacciones")
        print("---------------------------------------------")
        print(f"Balance Final: {balance_final:.2f}")
        print(f"Transacción de Mayor Monto: ID {transaccion_mayor['id']} - {transaccion_mayor['monto']:.2f}")
        print(f"Conteo de Transacciones: Crédito: {conteo.get('Crédito', 0)} Débito: {conteo.get('Débito', 0)}\n")

    except FileNotFoundError:
        print("Archivo no encontrado.")
    except Exception as e:
        print(f"Error procesando el archivo: {e}")

def seleccionar_archivo():
    root = tk.Tk()
    root.withdraw()
    archivo = filedialog.askopenfilename(
        title="Selecciona el archivo CSV",
        filetypes=[("Archivos CSV", "*.csv")])
    
    if archivo:
        procesar_transacciones_pandas(archivo)
    else:
        print("No se seleccionó ningún archivo.")

if __name__ == "__main__":
    seleccionar_archivo()

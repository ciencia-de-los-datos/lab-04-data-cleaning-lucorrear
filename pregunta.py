"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    # Leer el archivo CSV
    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    # Eliminar filas duplicadas completamente
    df = df.drop_duplicates()

    # Limpiar la columna 'sexo'
    df['sexo'] = df['sexo'].str.strip().str.lower()

    # Limpiar la columna 'tipo_de_emprendimiento'
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.strip().str.lower()

    # Limpiar la columna 'idea_negocio'
    df['idea_negocio'] = df['idea_negocio'].str.strip().str.lower()

    # Limpiar la columna 'barrio'
    df['barrio'] = df['barrio'].str.strip().str.lower()

    # Limpiar la columna 'estrato'
    df['estrato'] = df['estrato'].str.strip().str.lower()

    # Limpiar la columna 'comuna_ciudadano'
    df['comuna_ciudadano'] = df['comuna_ciudadano'].str.strip().str.lower()

    # Limpiar la columna 'fecha_de_beneficio'
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'])

    # Limpiar la columna 'monto_del_credito'
    df['monto_del_credito'] = df['monto_del_credito'].str.replace('$', '').str.replace('.', '').astype(float)

    # Limpiar la columna 'línea_credito'
    df['línea_credito'] = df['línea_credito'].str.strip().str.lower()

    return df


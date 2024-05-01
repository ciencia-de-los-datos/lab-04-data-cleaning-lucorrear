"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
import re

def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0) 
    df = df.copy()
    df = df.rename(columns={0: 'ID'}) 

    #Columna "sexo" y "tipo_de_emprendimiento"
    df["sexo"] = df["sexo"].str.lower()
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.lower()
    
    #Columna "idea_negocio" len=75
    df["idea_negocio"] = df["idea_negocio"].str.lower()
    df["idea_negocio"] = df["idea_negocio"].str.replace("-", " ")
    df["idea_negocio"] = df["idea_negocio"].str.replace("_", " ")

    #Columna "barrio" len=225 
    df["barrio"] = df["barrio"].str.lower()
    df["barrio"] = df["barrio"].str.replace("_", " ")
    df["barrio"] = df["barrio"].str.replace("-", " ")
    #df[df["barrio"].str.contains("julio", case=False, na=False)]["barrio"].value_counts()

    #Columna "fecha_de_beneficio" len=795 ?????????????????
    def cambiar_orden(lista):
        if len(lista[0]) == 4:
            lista[0], lista[2] = lista[2], lista[0]
        return lista

    df["fecha_de_beneficio"] = df["fecha_de_beneficio"].str.split("/")
    df["fecha_de_beneficio"] = df["fecha_de_beneficio"].apply(cambiar_orden)
    df["fecha_de_beneficio"] = df["fecha_de_beneficio"].apply(lambda x: "/".join(x))

    #Columna "monto_del_credito" len=277
    df["monto_del_credito"] = df["monto_del_credito"].str.strip("$")
    df["monto_del_credito"] = df["monto_del_credito"].str.replace(",", "")
    df["monto_del_credito"] = df["monto_del_credito"].str.replace(".00", "")
    df["monto_del_credito"] = df["monto_del_credito"].str.replace(" ", "")

    #Columna "línea_credito" len=9
    df["línea_credito"] = df["línea_credito"].str.lower()
    df["línea_credito"] = df["línea_credito"].str.replace("-", " ")
    df["línea_credito"] = df["línea_credito"].str.replace("_", " ")

    df.dropna(inplace=True) #Elimino los nulos
    df.drop_duplicates(inplace=True) #Elimino los duplicados
    return df 

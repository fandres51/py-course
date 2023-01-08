# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 18:11:51 2023

@author: fabio
"""

import pandas as pd
import numpy as np
import math

path_guardado = 'C://Users//fabio//Documents//Github//py-course//03-Pandas//data//artwork_data.pickle'

df = pd.read_pickle(path_guardado)

seccion_df = df.iloc[49980:50019,:].copy()

df_agrupar_artista = seccion_df.groupby('artist')

for columna, df_agrupado in df_agrupar_artista:
    print(columna)
    print(df_agrupado)
    
# Hacer cálculos en columnas del dataframe
    
a = seccion_df['units'].value_counts() # 28 mm & 1 nan

print(a.empty) # verificar si la columna está vacía

# funcion para llenar huecos de las series
def llenar_valores_vacios(series, tipo):
    lista_valores = series.value_counts()
    # si está vacía no hacemos nada
    if(lista_valores.empty == True):
        return series
    else:
        if(tipo == 'promedio'):
            suma = 0
            numero_valores = 0
            for valor_serie in series:
                if(isinstance(valor_serie, str)):
                    valor = int(valor_serie)
                    numero_valores = numero_valores + 1
                    suma = suma + valor
                else:
                    pass
            promedio = suma / numero_valores
            series_valores_llenos = series.fillna(promedio) # esta función es la que llena los valores vacíos de una serie con un valor que se le pase
            return series_valores_llenos
                    
        if(tipo == 'mas_repetido'):
            pass

def transformar_df(df):
    df_artist = df.groupby('artist')
    lista_df = []
    for artista, df in df_artist:
        copia_df = df.copy()
        
        serie_w = copia_df['width']
        serie_h = copia_df['height']
        serie_u = copia_df['units']
        serie_i = copia_df['title']
        
        copia_df.loc[:, 'width'] = llenar_valores_vacios(serie_w, 'promedio')
        copia_df.loc[:, 'height'] = llenar_valores_vacios(serie_w, 'promedio')
        copia_df.loc[:, 'units'] = llenar_valores_vacios(serie_w, 'promedio')
        copia_df.loc[:, 'title'] = llenar_valores_vacios(serie_w, 'promedio')
        
        lista_df.append(copia_df)
    df_completo = pd.concat(lista_df)
    return df_completo

df_lleno = transformar_df(seccion_df)















    
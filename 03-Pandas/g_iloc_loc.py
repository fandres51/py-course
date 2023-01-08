# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 14:40:07 2023

@author: fabio
"""

import pandas as pd
import numpy as np

path_guardado = 'C://Users//fabio//Documents//Github//py-course//03-Pandas//data//artwork_data.pickle'
df = pd.read_pickle(path_guardado)

# loc

filtrado_horizontal = df.loc[1035] # serie
print(filtrado_horizontal)
print(filtrado_horizontal['artist'])
print(filtrado_horizontal.index) # indices columnas
print(df.loc[1035, 'artist']) # otra forma más directa

filtrado_vertical = df['artist']
print(filtrado_vertical)
print(filtrado_vertical.index) # indices indices

#filtrado por indice
df_1035 = df[df.index == 1035]

segundo = df.loc[1035] # filtrar por índice (1)
segundo = df.loc[[1035, 1036]] # filtrar por arr índice

segundo = df.loc[3:5] # filtrado desde X índice hasta Y índice

segundo = df.loc[1035, 'artist'] # 1 índice
segundo = df.loc[1035, ['artist', 'medium']] # varios índices

segundo = df.loc[df.index < 10] # arreglo de verdaderos y falsos

# segundo = df.loc[0] o segundo = df[0] no sirven porque lo que se pasa es un índice existente en el df

# iloc
# indices basados en en 0

tercero = df.iloc[0] # índice
tercero = df.iloc[[0,1]] # varios índices
tercero = df.iloc[0:10] # rangos
tercero = df.iloc[df.index < 10] # booleanos (igual a loc)

tecero = df.iloc[0:10, 0:4] # filtrado de índice por rango de índices

###############################################################################

datos = {
    'nota 1': {
        'Pepito':7,
        'Juanita':8,
        'Maria':9
        },
    'disciplina': {
        'Pepito':4,
        'Juanita':9,
        'Maria':2
        },
    'nota 2': {
        'Pepito':4,
        'Juanita':9,
        'Maria':7
        }
    }

notas = pd.DataFrame(datos)

condicion_nota = notas['nota 1'] >= 7
condicion_nota_dos = notas['nota 2'] >= 7
condicion_disc = notas['disciplina'] >= 7

mayores_siete = notas.loc[ condicion_nota, ['nota 1']]

pasaron = notas.loc[condicion_nota][condicion_disc][condicion_nota_dos]

notas.loc['Maria', 'disciplina'] = 7 # afectar los registros

notas.loc[:, 'disciplina'] = 7 # todos los registros


















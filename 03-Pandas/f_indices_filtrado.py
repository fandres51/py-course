# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 14:17:17 2023

@author: fabio
"""

import pandas as pd

path_guardado = 'C://Users//fabio//Documents//Github//py-course//03-Pandas//data//artwork_data.pickle'

df = pd.read_pickle(path_guardado)

serie_artistas_dup = df['artist']

# contar datos

artistas = pd.unique(serie_artistas_dup) # devuelve un np array
print(artistas.size)

# filtrar datos

blake = df['artist'] == 'Blake, William' # serie
print(blake.value_counts())

df_blake = df[blake]
print(len(df_blake))
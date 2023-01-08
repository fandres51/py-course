# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 18:03:29 2023

@author: fabio
"""

import numpy as np
import pandas as pd

path = 'C://Users//fabio//Documents//Github//py-course//03-Pandas//data//artwork_data.csv'
# path = '..//03-Pandas//data//artwork_data.csv'

df1 = pd.read_csv(
    path,
    nrows=10)

columnas = ['id', 'artist', 'title', 'medium', 'year',  'acquisitionYear', 'height', 'width', 'units']

df2 = pd.read_csv(
    path,
    nrows = 10,
    usecols=columnas)

df3 = pd.read_csv(
    path,
    usecols=columnas,
    index_col='id')

path_guardado = 'C://Users//fabio//Documents//Github//py-course//03-Pandas//data//artwork_data.pickle'
df3.to_pickle(path_guardado)

df5 = pd.read_pickle(path_guardado)





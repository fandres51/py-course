# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 14:30:16 2023

@author: fabio
"""

import numpy as np
import pandas as pd

arr_pnd = np.random.randint(0,10,6).reshape(2,3)

df1 = pd.DataFrame(arr_pnd)

s1 = df1[0]
s2 = df1[1]
s3 = df1[2]

df1[3] = s1
df1[4] = s1 * s2

datos_fisicos_1 = pd.DataFrame(
    arr_pnd,
    columns = [
        "Estatura (cm)",
        "Peso (kg)",
        "Edad (anios)"
        ]
    )

datos_fisicos_2 = pd.DataFrame(
    arr_pnd,
    columns = [
        "Estatura (cm)",
        "Peso (kg)",
        "Edad (anios)"
        ],
    index = [
        'Fabio',
        'Andres'
        ]
    )

print(datos_fisicos_2['Peso (kg)'])
print(datos_fisicos_2['Peso (kg)']['Andres'])

# Renombrar
df1.index = ['X', 'Y']
df1.columns = ['Peso', 'Edad', 'Altura', 'IQ', 'IMC']





















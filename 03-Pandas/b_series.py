# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 21:55:57 2022

@author: fabio
"""


# lista_num = [1,2,3,4]
# tupla_num = (1,2,3,4)
# np_num = np.array([1,2,3,4])

# series_a = pd.Series(
#     lista_num)
# series_b = pd.Series(
#     tupla_num)
# series_c = pd.Series(
#     np_num)
# series_d = pd.Series(
#     [True,
#     False,
#     1,
#     1.1,
#     'Hola',
#     None,
#     (1),
#     [1],
#     {'1':'2'}])

# print (series_d[3])

# lista_ciudades = ["Ambato", "Cuenca", "Loja", "Quito"]
# serie_de_ciudad = pd.Series(lista_ciudades, index = ["A", "C", "L", "Q"])

# print(serie_de_ciudad[3])
# print(serie_de_ciudad['C'])

import numpy as np
import pandas as pd

valores_ciudades = {
    "Ibarra":234,
    "Riobamba": 364,
    "Quito": 3425,
    "Cuenca": 2034,
    "Loja": 150
    }

serie_valor_ciudad = pd.Series(valores_ciudades)

ciudades_menor_1k = serie_valor_ciudad < 1000

# print(type(serie_valor_ciudad))
# print(type(ciudades_menor_1k))
# print(ciudades_menor_1k)

s_filtrada = serie_valor_ciudad[ciudades_menor_1k]
serie_valor_ciudad = serie_valor_ciudad * 1.1
serie_valor_ciudad["Quito"] = serie_valor_ciudad["Quito"] - 100

# print('Lima' in serie_valor_ciudad)

serie_cuadrado = np.square(serie_valor_ciudad)

ciudades_1 = pd.Series({
    "Toronto": 3000,
    "Washintong": 2000,
    "Mexico": 1000
    })

ciudades_2 = pd.Series({
    "Madrid": 1000,
    "Paris": 2000
    })

ciudades_2["Mexico"] = 2000

print(ciudades_1 + ciudades_2)

ciudades_add = ciudades_1.add(ciudades_2)
#sub()
#mul()
#div()

ciudades_concat = pd.concat([ciudades_1, ciudades_2])
ciudades_concat = pd.concat([ciudades_1, ciudades_2], verify_integrity = False) # Vota un error en True

print(ciudades_1.max())
print(pd.Series.max(ciudades_1))
print(np.max(ciudades_1))

print(ciudades_1.min())
print(pd.Series.min(ciudades_1))
print(np.min(ciudades_1))

print(ciudades_1.mean())
print(ciudades_1.median())
print(np.average(ciudades_1))

print(ciudades_1.head(2))
print(ciudades_1.tail(2))

print(ciudades_1.sort_values(
    ascending=False).head(2))

print(ciudades_1.sort_values().tail(2))

# Ejercicio
# Si ciudad 0 - 1000 sumar 5%
# Si ciudad 1001 - 2000 sumar 10%
# Si ciudad 2001 - ... sumar 20%

def calcular(valor_serie):
    if(valor_serie <= 1000): 
        return valor_serie * 1.05
    if(valor_serie > 1000 and valor_serie <= 2000): 
        return valor_serie * 1.1
    if(valor_serie > 2000): 
        return valor_serie * 1.2
    
ciudad_calculada = ciudades_1.map(calcular)

# where: if else
# las que NO CUMPLEN aplican

resultado = ciudades_1.where(ciudades_1 < 1001, ciudades_1 * 1.1)

# series de numeros

serie_num = pd.Series(['1', '2.3', -5])

print(pd.to_numeric(serie_num))

# integer, signed, unsigned, float

print(pd.to_numeric(serie_num, downcast="integer"))

# ignore, coerce, raise(default)

serie_err = pd.Series(['no hay', '1', '2.3', -5])
print(pd.to_numeric(serie_err, errors='ignore')) 
print(pd.to_numeric(serie_err, errors='coerce'))      













# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 16:37:26 2023

@author: fabio
"""

import numpy as np
import pandas as pd
import os
import sqlite3
import xlsxwriter

path_guardado = 'C://Users//fabio//Documents//Github//py-course//03-Pandas//data//artwork_data.pickle'

df = pd.read_pickle(path_guardado)

sub_df = df.iloc[49980:50519,:].copy()

# Tipos de archivos (excel, sql, json)

# 1) Excel

path_excel = 'C://Users//fabio//Documents//Github//py-course//03-Pandas//data//artwork_data.xlsx'
sub_df.to_excel(path_excel)
sub_df.to_excel(path_excel, index=False) # sin el indice como columna

columnas = ['artist', 'title', 'year']
sub_df.to_excel(path_excel, columns=columnas) # columnas específicas

# Multiples hojas de trabajo

path_excel_mt = 'C://Users//fabio//Documents//Github//py-course//03-Pandas//data//artwork_data_mt.xlsx'

writer = pd.ExcelWriter(path_excel_mt, engine='xlsxwriter')
sub_df.to_excel(writer, sheet_name = 'Primera')
sub_df.to_excel(writer, sheet_name = 'Segunda')
sub_df.to_excel(writer, sheet_name = 'Tercera')
writer.save() 

# Estilos de celdas

path_excel_colores = 'C://Users//fabio//Documents//Github//py-course//03-Pandas//data//artwork_data_colores.xlsx'
writer = pd.ExcelWriter(path_excel_colores, engine='xlsxwriter')

num_artistas = sub_df['artist'].value_counts() #Genera una serie que cuenta cuantos registros hay de cada uno
# print(num_artistas)
num_artistas.to_excel(writer, sheet_name = 'Artistas')

hoja_artistas = writer.sheets['Artistas'] # selecciona la hoja del archivo

# A partir de aquí se aplican los estilos
rango_celdas = 'B2:B{}'.format(len(num_artistas.index) + 1) # selecciona donde aplicar los estilos (la funcion format de STRING, reemplaza algo en un {} de un string)
formato_artistas = { # Define los estilos a aplicar
    'type':'2_color_scale',
    'min_value':'10',
    'min_type':'percentile',
    'max_value':'99',
    'max_type':'percentile'}

hoja_artistas.conditional_format(rango_celdas, formato_artistas) # aplica los estilos

writer.save()

# charts

path_excel_grafico = 'C://Users//fabio//Documents//Github//py-course//03-Pandas//data//artwork_data_grafico.xlsx'
writer = pd.ExcelWriter(path_excel_grafico, engine='xlsxwriter')

num_artistas = sub_df['artist'].value_counts()
num_artistas.to_excel(writer, sheet_name = 'Artistas')

workbook = writer.book
worksheet = writer.sheets['Artistas']

chart = workbook.add_chart({'type': 'pie'})

chart.add_series({
    'categories': '=Artistas!A2:A{}'.format(len(num_artistas.index) + 1),
    'values':     '=Artistas!B2:B{}'.format(len(num_artistas.index) + 1)
})

# Insert the chart into the worksheet.
worksheet.insert_chart('D2', chart)

writer.save()

# 2) JSON

path_json = 'C://Users//fabio//Documents//Github//py-course//03-Pandas//data//artistas.json'
path_json_tabla = 'C://Users//fabio//Documents//Github//py-course//03-Pandas//data//artistas_tabla.json'
sub_df.to_json(path_json)
sub_df.to_json(path_json_tabla, orient = 'table')

# 3) SQL

path_sql = 'C://Users//fabio//Documents//Github//py-course//03-Pandas//data//artistas.bdd'

with sqlite3.connect(path_sql) as conection:
    sub_df.to_sql('py_artistas', conection)

## with mysql.connect(f'mysql://user:password@ip:puerto/{path_sql}') as conection:
##     sub_df.to_sql('nombre_tabla', conection)








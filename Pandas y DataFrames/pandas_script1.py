#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 14:22:23 2024

@author: mcerdeiro
"""

import pandas as pd
import numpy as np


#%% armo un dataframe a partir de un diccionario
d = {'nombre':['Antonio', 'Brenda', 'Camila', 'David', 'Esteban', 'Felicitas'], 'apellido': ['Restrepo', 'Saenz', 'Torres', 'Urondo', 'Valdes', 'Wainstein'], 'lu': ['78/23', '449/22', '111/24', '1/21', '201/06', '47/20'], 'nota1': [9, 7, 7, 4, 3, np.nan], 'nota2': [10, 6, 7, 8, 5, np.nan], 'aprueba': [True, True, True, False, False, np.nan]}

df = pd.DataFrame(data = d) # creamos un df a partir de un diccionario
df.set_index('lu', inplace = True) # seteamos una columna como index
#%%
df.head()   
df.tail()
df.info() 
df.dtypes
df.columns  
df.index
df.describe() 
df[['nombre', 'nota1']]
df['nombre']
df.iloc[2]
df.iloc[2:6]
df.loc['78/23']

df.loc['78/23', 'nombre']
df.sample()
df.sample(n = 3)

"""
Ejercicio - Consigna 1
1. mostrar sólo las columnas nombre y apellido 
"""
df[['nombre','apellido']]
"""
2. mostrar sólo la fila de libreta 449/22
"""
df.loc['449/22']
"""
3. mostrar las filas 2 a 4
"""
df.iloc[2:5]
"""
4. mostrar el nombre de lx estudiante de libreta 201/06
"""
df.loc['201/06','nombre']
"""
5. armar una tabla notas parcial con libretas y notas del primer
examen
"""
d2 = {'lu':d['lu'],'nota1':d['nota1']}
df2 = pd.DataFrame(data = d2) # creamos un df a partir de un diccionario
df2.set_index('lu', inplace = True)     


























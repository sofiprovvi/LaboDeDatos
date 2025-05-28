# -*- coding: utf-8 -*-
"""
Created on Wed May 28 17:49:39 2025

@author: sofia
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import duckdb as dd 

import seaborn
data_ping = seaborn.load_dataset('penguins') #leo el dataset 

#EJERCICIOS:

#%%    
""" 
2) Cargar el dataset con las siguientes líneas:
import seaborn
data_ping = seaborn.load_dataset(‘penguins’)
y responder las siguientes preguntas:
    
a. ¿Qué representa cada línea del dataframe? 
Un pingüino de una determinada especie que vive en alguna isla de la Antártida.

b. ¿Cuántas muestras hay en total? 344

c. ¿Cuáles son las especies de pingüinos consideradas? Adelie, Chinstrap y Gentoo.

d. ¿Cuáles son las islas estudiadas? Torgersen, Dream y Biscoe.

e. Para cada pingüino, ¿con qué datos contamos?

Especie
Isla
Largo del pico
Profundidad de pico
Longitud de la aleta
Masa corporal 
Sexo

"""
#%%
"""
3) Averiguar si las islas están pobladas mayormente por alguna especie en 
particular, o si éstas coexisten, y en ambos casos deberá notificar en qué 
proporciones.
Es importante mencionar que deberá reportar sus descubrimientos de manera
resumida a través de gráficos de barra y de torta.
"""
#GRÁFICO DE BARRAS

consultaSQL = """
                 SELECT species, COUNT(species) AS Cantidad
                 FROM data_ping,
                 WHERE island='Biscoe'
                 GROUP BY species
                 """
                 
biscoe = dd.sql(consultaSQL).df()  
consultaSQL = """
                 SELECT species, COUNT(species) AS Cantidad
                 FROM data_ping,
                 WHERE island='Dream'
                 GROUP BY species
                 """
                 
dream = dd.sql(consultaSQL).df()                 
consultaSQL = """
                 SELECT species, COUNT(species) AS Cantidad
                 FROM data_ping,
                 WHERE island='Torgersen'
                 GROUP BY species
                 """
                 
torgersen = dd.sql(consultaSQL).df()                

fig, ax  = plt.subplots()
ax.bar(biscoe['species'],biscoe['Cantidad'],label='Biscoe',color="purple")
ax.bar(dream['species'],dream['Cantidad'],label='Dream',color="aqua")
ax.bar(torgersen['species'],torgersen['Cantidad'],label='Togersen',color="yellow")
ax.set_title('Especies')
ax.set_xlabel('Especies',fontsize='medium')
ax.set_ylabel('Cantidad',fontsize='medium')
ax.set_xlim(0,3)
ax.set_yticks([]) #borro la escala de y
ax.bar_label(ax.containers[1],fontsize=10) #muestro solo los vaores de y importantes del 1er nivel
ax.bar_label(ax.containers[0],fontsize=10) #muestro solo los vaores de y importantes del 1er nivel
plt.legend()
plt.show()
#%%
















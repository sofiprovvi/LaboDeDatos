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

"""
3) Averiguar si las islas están pobladas mayormente por alguna especie en 
particular, o si éstas coexisten, y en ambos casos deberá notificar en qué 
proporciones.
Es importante mencionar que deberá reportar sus descubrimientos de manera
resumida a través de gráficos de barra y de torta.

Respuesta: Como se puede ver en el gráfico de abajo, en Biscoe se 
encuentra sólo la especie Gentoo, en Togersen hay sólo Adelie y en 
Dream hay Chinstrap y Adelie casi en la misma proporción.  
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
"""
4)Realizar un histograma de la variable grosor del pico. Repetir separando 
por especies (con el mismo rango de valores en los ejes, para poder 
comparar).
"""
#GRÁFICO DE BARRAS
consultaSQL = """
                 SELECT species, AVG(bill_depth_mm) AS Pico
                 FROM data_ping
                 GROUP BY species
                 """
d4 = dd.sql(consultaSQL).df()  
def graficar_corporal(df, title:str,y_lim:int):
   fig, ax  = plt.subplots()
   ax.bar(df['species'],df['Pico'],color=['gold','orange','purple'])
   ax.set_title(title)
   ax.set_xlabel('Especies',fontsize='medium')
   ax.set_ylabel('Pico',fontsize='medium')
   ax.set_ylim(0,y_lim)
   #ax.set_yticks([]) #borro la escala de y
   ax.bar_label(ax.containers[0],fontsize=10) #muestro solo los vaores de y importantes del 1er nivel
   plt.show()
   
graficar_corporal(d4, "Grosor de pico de las especies",25)   
#%%

"""
5) Realizar lo mismo con las demás variables corporales de los pingüinos. 
A partir de estos gráficos, responder:
a. ¿Se puede determinar la especie de un pingüino a partir de una sola
característica? 
No, en cada grafico hay al menos 2 especies con características corporales muy parecidas
b. ¿Hay alguna característica que permita discernir entre especies mejor 
que otras?
No, por la misma razón que en la pregunta anterior. 
"""
#GRÁFICO DE BARRAS
consultaSQL = """
                 SELECT species, AVG(bill_length_mm) AS Pico
                 FROM data_ping
                 GROUP BY species
                 """
d51 = dd.sql(consultaSQL).df()  
graficar_corporal(d51, "Largo del pico de las especies",60) 

consultaSQL = """
                 SELECT species, AVG(flipper_length_mm) AS Pico
                 FROM data_ping
                 GROUP BY species
                 """
d52 = dd.sql(consultaSQL).df() 
graficar_corporal(d52, "Longitud aleta de las especies",250) 

consultaSQL = """
                 SELECT species, AVG(body_mass_g) AS Pico
                 FROM data_ping,
                 GROUP BY species
                 """
d53 = dd.sql(consultaSQL).df() 
graficar_corporal(d53, "Masa corporal las especies",6000)
#%%
"""
6. Realizar ahora histogramas de las variables observadas, separadas por 
sexo (f/m). De manera análoga, considerar si hay alguna variable que 
permita deducir el sexo de un pingüino.
"""
def graficar_corporal_por_sexo(df, df2, title:str,y_lim:int):
   fig, ax  = plt.subplots()
   ax.bar(df2['species'],df2['Pico'],label='Male',color=['turquoise'])
   ax.bar(df['species'],df['Pico'],label='Female',color=['pink'])
   ax.set_title(title)
   ax.set_xlabel('Especies',fontsize='medium')
   ax.set_ylabel('Pico',fontsize='medium')
   ax.set_ylim(0,y_lim)
   ax.set_yticks([]) #borro la escala de y
   ax.bar_label(ax.containers[1],fontsize=10)
   ax.bar_label(ax.containers[0],fontsize=10)#muestro solo los vaores de y importantes del 1er nivel
   ax.legend()
   plt.show()
   
   
consultaSQL = """
                 SELECT species, AVG(body_mass_g) AS Pico
                 FROM data_ping
                 WHERE sex = 'Female'
                 GROUP BY species          
                 """
d61f = dd.sql(consultaSQL).df()
consultaSQL = """
                 SELECT species, AVG(body_mass_g) AS Pico
                 FROM data_ping
                 WHERE sex = 'Male'
                 GROUP BY species
                 """
d61m = dd.sql(consultaSQL).df() 
graficar_corporal_por_sexo(d61f,d61m,"Masa corporal por sexo",6000)


consultaSQL = """
                 SELECT species, AVG(flipper_length_mm) AS Pico
                 FROM data_ping
                 WHERE sex='Female'
                 GROUP BY species
                 """
d62f = dd.sql(consultaSQL).df() 
consultaSQL = """
                 SELECT species, AVG(flipper_length_mm) AS Pico
                 FROM data_ping
                 WHERE sex='Male'
                 GROUP BY species
                 """
d62m = dd.sql(consultaSQL).df() 
graficar_corporal_por_sexo(d62f,d62m,"Longitud aleta por sexo",250)


consultaSQL = """
                 SELECT species, AVG(bill_length_mm) AS Pico
                 FROM data_ping
                 WHERE sex='Female'
                 GROUP BY species
                 """
d63f = dd.sql(consultaSQL).df() 
consultaSQL = """
                 SELECT species, AVG(bill_length_mm) AS Pico
                 FROM data_ping
                 WHERE sex='Male'
                 GROUP BY species
                 """
d63m = dd.sql(consultaSQL).df() 
graficar_corporal_por_sexo(d63f,d63m,"Longitud del pico por sexo",60)


consultaSQL = """
                 SELECT species, AVG(bill_depth_mm) AS Pico
                 FROM data_ping
                 WHERE sex='Female'
                 GROUP BY species
                 """
d64f = dd.sql(consultaSQL).df() 
consultaSQL = """
                 SELECT species, AVG(bill_depth_mm) AS Pico
                 FROM data_ping
                 WHERE sex='Male'
                 GROUP BY species
                 """
d64m = dd.sql(consultaSQL).df() 
graficar_corporal_por_sexo(d64f,d64m,"Profundidad del pico por sexo",25)






 
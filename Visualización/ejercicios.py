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
                 SELECT species, AVG(bill_depth_mm) AS "Grosor del pico (mm)"
                 FROM data_ping
                 GROUP BY species
                 """
d4 = dd.sql(consultaSQL).df()  
def graficar_corporal(df, vartitle:chr, title:str,y_lim:int):
   fig, ax  = plt.subplots()
   ax.bar(df['species'],df[vartitle],color=['gold','orange','purple'])
   ax.set_title(title)
   ax.set_xlabel('Especies',fontsize='medium')
   ax.set_ylabel(vartitle,fontsize='medium')
   ax.set_ylim(0,y_lim)
   #ax.set_yticks([]) #borro la escala de y
   ax.bar_label(ax.containers[0],fontsize=10) #muestro solo los vaores de y importantes del 1er nivel
   plt.show()
   
graficar_corporal(d4, 'Grosor del pico (mm)',"Grosor de pico de las especies",25)   
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
                 SELECT species, AVG(bill_length_mm) AS "Longitud del pico (mm)"
                 FROM data_ping
                 GROUP BY species
                 """
d51 = dd.sql(consultaSQL).df()  
graficar_corporal(d51, 'Longitud del pico (mm)',"Largo del pico de las especies",60) 

consultaSQL = """
                 SELECT species, AVG(flipper_length_mm) AS "Longitud aleta (mm)"
                 FROM data_ping
                 GROUP BY species
                 """
d52 = dd.sql(consultaSQL).df() 
graficar_corporal(d52,'Longitud aleta (mm)', "Longitud aleta de las especies",250) 

consultaSQL = """
                 SELECT species, AVG(body_mass_g) AS "Masa corporal (g)"
                 FROM data_ping,
                 GROUP BY species
                 """
d53 = dd.sql(consultaSQL).df() 
graficar_corporal(d53,'Masa corporal (g)', "Masa corporal las especies",6000)
#%%
"""
6. Realizar ahora histogramas de las variables observadas, separadas por 
sexo (f/m). De manera análoga, considerar si hay alguna variable que 
permita deducir el sexo de un pingüino.

Sí. 
-si el pico tiene progundidad mayor o igual a 15000, seguro es Male. De lo contrario, Female
-si el pico tiene longitd mayor a 455638 entonces es Male seguro. De lo contrario, Female
-si la aleta tiene longitd mayor a 191735 entonces es Male seguro. De lo contrario, Female
-si la masa corporal es mayot a 4000, entonces es Male seguro. De lo contrario, Female
"""
def graficar_corporal_por_sexo(df, df2, vartitle:chr, title:str,y_lim:int):
   fig, ax  = plt.subplots()
   ax.bar(df2['species'],df2[vartitle],label='Male',color=['turquoise'])
   ax.bar(df['species'],df[vartitle],label='Female',color=['pink'])
   ax.set_title(title)
   ax.set_xlabel('Especies',fontsize='medium')
   ax.set_ylabel(vartitle,fontsize='medium')
   ax.set_ylim(0,y_lim)
   ax.set_yticks([]) #borro la escala de y
   ax.bar_label(ax.containers[1],fontsize=10)
   ax.bar_label(ax.containers[0],fontsize=10)#muestro solo los valores de y importantes del 1er nivel
   ax.legend()
   plt.show()
   
   
consultaSQL = """
                 SELECT species, AVG(body_mass_g) AS "Masa corporal (g)"
                 FROM data_ping
                 WHERE sex = 'Female'
                 GROUP BY species          
                 """
d61f = dd.sql(consultaSQL).df()
consultaSQL = """
                 SELECT species, AVG(body_mass_g) AS "Masa corporal (g)"
                 FROM data_ping
                 WHERE sex = 'Male'
                 GROUP BY species
                 """
d61m = dd.sql(consultaSQL).df() 
graficar_corporal_por_sexo(d61f,d61m,'Masa corporal (g)', "Masa corporal por sexo",6000)


consultaSQL = """
                 SELECT species, AVG(flipper_length_mm) AS "Longitud aleta (mm)"
                 FROM data_ping
                 WHERE sex='Female'
                 GROUP BY species
                 """
d62f = dd.sql(consultaSQL).df() 
consultaSQL = """
                 SELECT species, AVG(flipper_length_mm) AS "Longitud aleta (mm)"
                 FROM data_ping
                 WHERE sex='Male'
                 GROUP BY species
                 """
d62m = dd.sql(consultaSQL).df() 
graficar_corporal_por_sexo(d62f,d62m,'Longitud aleta (mm)',"Longitud aleta por sexo",250)


consultaSQL = """
                 SELECT species, AVG(bill_length_mm) AS "Longitud pico (mm)"
                 FROM data_ping
                 WHERE sex='Female'
                 GROUP BY species
                 """
d63f = dd.sql(consultaSQL).df() 
consultaSQL = """
                 SELECT species, AVG(bill_length_mm) AS "Longitud pico (mm)"
                 FROM data_ping
                 WHERE sex='Male'
                 GROUP BY species
                 """
d63m = dd.sql(consultaSQL).df() 
graficar_corporal_por_sexo(d63f,d63m,'Longitud pico (mm)',"Longitud del pico por sexo",60)


consultaSQL = """
                 SELECT species, AVG(bill_depth_mm) AS "Profundidad pico"
                 FROM data_ping
                 WHERE sex='Female'
                 GROUP BY species
                 """
d64f = dd.sql(consultaSQL).df() 
consultaSQL = """
                 SELECT species, AVG(bill_depth_mm) AS "Profundidad pico"
                 FROM data_ping
                 WHERE sex='Male'
                 GROUP BY species
                 """
d64m = dd.sql(consultaSQL).df() 
graficar_corporal_por_sexo(d64f,d64m,'Profundidad pico',"Profundidad del pico por sexo",25)
#%%
"""
7. Realizar scatterplots de pares de variables corporales, separadas por 
sexo. A partir de los gráficos, responder:
a. ¿Hay algún par de variables que permita deducir el sexo? No.
b. ¿Y si se fija una especie en particular? Tampoco
"""
def par_variable_por_sexo(df,var1:chr,var2:chr,cond:chr):
   df = df[[var1,var2,'sex','species']]
   df = df[df['sex']==cond]
   return df

df72m = par_variable_por_sexo(data_ping,'flipper_length_mm','body_mass_g','Male')
df72f = par_variable_por_sexo(data_ping,'flipper_length_mm','body_mass_g','Female')
df71m = par_variable_por_sexo(data_ping,'bill_length_mm','bill_depth_mm','Male')
df71f = par_variable_por_sexo(data_ping,'bill_length_mm','bill_depth_mm','Female')
df73m = par_variable_por_sexo(data_ping,'bill_length_mm','flipper_length_mm','Male')
df73f = par_variable_por_sexo(data_ping,'bill_length_mm','flipper_length_mm','Female')


def graficar_scatter7(df1,df2,x_title:chr,y_title:chr,title:str,xlim:int,ylim:int):
    plt.figure(figsize=(10, 6))
    plt.scatter(df1[x_title],df1[y_title], alpha=0.7, color="blue", label='Male', s =30)
    plt.scatter(df2[x_title], df2[y_title], color="magenta", alpha=0.7, label='Female', s = 30)
    plt.figtext(0.5, -0.05, title, wrap=True,horizontalalignment='center', fontsize=14)
    plt.xlabel(x_title)
    plt.ylabel(y_title)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.xlim([0,xlim])
    plt.ylim([0,ylim])
    plt.show()

graficar_scatter7(df71m, df71f,'bill_length_mm','bill_depth_mm',"Profundidad en función de la longitud del pico",65,25)
graficar_scatter7(df72m, df72f,'flipper_length_mm','body_mass_g',"Longitud de la aleta en función de la masa corporal",250,7500)
graficar_scatter7(df73m, df73f,'bill_length_mm','flipper_length_mm',"Longitud de la aleta en función de longitud del pico",65,250)

dfs = [df71m,df71f,df72m,df72f,df73m,df73f]

def por_especie(df, especie:chr):
    res=[]
    for d in df:
        d = d[d['species']==especie]
        res.append(d)
    return res 
    
dfss = por_especie(dfs,'Adelie')
graficar_scatter7(dfs[0], dfs[1],'bill_length_mm','bill_depth_mm',"Adelie: Profundidad en función de la longitud del pico",65,25)
graficar_scatter7(dfs[2], dfs[3],'flipper_length_mm','body_mass_g',"Adelie:Longitud de la aleta en función de la masa corporal",250,7000)
graficar_scatter7(dfs[4], dfs[5],'bill_length_mm','flipper_length_mm',"Adelie:Longitud de la aleta en función de longitud del pico",70,250)

dfss = por_especie(dfs,'Gentoo')
graficar_scatter7(dfs[0], dfs[1],'bill_length_mm','bill_depth_mm',"Gentoo: Profundidad en función de la longitud del pico",70,25)
graficar_scatter7(dfs[2], dfs[3],'flipper_length_mm','body_mass_g',"Gentoo: Longitud de la aleta en función de la masa corporal",300,7000)
graficar_scatter7(dfs[4], dfs[5],'bill_length_mm','flipper_length_mm',"Gentoo: Longitud de la aleta en función de longitud del pico",70,250)

dfss = por_especie(dfs,'Chinstrap')
graficar_scatter7(dfs[0], dfs[1],'bill_length_mm','bill_depth_mm',"Chinstrap: Profundidad en función de la longitud del pico",70,25)
graficar_scatter7(dfs[2], dfs[3],'flipper_length_mm','body_mass_g',"Chinstrap: Longitud de la aleta en función de la masa corporal",300,7000)
graficar_scatter7(dfs[4], dfs[5],'bill_length_mm','flipper_length_mm',"Chinstrap: Longitud de la aleta en función de longitud del pico",70,250)

#%%

















 
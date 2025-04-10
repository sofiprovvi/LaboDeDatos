# -*- coding: utf-8 -*-
"""
GUÍA DE EJERCICIOS 1:
    
 
1) 
Definir una función leer_parque(nombre_archivo, parque) que 
abra el archivo indicado y devuelva una lista de diccionarios 
con la información del parque especificado. La lista debe tener 
un diccionario por cada árbol del parque elegido. Dicho 
diccionario debe tener los datos correspondientes a un árbol
(recordar que cada fila del csv corresponde a un árbol).
Probar la función en el parque ‘GENERAL PAZ’ y debería dar
una lista con 690 árboles.    
"""
#%%
import csv 
def leer_parque(nombre_archivo: str, parque: str)->list[dict[str,str]]:
    arboles: list[dict[str,str]] =[]
    abrir_archivo = open(nombre_archivo, 'rt')
    leer_archivo = csv.reader(abrir_archivo)
    encabezado = next(leer_archivo)
    for fila in leer_archivo:
        if parque in fila:
            info = dict(zip(encabezado,fila))
            arboles.append(info)
    abrir_archivo.close()   
    return arboles  

generalpaz = leer_parque("arbolado-en-espacios-verdes.csv","GENERAL PAZ")
#%%       
"""
2)
Escribir una función especies(lista_arboles) que tome una lista 
de árboles como la generada en el ejercicio anterior y devuelva 
el conjunto de especies (la columna 'nombre_com' del archivo) 
que figuran en la lista.
"""           
def especies(lista_arboles: list[dict[str,str]])->list[str]:
    res:list[str]=[]
    for arbol in lista_arboles:
        if arbol['nombre_com'] not in res:
           res.append(arbol['nombre_com'])
    return res

print(especies(generalpaz))    
#%%             
"""
3)
Escribir una función contar_ejemplares(lista_arboles) que, 
dada una lista como la generada con leer_parque(...), devuelva 
un diccionario en el que las especies sean las claves y tengan 
como valores asociados la cantidad de ejemplares en esa especie 
en la lista dada. Debería verse que en el parque General Paz 
hay 20 Jacarandás, en el Parque Los Andes hay 3 Tilos y en 
Parque Centenario hay 1 Laurel.
"""
def contar_ejemplares(lista_arboles: list[dict[str,str]]) -> dict[str,int]:
    res:dict[str,int]={}
    claves_repetidas:list[str]=[]
    for arbol in lista_arboles:
        claves_repetidas.append(arbol['nombre_com'])
    claves_conjunto = especies(lista_arboles)       
    ejemplares:int=0
    i:int=0
    for clave in claves_conjunto:
        while i<len(claves_repetidas):
            if (claves_repetidas[i]==clave):
                ejemplares+=1
            i+=1
        res[clave]=ejemplares
        ejemplares=0
        i=0
    return res    

centenario = leer_parque("arbolado-en-espacios-verdes.csv","CENTENARIO")      
print(contar_ejemplares(centenario))                  
#%%    
"""
4)
Escribir una función obtener_alturas(lista_arboles, especie) 
que, dada una lista como la generada con leer_parque(...) y una
especie de árbol (un valor de la columna 'nombre_com' del 
archivo), devuelva una lista con las alturas (columna 
'altura_tot') de los ejemplares de esa especie en la lista.
"""
def obtener_alturas(lista_arboles:list[dict[str,str]],especie:str)->list[float]:
    res:list[float]=[]
    for arbol in lista_arboles:
        for clave in arbol.keys():
            if (arbol[clave]==especie):
                res.append(float(arbol['altura_tot']))
    return res       
#%%                                             
"""
5)
Escribir una función obtener_inclinaciones(lista_arboles, 
especie) que, dada una lista como la generada con 
leer_parque(...) y una especie de árbol, devuelva una lista con
las inclinaciones (columna 'inclinacio') de los ejemplares de 
esa especie.
"""
def obtener_inclinaciones(lista_arboles:list[dict[str,str]],especie:str)->list[float]:
    res:list[float]=[]
    for arbol in lista_arboles:
        for clave in arbol.keys():
            if (arbol[clave]==especie):
                res.append(float(arbol['inclinacio']))
    return res

centenario = leer_parque("arbolado-en-espacios-verdes.csv","CENTENARIO")      
print(obtener_inclinaciones(centenario,"Falso Guayabo (Guayaba del Brasil)"))            
#%%
"""
6)
Combinando la función especies() con obtener_inclinaciones() 
escribir una función especimen_mas_inclinado(lista_arboles) 
que, dada una lista de árboles devuelva la especie que tiene 
el ejemplar más inclinado y su inclinación.
"""
import numpy as np
def especimen_mas_inclinado(lista_arboles:list[dict[str,str]])->tuple[str,float]:
    lista_especies = especies(lista_arboles)
    inclinaciones = []
    for especie in lista_especies:
        inclinacion = obtener_inclinaciones(lista_arboles, especie)
        maximo = np.array(inclinacion)                                      
        inclinaciones.append(maximo.max())    
    datos = dict(zip(lista_especies,inclinaciones))
    res: tuple[str,float]=[]
    num=0
    for clave in datos.keys():
        if (datos[clave]> num):
            num = datos[clave]
            res = [clave, num] 
    return res
#%%    
"""
7)
Volver a combinar las funciones anteriores para escribir la 
función especie_promedio_mas_inclinada(lista_arboles) que, 
dada una lista de árboles devuelva la especie que en promedio 
tiene la mayor inclinación y el promedio calculado.
Resultados. Debería obtenerse, por ejemplo, que los Álamos 
Plateados del Parque Los Andes tiene un promedio de 
inclinación de 25 grados.                                              
"""                                              

def especie_promedio_mas_inclinada(lista_arboles:list[dict[str,str]])->tuple[str,float]:
    lista_especies = especies(lista_arboles)
    promedios:list[float] = []
    for especie in lista_especies:
        inclinacion = obtener_inclinaciones(lista_arboles, especie)
        inclinaciones = np.array(inclinacion)       
        promedios.append(inclinaciones.sum()/inclinaciones.size)   
    datos = dict(zip(lista_especies,promedios))
    res: tuple[str,float]=[]
    num=0
    for clave in datos.keys():
        if (datos[clave]> num):
            num = datos[clave]
            res = [clave, num] 
    return res
#%%
"""
Armar un DataFrame data_arboles_veredas que tenga solamente 
las siguiente
columnas: 'nombre_cientifico', 'ancho_acera', 
'diametro_altura_pecho',
'altura_arbol' """

import pandas as pd

filename1 = '~/Desktop/LaboDeDatos/clase0_1_2/ejercicios_clase1/arbolado-publico-lineal-2017-2018.csv'
data_arboles_veredas = pd.read_csv(filename1, usecols=['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho','altura_arbol'])
filename2 = '~/Desktop/LaboDeDatos/clase0_1_2/ejercicios_clase1/arbolado-en-espacios-verdes.csv'
data_arboles_parques = pd.read_csv(filename2, usecols=['nombre_cie', 'inclinacio', 'diametro', 'altura_tot'])

"""
8)
Para cada dataset, armar otro seleccionando solamente las filas 
correspondientes a las tipas (llamalos df_tipas_parques y 
df_tipas_veredas, respectivamente) y las
columnas correspondientes al diámetro a la altura del pecho y 
alturas. Usar como copias (usando .copy()) para poder trabajar 
en estos nuevos dataframes sin modificar los dataframes grandes
originales. Renombrar las columnas necesarias
para que se llamen igual en ambos dataframes. 
"""

df_tipas_veredas = data_arboles_veredas[data_arboles_veredas['nombre_cientifico']=='Tipuana tipu']
df_tipas_parques = data_arboles_parques[data_arboles_parques['nombre_cie']=='Tipuana Tipu']
df_tipas_veredas = df_tipas_veredas.rename(columns={"diametro_altura_pecho": "diametro","altura_arbol":"altura_tot"})
df_tipas_parques = df_tipas_parques.rename(columns={"nombre_cie": "nombre_cientifico", "inclinacio":"ancho_acera"})
                
"""
9)
Agregar a cada dataframe (df_tipas_parques y df_tipas_veredas) 
una columna llamada 'ambiente' que en un caso valga siempre 
'parque' y en el otro caso 'vereda'.
"""
df_tipas_veredas['ambiente']='vereda'
df_tipas_parques['ambiente']='parque'
        
"""
10) Concatenar los dataframes.
"""
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])
"""  
                                            
11. Explorar y analizar sobre la cuestión planteada:
¿Hay diferencias entre los ejemplares de una misma especie según si crecen en
un un parque o en la vereda?
"""
#%%    



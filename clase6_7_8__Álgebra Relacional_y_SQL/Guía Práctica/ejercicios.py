# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 13:43:28 2025

@author: sofia
"""

#Importamos bibliotecas:
import pandas as pd
import duckdb as dd


#%%===========================================================================
# Importamos los datasets que vamos a utilizar en este programa
#=============================================================================

carpeta = "~/Desktop/LaboDeDatos/clase6_7_8__Álgebra Relacional_y_SQL/Guía Práctica/"

casos = pd.read_csv(carpeta+"casos.csv")
departamento = pd.read_csv(carpeta+"departamento.csv")
grupoetario = pd.read_csv(carpeta+"grupoetario.csv")
provincia = pd.read_csv(carpeta+"provincia.csv")
tipoevento = pd.read_csv(carpeta+"tipoevento.csv")


#EJERCICIOS:

#%%===========================================================================
# A) CONSULTAS SOBRE UNA TABLA:
#=============================================================================
#%%
"""
a. Listar sólo los nombres de todos los departamentos que hay 
en la tabla departamento (dejando los registros repetidos).
"""

consultaSQL = """
              SELECT descripcion
              FROM departamento
              """

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)
#%%
"""
b. Listar sólo los nombres de todos los departamentos que hay en 
la tabla departamento (eliminando los registros repetidos).
"""
consultaSQL = """
              SELECT DISTINCT descripcion
              FROM departamento
              """

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)
#%%
"""
c. Listar sólo los códigos de departamento y sus nombres, de 
todos los departamentos que hay en la tabla departamento.
"""
consultaSQL = """
              SELECT DISTINCT id, descripcion
              FROM departamento
              """

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)
#%%
"""
d. Listar todas las columnas de la tabla departamento.
"""
consultaSQL = """
              SELECT DISTINCT id, descripcion, id_provincia
              FROM departamento
              """

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)
#%%
"""
e. Listar los códigos de departamento y nombres de todos los 
departamentos que hay en la tabla departamento. Utilizar los 
siguientes alias para las columnas: codigo_depto y 
nombre_depto, respectivamente.
"""
consultaSQL = """
              SELECT DISTINCT id as codigo_depto, 
                              descripcion as nombre_depto
              FROM departamento
              """

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)
#%%
"""
f. Listar los registros de la tabla departamento cuyo código 
de provincia es igual a 54
"""
consultaSQL = """
              SELECT DISTINCT id, descripcion, id_provincia
              FROM departamento
              WHERE id_provincia='54'
              """

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)
#%%
"""
g. Listar los registros de la tabla departamento cuyo código 
de provincia es igual a 22, 78 u 86.
"""
consultaSQL = """
              SELECT DISTINCT id, descripcion, id_provincia
              FROM departamento
              WHERE (id_provincia='22' OR id_provincia='78' OR id_provincia='86')
              """

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)
#%%
"""
h. Listar los registros de la tabla departamento cuyos códigos 
de provincia se encuentren entre el 50 y el 59 
(ambos valores inclusive).
"""
consultaSQL = """
              SELECT DISTINCT id, descripcion, id_provincia
              FROM departamento
              WHERE (id_provincia >='50' AND id_provincia <='59')
              """

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)
#%%

#===========================================================================
# B) CONSULTAS MULTITABLA (INNER JOIN):
#=============================================================================
#%%
"""
a. Devolver una lista con los código y nombres de departamentos,
asociados al nombre de la provincia al que pertenecen.
"""
consultaSQL = """
              SELECT DISTINCT d.id as id_depto,
                              d.descripcion as nombre_depto,
                              p.descripcion as nombre_provincia,
              FROM departamento AS d
              INNER JOIN provincia AS p
              ON id_provincia = p.id
              """

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)
#%%
"""
b. Devolver los casos registrados en la provincia de “Chaco”.
"""
data = """
        SELECT DISTINCT d.id as id_depto,
                        d.descripcion as nombre_depto,
                        p.descripcion as nombre_provincia,
        FROM departamento as d,provincia as p
        WHERE id_provincia = p.id AND 
              nombre_provincia = 'Chaco'
      """

deptos_provincia = dd.sql(data).df()

consultaSQL = """
              SELECT DISTINCT c.id, c.id_tipoevento, c.anio, 
                              c.semana_epidemiologica, c.id_depto,
                              c.id_grupoetario,c.cantidad
              FROM casos as c
              INNER JOIN deptos_provincia as dp
              ON c.id_depto = dp.id_depto
              """

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)
#%%
"""
c. Devolver aquellos casos de la provincia de “Buenos Aires” cuyo campo
cantidad supere los 10 casos.
"""
data = """
        SELECT DISTINCT d.id as id_depto,
                        d.descripcion as nombre_depto,
                        p.descripcion as nombre_provincia,
        FROM departamento as d,provincia as p
        WHERE id_provincia = p.id AND nombre_provincia = 'Buenos Aires'
      """

deptos_provincia = dd.sql(data).df()

consultaSQL = """
              SELECT DISTINCT c.id, c.id_tipoevento, c.anio, 
                              c.semana_epidemiologica, 
                              c.id_depto,
                              c.id_grupoetario,c.cantidad
              FROM casos as c
              INNER JOIN deptos_provincia as dp
              ON (c.id_depto = dp.id_depto AND 
                  c.cantidad>'10')
              """

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)
#%%

#===========================================================================
# C) CONSUTAS MULTITABLA (OUTER JOIN):
#=============================================================================
#%%
"""
a. Devolver un listado con los nombres de los departamentos que
no tienen ningún caso asociado.
"""
consultaSQL = """
              SELECT DISTINCT d.descripcion
              FROM departamento AS d
              LEFT OUTER JOIN casos AS c
              ON d.id=c.id_depto
              
              """

dataframeResultado = dd.sql(consultaSQL).df()
print(dataframeResultado)
#%%
"""
b. Devolver un listado con los tipos de evento que no tienen 
ningún caso asociado
"""
consultaSQL1 = """
              SELECT DISTINCT te.descripcion as nombre_evento 
              FROM tipoevento AS te, casos AS c
              where te.id != c.id_tipoevento
              """
consultaSQL2 = """
              SELECT DISTINCT te.descripcion as nombre_evento 
              FROM tipoevento AS te
              LEFT OUTER JOIN casos AS c
              ON te.id = c.id_tipoevento
              """
              
dataframeResultado1 = dd.sql(consultaSQL1).df()
dataframeResultado2 = dd.sql(consultaSQL2).df()
print(dataframeResultado1)
print(dataframeResultado2)
#%%




















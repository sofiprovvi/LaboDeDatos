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

carpeta = ""

casos = pd.read_csv(carpeta+"casos.csv")
departamento = pd.read_csv(carpeta+"departamento.csv")
grupoetario = pd.read_csv(carpeta+"grupoetario.csv")
provincia = pd.read_csv(carpeta+"provincia.csv")
tipoevento = pd.read_csv(carpeta+"tipoevento.csv")

consultaSQL = """
              SELECT DISTINCT c.anio AS anio
              FROM casos AS c
              """
anios = dd.sql(consultaSQL).df()
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
#%%
"""
d. Listar todas las columnas de la tabla departamento.
"""
consultaSQL = """
              SELECT DISTINCT id, descripcion, id_provincia
              FROM departamento
              """

dataframeResultado = dd.sql(consultaSQL).df()
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
#%%
"""
b. Devolver los casos registrados en la provincia de “Chaco”.
"""
consultaSQL = """
        SELECT DISTINCT d.id as id_depto,
                        d.descripcion as nombre_depto,
                        p.descripcion as nombre_provincia,
        FROM departamento as d,provincia as p
        WHERE id_provincia = p.id AND 
              nombre_provincia = 'Chaco'
      """

deptos_provincia = dd.sql(consultaSQL).df()

consultaSQL = """
              SELECT DISTINCT c.id, c.id_tipoevento, c.anio, 
                              c.semana_epidemiologica, c.id_depto,
                              c.id_grupoetario,c.cantidad
              FROM casos as c
              INNER JOIN deptos_provincia as dp
              ON c.id_depto = dp.id_depto
              """

dataframeResultado = dd.sql(consultaSQL).df()
#%%
"""
c. Devolver aquellos casos de la provincia de “Buenos Aires” cuyo campo
cantidad supere los 10 casos.
"""
consultaSQL = """
        SELECT DISTINCT d.id as id_depto,
                        d.descripcion as nombre_depto,
                        p.descripcion as nombre_provincia,
        FROM departamento as d,provincia as p
        WHERE id_provincia = p.id AND nombre_provincia = 'Buenos Aires'
      """

deptos_provincia = dd.sql(consultaSQL).df()

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
#%%

#===========================================================================
# C) CONSULTAS MULTITABLA (OUTER JOIN):
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
#%%
"""
b. Devolver un listado con los tipos de evento que no tienen 
ningún caso asociado
"""
consultaSQL = """
              SELECT DISTINCT te.descripcion as nombre_evento 
              FROM tipoevento AS te, casos AS c
              where te.id != c.id_tipoevento
              """
dataframeResultado = dd.sql(consultaSQL).df()
#%%
#===========================================================================
# D) CONSULTAS RESUMEN:
#=============================================================================
"""a. Calcular la cantidad total de casos que hay en la tabla casos.
"""
consultaSQL = """
              SELECT SUM(Cantidad) AS CantidadCasos
              FROM casos
              """
dataframeResultado = dd.sql(consultaSQL).df()
#%%
"""b. Calcular la cantidad total de casos que hay en la tabla casos
 para cada año y cada tipo de caso. Presentar la información de la 
 siguiente manera: descripción del tipo de caso, año y cantidad. 
 Ordenarlo por tipo de caso (ascendente) y año (ascendente).
"""
consultaSQL = """
              SELECT te.descripcion AS Descripción,
                     SUM(c.cantidad) AS Cantidad ,
                     c.anio AS Año
              FROM casos AS c
              INNER JOIN tipoevento AS te
              ON c.id_tipoevento=te.id
              GROUP BY c.anio,Descripcion
              ORDER BY te.descripcion ASC,
                       c.anio ASC
              """
dataframeResultado = dd.sql(consultaSQL).df()
#%%
"""c. Misma consulta que el ítem anterior, pero sólo para el año 2019.
"""
consultaSQL = """
              SELECT te.descripcion AS Descripción,
                     SUM(c.cantidad) AS Cantidad ,
                     c.anio AS Año
              FROM casos AS c
              INNER JOIN tipoevento AS te
              ON c.id_tipoevento=te.id
              WHERE anio=2019
              GROUP BY c.anio,Descripción
              ORDER BY te.descripcion ASC,
                       c.anio ASC
              """
dataframeResultado = dd.sql(consultaSQL).df()
#%%
"""d. Calcular la cantidad total de departamentos que hay por 
provincia. Presentar la información ordenada por código de 
provincia.
"""
consultaSQL = """
              SELECT p.descripcion AS Descripción,
                     COUNT(d.id) AS Departamentos
              FROM departamento AS d
              RIGHT OUTER JOIN provincia AS p
              ON p.id = d.id_provincia
              GROUP BY p.id,Descripción
              ORDER BY p.id ASC
              """
dataframeResultado = dd.sql(consultaSQL).df()
#%%
"""e. Listar los departamentos con menos cantidad de casos 
en el año 2019.
"""
consultaSQL = """
              SELECT d.descripcion AS Departamento,
                     CASE WHEN SUM(c.Cantidad) IS NULL
                                THEN 0
                                ELSE SUM(c.Cantidad)
                                END AS Casos
              FROM departamento AS d
              LEFT OUTER JOIN casos AS c
              ON d.id=c.id_depto AND c.anio=2019
              GROUP BY d.id, Departamento
              ORDER BY Casos ASC
              """
dataframeResultado = dd.sql(consultaSQL).df()
#%%
"""f. Listar los departamentos con más cantidad de casos 
en el año 2020.
"""
consultaSQL = """
              SELECT d.descripcion AS Departamento,
                     CASE WHEN SUM(c.Cantidad) IS NULL
                                THEN 0
                                ELSE SUM(c.Cantidad)
                                END AS Casos
              FROM departamento AS d
              LEFT OUTER JOIN casos AS c
              ON d.id=c.id_depto AND c.anio=2020
              GROUP BY d.id, Departamento
              ORDER BY Casos DESC
              """
dataframeResultado = dd.sql(consultaSQL).df()
#%%
"""g. Listar el promedio de cantidad de casos por provincia y año.
"""
consultaSQL = """
              SELECT p.descripcion AS Provincia,
                     c.anio AS Año,
                     CASE WHEN AVG(c.Cantidad) IS NULL
                                THEN 0
                                ELSE AVG(c.Cantidad)
                                END AS Casos
              FROM provincia AS p
              LEFT OUTER JOIN departamento AS d
              ON p.id=d.id_provincia
              LEFT OUTER JOIN casos AS c
              ON d.id=c.id_depto
              GROUP BY p.id, Provincia, Año
              """
dataframeResultado = dd.sql(consultaSQL).df()
#%%
"""
h. Listar, para cada provincia y año, cuáles fueron los departamentos 
que más cantidad de casos tuvieron.
"""
consultaSQL = """
              SELECT p.descripcion AS Provincia,
                     a.anio AS Año,
                     CASE WHEN SUM(c.Cantidad) IS NULL
                                THEN 0
                                ELSE SUM(c.Cantidad)
                                END AS Casos
              FROM provincia AS p
              CROSS JOIN anios AS a
              LEFT OUTER JOIN departamento AS d
              ON p.id=d.id_provincia
              LEFT OUTER JOIN casos AS c
              ON d.id=c.id_depto AND c.anio=a.anio
              GROUP BY p.id, Provincia, Año
              ORDER BY Casos DESC
              """
dataframeResultado = dd.sql(consultaSQL).df()
#%%
"""
i. Mostrar la cantidad de casos total, máxima, mínima y promedio 
que tuvo la provincia de Buenos Aires en el año 2019.
"""
consultaSQL = """
              SELECT p.descripcion AS Provincia,
                     SUM(c.Cantidad) AS Total,
                     CASE WHEN AVG(c.Cantidad) IS NULL
                          THEN 0
                          ELSE AVG(c.Cantidad)
                     END AS Promedio,
                     CASE WHEN MAX(c.Cantidad) IS NULL
                          THEN 0
                          ELSE MAX(c.Cantidad)
                     END AS Máxima,
                     CASE WHEN MIN(c.Cantidad) IS NULL
                          THEN 0
                          ELSE MIN(c.Cantidad)
                     END AS Mínima
              FROM provincia AS p
              LEFT OUTER JOIN departamento AS d
              ON p.id=d.id_provincia
              LEFT OUTER JOIN casos AS c
              ON d.id=c.id_depto
              WHERE p.descripcion = 'Buenos Aires' AND c.anio=2019
              GROUP BY p.id, Provincia
              """
dataframeResultado = dd.sql(consultaSQL).df()
#%%
"""
j. Misma consulta que el ítem anterior, pero sólo para aquellos 
casos en que la cantidad total es mayor a 1000 casos.
"""
consultaSQL = """
              SELECT p.descripcion AS Provincia,
                     SUM(c.Cantidad) AS Total,
                     CASE WHEN AVG(c.Cantidad) IS NULL
                          THEN 0
                          ELSE AVG(c.Cantidad)
                     END AS Promedio,
                     CASE WHEN MAX(c.Cantidad) IS NULL
                          THEN 0
                          ELSE MAX(c.Cantidad)
                     END AS Máxima,
                     CASE WHEN MIN(c.Cantidad) IS NULL
                          THEN 0
                          ELSE MIN(c.Cantidad)
                     END AS Mínima
              FROM provincia AS p
              LEFT OUTER JOIN departamento AS d
              ON p.id=d.id_provincia
              LEFT OUTER JOIN casos AS c
              ON d.id=c.id_depto 
              WHERE c.anio=2019
              GROUP BY p.id, Provincia
              HAVING Total >1000 
              """
dataframeResultado = dd.sql(consultaSQL).df()
#%%
"""
k. Listar los nombres de departamento (y nombre de provincia) que 
tienen mediciones tanto para el año 2019 como para el año 2020. 
Para cada uno de ellos devolver la cantidad de casos promedio. 
Ordenar por nombre de provincia (ascendente) y luego por nombre 
de departamento (ascendente).
"""
consultaSQL = """ 
SELECT  d.id AS Departamento,
        p.descripcion AS Provincia,
        a.anio AS Año,
        CASE WHEN SUM(c.Cantidad) IS NULL
                   THEN 0
                   ELSE SUM(c.Cantidad)
                   END AS Casos
 FROM departamento AS d
 CROSS JOIN anios AS a
 LEFT OUTER JOIN provincia AS p
 ON p.id=d.id_provincia
 LEFT OUTER JOIN casos AS c
 ON d.id=c.id_depto AND c.anio=a.anio
 GROUP BY d.id, Departamento, Provincia, Año
 """
k0 = dd.sql(consultaSQL).df()

consultaSQL = """  SELECT k0.Departamento AS id
                   FROM k0
                   
                   EXCEPT
                   
                   SELECT k0.Departamento AS id
                   FROM k0
                   WHERE k0.Casos=0
              """
k1 = dd.sql(consultaSQL).df()

consultaSQL = """SELECT d.descripcion AS Departamento,
                        p.descripcion AS Provincia,
                        AVG(c.Cantidad) AS Promedio
                 FROM departamento AS d
                 INNER JOIN k1
                 ON d.id=k1.id
                 INNER JOIN provincia AS p
                 ON d.id_provincia=p.id
                 INNER JOIN casos AS c
                 ON c.id_depto=d.id
                 GROUP BY c.id_depto,Provincia,Departamento
                        """

dataframeResultado = dd.sql(consultaSQL).df()
#%%
"""
i. Devolver una tabla que tenga los siguientes campos: descripción 
de tipo de evento, id_depto, nombre de departamento, id_provincia, 
nombre de provincia, total de casos 2019, total de casos 2020.
"""
consultaSQL = """ 
SELECT  d.id AS id_depto,
        p.id AS id_provincia,
        a.anio AS Año,
        te.id AS id_tipoevento,
        CASE WHEN SUM(c.Cantidad) IS NULL
                   THEN 0
                   ELSE SUM(c.Cantidad)
                   END AS Casos
 FROM departamento AS d
 CROSS JOIN anios AS a
 CROSS JOIN tipoevento AS te
 LEFT OUTER JOIN provincia AS p
 ON p.id=d.id_provincia
 LEFT OUTER JOIN casos AS c
 ON d.id=c.id_depto AND c.anio=a.anio AND c.id_tipoevento=te.id
 GROUP BY d.id, p.id, Año,te.id
 """
i0 = dd.sql(consultaSQL).df()

consultaSQL = """ 
SELECT  i0.id_depto,
        d.descripcion AS Departamento,
        i0.id_provincia,
        p.descripcion AS Provincia,
        te.descripcion AS tipoevento,
        i0.Casos AS "2019",
 FROM i0
 LEFT OUTER JOIN departamento AS d
 ON i0.id_depto=d.id
 LEFT OUTER JOIN provincia AS p
 ON i0.id_provincia = p.id
 LEFT OUTER JOIN tipoevento AS te
 ON i0.id_tipoevento=te.id
 WHERE i0.Año=2019
 GROUP BY i0.id_depto,Departamento,i0.id_provincia,Provincia,i0.id_tipoevento,i0.Casos,tipoevento,i0.Año      

         
"""
i1=dd.sql(consultaSQL).df()

consultaSQL=""" SELECT  i0.id_depto,
         d.descripcion AS Departamento,
         i0.id_provincia,
         p.descripcion AS Provincia,
         te.descripcion AS tipoevento,
         i0.Casos AS "2020"
  FROM i0
  LEFT OUTER JOIN departamento AS d
  ON i0.id_depto=d.id
  LEFT OUTER JOIN provincia AS p
  ON i0.id_provincia = p.id
  LEFT OUTER JOIN tipoevento AS te
  ON i0.id_tipoevento=te.id
  WHERE i0.Año=2020
  GROUP BY i0.id_depto,Departamento,i0.id_provincia,Provincia,i0.id_tipoevento,i0.Casos,tipoevento,i0.Año      
   """

i2=dd.sql(consultaSQL).df()

consultaSQL = """SELECT  i1.id_depto,
                         i1.Departamento,
                         i1.id_provincia,
                         i1.Provincia,
                         i1.tipoevento,
                            i1."2019",
                            i2."2020"
                FROM i1,i2
                WHERE i1.id_depto=i2.id_depto AND
               i1.tipoevento=i2.tipoevento
              """
dataframeResultado = dd.sql(consultaSQL).df()

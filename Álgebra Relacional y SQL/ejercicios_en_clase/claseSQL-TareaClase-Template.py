# -*- coding: utf-8 -*-
"""
Materia: Laboratorio de datos - FCEyN - UBA
Clase  : Clase SQL. Script clase. 
Autor  : Pablo Turjanski
Fecha  : 2025-02-03

Clases 06-08 - SQL - Archivos clase (template script + datos)-20250403
"""

# Importamos bibliotecas
import pandas as pd
import duckdb as dd


#%%===========================================================================
# Importamos los datasets que vamos a utilizar en este programa
#=============================================================================

carpeta = ""

# Ejercicios AR-PROJECT, SELECT, RENAME
empleado       = pd.read_csv(carpeta+"empleado.csv")
# Ejercicios AR-UNION, INTERSECTION, MINUS
alumnosBD      = pd.read_csv(carpeta+"alumnosBD.csv")
alumnosTLeng   = pd.read_csv(carpeta+"alumnosTLeng.csv")
# Ejercicios AR-CROSSJOIN
persona        = pd.read_csv(carpeta+"persona.csv")
nacionalidades = pd.read_csv(carpeta+"nacionalidades.csv")
# Ejercicios ¿Mismos Nombres?
se_inscribe_en=pd.read_csv(carpeta+"se_inscribe_en.csv")
materia       =pd.read_csv(carpeta+"materia.csv")
# Ejercicio JOIN múltiples tablas
vuelo      = pd.read_csv(carpeta+"vuelo.csv")    
aeropuerto = pd.read_csv(carpeta+"aeropuerto.csv")    
pasajero   = pd.read_csv(carpeta+"pasajero.csv")    
reserva    = pd.read_csv(carpeta+"reserva.csv")    
# Ejercicio JOIN tuplas espúreas
empleadoRol= pd.read_csv(carpeta+"empleadoRol.csv")    
rolProyecto= pd.read_csv(carpeta+"rolProyecto.csv")    
# Ejercicios funciones de agregación, LIKE, Elección, Subqueries 
# y variables de Python
examen     = pd.read_csv(carpeta+"examen.csv")
# Ejercicios de manejo de valores NULL
examen03 = pd.read_csv(carpeta+"examen03.csv")



#%%===========================================================================
# Ejemplo inicial
#=============================================================================

print(empleado)

consultaSQL = """
               SELECT DISTINCT DNI, Salario
               FROM empleado;
              """

dataframeResultado = dd.sql(consultaSQL).df()

print(dataframeResultado)


#%%===========================================================================
# Ejercicios AR-PROJECT <-> SELECT
#=============================================================================
# a.- Listar DNI y Salario de empleados 
consultaSQL = """
              SELECT DNI,Salario
              FROM empleado
              """

dataframeResultado = dd.sql(consultaSQL).df()

#%%-----------
# b.- Listar Sexo de empleados 
consultaSQL = """
              SELECT DISTINCT Sexo
              FROM empleado
              """

dataframeResultado = dd.sql(consultaSQL).df()

#%%-----------
#c.- Listar Sexo de empleados (sin DISTINCT)
consultaSQL = """
              SELECT Sexo
              FROM empleado

              """

dataframeResultado = dd.sql(consultaSQL).df()

#%%===========================================================================
# Ejercicios AR-SELECT <-> WHERE
#=============================================================================
# a.- Listar de EMPLEADO sólo aquellos cuyo sexo es femenino
consultaSQL = """
              SELECT DISTINCT DNI AS id, Salario AS Ingreso
              FROM empleado
              """

dataframeResultado = dd.sql(consultaSQL).df()

#%% -----------
#b.- Listar de EMPLEADO aquellos cuyo sexo es femenino y su salario es mayor a $15.000
consultaSQL = """
               SELECT DNI, Nombre, Sexo, Salario
               FROM empleado 
               WHERE Sexo='F' and Salario>15000
              """

dataframeResultado = dd.sql(consultaSQL).df()

#%%===========================================================================
# Ejercicios AR-RENAME <-> AS
#=============================================================================
#a.- Listar DNI y Salario de EMPLEADO, y renombrarlos como id e Ingreso
consultaSQL = """
              SELECT DISTINCT DNI AS ID, Salario AS Ingreso
              From empleado
              """

dataframeResultado = dd.sql(consultaSQL).df()


#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    INICIO -->           EJERCICIO Nro. 01                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# IMPORTANTE: Recordar que se utilizaran los datos de vuelo, aeropuerto, pasajero y reserva

#%%===========================================================================
# EJERCICIOS PARA REALIZAR DE MANERA INDIVIDUAL --> EJERCICIO Nro. 01
#=============================================================================
# Ejercicio 01.1.- Retornar Codigo y Nombre de los aeropuertos de Londres
consultaSQL = """
              SELECT DISTINCT Codigo, Nombre
              FROM aeropuerto 
              WHERE Ciudad='Londres'
              """

dataframeResultado = dd.sql(consultaSQL).df()

#%% -----------
# Ejercicio 01.2.- ¿Qué retorna 
#                       SELECT DISTINCT Ciudad AS City 
#                       FROM aeropuerto 
#                       WHERE Codigo='ORY' OR Codigo='CDG'; ? Paris
consultaSQL = """
                SELECT DISTINCT Ciudad AS City 
                FROM aeropuerto 
                WHERE Codigo='ORY' OR Codigo='CDG';

              """

dataframeResultado = dd.sql(consultaSQL).df()

#%% -----------
# Ejercicio 01.3.- Obtener los números de vuelo que van desde CDG hacia LHR
consultaSQL = """
              SELECT DISTINCT Numero 
              FROM vuelo
              WHERE Origen='CDG' AND Destino='LHR'
              """

dataframeResultado = dd.sql(consultaSQL).df()

#%% -----------
# Ejercicio 01.4.- Obtener los números de vuelo que van desde CDG hacia LHR o viceversa
consultaSQL = """
              SELECT DISTINCT Numero 
              FROM vuelo
              WHERE (Origen='CDG' AND Destino='LHR') OR (Destino='CDG' AND Origen='LHR')
              """

dataframeResultado = dd.sql(consultaSQL).df()

#%% 
# Ejercicio 01.5.- Devolver las fechas de reservas cuyos precios son mayores a $200
consultaSQL = """
              SELECT DISTINCT Fecha 
              FROM reserva
              WHERE Precio > 200
              """

dataframeResultado = dd.sql(consultaSQL).df()


#%% 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    FIN -->              EJERCICIO Nro. 01                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    
#=============================================================================
# Ejercicios AR-UNION, INTERSECTION, MINUS <-> UNION, INTERSECTION, EXCEPT
#=============================================================================
# a1.- Listar a los alumnos que cursan BDs o TLENG

consultaSQL = """
              SELECT DISTINCT *
              FROM alumnosBD
              UNION
              SELECT DISTINCT *
              FROM alumnosTLeng
              
              """

dataframeResultado = dd.sql(consultaSQL).df()


#%% -----------
# a2.- Listar a los alumnos que cursan BDs o TLENG (usando UNION ALL)

consultaSQL = """
              SELECT DISTINCT *
              FROM alumnosBD
              UNION ALL
              SELECT DISTINCT *
              FROM alumnosTLeng
              """

dataframeResultado = dd.sql(consultaSQL).df()

#%% -----------
# b.- Listar a los alumnos que cursan simultáneamente BDs y TLENG

consultaSQL = """
              SELECT DISTINCT *
              FROM alumnosBD
              INTERSECT
              SELECT DISTINCT *
              FROM alumnosTLeng
              
              """

dataframeResultado = dd.sql(consultaSQL).df()

#%% -----------
# c.- Listar a los alumnos que cursan BDs y no cursan TLENG 

consultaSQL = """
             SELECT DISTINCT *
             FROM alumnosBD
             EXCEPT
             SELECT DISTINCT *
             FROM alumnosTLeng
              """

dataframeResultado = dd.sql(consultaSQL).df()

#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    INICIO -->           EJERCICIO Nro. 02                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# IMPORTANTE: Recordar que se utilizaran los datos de vuelo, aeropuerto, pasajero y reserva

#=============================================================================
#  EJERCICIOS PARA REALIZAR DE MANERA INDIVIDUAL --> EJERCICIO Nro. 02
#=============================================================================
# Ejercicio 02.1.- Devolver los números de vuelo que tienen reservas generadas (utilizar intersección)
consultaSQL = """
              SELECT DISTINCT NroVuelo
              FROM reserva
              """

dataframeResultado = dd.sql(consultaSQL).df()

#%%-----------
# Ejercicio 02.2.- Devolver los números de vuelo que aún no tienen reservas
consultaSQL = """
                SELECT DISTINCT Numero
                FROM vuelo
                EXCEPT
                SELECT DISTINCT NroVuelo
                FROM reserva
              """

dataframeResultado = dd.sql(consultaSQL).df()

#%%-----------
# Ejercicio 02.3.- Retornar los códigos de aeropuerto de los que parten o arriban los vuelos
consultaSQL = """
                 SELECT DISTINCT Codigo
                 FROM aeropuerto
                 INTERSECT
                 SELECT DISTINCT Origen
                 FROM vuelo
                 UNION
                 SELECT DISTINCT Codigo
                 FROM aeropuerto
                 INTERSECT
                 SELECT DISTINCT Destino
                 FROM vuelo
                 
              """
              
dataframeResultado = dd.sql(consultaSQL).df()



#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    FIN -->              EJERCICIO Nro. 02                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

#=============================================================================
# Ejercicios AR-... JOIN <-> ... JOIN
#=============================================================================
# a1.- Listar el producto cartesiano entre las tablas persona y nacionalidades

consultaSQL = """
               SELECT DISTINCT *
               FROM persona
               CROSS JOIN nacionalidades
              """

dataframeResultado = dd.sql(consultaSQL).df()


#%%-----------
# a2.- Listar el producto cartesiano entre las tablas persona y nacionalidades (sin usar CROSS JOIN)

consultaSQL = """
               SELECT DISTINCT *
               FROM persona,nacionalidades
              """

dataframeResultado = dd.sql(consultaSQL).df()


#%%
# Carga los nuevos datos del dataframe persona para los ejercicios de AR-INNER y LEFT OUTER JOIN
# ----------------------------------------------------------------------------------------------
persona        = pd.read_csv(carpeta+"persona_ejemplosJoin.csv")
# ----------------------------------------------------------------------------------------------
# b1.- Vincular las tablas persona y nacionalidades a través de un INNER JOIN

consultaSQL = """
            SELECT DISTINCT *
            FROM persona
            INNER JOIN nacionalidades
            ON Nacionalidad=IDN
              """

dataframeResultado = dd.sql(consultaSQL).df()

#%%-----------
# b2.- Vincular las tablas persona y nacionalidades (sin usar INNER JOIN)

consultaSQL = """
            SELECT DISTINCT *
            FROM persona,nacionalidades
            WHERE Nacionalidad=IDN
              """

dataframeResultado = dd.sql(consultaSQL).df()

#%%-----------
# c.- Vincular las tablas persona y nacionalidades a través de un LEFT OUTER JOIN

consultaSQL = """
            SELECT DISTINCT *
            FROM persona
            LEFT OUTER JOIN nacionalidades
            ON  Nacionalidad=IDN

              """

dataframeResultado = dd.sql(consultaSQL).df()

#%%===========================================================================
# Ejercicios SQL - ¿Mismos Nombres?
#=============================================================================
# a.- Vincular las tablas Se_inscribe_en y Materia. Mostrar sólo LU y Nombre de materia

consultaSQL = """
             SELECT i.LU,m.Nombre
             FROM se_inscribe_en AS i
             INNER JOIN materia AS m
             ON i.codigo_materia=m.codigo_materia
              """

dataframeResultado = dd.sql(consultaSQL).df()

    
#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    INICIO -->           EJERCICIO Nro. 03                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# IMPORTANTE: Recordar que se utilizaran los datos de vuelo, aeropuerto, pasajero y reserva

#%%===========================================================================
# EJERCICIOS PARA REALIZAR DE MANERA INDIVIDUAL --> EJERCICIO Nro. 03
#=============================================================================
# Ejercicio 03.1.- Devolver el nombre de la ciudad de partida del vuelo número 165

vuelo_aeropuerto = """
            SELECT DISTINCT *
            FROM vuelo,aeropuerto;
              """
vuelo_aeropuerto_data=dd.sql(vuelo_aeropuerto).df()         
consultaSQL=""" 
            SELECT DISTINCT Ciudad
            FROM vuelo_aeropuerto_data
            WHERE Numero=165
"""

dataframeResultado = dd.sql(consultaSQL).df()

#%%-----------
# Ejercicio 03.2.- Retornar el nombre de las personas que realizaron reservas a un valor menor a $200

menor_a_200="""
                SELECT DISTINCT DNI
                FROM reserva
                WHERE Precio<200
            """
menor=dd.sql(menor_a_200).df()

consultaSQL = """
                SELECT DISTINCT Nombre
                FROM menor,pasajero
                WHERE menor.DNI=pasajero.DNI
                
              """

dataframeResultado = dd.sql(consultaSQL).df()

#%%-----------
# Ejercicio 03.3.- Obtener Nombre, Fecha y Destino del Viaje de todos los pasajeros que vuelan desde Madrid

vuelosAMadrid = dd.sql("""
               SELECT DISTINCT Numero,Destino
               FROM vuelo
               WHERE Origen='MAD'
              """).df()
              
dniPersonasDesdeMadrid = dd.sql("""
               SELECT DISTINCT DNI,Fecha,Destino
               FROM reserva,vuelosAMadrid
               WHERE reserva.NroVuelo=vuelosAMadrid.Numero

              """).df()

consultaSQL = """
              SELECT DISTINCT Nombre,Fecha,Destino
              FROM dniPersonasDesdeMadrid,pasajero
              WHERE dniPersonasDesdeMadrid.DNI=pasajero.DNI
              """

dataframeResultado = dd.sql(consultaSQL).df()


#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    FIN -->              EJERCICIO Nro. 03                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    
#%%===========================================================================
# Ejercicios SQL - Join de varias tablas en simultáneo
#=============================================================================
# a.- Vincular las tablas Reserva, Pasajero y Vuelo. Mostrar sólo Fecha de reserva, hora de salida del vuelo y nombre de pasajero.
 
DNI_Fecha_Salida__ReservaVuelo= dd.sql("""
                SELECT DISTINCT reserva.DNI,reserva.Fecha,vuelo.Salida
                FROM reserva, vuelo
                WHERE NroVuelo = Numero
              """).df()
                 
consultaSQL = """ 
               SELECT DISTINCT pasajero.Nombre,t.Fecha,t.Salida
               FROM DNI_Fecha_Salida__ReservaVuelo AS t , pasajero
               WHERE t.DNI = pasajero.DNI
              """

dataframeResultado = dd.sql(consultaSQL).df()

    
#%%===========================================================================
# Ejercicios SQL - Tuplas espúreas
#=============================================================================
# a.- Vincular (JOIN)  EmpleadoRol y RolProyecto para obtener la tabla original EmpleadoRolProyecto
    
consultaSQL = """
               SELECT DISTINCT empleado,rol
               FROM empleadoRol, rolProyecto 
               WHERE empleadoRol.rol=rolProyecto.rol
              """

dataframeResultado = dd.sql(consultaSQL).df()

#%%===========================================================================
# Ejercicios SQL - Funciones de agregación
#=============================================================================
# a.- Usando sólo SELECT contar cuántos exámenes fueron rendidos (en total)
    
consultaSQL = """
               SELECT COUNT(*) AS cantidadExamenes
               FROM examen
               
              """

dataframeResultado = dd.sql(consultaSQL).df()


#%%-----------
# b1.- Usando sólo SELECT contar cuántos exámenes fueron rendidos en cada Instancia
    
consultaSQL = """
              SELECT Instancia, COUNT(*) AS cantidadExamenes
              FROM examen
              GROUP BY Instancia

              """

dataframeResultado = dd.sql(consultaSQL).df()


#%%-----------
# b2.- Usando sólo SELECT contar cuántos exámenes fueron rendidos en cada Instancia (ordenado por instancia)
    
consultaSQL = """
              SELECT Instancia, COUNT(*) AS cantidadExamenes
              FROM examen
              GROUP BY Instancia
              ORDER BY Instancia

              """

dataframeResultado = dd.sql(consultaSQL).df()


#%%-----------
# b3.- Ídem ejercicio anterior, pero mostrar sólo las instancias a las que asistieron menos de 4 Estudiantes
    
consultaSQL = """
              SELECT Instancia, COUNT(*) AS cantidadExamenes
              FROM examen
              GROUP BY Instancia
              HAVING cantidadExamenes < 4
              ORDER BY Instancia

              """

dataframeResultado = dd.sql(consultaSQL).df()

#%%-----------
# c.- Mostrar el promedio de edad de los estudiantes en cada instancia de examen
    
consultaSQL = """
              SELECT Instancia, AVG(Edad) AS PromedioEdad
              FROM examen
              GROUP BY Instancia
              """

dataframeResultado = dd.sql(consultaSQL).df()


#%%===========================================================================
# Ejercicios SQL - LIKE")
#=============================================================================
# a1.- Mostrar cuál fue el promedio de notas en cada instancia de examen, sólo para instancias de parcial.
    
consultaSQL = """
              SELECT Instancia, AVG(Nota) AS PromedioNota
              FROM examen
              WHERE Instancia='Parcial-01' OR Instancia='Parcial-02'
              GROUP BY Instancia
              ORDER BY Instancia
              """

dataframeResultado = dd.sql(consultaSQL).df()

#%%-----------
# a2.- Mostrar cuál fue el promedio de notas en cada instancia de examen, sólo para instancias de parcial. Esta vez usando LIKE.
    
consultaSQL = """
              SELECT Instancia, AVG(Nota) AS PromedioNota
              FROM examen
              GROUP BY Instancia
              HAVING Instancia LIKE 'Parcial%'
              ORDER BY Instancia ASC

              """

dataframeResultado = dd.sql(consultaSQL).df()


#%%===========================================================================
# Ejercicios SQL - Eligiendo
#=============================================================================
# a1.- Listar a cada alumno que rindió el Parcial-01 y decir si aprobó o no (se aprueba con nota >=4).
    
consultaSQL = """
              SELECT Nombre, Instancia,
                     CASE WHEN Nota>=4
                          THEN 'APROBÓ'
                          ELSE 'NO APROBÓ'
                     END AS Estado
              FROM examen
              WHERE Instancia = 'Parcial-01'
              GROUP BY Instancia,Estado,Nombre
              ORDER BY Instancia, Estado
              
              """

dataframeResultado = dd.sql(consultaSQL).df()


#%%-----------
# a2.- Modificar la consulta anterior para que informe cuántos estudiantes aprobaron/reprobaron en cada instancia.
consultaSQL = """
               SELECT Nombre, Instancia,
                      CASE WHEN Nota>=4
                           THEN 'APROBÓ'
                           ELSE 'NO APROBÓ'
                      END AS Estado
               FROM examen
               GROUP BY Instancia,Estado,Nombre
               ORDER BY Instancia, Estado
               
              """

dataframeResultado = dd.sql(consultaSQL).df()


#%%===========================================================================
# Ejercicios SQL - Subqueries
#=============================================================================
#a.- Listar los alumnos que en cada instancia obtuvieron una nota mayor al promedio de dicha instancia

consultaSQL = """
              SELECT e1.Instancia,e1.Nombre,e1.Nota
              FROM examen AS e1
              WHERE e1.Nota > (
                   SELECT AVG(e2.Nota) 
                   FROM examen AS e2
                   WHERE e1.instancia=e2.instancia
                   )
              ORDER BY Instancia, Nombre ASC
              """


dataframeResultado = dd.sql(consultaSQL).df()


#%%-----------
# b.- Listar los alumnos que en cada instancia obtuvieron la mayor nota de dicha instancia

consultaSQL = """
              SELECT e1.Instancia,e1.Nombre,e1.Nota
              FROM examen AS e1
              WHERE e1.Nota >= ALL (
                   SELECT(e2.Nota) 
                   FROM examen AS e2
                   WHERE e1.instancia=e2.instancia
                   )
              ORDER BY Instancia, Nombre ASC
              """

dataframeResultado = dd.sql(consultaSQL).df()


#%%-----------
# c.- Listar el nombre, instancia y nota sólo de los estudiantes que no rindieron ningún Recuperatorio

consultaSQL = """
              SELECT e1.Instancia,e1.Nombre,e1.Nota
              FROM examen AS e1
              WHERE NOT EXISTS (
                  SELECT *
                  FROM examen AS e2
                  where e2.nombre=e1.nombre AND e2.instancia LIKE 'Recu%'
                  )
              ORDER BY e1.Nombre,e1.Instancia
              """

dataframeResultado = dd.sql(consultaSQL).df()


#%%===========================================================================
# Ejercicios SQL - Integrando variables de Python
#=============================================================================
# a.- Mostrar Nombre, Instancia y Nota de los alumnos cuya Nota supera el umbral indicado en la variable de Python umbralNota

umbralNota = 7

consultaSQL = """
              SELECT Nombre,Instancia,Nota
              FROM examen
              WHERE Nota>7
              """

dataframeResultado = dd.sql(consultaSQL).df()


#%%===========================================================================
# Ejercicios SQL - Manejo de NULLs
#=============================================================================
# a.- Listar todas las tuplas de Examen03 cuyas Notas son menores a 9

consultaSQL = """
               SELECT *
               from examen03
               WHERE Nota<=9
               
              """

dataframeResultado = dd.sql(consultaSQL).df()

#%%-----------
# b.- Listar todas las tuplas de Examen03 cuyas Notas son mayores o iguales a 9

consultaSQL = """
                    SELECT *
                    from examen03
                    WHERE Nota>=9
                    
              """


dataframeResultado = dd.sql(consultaSQL).df()


#%%-----------
# c.- Listar el UNION de todas las tuplas de Examen03 cuyas Notas son menores a 9 y las que son mayores o iguales a 9

consultaSQL = """
              SELECT *
              from examen03
              WHERE Nota<9
              
              UNION
              
              SELECT *
              from examen03
              WHERE Nota>9
              """


dataframeResultado = dd.sql(consultaSQL).df()


#%%-----------
# d1.- Obtener el promedio de notas

consultaSQL = """
              SELECT AVG(Notas) as NotaPromedio
              from examen03

              """


dataframeResultado = dd.sql(consultaSQL).df()


#%%-----------
# d2.- Obtener el promedio de notas (tomando a NULL==0)

consultaSQL = """
              SELECT AVG(
                  CASE WHEN
                  Nota IS NULL
                    THEN 0
                    ELSE Nota 
                    END) 
                    AS NotaPromedio
              from examen03

              """


dataframeResultado = dd.sql(consultaSQL).df()

#%%===========================================================================
# Ejercicios SQL - Mayúsculas/Minúsculas
#=============================================================================
# a.- Consigna: Transformar todos los caracteres de las descripciones de los roles a mayúscula

consultaSQL = """
              SELECT EMPLEADO, UPPER(rol) AS rol
              FROM empleadoRol
              """

dataframeResultado = dd.sql(consultaSQL).df()

#%%-----------
# b.- Consigna: Transformar todos los caracteres de las descripciones de los roles a minúscula

consultaSQL = """
              SELECT EMPLEADO, LOWER(rol) AS rol
              FROM empleadoRol

              """

dataframeResultado = dd.sql(consultaSQL).df()




#%%===========================================================================
# Ejercicios SQL - Reemplazos
#=============================================================================
# a.- Consigna: En la descripción de los roles de los empleados reemplazar las ñ por ni

consultaSQL = """
              SELECT EMPLEADO, REPLACE(rol,'ni','ñ') AS rol
              FROM empleadoRol

              """

dataframeResultado = dd.sql(consultaSQL).df()


#%%===========================================================================
# Ejercicios SQL - Desafío
#=============================================================================
# a.- Mostrar para cada estudiante las siguientes columnas con sus datos: Nombre, Sexo, Edad, Nota-Parcial-01, Nota-Parcial-02, Recuperatorio-01 y , Recuperatorio-02

# ... Paso 1: Obtenemos los datos de los estudiantes #TERMINAR
consultaSQL = """
              SELECT DISTINCT e.Nombre,e.Sexo,e.Edad,e.Nota AS "Nota-Parcial-01",
              FROM examen AS e 
              WHERE Instancia='Parcial-01'
              """
parcial1=dd.sql(consultaSQL).df()
      
consultaSQL="""
              SELECT DISTINCT e.Nombre,e.Sexo,e.Edad,e.Nota AS "Nota-Parcial-02",
              FROM examen AS e
              WHERE e.Instancia='Parcial-02' 
            """
parcial2=dd.sql(consultaSQL).df()

consultaSQL="""
              SELECT DISTINCT e.Nombre,e.Sexo,e.Edad,e.Nota AS "Nota-Recuperatorio-01",
              FROM examen AS e
              WHERE Instancia='Recuperatorio-01' 
         """
recu1=dd.sql(consultaSQL).df()

consultaSQL="""
             SELECT DISTINCT e.Nombre,e.Sexo,e.Edad,e.Nota AS "Nota-Recuperatorio-02",
             FROM examen AS e
             WHERE e.Instancia='Recuperatorio-02'
         """
recu2=dd.sql(consultaSQL).df()


consultaSQL="""
              SELECT DISTINCT p1.Nombre,
                              p1.Sexo,
                              p1.Edad,
                              p1."Nota-Parcial-01",
                              p2."Nota-Parcial-02",
                              r1."Nota-Recuperatorio-01",
                              r2."Nota-Recuperatorio-02",
              FROM parcial1 AS p1
              LEFT OUTER JOIN parcial2 AS p2
              ON p1.Nombre=p2.Nombre 
              LEFT OUTER JOIN recu1 AS r1
              ON p1.Nombre=r1.Nombre
              LEFT OUTER JOIN recu2 AS r2
              ON p1.Nombre=r2.Nombre
         """
         
desafio1 = dd.sql(consultaSQL).df()
#%% -----------
# b.- Agregar al ejercicio anterior la columna Estado, que informa si el alumno aprobó la cursada (APROBÓ/NO APROBÓ). Se aprueba con 4.

consultaSQL = """
              SELECT DISTINCT d1.Nombre,
                              d1.Sexo,
                              d1.Edad,
                              d1."Nota-Parcial-01" ,
                              d1."Nota-Parcial-02",
                              d1."Nota-Recuperatorio-01",
                              d1."Nota-Recuperatorio-02",
                              CASE WHEN 
                                (d1."Nota-Parcial-01">4 AND d1."Nota-Parcial-02">4) OR 
                                (d1."Nota-Recuperatorio-01">4 AND d1."Nota-Parcial-02">4) OR
                                (d1."Nota-Parcial-01">4 AND d1."Nota-Recuperatorio-02">4) OR
                                (d1."Nota-Recuperatorio-01">4 AND d1."Nota-Recuperatorio-02">4)
                                THEN 'APROBÓ'
                                ELSE 'NO APROBÓ'
                                END AS Estado
              FROM desafio1 AS d1                  
              """

desafio2 = dd.sql(consultaSQL).df()
#%% -----------
# c.- Generar la tabla Examen a partir de la tabla obtenida en el desafío anterior.
consultaSQL = """
              SELECT Nombre, Sexo, Edad, "Nota-Parcial-01" AS Nota, 'Parcial-01' AS Instancia
              FROM desafio2
              WHERE "Nota-Parcial-01" IS NOT NULL
              
              UNION 
              
              SELECT Nombre, Sexo, Edad, "Nota-Parcial-02" AS Nota, 'Parcial-02' AS Instancia
              FROM desafio2
              WHERE "Nota-Parcial-02" IS NOT NULL
              
              UNION 
              
              SELECT Nombre, Sexo, Edad, "Nota-Recuperatorio-01" AS Nota, 'Recuperatorio-01' AS Instancia
              FROM desafio2
              WHERE "Nota-Recuperatorio-01" IS NOT NULL
              
              UNION 
              
              SELECT Nombre, Sexo, Edad, "Nota-Recuperatorio-02" AS Nota, 'Recuperatorio-02' AS Instancia
              FROM desafio2
              WHERE "Nota-Recuperatorio-02" IS NOT NULL
        """

desafio3 = dd.sql(consultaSQL).df()




















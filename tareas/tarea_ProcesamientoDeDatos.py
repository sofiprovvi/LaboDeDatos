# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 20:43:44 2025

@author: sofia
"""
"""
ACTIVIDAD 1:
Programar a función superanSalarioActividad01 en Python,
que toma como entrada la matriz empleado_01 y un valor
entero denominado umbral, y devuelve una nueva matriz (con las
4 columnas) conteniendo a aquellos empleados que ganan un 
salario>umbral.Solo está permitido utilizar comandos básicos de Python, 
es decir, ciclos(while/for), condicionales(if), etc. 
No está permitido importar funciones de bibliotecas.                                                      
"""
empleado_01 = [[20222333,45,2,20000],
               [33456234,40,0,25000],
               [45432345,41,1,10000]
              ]

def superanSalarioActividad01(matriz: list[list[int]],umbral:int)->list[list[int]]:
    res: list[list[int]]=[]
    for empleados in matriz:
        if (empleados[3]>umbral):
            res+=[empleados]
    return res

print(superanSalarioActividad01(empleado_01,15000))   
#No me costó impementarlo. 

    
            
"""
ACTIVIDAD 2:
"""
empleado_02 = [[20222333,45,2,20000],
               [33456234,40,0,25000],
               [45432345,41,1,10000],
               [43967394,37,0,12000],
               [42236276,36,0,18000]
              ]
print(superanSalarioActividad01(empleado_02,15000)) 
#La función de la Actividad1 sigue funcionando.



"""
ACTIVIDAD 3:
"""
empleado_03 = [[20222333,20000,45,2],
               [33456234,25000,40,0],
               [45432345,10000,41,1],
               [43967394,12000,37,0],
               [42236276,18000,36,0]
              ]

def superanSalarioActividad03(matriz: list[list[int]],umbral:int)->list[list[int]]:
    res: list[list[int]]=[]
    for empleados in matriz:
        if (empleados[1]>umbral):
            res+=[[empleados[0],empleados[2],
                  empleados[3],empleados[1]]]
    return res

print(superanSalarioActividad03(empleado_03,15000)) 



"""ACTIVIDAD 4"""

empleado_04 = [[20222333,33456234,45432345,43967394,42236276],
               [45,40,41,37,36],
               [2,0,1,0,0],
               [20000,25000,10000,12000,18000],
              ]

def superanSalarioActividad04(matriz: list[list[int]],umbral:int)->list[list[int]]:
    salarios=matriz[3]
    i:int=0
    res=[]
    fila=[]
    while i<len(salarios):
        if salarios[i]>umbral:
           for categoria in matriz:
               fila+=[categoria[i]]
           res+=[fila]
        i+=1
        fila=[]
    return res

print(superanSalarioActividad04(empleado_04,15000))



"""ACTIVIDAD 5

1)¿Cómo afetó a la programación de la función cuando cambiaron 
  levemente la matriz empleado?
    a)En el caso en que le agregaron más filas:
      No afectó en nada.
    
    b)En el caso en que le alteraron el orden de las columnas:
    
      En la función anterior, lo que hice fue fijarme dentro de la 
      lista de filas, el índice de las filas que correspondiera 
      al salario. Pero cuando se alteró el orden de las columnas, 
      ese índice cambió y tuve que modificarlo. 
      
      Una vez modificado, por cada salario que fuera mayor al umbral, 
      en vez de agregar la fila directamente a res como hacía en la
      función anterior, implementé una fila nueva en la que ordené
      los elementos de a fila como en la matriz empleado_01. 
      
    
    
2)¿Y cuando a empleado le cambiaron la forma de representar las 
    matrices (de lista de filas a lista de columnas)?
    
    Para la matriz como lista de filas, lo que hacía era fijarme  
    cuál era el índice de las filas que correspondía 
    al salario.
    
    Para la matriz como lista de columnas,en cambio,
    tuve que fijarme cuál de las listas correspondía al salario. 
    Con eso me fijaba si el i-ésimo elemento de "salarios" cumplía 
    con la condición; si cumplía, implementaba la lista "fila" en la 
    que agregaba el iésimo elemento de cada lista de la matriz. 
    Una vez terminada la fila nueva, la agregaba a res.
    
    
    
3)¿Cuál es la ventaja desde el punto de vista del usuario de 
  la función, disponer de ella y no escribir directamente 
  el código de la consulta dentro de su programa?  

  Una de las mayores ventajas para el usuario de disponer de 
  la función es el ahorro de tiempo a la hora de programar. 
  No obstante, antes de utilizar la función en su código, debe 
  asegurarse de conocer bien sus parámetros de entrada y salida,
  para no cometer errores en su programa. 
    
"""































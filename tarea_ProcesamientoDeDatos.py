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
      Para el (if salario>umbral),tuve que cambiar el índice 
      de la fila correspondiente al salario. 
      Luego, por cada fila que cumplía con la condición del if, en 
      vez de agregarla directamente a res, implementaba una fila nueva 
      en la que ordenaba los elementos como me pedían.
      
    
    
2)¿Y cuando a empleado le cambiaron a forma de representar las 
    matrices (de lista de filas a lista de columnas)?
    
    En las funciones anteriores, lo que hacía era fijarme  
    el índice de las listas que correspondían al salario, 
    y con eso hacía un if que si se cumplía, agregaba la fila 
    a res.
    
    En cambio, en la matriz implementada como lista de columnas,
    tuve que buscar, dentro de la matriz, la lista correspondiente
    a los salarios. Una vez que la obtenía, me fijaba si el
    i-ésimo elemento de "salarios" cumplía con la condición; 
    si cumplía, implementaba la lista "fila" en la que agregaba 
    el iésimo elemento de cada lista de la matriz. Una vez 
    que armaba la fila, la agregaba a res.
    
3)¿Cuál es a ventaja desde el punto de vista del usuario de 
  la función, disponer de ella y no escribir directamente 
  el código de la consulta dentro de su programa?    
    
"""































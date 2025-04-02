# -*- coding: utf-8 -*-
"""
Ejercicio 0:
Deﬁnir una función pisar_elemento(M,e) que tome una matriz
de enteros M y un entero e y devuelva una matriz similar a
M donde las entradas coincidentes con e fueron cambiadas 
por -1.Por ejemplo: 
M = np.array([[0, 1, 2, 3], [4, 5, 6, 7]]) y e = 2, 
entonces la función debe devolver la matriz 
np.array([[0, 1, -1, 3], [4, 5, 6, 7]])
"""
#%%
import numpy as np

def pisar_elemento (matriz,e:int):
    m:int=0
    n:int=0
    while (m<matriz.ndim): #m<2
        while n<matriz.shape[1]: #n<4
          if (matriz[m,n]==e): 
              matriz[m,n]=(-1)  
          n+=1    
        m+=1    
    return matriz

m = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])
print(pisar_elemento(m,2))
#%%   

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 22 09:34:57 2025

@author: Estudiante
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import duckdb as dd
carpeta=""

titanic = pd.read_csv(carpeta + "titanic.csv")

#%%
#CONSIGNA 1:

consultaSQL = """ SELECT COUNT(*) as n
                  FROM titanic
                  WHERE Pclass=1
                  """

clase1 = dd.sql(consultaSQL).df()  
clase1=clase1.iloc[0]  

consultaSQL = """ SELECT COUNT(*) as n
                  FROM titanic
                  WHERE Pclass=2
                  """

clase2 = dd.sql(consultaSQL).df()  
clase2=clase2.iloc[0] 

consultaSQL = """ SELECT COUNT(*) as n
                  FROM titanic
                  WHERE Pclass=3
                  """
clase3 = dd.sql(consultaSQL).df()  
clase3=clase3.iloc[0] 

consultaSQL = """ SELECT COUNT(*) as n
                   FROM titanic
                   WHERE Age < 12
                   """  
                   
niños=dd.sql(consultaSQL).df()  
niños = niños.iloc[0]           
#%%
def clasificador(tabla):
    vive =False
    if regla:
        vive=True
    return vive
        

def regla(fila):
    if fila['Sex']=='female' or fila['Age']<13 or fila['Pclass']==1:
        return True
    else:
        return False

for i in range(10):
    print(clasificador(titanic.iloc[0:i]))

#%%
from sklearn import tree

atributos=(titanic['Age'],titanic['Fare'],titanic['Pclass'])
X = atributos
Y = titanic['Survived']
   
clf_info = tree.DecisionTreeClassifier(criterion = "entropy", max_depth= 4)
clf_info = clf_info.fit(X, Y)


plt.figure(figsize= [15,10])
titanic.plot_titanic(clf_info, feature_names = titanic['Paseengerld'], class_names = titanic['Survived'],filled = True, rounded = True, fontsize = 10)


datonuevo= pd.DataFrame([dict(zip(titanic['Survived'], [6.8,3,4.5, 2.15]))])
clf_info.predict(datonuevo)


#%%
# otra forma de ver el arbol
r = tree.export_text(clf_info, feature_names=iris['feature_names'])
print(r)






















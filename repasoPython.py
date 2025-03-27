#GUÍA PRELIMINAR DE PYTHON:

"""
EJERCICIO 1:
"Una mañana ponés un billete en la vereda al lado del obelisco porteño. A partir
de ahí, cada día vas y duplicás la cantidad de billetes, apilándolos prolijamente.
¿Cuánto tiempo pasa antes de que la pila de billetes sea más alta que el
obelisco?
Datos: espesor del billete: 0.11 mm, altura obelisco: 67.5 m
"""
from encodings.punycode import T


def masObelisco (billete: float, h: float) -> int:
    dias: int = 0
    total: int = 0
    while total < h :
          total+=(billete*2)
          dias+=1
    return ("Pasan " + str(dias) + " días.")

"""
EJERCICIO 2:
"""
def cadena_geringosa1 (cadena: str) -> str:
    res: str = ""
    vocales = ['a','e','i','o','u'] 
    for letra in cadena:
        if letra in vocales:
            res+=letra + "p" + letra 
        else:
            res+=letra 
    return res

def cadena_geringosa2 (cadena: str) -> str:
    res: str = ""
    i=0
    vocales = ['a','e','i','o','u'] 
    while i<len(cadena):
        if cadena[i] in vocales:
            res+=cadena[i] + "p" + cadena[i]
        else:
            res+=cadena[i]
        i+=1    
    return res

       
"""EJERCICIO 3"""
def pertenece (lista: list[T], elem: T) -> bool:
    if (elem in lista):
        return True
    else:
        return False
    


"""EJERCICIO 4"""    
def listaMasLarga (lista1: list[T], lista2: list[T]) -> bool:
    if len(lista1) >= len(lista2):
       return lista1
    else:
       return lista2
    


"""EJERCICIO 5
Una pelota de goma es arrojada desde una altura de 100 metros y cada vez que
toca el piso salta 3/5 de la altura desde la que cayó. Escribí un programa
rebotes.py que imprima una tabla mostrando las alturas que alcanza en cada uno
de sus primeros diez rebotes
"""

def rebotes():
    res: str = ""
    i: int = 0
    caida: int = 100
    while i<10:
        caida = (3/5)*caida
        i+=1
        res += "Rebote " + str(i) + ": " + str(caida) + "\n"
    return res    


"""EJERCICIO 6:
Definir la función mezclar(cadena1, cadena2) que tome dos strings y
devuelva el resultado de intercalar elemento a elemento. Por ejemplo: si
intercalamos Pepe con Jose daría PJeopsee. En el caso de Pepe con Josefa daría
PJeopseefa"""

def mezclar (cadena1: str, cadena2: str) -> str:
    mezclada: str = ""
    i: int = 0
    while (i<len(cadena1) and i<len(cadena2)):
        mezclada+=cadena1[i]+cadena2[i]
        i+=1
    if listaMasLarga(cadena1,cadena2)==cadena1:
        while i<len(cadena1):
              mezclada+=cadena1[i]
              i+=1
    else:
        while i<len(cadena2):
              mezclada+=cadena2[i]
              i+=1
    return mezclada

  

"""EJERCICIO 7
David solicitó un crédito a 30 años para comprar una vivienda, con una tasa fija
nominal anual del 5%. Pidió $500000 al banco y acordó un pago mensual fijo de
$2684,11.
a. Escribir un programa que calcula el monto total que pagará David a lo
largo de los años. Deberías obtener que en total paga $966279.6.
"""
def montoTotal () -> float:
    mes:float=2684.11
    return (mes*(30*12)) 

"""
b. Supongamos que David adelanta pagos extra de $1000/mes durante los
primeros 12 meses de la hipoteca. Modificá el programa para incorporar
estos pagos extra y que imprima el monto total pagado junto con la
cantidad de meses requeridos. Deberías obtener que el pago total es de
$929965.62 en 342 meses.
"""
def pagoRapido () -> str:
    credito:float=500000 #lo que tiene que devolver
    meses:int=0 #la cantidad de meses que le va a llevar
    pagar:float=0 #cuánto pagó
    while credito>0 : #mientras siga debiendo plata
        if meses<12 : #los primeros 12 meses va a pagar 1000 pesos extra
            interes:float=((0.05/12)*credito) #calculo el interes por mes de la tasa fija nominal anual del banco
            pagar+=3684.11 #sumo la cuota mensual
            credito=credito-(3684.11-interes) #la cuota menos lo que se queda el banco, es lo que uso para devolver el crédito
        else:
           interes:float=((0.05/12)*credito)
           pagar+=2684.11
           credito=credito-(2684.11-interes)
        meses+=1
    return "El pago total es de " + str(pagar) + " en " + str(meses) + " meses."          

print(pagoRapido())
"""
c. ¿Cuánto pagaría David si agrega $1000 por mes durante cuatro años,
comenzando en el sexto año de la hipoteca (es decir, luego de 5 años)?
Modificá tu programa de forma que la información sobre pagos extras sea
incorporada de manera versátil. Sugerimos utilizar los parámetros:
pago_extra_monto, pago_extra_mes_comienzo, pago_extra_mes_fin."""

def pagoMasRapido () -> str:
    credito:float=500000 #lo que tiene que devolver
    meses:int=0 #la cantidad de meses que le va a llevar
    pagar:float=0 #cuánto pagó
    while credito>0 : #mientras siga debiendo plata
        if meses>(12*5) and meses < (12*(5+4)) : 
            interes:float=((0.05/12)*credito)
            pagar+=3684.11 
            credito=credito-(3684.11-interes) 
        else:
           interes:float=((0.05/12)*credito)
           pagar+=2684.11
           credito=credito-(2684.11-interes)
        meses+=1
    return "El pago total es de " + str(pagar) + " en " + str(meses) + " meses."  

print(pagoMasRapido())
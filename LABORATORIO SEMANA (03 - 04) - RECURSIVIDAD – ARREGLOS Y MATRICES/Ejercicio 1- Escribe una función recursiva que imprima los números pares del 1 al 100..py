# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 10:22:12 2024

@author: USUARIO
"""

"""1) Ejercicio 1: Escribe una función recursiva que imprima los números pares 
del 1 al 100."""


#Definimos el parametro numero=2 dentro de la función
def imprimir_numeros_pares(numero=2):

#Evaluar si el número e mayor a 1 y si es menor o igual a 100
    if 1 < numero and numero <= 100:

# Imprime el número actual en la misma línea mas un espacio libre
        print(numero, end=" ")

#Llamada recursiva a la función con el siguiente número par (número actual + 2)
        imprimir_numeros_pares(numero+2)
        
#Llamando función imprimir_numeros_pares() para ejecutar
imprimir_numeros_pares()

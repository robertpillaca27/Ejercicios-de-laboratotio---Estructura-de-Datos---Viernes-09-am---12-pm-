# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 04:37:10 2024

@author: USUARIO
"""

#Ejercicio parte 01 – Colas:
#Verificar si una palabra es palíndroma
#1. Implementa una función que determine si una palabra es palíndroma o no. 
#Utiliza una cola para comparar los caracteres de la palabra en orden original y reverso.

# Definición de la función con un parametro palabra
def es_palindroma(palabra):
    
# Iniciamos una lista que funcionará como cola
    cola = []
# Iteramos a través de cada letra en la palabra
    for letra in palabra:
# Añadir cada letra a la cola
        cola.append(letra)

# Mientras exista elementos mayores en la cola
    while len(cola) > 1:
# Comparar el primer y último elemento de la cola
# Si son distintos, la palabra no es palíndroma
        if cola.pop(0) != cola.pop():
            return False
    
# Si todos los caracteres coinciden, la palabra es palíndroma
    return True

# Ingresamos una palabra palindroma.
palabra = str(input('Ingrese un palabra palindroma: '))
if es_palindroma(palabra):
    print(palabra, "es una palabra palíndroma.")
else:
    print(palabra, "no es una palabra palíndroma.")







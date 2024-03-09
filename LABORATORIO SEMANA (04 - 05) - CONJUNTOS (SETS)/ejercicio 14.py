# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 11:36:50 2024

@author: USUARIO
"""

#14. Escriba una función que reciba un conjunto de números y devuelva un 
#conjunto con los números que no están duplicados.

def diferencia(a, b):         
    # Calcula la diferencia entre el conjunto B y el conjunto A
    conjunto_diferencia1 = b.difference(a)  
    # Calcula la diferencia entre el conjunto A y el conjunto B
    conjunto_diferencia2 = a.difference(b)   

    # Devuelve la unión de los dos conjuntos de diferencia
    return conjunto_diferencia1.union(conjunto_diferencia2)

# Conjuntos de números A y B
A = {4, 8, 6, 2, 10, 12, 17, 5}
B = {1, 8, 5, 6, 12, 14, 11, 22}

# Llama a la función diferencia para encontrar la diferencia entre A y B
c = diferencia(A, B)  

# Imprime la diferencia encontrada
print('La diferencia es:', c)

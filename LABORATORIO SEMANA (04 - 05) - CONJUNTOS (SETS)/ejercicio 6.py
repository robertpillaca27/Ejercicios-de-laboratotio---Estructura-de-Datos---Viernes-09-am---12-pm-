# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 11:04:42 2024

@author: USUARIO
"""

#6. Escriba una función que reciba dos conjuntos de números y devuelva un 
#conjunto con los números que están en el segundo conjunto pero no en el primero.

# Definir una función que encuentre la diferencia entre dos conjuntos
def diferencia_entre_conjuntos(conjunto1, conjunto2):
    return conjunto2 - conjunto1  # Utilizar el operador de resta para encontrar la diferencia de los conjuntos

# Definir los conjuntos dados
conjuntoA = {1, 2, 8, 4, 5}
conjuntoB = {3, 4, 5, 1, 9}

# Llamar a la función para encontrar la diferencia entre los conjuntos
diferencia = diferencia_entre_conjuntos(conjuntoA, conjuntoB)

# Imprimir los elementos en el segundo conjunto pero no en el primer conjunto
print("Números en el segundo conjunto pero no en el primero:", diferencia)


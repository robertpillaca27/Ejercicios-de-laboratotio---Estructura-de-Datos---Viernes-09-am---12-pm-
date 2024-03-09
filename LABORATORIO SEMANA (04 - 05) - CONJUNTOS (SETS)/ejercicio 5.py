# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 10:59:45 2024

@author: USUARIO
"""

#5. Escriba una función que reciba dos conjuntos de números y devuelva un 
#conjunto con los números que están en el primer conjunto pero no en el segundo.

# Definir una función que encuentre la diferencia entre dos conjuntos
def diferencia_entre_conjuntos(conjunto1, conjunto2):
    return conjunto1.difference(conjunto2)  # Utilizar el método difference() para encontrar la diferencia de los conjuntos

# Definir los conjuntos dados
conjuntoA = {1, 2, 3, 4, 5, 8001, 89653}
conjuntoB = {3, 4, 5, 6, 7, 7, 8}

# Llamar a la función para encontrar la diferencia entre los conjuntos
diferencia = diferencia_entre_conjuntos(conjuntoA, conjuntoB)

# Imprimir los elementos en el primer conjunto pero no en el segundo conjunto
print("Números en el primer conjunto pero no en el segundo:", diferencia)


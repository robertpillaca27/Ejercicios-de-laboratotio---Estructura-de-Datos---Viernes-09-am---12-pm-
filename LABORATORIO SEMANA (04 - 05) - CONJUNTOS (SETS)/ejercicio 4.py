# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 10:56:34 2024

@author: USUARIO
"""

#4. Escriba una función que reciba dos conjuntos de números y devuelva un 
#conjunto con los números que están en ambos conjuntos.
# Definir una función que encuentre los números comunes entre dos conjuntos
def numeros_comunes(conjunto1, conjunto2):
    return conjunto1.intersection(conjunto2)  # Utilizar el método intersection() para encontrar la intersección de los conjuntos

# Definir los conjuntos dados
conjuntoA = {1, 2, 3, 4, 8, 9, 42, 1, 8}
conjuntoB = {3, 4, 5, 6, 7, 12, 42, 5, 6}

# Llamar a la función para encontrar los números comunes entre los conjuntos
numeros_comunes_resultantes = numeros_comunes(conjuntoA, conjuntoB)

# Imprimir los números comunes encontrados
print("Números comunes en ambos conjuntos:", numeros_comunes_resultantes)


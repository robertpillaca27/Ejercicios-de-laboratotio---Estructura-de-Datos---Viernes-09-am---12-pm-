# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 19:31:42 2024

@author: USUARIO
"""

#Ejercicio 3: Escribe una función que encuentre el elemento máximo de una 
#matriz.

#Importamos la función numpy
import numpy as np

#La matriz principal
matriz = np.array([[1,821,5],[4,6485,8],[225,5,6875],[452,589,584]])

# Definimos la funcion con un parametro: matriz
def encontrar_maximo(matriz):
    
# Utilizar la función numpy.max() para encontrar el máximo
    maximo = np.max(matriz)
    
    return maximo

# Llamamos a la función para encontrar el máximo
maximo_matriz = encontrar_maximo(matriz)

# Imprimir el resultado
print("El elemento máximo de la matriz es:", maximo_matriz)

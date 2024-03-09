# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 19:31:24 2024

@author: USUARIO
"""

#Ejercicio 1: Crea una matriz de números aleatorios de tamaño 100x100.

#Importar la función numpy
import numpy as np

# Definimos el tamaño de la matriz
filas = 100
columnas = 100

# Crear una matriz de números aleatorios entre 0 y 98
# La matriz toma tres argumentos: Valor mínimo, máximo y tamaño de la matriz
matriz_aleatoria = np.random.randint(0, 99, size=(filas, columnas))

# Imprimimos la matriz
print(matriz_aleatoria)


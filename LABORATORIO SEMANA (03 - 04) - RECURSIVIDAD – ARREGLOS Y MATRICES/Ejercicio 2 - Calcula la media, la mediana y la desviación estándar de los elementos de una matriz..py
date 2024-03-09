# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 19:31:28 2024

@author: USUARIO
"""

#Ejercicio 2: Calcula la media, la mediana y la desviación estándar de los 
#elementos de una matriz.

#Importamos la biblioteca Numpy
import numpy as np

# Definir la matriz
matriz = np.array([[56, 7, 9], [2, 5, 7], [5, 1, 9]])

# Calcular la media de la matriz
media_de_matriz = np.mean(matriz)

# Calcular la mediana de la matriz
mediana_de_matriz = np.median(matriz)

# Calcular la desviación estándar de la matriz
desviacion_estandar = np.std(matriz)

# Imprimir los resultados
print('La media de los elementos de la matriz es:', round(media_de_matriz, 2))
print('La mediana de los elementos de la matriz es:', round(mediana_de_matriz, 2))
print('La desviación estándar de los elementos de la matriz es:', round(desviacion_estandar, 2))


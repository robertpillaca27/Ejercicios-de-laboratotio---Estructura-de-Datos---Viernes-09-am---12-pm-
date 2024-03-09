# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 19:31:43 2024

@author: USUARIO
"""

#Ejercicio 5: Escribe una función que encuentre la matriz de covarianza de 
#dos matrices

#Importamos la función numpy
import numpy as np

#Definimos la función con dos parametros
def covarianza_matrices(matriz1, matriz2):
 
# Verificar que las matrices tengan la misma longitud
    if len(matriz1) != len(matriz2):
        raise ValueError("Las matrices deben tener la misma longitud")

# Calcular las medias de las columnas para cada matriz
    media_matriz1 = np.mean(matriz1, axis=0)
    media_matriz2 = np.mean(matriz2, axis=0)

# Restar las medias de las columnas a cada elemento de la matriz
    matriz1_cent = matriz1 - media_matriz1
    matriz2_cent = matriz2 - media_matriz2

# Calcular la matriz de covarianza
    covarianza = np.dot(matriz1_cent.T, matriz2_cent) / (len(matriz1) - 1)

    return covarianza

# Ejemplo de usO con dos matrices
matrizA = np.array([[1, 5, 8], [8, 9, 6], [7, 2, 9]])
matrizB = np.array([[8, 8, 5], [1, 5, 4], [3, 3, -1]])

matriz_covarianza = covarianza_matrices(matrizA, matrizB)

#Imprimir la matriz de covarianza
print("Matriz de Covarianza:")
print(matriz_covarianza)

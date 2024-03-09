# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 18:49:48 2024

@author: USUARIO
"""

#Ejercicio 10 - Suma dos matrices de diferentes tamaños.

# Definir dos matrices de diferentes tamaños
import numpy as np

# Definir dos matrices de diferentes tamaños
matrizA = np.array([[10, 21],
                     [30, 40]])

matrizB = np.array([[51,16, 7],
                     [80,29, 10]])

# Obtener las dimensiones de ambas matrices con atributo .shape
filasA, columnasA = matrizA.shape
filasB, columnasB = matrizB.shape

# Nueva matriz con la suma de las matrices, rellenado con ceros
suma_matrices = np.zeros((max(filasA, filasB), max(columnasA, columnasB)))

# Sumar las matrices en la esquina superior izquierda
suma_matrices[:filasA, :columnasA] += matrizA
suma_matrices[:filasB, :columnasB] += matrizB

# Imprimir el resultado
print("Matriz A:")
print(matrizA)
print("\nMatriz B:")
print(matrizB)
print("\nResultado de la suma ajustada:")
print(suma_matrices)
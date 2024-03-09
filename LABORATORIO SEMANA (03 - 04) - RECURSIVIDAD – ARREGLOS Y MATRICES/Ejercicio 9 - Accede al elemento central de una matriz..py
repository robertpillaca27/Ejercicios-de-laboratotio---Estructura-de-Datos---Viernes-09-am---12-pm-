# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 18:28:06 2024

@author: USUARIO
"""

#Ejercicio 9 - Accede al elemento central de una matriz.

#Importar la función numpy
import numpy as np

# Definir una matriz
matriz = np.array([[11, 25, 36,18,17],
                   [48, 51, 60,56,12],
                   [71, 89, 95,51,11],
                   [71, 89, 59,41,13],
                   [80, 23, 16,47,91]])

# Calcular las coordenadas del elemento central con el atributo matriz.shape
filas, columnas = matriz.shape
fila_central, columna_central = filas //2 , columnas // 2

# Accediendo al elemento central
elemento_central = matriz[fila_central, columna_central]

# Imprimir el resultado
print(f"Elemento central: {elemento_central}")

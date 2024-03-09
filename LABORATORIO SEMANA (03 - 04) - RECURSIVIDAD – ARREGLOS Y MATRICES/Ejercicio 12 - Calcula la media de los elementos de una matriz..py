# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 19:23:12 2024

@author: USUARIO
"""

#Ejercicio 12 - Calcula la media de los elementos de una matriz.

import numpy as np

matriz = np.array([[1,8,9],[2,5,6],[4,8,9]])

media_de_matriz = np.mean(matriz)
print('La media de los elementos de la matriz es: ', round(media_de_matriz,2))
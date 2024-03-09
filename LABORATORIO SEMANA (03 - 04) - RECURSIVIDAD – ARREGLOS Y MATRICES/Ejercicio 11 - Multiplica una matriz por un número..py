# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 19:15:27 2024

@author: USUARIO
"""

#Ejercicio 11 - Multiplica una matriz por un número

#Importamos la función numpy
import numpy as np

# Definimos una matriz
matriz = np.array([[1, 7, 10],
                   [4, 15, 6],
                   [71, 7, 9]])

# Ingresar número por el cual multiplicar la matriz
numero = int(input("Ingrese número a multiplicar: "))

# Multiplicar la matriz por el número
respuesta = numero * matriz

# Imprimir el resultado
print("Matriz inicial:")
print(matriz)
print("\nEl resultado de la multiplicación:")
print(respuesta)

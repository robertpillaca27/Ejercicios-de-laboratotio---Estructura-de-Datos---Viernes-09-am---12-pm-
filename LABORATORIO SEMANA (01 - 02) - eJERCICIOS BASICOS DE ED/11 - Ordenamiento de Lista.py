# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 23:31:32 2024

@author: USUARIO
"""

"""Ordenamiento de Lista:
11) Ordena una lista de números ingresados por el usuario de menor a mayor."""

    # Solicitar al usuario que ingrese una lista de números separados por comas
lista_numeros = input("Ingrese una lista de números separados por comas: ")

# Convertir la cadena de entrada en una lista de enteros utilizando una comprensión de lista y el método split(",")
numeros = [int(numero) for numero in lista_numeros.split(",")]

# Ordenar la lista de números de menor a mayor
numeros.sort()

# Imprimir la lista ordenada
print("Lista ordenada de menor a mayor:", numeros)

   

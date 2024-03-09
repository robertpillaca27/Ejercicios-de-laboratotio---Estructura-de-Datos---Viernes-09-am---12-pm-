# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 11:26:21 2024

@author: USUARIO
"""

#11. Escriba una función que reciba un conjunto de números y devuelva un 
#conjunto con los números que están ordenados de menor a mayor.

# Definición de la función que ordena una lista de números
def numeros_ordenados(lista_numeros):
    # Utiliza la función sorted() para ordenar la lista de números
    lista_ordenada = sorted(lista_numeros)
    # Devuelve la lista ordenada
    return lista_ordenada

# Conjunto de números desordenados
conjunto_numeros = {7, 1, 0, -1, 5, -12, 70, 61, 51, -31, 5}
# Convierte el conjunto a una lista y llama a la función para ordenarla
lista_ordenada = numeros_ordenados(list(conjunto_numeros))
# Imprime la lista ordenada
print("Lista de números ordenados:", lista_ordenada)


# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 11:28:11 2024

@author: USUARIO
"""

#12. Escriba una función que reciba un conjunto de números y devuelva
#un conjunto con los números que están ordenados de mayor a menor.

# Definición de la función que ordena una lista de números en orden descendente
def numeros_ordenados_desc(lista_numeros):
    # Utiliza la función sorted() para ordenar la lista de números en orden descendente
    lista_ordenada_desc = sorted(lista_numeros, reverse=True)
    # Devuelve la lista ordenada en orden descendente
    return lista_ordenada_desc

# Conjunto de números desordenados
conjunto_numeros = {-10, 6, 35, -5, 8, 72, 17, 3, 6, 0}
# Convierte el conjunto a una lista y llama a la función para ordenarla de mayor a menor
lista_ordenada_desc = numeros_ordenados_desc(list(conjunto_numeros))
# Imprime la lista ordenada de mayor a menor
print("Lista de números ordenados de mayor a menor:", lista_ordenada_desc)

# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 11:52:33 2024

@author: USUARIO
"""

#19. Escriba una función que reciba un conjunto de números y devuelva un
#conjunto con los números que están ordenados de menor a mayor y que no están duplicados.

def numeros_ordenados_no_duplicados(conjunto_numeros):
    # Ordena los números del conjunto y los convierte en una lista
    lista_ordenada = sorted(conjunto_numeros)
    # Convierte la lista ordenada en un conjunto para eliminar los duplicados
    conjunto_ordenado_no_duplicados = set(lista_ordenada)
    # Devuelve el conjunto de números ordenados y sin duplicados
    return conjunto_ordenado_no_duplicados

# Conjunto de números de entrada, que puede contener duplicados
conjunto_numeros = {7, 0, 1, -9, 51, 91, 2, 6, 5, 2, 5}

# Llama a la función para obtener el conjunto de números ordenados y sin duplicados
ordenado_no_duplicados = numeros_ordenados_no_duplicados(conjunto_numeros)

# Imprime el conjunto de números ordenados y sin duplicados
print("Conjunto de números ordenados y sin duplicados:", ordenado_no_duplicados)


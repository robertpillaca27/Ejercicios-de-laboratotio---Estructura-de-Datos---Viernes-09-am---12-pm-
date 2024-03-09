# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 11:33:56 2024

@author: USUARIO
"""
#13. Escriba una función que reciba un conjunto de números y devuelva un 
#conjunto con los números que están duplicados.

# Definición de la función que encuentra los números duplicados en un conjunto de números
def numeros_duplicados(conjunto_numeros):
    # Inicialización de un conjunto vacío para almacenar los números duplicados
    conjunto_duplicados = set()
    # Inicialización de un conjunto vacío para almacenar los números que ya hemos visto
    numeros_vistos = set()

    # Iteración sobre cada número en el conjunto de números
    for numero in conjunto_numeros:
        # Verifica si el número ya ha sido visto
        if numero in numeros_vistos:
            # Si el número ya ha sido visto, lo agrega al conjunto de duplicados
            conjunto_duplicados.add(numero)
        else:
            # Si el número no ha sido visto, lo agrega al conjunto de números vistos
            numeros_vistos.add(numero)
    
    # Devuelve el conjunto de números duplicados
    return conjunto_duplicados

# Conjunto de números de entrada que puede contener duplicados
conjunto_numeros = {7, 1, 8, 10, 5, 91, 20, 61, 5, 7, 8}
# Llama a la función para encontrar los números duplicados en el conjunto
duplicados = numeros_duplicados(conjunto_numeros)
# Imprime el conjunto de números duplicados
print("Conjunto de números duplicados:", duplicados)




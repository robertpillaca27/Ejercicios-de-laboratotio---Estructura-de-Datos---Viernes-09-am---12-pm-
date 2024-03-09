# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 11:40:33 2024

@author: USUARIO
"""

#15. Escriba una función que reciba un conjunto de números y devuelva un 
#conjunto con los números que son primos y están ordenados de menor a mayor

# Función para verificar si un número es primo
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Función para generar un conjunto de números primos ordenados
def primos_ordenados(conjunto_numeros):
    # Utiliza un conjunto de comprensión para generar un conjunto de números primos ordenados
    conjunto_primos_ordenados = {numero for numero in sorted(conjunto_numeros) if es_primo(numero)}
    return conjunto_primos_ordenados

# Conjunto de números de entrada
conjunto_numeros = {3, 1, 4, 5, 9, 2, 6, 7, 11}
# Llama a la función para obtener el conjunto de números primos ordenados
resultado_primos_ordenados = primos_ordenados(conjunto_numeros)
# Imprime el conjunto de números primos ordenados
print("Conjunto de números primos ordenados:", resultado_primos_ordenados)


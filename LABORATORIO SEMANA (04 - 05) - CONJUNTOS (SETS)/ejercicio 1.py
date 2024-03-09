# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 10:05:22 2024

@author: USUARIO
"""

#1. Escriba una función que reciba un conjunto de números y devuelva
#un conjunto con los números primos

# Definir una función para verificar si un número es primo
def es_numero_primo(numero):
    # Verificar si el número es menor que 2, ya que los números primos son mayores o iguales a 2
    if numero < 2:
        return False
    # Iterar desde 2 hasta la raíz cuadrada del número
    for i in range(2, int(numero**0.5) + 1):
        # Verificar si el número es divisible por algún número en este rango
        if numero % i == 0:
            return False  # Si es divisible, el número no es primo
    return True  # Si el bucle termina sin encontrar divisores, el número es primo

# Definir una función para encontrar los números primos en un conjunto dado
def numeros_primos(conjunto):
    primos = set()  # Crear un conjunto para almacenar los números primos encontrados
    # Iterar sobre cada número en el conjunto dado
    for num in conjunto:
        # Verificar si el número es primo utilizando la función es_numero_primo
        if es_numero_primo(num):
            primos.add(num)  # Si es primo, agregarlo al conjunto de números primos
    return primos  # Devolver el conjunto de números primos encontrados

# Conjunto de números dado
conjunto_de_numeros = {2, 8, 7, 15, 71, 12, 1200, 45, 7, 89, 51, 1051}
# Encontrar los números primos en el conjunto utilizando la función numeros_primos
conjunto_de_primos = numeros_primos(conjunto_de_numeros)
# Imprimir el conjunto de números primos encontrados
print("El conjunto de los números primos es:", conjunto_de_primos)



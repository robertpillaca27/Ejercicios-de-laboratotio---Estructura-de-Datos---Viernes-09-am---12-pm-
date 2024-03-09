# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 11:42:16 2024

@author: USUARIO
"""

#16. Escriba una función que reciba un conjunto de palabras y devuelva un
# conjunto con las palabras que son palíndromos y están ordenadas de menor a mayor.

# Función para verificar si una palabra es un palíndromo
def es_palindromo(palabra):
    return palabra == palabra[::-1]

# Función para generar un conjunto de palíndromos ordenados
def palindromos_ordenados(conjunto_palabras):
    # Utiliza un conjunto de comprensión para generar un conjunto de palíndromos ordenados
    conjunto_palindromos_ordenados = {palabra for palabra in sorted(conjunto_palabras) if es_palindromo(palabra)}
    return conjunto_palindromos_ordenados

# Conjunto de palabras de entrada
conjunto_palabras = {"ana", "reconocer", "dilema", "nadar", "recorrer"}
# Llama a la función para obtener el conjunto de palíndromos ordenados
resultado_palindromos_ordenados = palindromos_ordenados(conjunto_palabras)
# Imprime el conjunto de palíndromos ordenados
print("Conjunto de palíndromos ordenados:", resultado_palindromos_ordenados)


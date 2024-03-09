# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 11:54:38 2024

@author: USUARIO
"""

#20. Escriba una función que reciba un conjunto de palabras y devuelva un 
#conjunto con las palabras que sonpalíndromos, tienen una longitud determinada 
#y están ordenadas de menor a mayor.

# Función para verificar si una palabra es un palíndromo
def es_palindromo(palabra):
    return palabra == palabra[::-1]

# Función para generar un conjunto de palíndromos de una longitud específica y ordenarlos
def palindromos_longitud_ordenados(conjunto_palabras, longitud):
    # Utiliza un conjunto de comprensión para generar un conjunto de palíndromos de la longitud deseada
    # Los palíndromos se seleccionan si la palabra es un palíndromo y tiene la longitud deseada
    conjunto_palindromos_longitud_ordenados = {
        palabra for palabra in sorted(conjunto_palabras) if es_palindromo(palabra) and len(palabra) == longitud
    }
    # Devuelve el conjunto de palíndromos seleccionados y ordenados
    return conjunto_palindromos_longitud_ordenados

# Conjunto de palabras de entrada
conjunto_palabras = {"tautologia", "reconocer", "ana", "consentimiento", "partido"}

# Longitud deseada ingresada por el usuario
longitud_deseada = int(input("Ingresar longitud deseada: "))

# Llama a la función para obtener el conjunto de palíndromos de la longitud deseada y ordenados
palindromos_longitud_ordenados = palindromos_longitud_ordenados(conjunto_palabras, longitud_deseada)

# Imprime el conjunto de palíndromos seleccionados y ordenados
print(f"Conjunto de palíndromos de longitud {longitud_deseada} ordenados:", palindromos_longitud_ordenados)


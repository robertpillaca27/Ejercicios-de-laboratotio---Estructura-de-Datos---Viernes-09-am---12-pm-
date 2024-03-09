# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 23:40:04 2024

@author: USUARIO
"""

"""Palíndromo:
12) Verifica si una palabra ingresada por el usuario es un palíndromo."""

# Solicitar al usuario que ingrese una palabra
palabra = input("Ingrese una palabra cualquiera: ")

# Eliminar los espacios en blanco de la palabra ingresada
palabra_espaciada = "".join(palabra.split())

# Convertir la palabra sin espacios a minúsculas
palabra_sin_espaciar = palabra_espaciada.lower()

# Verificar si la palabra es un palíndromo comparando la palabra con su reverso
es_palindromo = palabra_sin_espaciar == palabra_sin_espaciar[::-1]

# Imprimir si la palabra ingresada es o no un palíndromo
print(f"{palabra} {'es' if es_palindromo else 'no es'} un palíndromo.")


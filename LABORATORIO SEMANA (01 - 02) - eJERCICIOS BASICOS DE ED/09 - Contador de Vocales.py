# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 23:17:05 2024

@author: USUARIO
"""

"""Contador de Vocales:
9) Cuenta el número de vocales en una cadena de texto."""

# Solicitar al usuario que ingrese una cadena de texto
cadena = input("Ingrese una cadena de texto: ")

# Contar el número de vocales en la cadena utilizando una expresión generadora
numero_vocales = sum(1 for letra in cadena if letra.lower() in 'aeiou')

# Imprimir el resultado
print(f"El número de vocales en la cadena es: {numero_vocales}")

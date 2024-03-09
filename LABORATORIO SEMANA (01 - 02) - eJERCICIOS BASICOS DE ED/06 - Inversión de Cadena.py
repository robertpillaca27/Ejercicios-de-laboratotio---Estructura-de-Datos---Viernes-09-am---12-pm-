# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 21:48:09 2024

@author: USUARIO
"""

'''Inversión de Cadena:
6) Toma una cadena de texto y muestra su inversión'''

# Solicitar al usuario que ingrese una cadena de texto
cadena = input("Ingresa una cadena de texto: ")

# Invertir la cadena ingresada utilizando la técnica de "slicing"
inverso_cadena = cadena[::-1]

# Imprimir la cadena invertida
print(inverso_cadena)

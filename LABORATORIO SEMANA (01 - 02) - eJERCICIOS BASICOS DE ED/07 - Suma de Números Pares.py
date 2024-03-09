# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 22:06:06 2024

@author: USUARIO
"""

"""Suma de Números Pares:
7) Calcula la suma de los números pares en un rango especificado por el usuario."""
    
# Solicitar al usuario que ingrese el número inicial del rango
inicial = int(input("Ingrese el número inicial del rango: "))
# Solicitar al usuario que ingrese el número final del rango
final = int(input("Ingrese el número final del rango: "))

# Calcular la suma de los números pares dentro del rango utilizando una comprensión de lista
suma_pares = sum(numero for numero in range(inicial, final + 1) if numero % 2 == 0)

# Imprimir el resultado
print("La suma de números pares en el rango de:", inicial, "a", final, "es igual:", suma_pares)


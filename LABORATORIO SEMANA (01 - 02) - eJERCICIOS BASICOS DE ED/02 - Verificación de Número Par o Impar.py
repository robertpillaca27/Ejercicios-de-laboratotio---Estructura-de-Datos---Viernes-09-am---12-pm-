# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 20:22:04 2024

@author: USUARIO
"""

"""Verificación de Número Par o Impar:
2) Solicita un número al usuario y determina si es par o impar."""
    
# Solicitar al usuario que ingrese un número
num1 = int(input("Ingresa un número: "))

# Comprobar si el número es divisible por 2 (es decir, si es par)
if num1 % 2 == 0:
    # Si el residuo de la división entre 2 es cero, el número es par
    print("El número es par")
else:
    # Si el residuo de la división entre 2 no es cero, el número es impar
    print("El número es impar")

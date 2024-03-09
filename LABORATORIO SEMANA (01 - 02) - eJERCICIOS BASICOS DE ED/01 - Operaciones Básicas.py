# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 20:06:08 2024

@author: USUARIO
"""

'''Operaciones Básicas:
1) Realiza la suma, resta, multiplicación y división de dos números
ingresados por el usuario.'''


# Solicitar al usuario que ingrese dos números
num1 = int(input("Ingresar un número: "))
num2 = int(input("Ingresar un número: "))

# Realizar operaciones matemáticas con los números ingresados
suma = num1 + num2
resta = num1 - num2
multiplicación = num1 * num2
división = num1 / num2

# Imprimir los resultados de las operaciones
print("La suma de los dos números es:", suma)
print("La resta de los dos números es:", resta)
print("La multiplicación de los dos números es:", multiplicación)
# Redondear el resultado de la división a 2 decimales antes de imprimir
print("La división de los dos números es:", round(división, 2))


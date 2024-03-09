# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 20:30:23 2024

@author: USUARIO
"""

"""Calculadora de Factorial:
4) Crea una función que calcule la factorial de un número."""
    
# Solicitar al usuario que ingrese un número
num1 = int(input("Ingresar un número: "))

# Inicializar la variable para almacenar el factorial
factorial = 1

# Iterar a través de los números desde 1 hasta el número ingresado por el usuario
for i in range(1, num1 + 1):
    # Multiplicar el número actual por el factorial acumulado hasta ahora
    factorial = factorial * i

# Imprimir el factorial calculado
print("El factorial del número", num1, "es igual a:", factorial)

# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 20:49:07 2024

@author: USUARIO
"""

"""Número Primo:
5) Verifica si un número ingresado por el usuario es primo o no."""

def Es_Numero_Primo(num1):
    # Verificar si el número es menor o igual a 1, ya que los números primos son mayores que 1
    if num1 <= 1:
        return False
    # Iterar a través de los números desde 2 hasta la raíz cuadrada del número dado
    for i in range(2, int(num1**0.5) + 1):
        # Verificar si el número es divisible por algún número en este rango
        if num1 % i == 0:
            # Si es divisible, el número no es primo
            return False
    # Si el bucle termina sin encontrar ningún divisor, el número es primo
    return True

# Solicitar al usuario que ingrese un número
num1 = int(input("Ingrese un número cualquiera: "))

# Llamar a la función Es_Numero_Primo para verificar si el número ingresado es primo o no
if Es_Numero_Primo(num1):
    print("El número", num1, "es un número primo.")
else:
    print("El número", num1, "no es un número primo.")




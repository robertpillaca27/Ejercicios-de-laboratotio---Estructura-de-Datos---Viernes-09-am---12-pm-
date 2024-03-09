# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 00:05:26 2024

@author: USUARIO
"""

"""Generador de Tablas de Multiplicar:
13) Crea un programa que genere la tabla de multiplicar de un número ingresado por el usuario."""

    # Solicitar al usuario que ingrese un número
numero = int(input("Ingrese un número: "))

# Imprimir la tabla de multiplicar del número ingresado
print("Tabla de multiplicar del número:", numero)

# Iterar sobre los números del 0 al 11 para calcular los resultados de la multiplicación
for i in range(0, 12):
    resultado = numero * i
    # Imprimir cada resultado de la multiplicación en formato: "numero x i = resultado"
    print(f"{numero} x {i} = {resultado}")


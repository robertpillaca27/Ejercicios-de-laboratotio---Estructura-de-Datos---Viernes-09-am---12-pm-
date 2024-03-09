# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 23:24:17 2024

@author: USUARIO
"""

"""Números de la Serie Fibonacci:
10) Genera los primeros 10 números de la serie Fibonacci."""
    
# Inicializar la lista con los dos primeros números de la serie Fibonacci
fibonacci = [0, 1]

# Iterar para generar los siguientes 8 números de la serie Fibonacci
for _ in range(8):
    siguiente_numero = fibonacci[-1] + fibonacci[-2]  # Calcular el siguiente número sumando los dos últimos números
    fibonacci.append(siguiente_numero)  # Agregar el siguiente número a la lista de Fibonacci

# Imprimir la lista con los primeros 10 números de la serie Fibonacci
print("Los primeros 10 números de la serie Fibonacci son:", fibonacci)

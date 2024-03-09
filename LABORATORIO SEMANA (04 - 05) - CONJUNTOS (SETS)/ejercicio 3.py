# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 10:45:38 2024

@author: USUARIO
"""

#3. Escriba una función que reciba un conjunto de números y devuelva un 
#conjunto con los números que son divisibles por un número determinado.

# Definir una función que encuentre los números divisibles por un divisor dado en un conjunto dado
def numeros_divisibles(conjunto_numeros, divisor):
    numeros_divisibles = set()  # Crear un conjunto vacío para almacenar los números divisibles
    
    # Iterar sobre cada número en el conjunto de números dado
    for numero in conjunto_numeros:
        # Verificar si el número es divisible por el divisor especificado
        if numero % divisor == 0:
            numeros_divisibles.add(numero)  # Si es divisible, agregar el número al conjunto de números divisibles
    
    return numeros_divisibles  # Devolver el conjunto de números divisibles

# Ejemplo de uso:
conjunto_de_numeros = {2, 700, 1201, 1545, 45, 12, 15, 20556658}  # Conjunto de números dado
divisor = int(input("Ingresar un número para ver si es divisible por el conjunto de números:"))  # Solicitar al usuario que ingrese el divisor
# Llamar a la función para encontrar los números divisibles por el divisor en el conjunto de números dado
numeros_divisibles_resultantes = numeros_divisibles(conjunto_de_numeros, divisor)
# Imprimir los números divisibles por el divisor especificado
print(f"Números divisibles por {divisor}:", numeros_divisibles_resultantes)

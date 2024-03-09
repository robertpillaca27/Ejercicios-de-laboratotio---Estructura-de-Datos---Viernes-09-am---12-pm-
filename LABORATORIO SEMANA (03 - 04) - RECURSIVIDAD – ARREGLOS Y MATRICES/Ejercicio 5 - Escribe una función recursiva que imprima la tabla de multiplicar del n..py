# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 16:51:53 2024

@author: USUARIO
"""

'''Ejercicio 5:Escribe una función recursiva que imprima la tabla de 
multiplicar del n.'''

#solicitar al usuario ingresar el numero hasta donde multiplicar
m = int(input('Ingresa el número límite del multiplicador: '))

# Solicitar al usuario que ingrese el valor de n
n = int(input('Ingresar un número para mostrar su tabla de multiplicar: '))

# Define la funcion recursividad de dos variables para imprimir tabla de multiplicar
def imprimir_tabla_multiplicar(n, multiplicador=1):

# Evaluar si el multiplicador actual es menor o igual a 10
    if multiplicador <= m :
        
# Imprimir la multiplicación actual
        print(f"{n} x {multiplicador} = {n * multiplicador}")

# Llamar recursivamente a la función para el siguiente multiplicador
        imprimir_tabla_multiplicar(n, multiplicador + 1)

# Llamar a la función para imprimir la tabla de multiplicar
imprimir_tabla_multiplicar(n)

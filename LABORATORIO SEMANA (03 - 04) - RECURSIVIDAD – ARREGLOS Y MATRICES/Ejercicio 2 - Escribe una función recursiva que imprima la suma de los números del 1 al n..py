# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 11:25:49 2024

@author: USUARIO
"""

'''Ejercicio 2: Escribe una función recursiva que imprima la suma de
 los números del 1 al n.'''
 
# Solicitar al usuario que ingrese un número
numero = int(input('Ingresar un número:'))

# Definir la función recursiva para sumar los números desde 1 hasta n
def suma_numeros(numero = 1):
    
# Caso base: si el número llega a 0, devuelve 0
     if numero == 0:
         return 0
     
# Caso recursivo: sumar el número actual y llamar a la función con el número
# decrementado
     else:
         return numero +suma_numeros(numero-1)
     
# Imprimir el resultado de la suma: suma_numeros(numero)
print(f'la suma de los números de 1 a {numero} es igual a : {suma_numeros(numero)}')


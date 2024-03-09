# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 12:59:22 2024

@author: USUARIO
"""
 
'''Ejercicio 4: Escribe una función recursiva que imprima la pirámide 
de números invertidos del 1 al n.'''


# Solicitar al usuario que ingrese el valor de n
n = int(input("Ingrese un número para la altura de la pirámide invertida: "))

# Defina la función recursiva para imprimir la pirámide invertida
def imprimir_piramide_invertida(n, fila=n,i=0):
    if fila >= 1:
        
# Imprima espacios en blanco para centrar la fila
        print(" " * (n - fila) , "  "*i, end=" ")

# Imprima la fila actual de números invertidos
        print(" ".join(str(i) for i in range(fila, 0, -1)))

# Llamado recursivo a la función para la siguiente fila
        imprimir_piramide_invertida(n, fila - 1)

# Llamado de la función para imprimir la pirámide invertida:
imprimir_piramide_invertida(n)


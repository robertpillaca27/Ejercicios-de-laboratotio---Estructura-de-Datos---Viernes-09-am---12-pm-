# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 12:10:43 2024

@author: USUARIO
"""

'''Ejercicio 3: Escribe una función recursiva que imprima la pirámide de 
números del 1 al n.'''


# Solicita al usuario que introduzca el valor de n
n = int(input("Ingrese un número para la altura de la pirámide: "))

# Definir la función recursiva de 3 parametros, para imprimir la pirámide 
#de números
def imprimir_piramide_numeros(n, fila=1,i=0):
    
# Evaluar si la fila actual es menor o igual a n
    if fila <= n:

# Imprimir espacios en blanco para centrar la fila
        print(" " * (n - fila)," "*i, end="")

# Imprime la fila actual de números
        print(" ".join(str(i) for i in range(1, fila+1)))

# Llamado recursivo de la función para la siguiente fila
        imprimir_piramide_numeros(n, fila + 1)

# Llamar a la función para imprimir la pirámide: imprimir_piramide_numeros(n)
imprimir_piramide_numeros(n)

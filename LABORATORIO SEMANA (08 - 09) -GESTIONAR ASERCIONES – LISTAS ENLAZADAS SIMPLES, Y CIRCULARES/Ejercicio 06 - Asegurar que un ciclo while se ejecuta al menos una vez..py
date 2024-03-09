# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 11:22:15 2024

@author: USUARIO
"""

#6. Asegurar que un ciclo while se ejecuta al menos una vez.

def ejecutar_al_menos_una_vez():
# Inicializa una variable para controlar el bucle
    ejecutar = True 
# Bucle que se ejecuta al menos una vez
    while ejecutar:  
# Solicita al usuario que ingrese su nombre
        entrada = input("Ingrese su nombre: ")  
# Verifica si se ingresó algo (si la cadena no está vacía)
        if entrada:  
 # Imprime un saludo con el nombre ingresado
            print("Hola,", entrada) 
 # Cambia la variable de control para salir del bucle
            ejecutar = False 
        else:
 # Imprime un mensaje de error si no se ingresó nada
            print("Debe ingresar al menos un nombre.") 
# Llama a la función para que solicite al usuario ingresar su nombre al menos una vez
ejecutar_al_menos_una_vez()

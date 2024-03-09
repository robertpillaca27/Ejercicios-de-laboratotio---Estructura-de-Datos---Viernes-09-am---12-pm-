# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 11:16:12 2024

@author: USUARIO
"""

#1. Validar la edad de un usuario.
def validar_edad():
    
# Bucle infinito para solicitar la entrada hasta que sea válida
    while True: 
# Solicita al usuario que ingrese su edad
        entrada = input("Por favor, ingrese su edad: ")  
# Verifica si la entrada no es un número entero
        if not entrada.isdigit(): 
# Imprime un mensaje de error si la entrada no es un número
            print("Por favor, ingrese un número válido.")  
# Continúa solicitando la entrada al usuario
            continue
# Convierte la entrada a un entero
        edad = int(entrada) 
# Verifica si la edad es negativa
        if edad < 0:  
# Imprime un mensaje de error si la edad es negativa
            print("La edad no puede ser un número negativo.") 
# Continúa solicitando la entrada al usuario
            continue
# Verifica si la edad es menor de 18 años
        if edad < 18: 
# Imprime un mensaje de error si la edad es menor de 18 años
            print("Debe ser mayor de edad para continuar.")
# Continúa solicitando la entrada al usuario
            continue 
# Devuelve la edad si es válida
        return edad  

# Ejemplo de uso
# Llama a la función para validar la edad
edad_usuario = validar_edad() 
# Imprime la edad válida obtenida
 
print("Edad válida:", edad_usuario)  





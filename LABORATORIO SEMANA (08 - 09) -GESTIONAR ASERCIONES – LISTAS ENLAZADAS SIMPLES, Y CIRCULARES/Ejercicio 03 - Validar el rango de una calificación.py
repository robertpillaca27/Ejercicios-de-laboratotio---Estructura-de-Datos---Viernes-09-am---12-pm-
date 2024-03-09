# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 11:19:02 2024

@author: USUARIO
"""

#3. Validar el rango de una calificación

def validar_calificacion():
    while True:  # Bucle infinito para continuar solicitando la entrada hasta que sea válida
        entrada = input("Ingrese una calificación: ")  # Solicita al usuario que ingrese una calificación
        try:
            calificacion = float(entrada)  # Intenta convertir la entrada a un número de punto flotante
            if 0 <= calificacion <= 5:  # Verifica si la calificación está en el rango de 0 a 5
                return calificacion  # Devuelve la calificación si es válida
            else:
                print("La calificación debe estar en el rango de 0 a 5")  # Imprime un mensaje de error si la calificación está fuera del rango
        except ValueError:
            print("Ingresa una calificación válida.")  # Imprime un mensaje de error si la entrada no es un número

# Llama a la función para validar la calificación
calificacion_usuario = validar_calificacion()
# Imprime la calificación válida obtenida
print("Calificación válida:", calificacion_usuario)

# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 11:18:17 2024

@author: USUARIO
"""

#9. Escriba una función que reciba un conjunto de palabras y devuelva un 
#conjunto con las palabras que tienen una longitud determinada.

# Definir una función que encuentre las palabras en un conjunto con una longitud específica
def palabras_con_longitud(conjunto_palabras, longitud):
    # Utilizar una comprensión de conjuntos para filtrar las palabras que tienen la longitud deseada
    conjunto_palabras_longitud = {palabra for palabra in conjunto_palabras if len(palabra) == longitud}
    return conjunto_palabras_longitud  # Devolver el conjunto de palabras con la longitud especificada

# Conjunto de palabras dado
conjunto_palabras = {"praxis", "reconocer", "nacionalidad", "nadar", "pito"}

# Solicitar al usuario que ingrese la longitud deseada
longitud_deseada = int(input('Ingresar la longitud deseada: '))

# Encontrar las palabras en el conjunto dado con la longitud deseada
palabras_longitud = palabras_con_longitud(conjunto_palabras, longitud_deseada)

# Imprimir el conjunto de palabras con la longitud deseada
print(f"Conjunto de palabras con longitud {longitud_deseada}:", palabras_longitud)


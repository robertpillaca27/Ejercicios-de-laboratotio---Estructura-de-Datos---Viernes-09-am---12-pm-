# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 11:48:36 2024

@author: USUARIO
"""

#18. Escriba una función que reciba un conjunto de palabras y devuelva un 
#conjunto con las palabras que contienen una letra determinada y están ordenadas de mayor a menor.

def palabras_con_letra_ordenadas(conjunto_palabras, letra):
    # Convierte la letra deseada a minúscula para hacer la comparación insensible a mayúsculas/minúsculas
    letra = letra.lower()  
    
    # Utiliza un conjunto de comprensión para generar un conjunto de palabras que contienen la letra deseada
    # Las palabras se ordenan alfabéticamente en orden descendente usando el parámetro reverse=True en la función sorted()
    conjunto_palabras_con_letra_ordenadas = {
        palabra for palabra in sorted(conjunto_palabras, reverse=True) if letra in palabra.lower()
    }
    
    # Devuelve el conjunto de palabras seleccionadas
    return conjunto_palabras_con_letra_ordenadas

# Conjunto de palabras de entrada
conjunto_palabras = {"tendencia", "urgencia", "retencion", "tenencias", "objeto"}

# Letra deseada ingresada por el usuario
letra_deseada = input("Ingresar letra deseada: ")

# Llama a la función para obtener el conjunto de palabras que contienen la letra deseada, ordenadas de mayor a menor
palabras_con_letra_ordenadas = palabras_con_letra_ordenadas(conjunto_palabras, letra_deseada)

# Imprime el conjunto de palabras seleccionadas
print(f"Conjunto de palabras con la letra '{letra_deseada}' ordenadas de mayor a menor:", palabras_con_letra_ordenadas)




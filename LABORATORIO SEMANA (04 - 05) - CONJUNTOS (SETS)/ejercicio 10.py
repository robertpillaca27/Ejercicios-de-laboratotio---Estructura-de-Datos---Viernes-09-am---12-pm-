# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 11:22:05 2024

@author: USUARIO
"""
#10. Escriba una función que reciba un conjunto de palabras y devuelva un 
#conjunto con las palabras que contienen una letra determinada.

# Definir una función que encuentre las palabras en un conjunto que contienen una letra específica
def palabras_con_letra(conjunto_palabras, letra):
    # Utilizar una comprensión de conjuntos para filtrar las palabras que contienen la letra deseada
    conjunto_palabras_con_letra = {palabra for palabra in conjunto_palabras if letra in palabra}
    return conjunto_palabras_con_letra  # Devolver el conjunto de palabras con la letra especificada

# Conjunto de palabras dado
conjunto_palabras = {"osculo", "dieron", "pasada", "romper", "torcer"}

# Solicitar al usuario que ingrese la letra deseada
letra_deseada = str(input("Ingresar letra deseada: ")).lower()

# Encontrar las palabras en el conjunto dado que contienen la letra deseada
palabras_con_letra = palabras_con_letra(conjunto_palabras, letra_deseada)

# Imprimir el conjunto de palabras con la letra deseada
print(f"Conjunto de palabras con la letra '{letra_deseada}':", palabras_con_letra)


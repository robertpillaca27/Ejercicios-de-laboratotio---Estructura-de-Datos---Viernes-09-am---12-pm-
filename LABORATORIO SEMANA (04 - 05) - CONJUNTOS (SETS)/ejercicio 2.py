# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 10:22:15 2024

@author: USUARIO
"""

#2. Escriba una función que reciba un conjunto de palabras y devuelva un 
#conjunto con las palabras que comienzan con una letra determinada.

# Definir una función que selecciona palabras de un conjunto dado que comienzan con una letra específica
def palabras_con_letra_inicial(conjunto_palabras, letra):
    palabras_seleccionadas = set()  # Crear un conjunto vacío para almacenar las palabras seleccionadas
    
    # Iterar sobre cada palabra en el conjunto de palabras dado
    for palabra in conjunto_palabras:
        # Verificar si la palabra comienza con la letra especificada
        if palabra.startswith(letra):
            palabras_seleccionadas.add(palabra)  # Si comienza con la letra, agregar la palabra al conjunto seleccionado
            
    return palabras_seleccionadas  # Devolver el conjunto de palabras seleccionadas

# Ejemplo de uso:
conjunto_de_palabras = {"pera", "naranja", "plátano", "mandarina", "manzana", "sandía"}  # Conjunto de palabras dado
letra_inicial = str(input('Ingresar letra inicial: ')).lower()  # Solicitar al usuario que ingrese la letra inicial
# Llamar a la función para seleccionar palabras que comienzan con la letra especificada
palabras_seleccionadas = palabras_con_letra_inicial(conjunto_de_palabras, letra_inicial)
# Imprimir las palabras seleccionadas que comienzan con la letra especificada
print("Palabras que comienzan con la letra", letra_inicial + ":", palabras_seleccionadas)

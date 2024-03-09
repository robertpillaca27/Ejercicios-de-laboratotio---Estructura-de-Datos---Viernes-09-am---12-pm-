# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 11:08:54 2024

@author: USUARIO
"""

#7. Escriba una función que reciba un conjunto de palabras y devuelva un 
#conjunto con las palabras que son anagramas.

# Definir una función que verifica si dos palabras son anagramas
def son_anagramas(palabra1, palabra2):
    # Ordenar las letras de ambas palabras y verificar si son iguales
    return sorted(palabra1) == sorted(palabra2)

# Definir una función que encuentra los anagramas en un conjunto de palabras
def anagramas_en_conjunto(conjunto_palabras):
    conjunto_anagramas = set()  # Crear un conjunto vacío para almacenar los anagramas
    
    # Iterar sobre todas las combinaciones únicas de palabras en el conjunto
    for palabra1 in conjunto_palabras:
        for palabra2 in conjunto_palabras:
            # Evitar comparar una palabra consigo misma
            if palabra1 != palabra2:
                # Verificar si las dos palabras son anagramas utilizando la función son_anagramas
                if son_anagramas(palabra1, palabra2):
                    # Agregar las palabras al conjunto de anagramas
                    conjunto_anagramas.add(palabra1)
                    conjunto_anagramas.add(palabra2)
    
    return conjunto_anagramas  # Devolver el conjunto de anagramas encontrados

# Conjunto de palabras dado
conjunto_palabras = {"roma", "amor", "pato", "topa", "perro", "cocodrillo"}

# Encontrar los anagramas en el conjunto de palabras dado
anagramas = anagramas_en_conjunto(conjunto_palabras)

# Imprimir el conjunto de anagramas encontrados
print("Conjunto de anagramas:", anagramas)

# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 11:12:48 2024

@author: USUARIO
"""

#8. Escriba una función que reciba un conjunto de palabras y devuelva un 
#conjunto con las palabras que son palíndromos.
# Definir una función que encuentre los palíndromos en un conjunto de palabras
def son_palindromos(conjunto_palabras):
    # Utilizar una comprensión de conjuntos para filtrar las palabras que son iguales a su inversa
    conjunto_palindromos = {palabra for palabra in conjunto_palabras if palabra == palabra[::-1]}
    return conjunto_palindromos  # Devolver el conjunto de palíndromos

# Conjunto de palabras dado
conjunto_palabras = {"oso", "reconocer", "puntual", "ana", "desarrollo", "reto"}

# Encontrar los palíndromos en el conjunto de palabras dado
palindromos = son_palindromos(conjunto_palabras)

# Imprimir el conjunto de palíndromos encontrados
print("Conjunto de palíndromos:", palindromos)


# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 11:20:17 2024

@author: USUARIO
"""

#4. Asegurar que una lista no esté vacía.
def asegurar_no_vacia(lista):
    if lista:  # Verifica si la lista no está vacía (equivalente a if len(lista) > 0:)
        print("La lista no está vacía.")  # Imprime un mensaje indicando que la lista no está vacía
    else:
        print("La lista está vacía.")  # Imprime un mensaje indicando que la lista está vacía

listaA = [3, 5.6, 8, 16, -1]  # Define una lista no vacía
listaB = []  # Define una lista vacía

# Llama a la función con la lista no vacía
asegurar_no_vacia(listaA) 
 
# Llama a la función con la lista vacía
asegurar_no_vacia(listaB)  


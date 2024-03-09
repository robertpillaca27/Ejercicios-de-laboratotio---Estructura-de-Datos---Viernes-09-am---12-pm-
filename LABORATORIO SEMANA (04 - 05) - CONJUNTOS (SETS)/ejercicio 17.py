# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 11:45:33 2024

@author: USUARIO
"""

#17. Escriba una función que reciba un conjunto de palabras y devuelva un 
#conjunto con las palabras que tienen una longitud determinada y están ordenadas de menor a mayor.

def palabras_con_longitud_ordenadas(conjunto_palabras, longitud):
    if not isinstance(longitud, int) or longitud <= 0:
        return set()  # Devuelve un conjunto vacío si la longitud no es válida
    conjunto_palabras_longitud_ordenadas = {palabra for palabra in sorted(conjunto_palabras) if len(palabra) == longitud}
    return conjunto_palabras_longitud_ordenadas

conjunto_palabras = {"persona", "decidir", "caminar", "levantar", "perfectamente"}

# Solicitar al usuario que ingrese la longitud deseada
longitud_deseada = int(input("Ingresar longitud deseada: "))

resultado_palabras_longitud_ordenadas = palabras_con_longitud_ordenadas(conjunto_palabras, longitud_deseada)
print(f"Conjunto de palabras con longitud {longitud_deseada} ordenadas:", resultado_palabras_longitud_ordenadas)

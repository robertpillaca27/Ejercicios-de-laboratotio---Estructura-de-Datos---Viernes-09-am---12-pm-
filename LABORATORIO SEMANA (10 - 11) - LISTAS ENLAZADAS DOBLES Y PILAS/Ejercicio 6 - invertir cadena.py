# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 04:09:46 2024

@author: USUARIO
"""

#6) invertir cadena
def invertir_cadena(cadena):
    pila = pila()
    
#inicia un bucle que itera sobre cada caracter en la cadena de entrada
    for caracter in cadena: 
#cada caracter de la cadena se apila en la pila
        pila.apilar(caracter)  
#inicializa una cadena vacía que se utilizará para almacenar la cadena invertida
    cadena_invertida = ""
#se inicia un bucle que se ejecutará mientras la pila no esté vacía
    while not pila.esta_vacia():
#se desapila un caracter de la pila y se concatena a la cadena invertida
        cadena_invertida += pila.desapilar() 
    return cadena_invertida
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 04:09:47 2024

@author: USUARIO
"""

#13. Comprobar palindromos:
def es_palindromo(palabra):
    palabra = palabra.replace(" ", "").lower()  
# Se elimina cualquier espacio en blanco y se convierte la palabra a minúsculas.
    pila = Pila()  
    # Se crea una pila para almacenar los caracteres de la palabra.
    for caracter in palabra:  
# Se itera sobre cada caracter en la palabra.
        pila.apilar(caracter)  
# Cada caracter se apila en la pila.
    palabra_invertida = ""  
# Se inicializa una cadena vacía para almacenar la palabra invertida.
    while not pila.esta_vacia():  
# Se inicia un bucle que se ejecuta mientras la pila no esté vacía.
        palabra_invertida += pila.desapilar()  
# Se desapila un caracter de la pila y se agrega a la palabra invertida.
    return palabra == palabra_invertida 
# Se compara la palabra original con la palabra invertida para determinar si es un palíndromo.


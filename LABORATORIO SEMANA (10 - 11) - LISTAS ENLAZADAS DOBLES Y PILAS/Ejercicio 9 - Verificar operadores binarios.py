# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 04:09:46 2024

@author: USUARIO
"""

#9. Verificar operadores binarios.
def verificar_operadores_anidados(expresion):
    pila = Pila()   
#clase Pila para almacenar los paréntesis de la expresión
    for caracter in expresion:   
#inicia un bucle que itera sobre cada caracter
        if caracter == '(':   
#verifica si el caracter es un paréntesis de apertura
            pila.apilar(caracter)   
#se apila en la pila
        elif caracter == ')':  
#verifica si el caracter
            if pila.esta_vacia() or pila.desapilar() != '(':   
#indica que los paréntesis no están correctamente anidados.
                return False
    return pila.esta_vacia()
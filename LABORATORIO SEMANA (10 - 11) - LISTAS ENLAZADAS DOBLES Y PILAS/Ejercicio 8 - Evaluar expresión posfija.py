# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 04:09:46 2024

@author: USUARIO
"""

#8. Evaluar expresión posfija
def evaluar_expresion_posfija(expresion):
    pila = Pila()
#clase Pila para almacenar los operandos
    tokens = expresion.split()  
#crea una lista de cadenas donde cada cadena representa un token individual en la expresión.
    for token in tokens: 
#inicia un bucle que itera sobre cada token en la lista de tokens de la expresión
        if token.isdigit():   
#verifica si el token es un dígito utilizando el método isdigit() de las cadenas
            pila.apilar(float(token))
        elif token in {'+', '-', '*', '/'}:  
#Si el token no es un dígito, se verifica si es uno de los operadores básicos
            operando2 = pila.desapilar()
            operando1 = pila.desapilar()
            if token == '+':
                resultado = operando1 + operando2
            elif token == '-':
                resultado = operando1 - operando2
            elif token == '*':
                resultado = operando1 * operando2
            elif token == '/':
                resultado = operando1 / operando2
            pila.apilar(resultado)
        else:
            raise ValueError("Expresión no válida")
    return pila.desapilar()
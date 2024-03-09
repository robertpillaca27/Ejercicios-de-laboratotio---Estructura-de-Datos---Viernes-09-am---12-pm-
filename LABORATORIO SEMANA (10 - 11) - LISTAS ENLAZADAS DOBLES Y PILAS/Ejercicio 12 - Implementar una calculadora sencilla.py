# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 04:09:47 2024

@author: USUARIO
"""

#12. Implementar una calculadora sencilla:
def calcular_expresion(expresion):
    pila = Pila()  
# Se crea una pila para almacenar los operandos y resultados de la expresión.
    tokens = expresion.split()  
# Se dividen los tokens de la expresión utilizando el espacio como separador.
    for token in tokens: 
# Se itera sobre cada token en la lista de tokens de la expresión.
        if token.isdigit():
# Si el token es un dígito, se convierte a un número de punto flotante y se apila en la pila.
            pila.apilar(float(token))
        elif token in {'+', '-', '*', '/'}:  
# Si el token es un operador, se procede a evaluar la operación correspondiente.
            operando2 = pila.desapilar()  
# Se desapila el segundo operando de la pila.
            operando1 = pila.desapilar()  
# Se desapila el primer operando de la pila.
            if token == '+':  
# Si el operador es suma, se suma los operandos.
                resultado = operando1 + operando2
            elif token == '-':                
# Si el operador es resta, se resta los operandos.
                resultado = operando1 - operando2
            elif token == '*':  
# Si el operador es multiplicación, se multiplica los operandos.
                resultado = operando1 * operando2
            elif token == '/':  
# Si el operador es división, se divide los operandos.
                resultado = operando1 / operando2
            pila.apilar(resultado)  
# El resultado de la operación se apila en la pila.
        else:
            raise ValueError("Expresión no válida")  
# Si el token no es ni un dígito ni un operador, se levanta una excepción.
    return pila.desapilar() 
# Una vez que se han procesado todos los tokens y se ha evaluado la expresión, se devuelve el resultado final.

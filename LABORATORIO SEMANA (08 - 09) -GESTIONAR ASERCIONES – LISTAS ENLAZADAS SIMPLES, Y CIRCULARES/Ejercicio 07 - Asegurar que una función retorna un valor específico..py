# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 11:24:02 2024

@author: USUARIO
"""

#7. Asegurar que una función retorna un valor específico.

def funcion_esperada():
    return 45  # Retorna el valor esperado, que es 45

def asegurar_retorno_valor_especifico():
# Llama a la función esperada
    valor_retornado = funcion_esperada()
# Verifica si el valor retornado es diferente de 42
    if valor_retornado != 42:
 # Lanza una excepción si el valor no es 42
        raise ValueError("La función no retornó el valor esperado.") 

try:
# Llama a la función para asegurar que el valor retornado sea el esperado
    asegurar_retorno_valor_especifico() 
# Imprime un mensaje si la función retorna el valor esperado
    print("La función retornó el valor esperado.")  
except ValueError as error:
# Captura y maneja la excepción si la función no retorna el valor esperado
    print(error)  

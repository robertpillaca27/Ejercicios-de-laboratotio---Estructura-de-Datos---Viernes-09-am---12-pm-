# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 11:24:52 2024

@author: USUARIO
"""

#8. Validar el estado de una variable después de una operación.

# Definimos una variable
numero = 5
numero *= 2

if numero == 11:
    print("El estado de la variable después de la operación es correcto.")
else:
    print("El estado de la variable después de la operación es incorrecto.")

# También podemos usar la afirmación assert para validar el estado de la variable
assert numero == 10, "El estado de la variable después de la operación es incorrecto."

#Imprimimos
print("El estado de la variable después de la operación es correcto.")

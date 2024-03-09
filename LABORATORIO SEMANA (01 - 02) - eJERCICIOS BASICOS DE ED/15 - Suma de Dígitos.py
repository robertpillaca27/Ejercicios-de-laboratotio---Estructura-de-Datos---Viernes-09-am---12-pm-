# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 00:20:08 2024

@author: USUARIO
"""

"""Suma de Dígitos:
15) Toma un número entero y calcula la suma de sus dígitos."""
    
# Solicitar al usuario que ingrese un número entero
numero_entero = int(input("Ingrese un número entero: "))

# Convertir el número entero a una cadena, tomar el valor absoluto y sumar los dígitos convertidos a enteros
suma_digitos = sum(int(digito) for digito in str(abs(numero_entero)))

# Imprimir el resultado de la suma de los dígitos
print(f"La suma de los dígitos de {numero_entero} es: {suma_digitos}")



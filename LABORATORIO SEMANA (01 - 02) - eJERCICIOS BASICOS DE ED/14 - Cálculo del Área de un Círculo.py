# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 00:14:23 2024

@author: USUARIO
"""

"""Cálculo del Área de un Círculo:
14) Pide el radio de un círculo al usuario y calcula su área."""

#Importamos la biblioteca Math

import math
# Solicitar al usuario que ingrese el radio del círculo
radio = int(input("Ingrese el radio del círculo: "))

# Calcular el área del círculo utilizando la fórmula pi * radio^2
area_circulo = radio**2 * math.pi

# Imprimir el resultado del área del círculo
print("El área del círculo es igual a:", area_circulo)


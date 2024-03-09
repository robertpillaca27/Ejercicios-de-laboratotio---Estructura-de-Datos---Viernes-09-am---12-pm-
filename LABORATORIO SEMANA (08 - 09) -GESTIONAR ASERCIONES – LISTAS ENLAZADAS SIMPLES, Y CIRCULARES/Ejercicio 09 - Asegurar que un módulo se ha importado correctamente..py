# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 11:25:50 2024

@author: USUARIO
"""

#9. Asegurar que un módulo se ha importado correctamente.
# mi_modulo.py

def mi_modulo():
# Define una función llamada mi_modulo que imprime un saludo
    print("¡Hola desde mi módulo!")  

try:
# Intenta importar el módulo mi_modulo
    import mi_modulo  
# Establece una bandera para indicar que el módulo se ha importado correctamente
    modulo_importado = True  
except ImportError:
# Establece la bandera en False si el módulo no se puede importar
    modulo_importado = False  
# Verifica si el módulo se ha importado correctamente
if modulo_importado:  
# Verifica si la función está definida en el módulo
    try:
# Intenta acceder a la función mi_modulo dentro del módulo
        if mi_modulo.mi_modulo:
# Imprime un mensaje si la función está disponible
            print("El módulo se ha importado correctamente y la función mi_modulo está disponible.")  
        else:
# Imprime un mensaje si la función no está disponible
            print("El módulo se ha importado correctamente pero la función mi_modulo no está disponible.")  
    except AttributeError:
# Captura una excepción si la función no está definida en el módulo
        print("El módulo se ha importado correctamente pero la función mi_modulo no está disponible.")  
else:
# Imprime un mensaje si el módulo no se ha importado correctamente
    print("El módulo no se ha importado correctamente.")  

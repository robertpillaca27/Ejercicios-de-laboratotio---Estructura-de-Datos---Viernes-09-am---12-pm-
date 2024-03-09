# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 04:09:47 2024

@author: USUARIO
"""

#11. Eliminar duplicados
def eliminar_duplicados_pila(pila):
    elementos_vistos = set()  
# Se crea un conjunto para almacenar los elementos únicos que se han visto.
    pila_temporal = Pila()  
# Se crea una pila temporal para almacenar los elementos únicos.
    while not pila.esta_vacia():  
# Se inicia un bucle para procesar todos los elementos de la pila original.
        elemento = pila.desapilar()  
# Se desapila un elemento de la pila original.
        if elemento not in elementos_vistos:  
# Se verifica si el elemento ya ha sido visto.
            pila_temporal.apilar(elemento)  
# Si el elemento no ha sido visto, se apila en la pila temporal.
            elementos_vistos.add(elemento)  
# Se agrega el elemento al conjunto de elementos vistos para evitar duplicados.
    while not pila_temporal.esta_vacia():  
# Se inicia un bucle para procesar todos los elementos de la pila temporal.
        pila.apilar(pila_temporal.desapilar())  
# Se desapila un elemento de la pila temporal y se apila de nuevo en la pila original.


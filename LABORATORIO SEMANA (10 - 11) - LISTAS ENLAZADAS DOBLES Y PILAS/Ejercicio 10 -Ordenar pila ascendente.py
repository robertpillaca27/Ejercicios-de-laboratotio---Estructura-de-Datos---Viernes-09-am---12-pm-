# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 04:09:46 2024

@author: USUARIO
"""

#10. Ordenar pila ascendente
def ordenar_pila_ascendente(pila):
    pila_temporal = Pila()  
# Se crea una pila temporal para almacenar los elementos durante el proceso de ordenamiento.
    while not pila.esta_vacia():  
# Se inicia un bucle para procesar todos los elementos de la pila original.
        temp = pila.desapilar()  
# Se desapila un elemento de la pila original y se almacena temporalmente en 'temp'.
        while not pila_temporal.esta_vacia() and pila_temporal.ver_tope() > temp:
# Se inicia un bucle interno para desapilar elementos de la pila temporal
# y apilarlos en la pila original hasta que se encuentre un elemento menor o igual que 'temp'.
            pila.apilar(pila_temporal.desapilar())  
# Se apila el elemento desapilado de 'pila_temporal' en la pila original.
        pila_temporal.apilar(temp)  
# Se apila 'temp' en la pila temporal.
    while not pila_temporal.esta_vacia():
# Una vez que se han procesado todos los elementos de la pila original y se han colocado en la pila temporal en orden ascendente,
# se desapilan los elementos de la pila temporal y se apilan de nuevo en la pila original, lo que resulta en una pila ordenada de manera ascendente.
        pila.apilar(pila_temporal.desapilar())
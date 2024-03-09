# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 01:51:53 2024

@author: USUARIO
"""

#Duplicar Nodos:
#1. Crea una lista con al menos 4 nodos, duplica cada nodo de la lista e 
#imprime la lista original y la lista duplicada hacia adelante y hacia atrás.

# Definimos la clase Nodo que representa cada elemento de la lista
class Nodo:
    def __init__(self, valor):
        
 # Inicializamos el nodo con un valor dado
        self.valor = valor 

# Creamos una lista original con nodos x,y
lista_original = [Nodo('x'), Nodo('y'),Nodo("z"),Nodo("w")]

# Duplicamos los nodos en la lista original y creamos nueva lista duplicada directa
# Utilizamos una lista que recorre cada nodo en la lista original y
# agrega dos veces a la lista duplicada
lista_duplicada_directa = sum([[nodo, nodo] for nodo in lista_original], [])

# Duplicamos cada nodo en la lista original y creamos una nueva lista duplicada hacia atrás
# Invertimos la lista original usando slicing y luego aplicamos la misma lógica de duplicación
lista_duplicada_inversa = sum([[nodo, nodo] for nodo in lista_original[::-1]], [])


# creamos un ciclo for para iterar sobre cada lista y otro bucle for anidado
#para imprimir los valores de los nodos en cada lista
for lista, nombre in zip([lista_original, lista_duplicada_directa, lista_duplicada_inversa],
                         ["Original", "Duplicada directa", "Duplicada inversa"]):
    
# Imprimimos el nombre de la lista
    print(f"\nLista {nombre}:")  
    
#Iteramos sobre cada nodo en la lista
    for nodo in lista: 
# Imprimimos el valor del nodo
        print(nodo.valor)  

# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 04:09:44 2024

@author: USUARIO
"""

#Insertar Nodo en Posición Específica:
#3. Crea una lista con al menos 5 nodos, inserta un nuevo nodo con el dato 15 
#en la posición 3 e imprime la lista hacia adelante y hacia atrás.

# Definimos la clase Nodo que representa cada elemento de la lista
class Nodo:
    def __init__(self, valor):
        
# Inicializamos el nodo con un valor dado.
        self.valor = valor 
 # Inicializamos el enlace al siguiente nodo como None
        self.siguiente = None 
# Inicializamos el enlace al nodo anterior como None
        self.anterior = None  

# Función para imprimir la lista hacia adelante
def imprimir_adelante(nodo):
    while nodo:
        print(nodo.valor)  # Imprimimos el valor del nodo actual
        nodo = nodo.siguiente  # Pasamos al siguiente nodo

# Función para imprimir la lista hacia atrás
def imprimir_atras(nodo):
    while nodo:
        print(nodo.valor)  # Imprimimos el valor del nodo actual
        nodo = nodo.anterior  # Pasamos al nodo anterior

# Creamos la lista inicial con al menos 5 nodos utilizando una lista por comprensión
lista_nodos = [Nodo(i) for i in range(1, 6)]

# Insertamos un nuevo nodo con el valor 15 en la posición 3 (índice 2)
# Establece enlaces entre los nodos para mantener la estructura de la lista 
#de doble enlazada

# Creamos un nuevo nodo con valor 15 y lo establecemos como el anterior al nodo en la posición 3
lista_nodos[2].anterior = Nodo(15)
# Establecemos el enlace siguiente del nuevo nodo al nodo en la posición 3  
lista_nodos[2].anterior.siguiente = lista_nodos[2]  
# Establecemos el enlace anterior del nuevo nodo al nodo en la posición 2
lista_nodos[2].anterior.anterior = lista_nodos[1]
# Establecemos el enlace siguiente del nodo en la posición 2 al nuevo nodo  
lista_nodos[1].siguiente = lista_nodos[2].anterior  

# Imprimimos la lista hacia adelante llamando a la función imprimir_adelante
print("Lista hacia adelante:")
imprimir_adelante(lista_nodos[0])

# Imprimimos la lista hacia atrás llamando a la función imprimir_atras
print("\nLista hacia atrás:")
imprimir_atras(lista_nodos[-1])

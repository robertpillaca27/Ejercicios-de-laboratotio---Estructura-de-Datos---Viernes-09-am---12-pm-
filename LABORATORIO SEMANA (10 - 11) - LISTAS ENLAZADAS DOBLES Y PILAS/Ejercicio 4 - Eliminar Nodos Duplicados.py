# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 04:09:45 2024

@author: USUARIO
"""

#Eliminar Nodos Duplicados:
#4. Crea una lista con nodos que contengan datos duplicados, elimina todos los 
#nodos duplicados, dejando solo una instancia de cada dato e imprime la lista 
#hacia adelante y hacia atrás.

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

# Función para imprimir la lista hacia adelante
def imprimir_adelante(nodo):
    while nodo:
        print(nodo.valor)
        nodo = nodo.siguiente

# Función para imprimir la lista hacia atrás
def imprimir_atras(nodo):
    while nodo:
        print(nodo.valor)
        nodo = nodo.anterior

# Función para eliminar nodos duplicados de la lista
def eliminar_duplicados(nodo):
 # Utilizamos un conjunto para rastrear los valores únicos vistos
    valores = set()
    
# Iniciamos desde el primer nodo
    siguiente_nodo = nodo
    while siguiente_nodo:
#Si el valor ya está en el conjunto, es un duplicado
        if siguiente_nodo.valor in valores:  
# Eliminamos el nodo actual
            siguiente_nodo.anterior.siguiente = siguiente_nodo.siguiente  
# Si hay un nodo siguiente
            if siguiente_nodo.siguiente:  
                siguiente_nodo.siguiente.anterior = siguiente_nodo.anterior 
# Actualizamos el enlace del nodo siguiente
        else:
# Agregamos el valor al conjunto
            valores.add(siguiente_nodo.valor)  
# Pasamos al siguiente nodo
        siguiente_nodo = siguiente_nodo.siguiente  

# Creamos la lista con nodos que contienen datos duplicados
lista_nodos = [Nodo(i) for i in [1, 2, 2, 3, 3, 3, 4, 5, 5]]

# Establecemos los enlaces entre los nodos para formar una lista doblemente enlazada
for i in range(len(lista_nodos)):
    if i > 0:
        lista_nodos[i].anterior = lista_nodos[i - 1]
    if i < len(lista_nodos) - 1:
        lista_nodos[i].siguiente = lista_nodos[i + 1]

# Eliminamos los nodos duplicados de la lista
eliminar_duplicados(lista_nodos[0])

# Imprimimos la lista hacia adelante
print("Lista hacia adelante:")
imprimir_adelante(lista_nodos[0])

# Imprimimos la lista hacia atrás
print("\nLista hacia atrás:")
imprimir_atras(lista_nodos[-1])
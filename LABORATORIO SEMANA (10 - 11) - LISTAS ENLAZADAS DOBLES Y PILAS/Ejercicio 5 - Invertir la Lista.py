# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 04:09:46 2024

@author: USUARIO
"""

#Invertir la Lista:
#5. Crea una lista con al menos 6 nodos, invierte el orden de la lista
#(el último elemento se convierte en el 
#primero y viceversa) e imprime la lista hacia adelante y hacia atrás.

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

# Función para invertir la lista
def invertir_lista(nodo):
    ultimo_nodo = None
    while nodo:
        siguiente_nodo = nodo.siguiente
        nodo.siguiente = ultimo_nodo
        nodo.anterior = siguiente_nodo
        ultimo_nodo = nodo
        nodo = siguiente_nodo

# Creamos la lista con al menos 6 nodos
lista_nodos = [Nodo(i) for i in range(1, 7)]

# Establecemos los enlaces entre los nodos para formar una lista doblemente enlazada
for i in range(len(lista_nodos)):
    if i > 0:
        lista_nodos[i].anterior = lista_nodos[i - 1]
    if i < len(lista_nodos) - 1:
        lista_nodos[i].siguiente = lista_nodos[i + 1]

# Invertimos el orden de la lista llamando a la función invertir_lista
invertir_lista(lista_nodos[0])

# Imprimimos la lista hacia adelante
print("Lista invertida hacia adelante:")
imprimir_adelante(lista_nodos[-1])

# Imprimimos la lista hacia atrás
print("\nLista invertida hacia atrás:")
imprimir_atras(lista_nodos[0])



class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0
#apilar
    def apilar(self, item):
        self.items.append(item)
#desapilar
    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
#ver tope
    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]
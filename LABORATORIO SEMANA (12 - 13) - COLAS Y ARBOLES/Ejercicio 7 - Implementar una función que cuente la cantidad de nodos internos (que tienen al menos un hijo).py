# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 04:46:50 2024

@author: USUARIO
"""

#Ejercicios parte 02 - Arboles:
#Contar nodos:
#7. Implementar una función que cuente la cantidad de nodos internos (que tienen al menos
#un hijo).

class Nodo:
    def __init__(self, valor, izquierda=None, derecha=None):

# Inicialización de un nodo con un valor y referencias a sus hijos izquierdo y derecho
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha

def imprimir_nodos_internos(nodo):

# Función para imprimir los nodos internos de un árbol binario
# Si el nodo es None o es una hoja (ambos hijos son None), no hace nada (no imprime nada).
    if nodo is None or (nodo.izquierda is None and nodo.derecha is None):
        return
    else:

# Imprime el valor del nodo actual, ya que no es una hoja (es un nodo interno).
        print(nodo.valor)

# Luego, continúa la búsqueda de manera recursiva en los subárboles izquierdo y derecho.
        imprimir_nodos_internos(nodo.izquierda)
        imprimir_nodos_internos(nodo.derecha)

# Construimos el árbol binario:
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6
nodo4 = Nodo(4)
nodo5 = Nodo(5)
nodo6 = Nodo(6)
nodo2 = Nodo(2, nodo4, nodo5)
nodo3 = Nodo(3, derecha=nodo6)
raiz = Nodo(1, nodo2, nodo3)

# Imprimimos los nodos internos del árbol
imprimir_nodos_internos(raiz)

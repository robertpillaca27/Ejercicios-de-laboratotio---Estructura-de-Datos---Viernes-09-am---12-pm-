# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 04:38:28 2024

@author: USUARIO
"""

#Ejercicios parte 02 - Arboles:
#Contar nodos:
#6. Implementar una función que cuente la cantidad de nodos hoja (que no tienen hijos).

class Nodo:
    def __init__(self, valor):
# Inicialización de un nodo con un valor dado
        self.valor = valor
        self.izquierda = None  
# Referencia al hijo izquierdo
        self.derecha = None  
# Referencia al hijo derecho

def contar_nodos_hoja(nodo):
    if nodo is None:

# Si el nodo es None, no hay nodos hoja
        return 0
    elif nodo.izquierda is None and nodo.derecha is None:

# Si el nodo no tiene hijos, es una hoja y retornamos 1
        return 1
    else:

        # Recursivamente contar nodos hoja en los subárboles izquierdo y derecho
        return contar_nodos_hoja(nodo.izquierda) + contar_nodos_hoja(nodo.derecha)

# Ejemplo para usar en el ejecicio
if __name__ == "__main__":

    # Construimos un árbol de ejemplo
    raiz = Nodo(1)
    raiz.izquierda = Nodo(2)
    raiz.derecha = Nodo(3)
    raiz.izquierda.izquierda = Nodo(4)
    raiz.izquierda.derecha = Nodo(5)
    raiz.derecha.derecha = Nodo(6)

# Contamos la cantidad de nodos hoja en el árbol
    cantidad_hojas = contar_nodos_hoja(raiz)
    print("La cantidad de nodos hoja en el árbol es:", cantidad_hojas)

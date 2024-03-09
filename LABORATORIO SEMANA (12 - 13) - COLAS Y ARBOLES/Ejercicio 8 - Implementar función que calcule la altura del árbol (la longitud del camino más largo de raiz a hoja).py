# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 04:47:41 2024

@author: USUARIO
"""

#Ejercicios parte 02 - Arboles:
#Calcular altura y profundidad:
#8. Implementar una función que calcule la altura del árbol (la longitud del camino más largo desde la raíz 
#hasta una hoja).


class Nodo:
    def __init__(self, valor):

# Inicialización de un nodo con un valor dado y sin hijos
        self.valor = valor
        self.izquierda = None  # Referencia al hijo izquierdo
        self.derecha = None  # Referencia al hijo derecho

class ArbolBinario:
    def __init__(self, raiz=None):

# Inicialización de un árbol binario con una raíz opcional
        self.raiz = raiz

def altura_arbol(nodo):

# Función para calcular la altura de un árbol binario
    if nodo is None:
# Un árbol vacío tiene altura -1
        return -1
    else:

# Calcular la altura de cada subárbol
        altura_izquierda = altura_arbol(nodo.izquierda)
        altura_derecha = altura_arbol(nodo.derecha)
# La altura del árbol es el máximo de las alturas de los subárboles + 1
        return 1 + max(altura_izquierda, altura_derecha)

# Aqui tenemos un caso de uso
if __name__ == "__main__":
    # Crear nodos
    nodo1 = Nodo(1)
    nodo2 = Nodo(2)
    nodo3 = Nodo(3)
    nodo4 = Nodo(4)

# Construir el árbol
    arbol = ArbolBinario(nodo1)
    arbol.raiz.izquierda = nodo2
    arbol.raiz.derecha = nodo3

# Añadir un nivel más para hacer el árbol más interesante
    nodo2.izquierda = nodo4  


# Calcular y mostrar la altura del árbol
    print(f"Altura del árbol {altura_arbol(arbol.raiz)}")


# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 04:48:57 2024

@author: USUARIO
"""

#Ejercicios parte 02 - Arboles:
#Buscar el mínimo y el máximo:
#11. Implementar una función que encuentre el nodo con el valor máximo en el árbol

class Nodo:
    def __init__(self, valor):
        # Inicialización de un nodo con un valor dado y sin hijos
        self.valor = valor

# Referencia al hijo izquierdo
        self.izquierda = None 
        
# Referencia al hijo derecho
        self.derecha = None  

class ArbolBinarioBusqueda:
    def __init__(self, raiz=None):

# Inicialización de un árbol binario de búsqueda con una raíz opcional
        self.raiz = raiz

def encontrar_maximo(nodo):
    """Encuentra el valor máximo en el árbol binario de búsqueda."""
    actual = nodo

# El máximo está en el nodo más a la derecha
    while actual.derecha is not None:
        actual = actual.derecha
    return actual.valor

print("---------------------------- Ejercicio 11 --------------------------")
if __name__ == "__main__":

# Crear nodos y construir el árbol binario de búsqueda como en ejercicios anteriores
    raiz = Nodo(8)
    raiz.izquierda = Nodo(3)
    raiz.derecha = Nodo(10)
    raiz.izquierda.izquierda = Nodo(1)
    raiz.izquierda.derecha = Nodo(6)
    raiz.derecha.derecha = Nodo(14)
    raiz.izquierda.derecha.izquierda = Nodo(4)
    raiz.izquierda.derecha.derecha = Nodo(7)
    raiz.derecha.derecha.izquierda = Nodo(13)

# Crear un árbol binario de búsqueda con la raíz creada
    arbol = ArbolBinarioBusqueda(raiz)
    
# Encontrar el valor máximo en el árbol
    valor_maximo = encontrar_maximo(arbol.raiz)  
    print(f"El valor máximo en el árbol es: {valor_maximo}")

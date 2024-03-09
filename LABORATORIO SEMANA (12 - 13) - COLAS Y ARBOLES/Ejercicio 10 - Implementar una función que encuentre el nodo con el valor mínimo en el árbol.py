# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 04:48:39 2024

@author: USUARIO
"""

#Ejercicios parte 02 - Arboles:
#Buscar el mínimo y el máximo:
#10. Implementar una función que encuentre el nodo con el valor mínimo en el árbol.

class Nodo:
    def __init__(self, valor):

# Inicialización de un nodo con un valor y sin hijos
        self.valor = valor
        
 # Referencia al hijo izquierdo
        self.izquierda = None 

# Referencia al hijo derecho
        self.derecha = None  

class ArbolBinarioBusqueda:
    def __init__(self, raiz=None):

# Inicialización de un árbol binario de búsqueda con una raíz opcional
        self.raiz = raiz

def encontrar_minimo(nodo):
    """Encuentra el valor mínimo en el árbol binario de búsqueda."""
    actual = nodo

# El mínimo está en el nodo más a la izquierda
    while actual.izquierda is not None:
        actual = actual.izquierda
    return actual.valor

print("---------------------------- Ejercicio 10 --------------------------")
if __name__ == "__main__":

# Crear nodos y construir el árbol binario de búsqueda
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
    
# Encontrar el valor mínimo en el árbol
    valor_minimo = encontrar_minimo(arbol.raiz)
    
# Imprimir el valor mínimo
    print(f"El valor mínimo en el árbol es: {valor_minimo}")  

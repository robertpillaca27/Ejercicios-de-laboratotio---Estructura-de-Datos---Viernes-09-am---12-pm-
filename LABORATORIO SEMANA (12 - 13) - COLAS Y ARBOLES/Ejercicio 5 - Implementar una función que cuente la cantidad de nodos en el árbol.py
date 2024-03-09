# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 04:38:27 2024

@author: USUARIO
"""
#Ejercicios parte 02 - Arboles:
#Contar nodos:
#5. Implementar una función que cuente la cantidad de nodos en el árbol.

class Nodo:
    def __init__(self, valor):

# Inicialización de un nodo con un valor dado
        self.valor = valor

# Referencia al hijo izquierdo
        self.izquierda = None 
# Referencia al hijo derecho
        self.derecha = None  

class ArbolBinario:
    def __init__(self, raiz=None):

        # Inicialización de un árbol binario con una raíz opcional
        self.raiz = raiz

def contar_nodos(nodo):

    # Función para contar el número total de nodos en un árbol binario
    if nodo is None:  

# Si el nodo es None (vacío), no hay nodos
        return 0
    else:
# Si el nodo no es None, contamos este nodo y los nodos en sus subárboles izquierdo y derecho
        return 1 + contar_nodos(nodo.izquierda) + contar_nodos(nodo.derecha)

# Ejemplos para usar con el ejercicio
if __name__ == "__main__":
    # Crear nodos
    nodo1 = Nodo(1)
    nodo2 = Nodo(2)
    nodo3 = Nodo(3)

 # Construimos el árbol
# Creamos un árbol binario con nodo1 como raíz
    arbol = ArbolBinario(nodo1)  
    
 # Establecemos nodo2 como hijo izquierdo de la raíz
    arbol.raiz.izquierda = nodo2
# Establecemos nodo3 como hijo derecho de la raíz
    arbol.raiz.derecha = nodo3  

# Mostramos el número total de nodos en el árbol
print(f"Número total de nodos en el árbol {contar_nodos(arbol.raiz)}")

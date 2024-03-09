# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 04:48:12 2024

@author: USUARIO
"""

#Ejercicios parte 02 - Arboles:
#Calcular altura y profundidad:
#9. Implementar una función que calcule la profundidad de un nodo (la longitud del camino desde la raíz 
#hasta el nodo).

class Nodo:
    def __init__(self, valor):

# Inicialización de un nodo con un valor dado y sin hijos
        self.valor = valor

# Referencia al hijo izquierdo
        self.izquierda = None 
# Referencia al hijo derecho
        self.derecha = None  

class ArbolBinario:
    def __init__(self, raiz=None):

# Inicialización de un árbol binario con una raíz opcional
        self.raiz = raiz

def profundidad_nodo(nodo, valor, profundidad_actual=0):
    if nodo is None:
        
# Si el nodo es None, el valor no se encuentra en el árbol
        return -1
    elif nodo.valor == valor:
        
# Si el valor del nodo actual es igual al valor buscado, retorna la profundidad actual
        return profundidad_actual
    else:
# Buscar el valor en los subárboles, incrementando la profundidad
        profundidad_izquierda = profundidad_nodo(nodo.izquierda, valor, profundidad_actual + 1)
        profundidad_derecha = profundidad_nodo(nodo.derecha, valor, profundidad_actual + 1)
        
# Si el valor no se encuentra en el subárbol izquierdo, retorna el resultado del derecho y viceversa
        if profundidad_izquierda != -1:
            return profundidad_izquierda
        else:
            return profundidad_derecha

# Tenemos el ejemplo de caso de uso
if __name__ == "__main__":
    
    
# Crear nodos y construir el árbol como en ejemplos anteriores
    nodo1 = Nodo(1)
    nodo2 = Nodo(2)
    nodo3 = Nodo(3)
    nodo4 = Nodo(4)
    
    arbol = ArbolBinario(nodo1)
    arbol.raiz.izquierda = nodo2
    arbol.raiz.derecha = nodo3

# Añadir un nivel más
    nodo2.izquierda = nodo4  

    valor_a_buscar = 4
    profundidad = profundidad_nodo(arbol.raiz, valor_a_buscar)
    if profundidad != -1:

# Si se encontró la profundidad del nodo con el valor buscado, imprimir la profundidad
        print(f"La profundidad del nodo con valor {valor_a_buscar} es: {profundidad}")
    else:

        # Si el valor no se encuentra en el árbol, imprimir un mensaje indicando esto
        print(f"El valor {valor_a_buscar} no se encuentra en el árbol.")








































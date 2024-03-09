# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 09:40:30 2024

@author: USUARIO
"""
#10. Desarrollar el código de buscar nodo en la lista enlazada simple.
class Nodo:
    def __init__(self, dato):
        self.dato = dato  # Inicializa el dato del nodo
# Inicializa el puntero al siguiente nodo como None
        self.siguiente = None  

class ListaEnlazada:
    def __init__(self):
# Inicializa la cabeza de la lista enlazada como None
        self.cabeza = None  

    def buscar_nodo(self, dato):
# Inicia desde la cabeza de la lista
        actual = self.cabeza  
# Itera sobre la lista hasta el final
        while actual is not None:  
# Comprueba si el dato del nodo actual coincide con el dato buscado
            if actual.dato == dato:
# Retorna el nodo si se encuentra
                return actual  
# Avanza al siguiente nodo
            actual = actual.siguiente  
# Retorna None si el dato no se encuentra en la lista
        return None  

# Creamos algunos nodos
nodo1 = Nodo(1)
nodo2 = Nodo([1,2])
nodo3 = Nodo(3)

# Creamos una lista enlazada y agregamos los nodos
lista = ListaEnlazada()
lista.cabeza = nodo1
nodo1.siguiente = nodo2
nodo2.siguiente = nodo3

# Solicitamos al usuario ingresar un dato a buscar
dato_buscado = input("Ingrese dato a buscar: ")

# Buscamos el nodo con el dato proporcionado en la lista
nodo_encontrado = lista.buscar_nodo(dato_buscado)

# Imprimimos si se encontró el nodo con el dato buscado o no
if nodo_encontrado:
    print(f"Se encontró un nodo con el dato {dato_buscado}.")
else:
    print(f"No se encontró ningún nodo con el dato {dato_buscado}.")

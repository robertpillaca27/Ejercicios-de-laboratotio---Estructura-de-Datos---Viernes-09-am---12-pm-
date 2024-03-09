# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 09:40:39 2024

@author: USUARIO
"""
#Longitud de la Lista
#12. Crea una función que devuelva la longitud de una lista enlazada simple.
#Concatenar Listas

# Definición de la clase Nodo que representa un nodo individual en la lista enlazada
class Nodo:
# Constructor que inicializa el nodo con un dato dado y un enlace al siguiente nodo (que inicialmente es None)
    def __init__(self, dato):
# Almacena el dato del nodo
        self.dato = dato
 # Inicialmente no hay ningún nodo siguiente
        self.siguiente = None 

# Definición de la clase ListaEnlazada que representa la lista enlazada en su conjunto
class ListaEnlazada:
# Constructor que inicializa la lista enlazada con una cabeza vacía (None)
    def __init__(self):
 # La cabeza de la lista enlazada inicialmente es None
        self.cabeza = None 

# Método para agregar un nuevo nodo al final de la lista enlazada
    def agregar_nodo(self, dato):
# Crea un nuevo nodo con el dato dado
        nuevo_nodo = Nodo(dato)
# Si la lista está vacía
        if not self.cabeza:  
# El nuevo nodo se convierte en la cabeza de la lista
            self.cabeza = nuevo_nodo  
        else:  # Si la lista no está vacía
# Comienza desde la cabeza de la lista
            actual = self.cabeza 
# Avanza hasta el último nodo de la lista
            while actual.siguiente:  
                actual = actual.siguiente
# Agrega el nuevo nodo al final de la lista
            actual.siguiente = nuevo_nodo  

# Método para calcular la longitud de la lista enlazada (cantidad de nodos)
    def longitud(self):
# Inicializa la longitud de la lista en 0
        longitud = 0
# Comienza desde la cabeza de la lista
        actual = self.cabeza
# Itera sobre todos los nodos de la lista
        while actual:  
# Incrementa la longitud por cada nodo encontrado
            longitud += 1
# Avanza al siguiente nodo
            actual = actual.siguiente  
# Devuelve la longitud total de la lista
        return longitud  

# Ejemplo de uso
# Crea una instancia de la lista enlazada
lista = ListaEnlazada()  

# Agregamos algunos nodos a la lista
lista.agregar_nodo(8)
lista.agregar_nodo(5)

# Calculamos la longitud de la lista enlazada
longitud = lista.longitud()

# Imprimimos la longitud de la lista enlazada
print("La longitud de la lista enlazada es:", longitud)

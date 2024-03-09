# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 09:40:38 2024

@author: USUARIO
"""
#Suma de Nodos
#11. Implementa una función que sume todos los nodos de una lista enlazada simple.

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
# Si la lista no está vacía
        else: 
# Comienza desde la cabeza de la lista
            actual = self.cabeza  
            while actual.siguiente:  
# Avanza hasta el último nodo de la lista
                actual = actual.siguiente
# Agrega el nuevo nodo al final de la lista
            actual.siguiente = nuevo_nodo  

# Método para calcular la suma de los valores almacenados en todos los nodos de la lista enlazada
    def suma_nodos(self):
# Inicializa la variable suma
        suma = 0  
# Comienza desde la cabeza de la lista
        actual = self.cabeza  
# Itera sobre todos los nodos de la lista
        while actual:  
# Agrega el valor del nodo actual a la suma
            suma += actual.dato
# Avanza al siguiente nodo
            actual = actual.siguiente()
# Devuelve la suma total de los valores de los nodos
        return suma  

# Creación de una instancia de ListaEnlazada
lista = ListaEnlazada()

# Agregamos algunos nodos a la lista
lista.agregar_nodo(1)
lista.agregar_nodo(15)
lista.agregar_nodo(3)
lista.agregar_nodo(4)

# Calculamos la suma de los valores de los nodos en la lista enlazada
suma_total = lista.suma_nodos()

# Imprimimos la suma total
print("La suma de los nodos en la lista enlazada es:", suma_total)

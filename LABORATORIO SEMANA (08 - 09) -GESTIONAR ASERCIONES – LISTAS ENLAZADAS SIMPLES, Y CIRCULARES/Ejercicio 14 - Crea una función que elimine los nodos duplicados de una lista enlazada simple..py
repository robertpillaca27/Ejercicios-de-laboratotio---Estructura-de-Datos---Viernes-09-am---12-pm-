# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 11:09:46 2024

@author: USUARIO
"""

#Eliminar Duplicados
#14. Crea una función que elimine los nodos duplicados de una lista enlazada simple.

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_nodo(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def eliminar_duplicados(self):
        if not self.cabeza:
            return

        valores_vistos = set([self.cabeza.dato])
        actual = self.cabeza

        while actual.siguiente:
            if actual.siguiente.dato in valores_vistos:
                actual.siguiente = actual.siguiente.siguiente
            else:
                valores_vistos.add(actual.siguiente.dato)
                actual = actual.siguiente
                
lista = ListaEnlazada()
lista.agregar_nodo(1)
lista.agregar_nodo(2)
lista.agregar_nodo(3)
lista.agregar_nodo(2)
lista.agregar_nodo(4)
lista.agregar_nodo(1)

print("Lista original:")
actual = lista.cabeza
while actual:
    print(actual.dato, end=" -> ")
    actual = actual.siguiente
print("None")

lista.eliminar_duplicados()

print("\nLista después de eliminar duplicados:")
actual = lista.cabeza
while actual:
    print(actual.dato, end=" -> ")
    actual = actual.siguiente
print("None")


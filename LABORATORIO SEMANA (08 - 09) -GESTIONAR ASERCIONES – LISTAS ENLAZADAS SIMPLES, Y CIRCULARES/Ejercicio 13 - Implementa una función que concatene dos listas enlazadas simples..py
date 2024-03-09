# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 11:09:45 2024

@author: USUARIO
"""
#Concatenar Listas
#13. Implementa una función que concatene dos listas enlazadas simples.

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

def concatenar_listas(lista1, lista2):
    if not lista1.cabeza:
        lista1.cabeza = lista2.cabeza
    else:
        actual = lista1.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = lista2.cabeza

# Ejemplo de uso
lista1 = ListaEnlazada()
lista1.agregar_nodo(1)
lista1.agregar_nodo(2)
lista1.agregar_nodo(3)

lista2 = ListaEnlazada()
lista2.agregar_nodo(4)
lista2.agregar_nodo(5)
lista2.agregar_nodo(6)

# Concatenar las listas
concatenar_listas(lista1, lista2)

actual = lista1.cabeza
while actual:
    print(actual.dato, end=" -> ")
    actual = actual.siguiente
print("None")

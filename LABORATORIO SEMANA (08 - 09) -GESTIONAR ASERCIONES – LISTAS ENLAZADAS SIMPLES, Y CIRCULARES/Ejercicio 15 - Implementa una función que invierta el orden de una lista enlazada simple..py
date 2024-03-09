# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 11:14:40 2024

@author: USUARIO
"""
#Invertir Lista
#15. Implementa una función que invierta el orden de una lista enlazada simple.

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

    def invertir(self):
        anterior = None
        actual = self.cabeza
        siguiente = None
        while actual:
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente
        self.cabeza = anterior

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

# Ejemplo de uso
lista = ListaEnlazada()
lista.agregar_nodo(1)
lista.agregar_nodo(2)
lista.agregar_nodo(3)
lista.agregar_nodo(4)

print("Lista original:")
lista.mostrar()

lista.invertir()

print("\nLista invertida:")
lista.mostrar()


# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 04:08:53 2024

@author: USUARIO
"""

#Contar Nodos Pares e Impares:
#2. Crea una lista con al menos 9 nodos, cuenta cuántos nodos tienen un dato 
#par y cuántos tienen un dato impar e imprime la lista hacia adelante y hacia atrás.

# Definimos la clase Nodo que representa cada elemento de la lista.
class Nodo:
    def __init__(self, valor):
        
 # Inicializamos el nodo con un valor dado
        self.valor = valor 

# Creamos lista con al menos 9 nodos utilizando una lista por comprensión
lista_nodos = [Nodo(i) for i in range(1, 10)]

# Inicializa contadores para nodos: pares e impares
contador_pares = 0
contador_impares = 0

# Recorre la lista de nodos para contar cuántos tienen un valor par e impar
for nodo in lista_nodos:

# Si el valor del nodo es par
    if nodo.valor % 2 == 0: 
        
# Incrementamos el contador de nodos pares
        contador_pares += 1 
        
# Si no, incrementamos el contador de nodos impares
    else:
        contador_impares += 1

# Imprimimos la lista hacia adelante
print("Lista hacia adelante:")
for nodo in lista_nodos:
    
# Imprimimos el valor de cada nodo
    print(nodo.valor)  

# Imprimimos lista hacia atrás utilizando la función reversed() para invertir la lista
print("\nLista hacia atrás:")
for nodo in reversed(lista_nodos):
    
# Imprimimos el valor de cada nodo en orden inverso
    print(nodo.valor)  

# Imprimimos el conteo de nodos pares e impares
print(f"\nNúmero de nodos pares: {contador_pares}")
print(f"Número de nodos impares: {contador_impares}")
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 04:37:56 2024

@author: USUARIO
"""
#Ejercicio parte 01 – Colas:
#Diseño de un sistema de gestión de pedidos
#2. Crea un sistema de gestión de pedidos que utilice una cola para procesar los pedidos
#en el orden en que fueron recibidos. Implementa funciones para agregar pedidos, procesar
#pedidos y mostrar el estado actual de la cola.

class SistemaGestionPedidos:
    def __init__(self):

# Inicializaciamos la cola de pedidos como una lista vacía
        self.cola_pedidos = []

    def agregar_pedido(self, pedido):

# Agrega un pedido a la cola de pedidos
        self.cola_pedidos.append(pedido)

    def procesar_pedido(self):

# Verifica si hay pedidos en la cola
        if self.cola_pedidos:  

# Si hay pedidos, saca y procesa el primero de la lista
            print(f"Procesando pedido: {self.cola_pedidos.pop(0)}")
        else:

# Si no hay pedidos, muestra un mensaje
            print("No hay pedidos pendientes.")

    def mostrar_estado_cola(self):
        if self.cola_pedidos:  # Verifica si hay pedidos en la cola
            # Si hay pedidos, muestra todos los pedidos en la cola
            print("Pedidos pendientes:", *self.cola_pedidos)
        else:
            # Si no hay pedidos, muestra un mensaje
            print("No hay pedidos pendientes.")

# Ejemplos para usar
sistema = SistemaGestionPedidos()
sistema.agregar_pedido("Mate")
sistema.agregar_pedido("Café")
sistema.agregar_pedido("Leche")

# Muestra el estado actual de la cola
sistema.mostrar_estado_cola()  

 # Procesa el primer pedido
sistema.procesar_pedido() 

# Muestra el estado actual de la cola
sistema.mostrar_estado_cola()  

# Procesa el siguiente pedido
sistema.procesar_pedido()  

# Muestra el estado actual de la cola
sistema.mostrar_estado_cola()  

# Procesa el siguiente pedido
sistema.procesar_pedido()  

 # Muestra el estado actual de la cola
sistema.mostrar_estado_cola() 

# Intenta procesar un pedido cuando no hay ninguno en la cola
sistema.procesar_pedido()  

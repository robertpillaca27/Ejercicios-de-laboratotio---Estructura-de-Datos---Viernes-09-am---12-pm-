# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 04:38:26 2024

@author: USUARIO
"""
#Ejercicio parte 01 – Colas:
#Diseño de un sistema de gestión de tareas (Avanzado)
#4. Implementa un sistema de gestión de tareas que permita agregar tareas, marcar 
#tareas como completadas y mostrar la próxima tarea pendiente.

class SistemaGestionTareas:
    def __init__(self):

# Inicialización de la lista de tareas vacía
        self.tareas = []

    def agregar_tarea(self, tarea):

# Método para agregar una nueva tarea a la lista de tareas
        self.tareas.append({"descripcion": tarea, "completada": False})

    def marcar_completada(self, indice):
        
# Método para marcar una tarea como completada, dado su índice en la lista
        if 0 <= indice < len(self.tareas):

            # Verifica que el índice sea válido
            self.tareas[indice]["completada"] = True
        else:
            print("Índice de tarea inválido.")
# Método para mostrar la próxima tarea pendiente en la lista de tareas
    def mostrar_proxima_pendiente(self):

# Itera sobre todas las tareas
        for tarea in self.tareas: 

# Verifica si la tarea no está completada
            if not tarea["completada"]:  
                print("Próxima tarea pendiente:", tarea["descripcion"])
# Termina el método después de mostrar la próxima tarea pendiente
                return  
 # Mensaje si no hay tareas pendientes
        print("No hay tareas pendientes.") 

# Ejemplos para usar
sistema = SistemaGestionTareas()
sistema.agregar_tarea("Completar informe")
sistema.agregar_tarea("Presentar monografía")
sistema.agregar_tarea("Preparar presentación")

 # Muestra la próxima tarea pendiente
sistema.mostrar_proxima_pendiente() 

 # Marca la primera tarea como completada
sistema.marcar_completada(0) 

 # Muestra la próxima tarea pendiente
sistema.mostrar_proxima_pendiente() 

# Marca la segunda tarea como completada
sistema.marcar_completada(1)  

# Muestra la próxima tarea pendiente
sistema.mostrar_proxima_pendiente()  

# Marca la tercera tarea como completada
sistema.marcar_completada(2)  

# Muestra la próxima tarea pendiente
sistema.mostrar_proxima_pendiente()  

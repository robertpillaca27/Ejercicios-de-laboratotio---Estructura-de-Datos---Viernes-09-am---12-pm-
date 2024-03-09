# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 04:09:47 2024

@author: USUARIO
"""

#14. Simular el proceso de deshacer (undo):
class SistemaDeshacer:
    def __init__(self):
        self.acciones = []  
# Lista para almacenar las acciones realizadas
        self.deshaceres = []  
# Lista para almacenar las acciones deshechas

    def realizar_accion(self, accion):
        print("Realizando:", accion)
        self.acciones.append(accion)  
# Agrega la acción a la lista de acciones

    def deshacer_accion(self):
        if self.acciones:
            accion_deshacer = self.acciones.pop()  
# Obtiene la última acción realizada
            print("Deshaciendo:", accion_deshacer)
            self.deshaceres.append(accion_deshacer)  
# Agrega la acción a la lista de deshaceres
        else:
            print("No hay acciones para deshacer")

    def rehacer_accion(self):
        if self.deshaceres:
            accion_rehacer = self.deshaceres.pop()  
# Obtiene la última acción deshecha
            print("Rehaciendo:", accion_rehacer)
            self.acciones.append(accion_rehacer)  
# Agrega la acción a la lista de acciones
        else:
            print("No hay acciones para rehacer")

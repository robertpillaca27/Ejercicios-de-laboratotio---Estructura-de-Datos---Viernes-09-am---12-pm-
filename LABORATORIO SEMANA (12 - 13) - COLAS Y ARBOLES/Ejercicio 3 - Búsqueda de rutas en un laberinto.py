# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 04:38:25 2024

@author: USUARIO
"""
#Ejercicio parte 01 – Colas:
#Búsqueda de rutas en un laberinto
#3. Desarrolla un programa que encuentre el camino más corto a través de un laberinto.
#Utiliza una cola para realizar un recorrido en anchura (BFS) desde el punto de inicio 
#hasta el punto de destino.

# Definimos una función con tres parametros
def encontrar_camino(laberinto, inicio, fin):
    
# Definimos las direcciones posibles (arriba, abajo, izquierda, derecha)
    direcciones = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Conjunto para almacenar las celdas visitadas
    visitado = set() 

 # Cola para realizar el recorrido en anchura
    cola = [(inicio, [])] 

    while cola:
        (x, y), camino = cola.pop(0)
# Obtenemos la celda actual y el camino recorrido

# Si alcanzamos el punto de destino, devolvemos el camino
        if (x, y) == fin:  
            return camino + [(x, y)]

# Exploramos las celdas vecinas
        for dx, dy in direcciones:  
            nx, ny = x + dx, y + dy
            # Evitamos ciclos y obstáculos
            if (nx, ny) != fin and (nx, ny) in visitado: continue
            if (nx, ny) not in laberinto or laberinto[(nx, ny)] == 1: continue

# Marcamos la celda como visitada
            visitado.add((nx, ny))  

# Añadimos la celda a la cola con el nuevo camino
            cola.append(((nx, ny), camino + [(x, y)]))  

# Si no hay camino posible, devolvemos None
    return None  

# Ejemplo de uso
laberinto = {
    (0, 0): 0, (0, 1): 1, (0, 2): 0, (0, 3): 0, (0, 4): 0,
    (1, 0): 0, (1, 1): 1, (1, 2): 0, (1, 3): 1, (1, 4): 0,
    (2, 0): 0, (2, 1): 0, (2, 2): 0, (2, 3): 1, (2, 4): 0,
    (3, 0): 0, (3, 1): 1, (3, 2): 1, (3, 3): 1, (3, 4): 0,
    (4, 0): 0, (4, 1): 0, (4, 2): 0, (4, 3): 0, (4, 4): 0,
}
inicio = (0, 0)
fin = (4, 4)

camino = encontrar_camino(laberinto, inicio, fin)
if camino:
    print(f"El camino más corto es:{camino}")
else:
    print("No existen caminos posibles.")

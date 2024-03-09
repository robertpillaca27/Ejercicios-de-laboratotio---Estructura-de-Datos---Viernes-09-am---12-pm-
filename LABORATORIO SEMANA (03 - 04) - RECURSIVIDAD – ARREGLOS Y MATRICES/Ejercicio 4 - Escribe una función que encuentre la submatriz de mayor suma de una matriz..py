
#Ejercicio 4: Escribe una funciÛn que encuentre la submatriz de mayor suma de una matriz.

def encontrar_submatriz_mayor_suma(matriz):
# Verificar si la matriz esta vacia
    if not matriz or not matriz[0]:
# Retorna coordenadas (i1, j1, i2, j2, suma)
        return 0, 0, 0, 0, 0  

    filas = len(matriz)
    columnas = len(matriz[0])

# Inicializar la suma maxima como infinito negativo
    max_suma = float('-inf')  
 # Inicializar las coordenadas y la suma del resultado
    resultado = (0, 0, 0, 0, 0) 

    for i in range(filas):
# Arreglo auxiliar para aplicar Cadena
        temp = [0] * columnas

        for j in range(i, filas):
            for k in range(columnas):
# Sumar valores de la columna a temp
                temp[k] += matriz[j][k]  

# Aplicar Kadane para encontrar la mayor suma en temp
            suma_temp, inicio_temp, fin_temp = kadane(temp)

            if suma_temp > max_suma:
                max_suma = suma_temp
                resultado = (i, inicio_temp, j, fin_temp, max_suma)

    return resultado

def kadane(arr):
# Inicializar la suma m√°xima como infinito negativo
    max_suma = float('-inf')  
    suma_actual = 0
    inicio = 0
    inicio_temp = 0
    fin_temp = 0

    for i in range(len(arr)):
# Sumar el elemento actual a la suma actual
        suma_actual += arr[i]  

        if suma_actual < 0:
# Si la suma actual es negativa, reiniciar la suma actual y actualizar el inicio temporal
            suma_actual = 0  

            inicio_temp = i + 1

        if suma_actual > max_suma:
            max_suma = suma_actual
            inicio = inicio_temp
            fin_temp = i

    return max_suma, inicio, fin_temp

# Ejemplo
matriz_ejemplo = [
    [1, 7, -1, -5, -20],
    [-8, -3, 4, 2, 111],
    [3, 80, 10, 1, 314],
    [-41, -1, 1, 7, -6]]

resultado = encontrar_submatriz_mayor_suma(matriz_ejemplo)
print("Submatriz de mayor suma:")
print("Coordenadas: ({}, {}) a ({}, {})".format(resultado[0], resultado[1], resultado[2], resultado[3]))
print("Suma:", resultado[4])

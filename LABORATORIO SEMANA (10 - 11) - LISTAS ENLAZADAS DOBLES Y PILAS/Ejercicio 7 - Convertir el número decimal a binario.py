# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 04:09:46 2024

@author: USUARIO
"""


#7. Convertir el número decimal a binario
def decimal_a_binario(decimal):
    pila = Pila()    
#crear clase pila para almacenar digitos
    while decimal > 0:  
#bucle que se ejecutará mientras el número decimal sea mayor que 0
        residuo = decimal % 2   
#calcula el residuo de la división del número decimal entre 2 se utiliza el operador % para calcular el residuo.
        pila.apilar(residuo)    
#residuo calculado se apila en la pila
        decimal //= 2    
#divide el número decimal entre 2 y se asigna el resultado a decimal
    binario = "" 
#inicializa una cadena vacía que se utilizará para almacenar
    while not pila.esta_vacia():      
#inicia un bucle que se ejecutará mientras la pila no esté vacía
        binario += str(pila.desapilar())    
#se desapila un dígito binario de la pila y se concatena a la cadena binario
    return binario if binario else "0"  
#se devuelve esta cadena como el resultado de la función.

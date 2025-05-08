# FUNCIONES
# 1 Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.
# 2 Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.
# 3 Crear una función que le solicite al usuario el ingreso de una cadena y la retorne. 
# 4 Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área. 
# 5 Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.
# 6 Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.
# 7 Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario.
# 8 Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.
# 9 Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.
# 10 Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.
# 11 Crear una función que (utilizando el algoritmo del ejercicio de la guia de for), muestre todos los números primos comprendidos entre entre la unidad y un número ingresado como parámetro. La función retorna la cantidad de números primos encontrados. Modularizar todo lo posible.
# 12 Crear una función que imprima la tabla de multiplicar de un número recibido como parámetro. La función debe aceptar parámetros opcionales (inicio y fin) para definir el rango de multiplicación. Por defecto es del 1 al 10.
# 13 Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. Agregar validaciones.

# 1
def pedir_entero():
    numero = input("Ingrese un numero entero: ")
    if numero.isdigit():
        numero = f"El numero es: {numero}"
    else:
        numero = "Error, ingrese un numero entero"
    return numero

# 2
def pedir_flotante():
    numero = input("Ingrese un numero flotante: ")
    if not numero.isdigit() and not numero.isalpha():
        numero = f"El numero es: {numero}"
    else:
        numero = "Error, ingrese un numero flotante"
    return numero

# 3
def pedir_cadena():
    cadena = input("Ingrese una cadena de texto: ")
    if cadena.isalpha():
        cadena = f"La cadena es {cadena}"
    else:
        cadena = "Error, ingrese una cadena"
    return cadena

# 4
def area_rectangulo(base : float, altura : float) -> float:
    return base * altura

# 5
def area_circulo(radio : float) -> float:
    pi = 3.14
    return pi * (radio ** 2)

# 6
def es_par_o_impar_mensaje(numero : int):
    if isinstance(numero, int):
        if numero % 2 == 0:
            print("El número es par.")
        else:
            print("El número es impar.")
    else:
        return "No ha ingresado un numero entero"

# 7
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
# 8
def maximo_de_tres(a, b, c):
        if a >= b and a >= c:
            return a
        elif b >= c:
            return b
        else:
            return c

# ejercicio clase
def es_flotante(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False
# entrada = input("Ingrese un número flotante: ")
# if es_flotante(entrada):
#     numero = float(entrada)
#     print(f"El número es válido: {numero}")
# else:
#     print("Error: No es un número flotante válido.")

# 9 
def calcular_potencia(base, potencia):
    resultado_potencia = base ** potencia
    return resultado_potencia

# 10

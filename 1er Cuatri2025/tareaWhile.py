#Ejercicio 1
for i in range(0, 11):
    print(i)

#Ejercicio 2
for i in range(10, 0, -1):
    print(i)

#Ejercicio 3
acumulador = 0
for i in range(0, 11):
    acumulador += i
print(acumulador)

#Ejercicio 4
acumulador = 0
for i in range(0, 11, 2):
    acumulador += i
print(acumulador)

#Ejercicio 5
acumulador = 0
for i in range(0, 5):
    numero_ingresado = int(input("Ingrese un numero: "))
    acumulador += numero_ingresado

promedio_acumulado = acumulador / 5

print(promedio_acumulado)

#Ejercicio 6
contador = 0
acumulador = 0

while True:
    numero_ingresado = int(input("Ingrese un numero: "))
    continua = str(input("Desea continuar? SI o NO: ")).lower()
    if continua == "no":
        break
    else:
        contador += 1
        acumulador += numero_ingresado

promedio_acumulado = acumulador / contador

print(f"La suma de los numeros es {acumulador} y el promedio es de {promedio_acumulado}")

#Ejercicio 7
contador_negativos = 0
contador_positivos = 0
producto_negativos = 1
acumulador_positivos = 0

while True:
    numero_ingresado = int(input("Ingrese un numero: "))
    continua = str(input("Desea continuar? SI o NO: ")).lower()
    if continua == "no":
        break
    else:
        if numero_ingresado > 0:
            acumulador_positivos += numero_ingresado
        else:
            producto_negativos *= numero_ingresado

if producto_negativos == 1:
    producto_negativos = 0



print(f"La suma de los numeros positivos es de {acumulador_positivos}, El producto de los negativos es de {producto_negativos}")

#Ejercicio 8
numero_minimo = float("inf")
numero_maximo = float("-inf")
for i in range(0, 10):
    numero_ingresado = int(input("Ingrese un numero: "))
    if numero_ingresado < numero_minimo:
        numero_minimo = numero_ingresado
    elif numero_ingresado > numero_maximo:
        numero_maximo = numero_ingresado

print(f"El numero maximo es {numero_maximo} y el numero minimo es {numero_minimo}")

#Ejercicio 9
contador = 0
acumulador = 0

while True:
    contador += 1
    numero_ingresado = int(input("Ingrese un numero: "))
    acumulador += numero_ingresado

    if contador > 4:
        continua = str(input("Desea continuar? SI o NO: ")).lower()
        if continua == "no":
            break

promedio = acumulador / contador

print(f"la suma de los numeros es {acumulador} y el promedio es {promedio}")

#Ejercicio 10
contador = 0
acumulador = 0

while True:
    contador += 1
    numero_ingresado = int(input("Ingrese un numero: "))
    acumulador += numero_ingresado

    if contador > 4 and contador < 9:
        continua = str(input("Desea continuar? SI o NO: ")).lower()
        if continua == "no":
            break
    elif contador > 9:
        break

promedio = acumulador / contador

print(f"la suma de los numeros es {acumulador} y el promedio es {promedio}")

acumulador_negativos = 0
acumulador_positivos = 0
contador_negativos = 0
contador_positivos = 0
contador = 0
numero_maximo = float("-inf")

while True:
    numero_ingresado = int(input("Ingrese un numero: "))
    contador += 1
    if numero_ingresado > 0:
        contador_positivos += 1
        acumulador_positivos += numero_ingresado
        if numero_ingresado > numero_maximo:
            numero_maximo = numero_ingresado

    elif numero_ingresado < 0:
        contador_negativos += 1
        acumulador_negativos += numero_ingresado

    continua = str(input("Desea continuar? SI o NO: ")).lower()
    if continua == "no":
        break

promedio_positivos = acumulador_positivos / contador_positivos
porcentaje_negativos = contador * (contador_negativos / 100)

while True:

    respuesta = str(input("Ingrese A para ver la suma acumulada de los números negativos.\n" \
    " Ingrese B para ver la suma acumulada de los números positivos.\n" \
    " Ingrese C para ver la cantidad de números negativos ingresados.\n" \
    " Ingrese D para ver el promedio de los números positivos.\n" \
    " Ingrese E para ver el número positivo más grande.\n" \
    " Ingrese F para ver el porcentaje de números negativos ingresados, respecto del total de ingresos.\n" \
    " Ingrese No para salir\n"
    " ")).lower()

    if respuesta == "a":
        print(f"la suma acumulada de los números negativos es {acumulador_negativos}")
    elif respuesta == "b":
        print(f"la suma acumulada de los números positivos es {acumulador_positivos}")
    elif respuesta == "c":
        print(f"la cantidad de números negativos ingresados es {contador_negativos}")
    elif respuesta == "d":
        print(f"el promedio de los números positivos es {promedio_positivos}")
    elif respuesta == "e":
        print(f"el número positivo más grande es {numero_maximo}")
    elif respuesta == "f":
        print(f"el porcentaje de números negativos ingresados, respecto del total de ingresos es {porcentaje_negativos}")
    elif respuesta == "no":
        break

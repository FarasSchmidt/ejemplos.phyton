# Ejercicio 1:

# Escribí un programa en Python que le pida al usuario ingresar su edad.
# Si la edad es menor a 0 o mayor a 120, mostrar un mensaje que diga: "Edad inválida".
# Si la edad es menor a 13, mostrar: "Acceso denegado. Debes tener al menos 13 años para entrar."
# Si la edad está entre 13 y 17 inclusive, mostrar: "Acceso restringido. Estás en modo adolescente."
# Si la edad es 18 o más, mostrar: "Acceso completo concedido."
# Pedir al usuario que ingrese su edad

edad = int(input("Por favor, ingresa tu edad: "))

if edad < 1 or edad > 120:
    print("Edad inválida")

elif edad < 13:
    print("Acceso denegado. Debes tener al menos 13 años para entrar.")

elif 13 <= edad <= 17:
    print("Acceso restringido. Estás en modo adolescente.")

else:
    print("Acceso completo concedido.")


# Ejercicio 2

# A partir del ingreso de la altura en centímetros de un jugador de baloncesto,
# el programa deberá determinar la posición del jugador en la cancha, considerando los siguientes parámetros:

# Menos de 160 cm: Base
# Entre 160 cm y 179 cm: Escolta
# Entre 180 cm y 199 cm: Alero
# 200 cm o más: Ala-Pívot o Pívot

altura = int(input("Ingrese la altura del jugador en cm: "))

if altura < 160:
    posicion = "Base"
elif altura < 180:
    posicion = "Escolta"
elif altura < 200:
    posicion = "Alero"
elif altura <= 250:
    posicion = "Ala-Pívot o Pívot"
else:
    posicion = "Altura no válida"
print(f"La posición del jugador es: {posicion}")



#Alumno: Faras Schmidt
#Consigna 1. A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el
#programa deberá determinar la posición del jugador en la cancha, considerando los
#siguientes parámetros:
#● Menos de 160 cm: Base
#● Entre 160 cm y 179 cm: Escolta
#● Entre 180 cm y 199 cm: Alero
#● 200 cm o más: Ala-Pívot o Pívot


import random

# altura = int(input("Ingrese su altura en cm: "))
# if altura < 160:
#     respuesta = "Usted es Base"
# elif altura > 161 and altura < 179:
#     respuesta = "Usted es Escolta"
# elif altura > 180 and altura < 199:
#     respuesta = "Usted es Alero"
# else:
#     respuesta = "Usted es Ala-Pivot o Pivot"

# print(respuesta)


#2. Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un
#mensaje según el valor:
#● 6, 7, 8, 9 y 10 ---> Promoción directa, la nota es ...
#● 4 y 5 ---> Aprobado, la nota es ...
#● 1, 2 y 3 ---> Desaprobado, la nota es ...


nota = random.randint(1, 10)
if nota == 1 or nota == 2 or nota == 3:
    print(f"Desaprobado, la nota es: {nota}")
elif nota == 4 or nota == 5:
    print(f"Aprobado, la nota es: {nota}")
elif nota == 6 or nota == 7 or nota == 8 or nota == 9 or nota == 10:
    print(f"Promocion directa, la nota es: {nota}")

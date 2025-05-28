from modulogranos import *
"""
Una empresa se dedica al almacenamiento y posterior distribución de cereales en el interior del país. Para ello cuentan con 20 depósitos en CABA, que generalmente se encuentran en las inmediaciones de las estaciones del ferrocarril. 
Los depósitos pueden almacenar 4 tipos diferentes de cereales: maíz, trigo, cebada y centeno. 
La oficina central, recibe mensualmente una planilla de existencias donde se indican las existencias de cada cereal para cada depósito. 
Realizar un menú de opciones: while - match case
1. Obtener existencias: para ello deberá crear una función que cargue la existencia de cada grano(input) en todos los depósitos. Los valores estarán comprendidos entre 5000 Kg y 20000 Kg. (validar, que sea número) deposito_1 =  depositos[0] = 500
2. Calcular por cada depósito la cantidad total de kilos almacenados entre todos los cereales. 
3. Nombre del cereal que almaceno menos kilos en cada depósito. 
4. Máxima cantidad de kilos almacenados de cada cereal. 
5. Depósito con mayor recaudación, teniendo en cuenta que disponemos de un vector con los valores por kilo de cada tipo de cereal. 
6. Cantidad de depósitos que hayan almacenado más de 50000 kilos entre los 4 cereales. 
7. Porcentaje de kilos de cada cereal sobre el total de kilos almacenados. Además mostrar el nombre del cereal con el máximo porcentaje. 
8. Generar un informe con la recaudación de cada depósito, ordenada de mayor a menor.
"""


filas = 3 # cantidad de depositos.
columnas = 4 # cantidad de cereales.

# Inicializo la matriz que contendra los depositos y las cantidades de sus cereales.
matriz_de_deposito = [[0 for c in range(columnas)] for f in range(filas)]


# Lista de cereales:
cereales = ["Maiz", "Trigo", "Cebada", "Centeno"]

# Lista de cotización de los cereales:
precios = [1500, 2000, 1200, 300]



def menu_de_opcione():
    """"""
    continuar = "si"
    while continuar != "no":
        print("1. Obtener existencias")
        print("2. Calcular por cada depósito la cantidad total de kilos almacenados entre todos los cereales.")
        print("3. Nombre del cereal que almaceno menos kilos en cada depósito.")
        print("4. Máxima cantidad de kilos almacenados de cada cereal.")
        print("5. Depósito con mayor recaudación")
        print("6. Cantidad de depósitos que hayan almacenado más de 50000 kilos entre los 4 cereales.")
        print("7. Porcentaje de kilos de cada cereal sobre el total de kilos almacenados.")
        print("8. Generar un informe con la recaudación de cada depósito, ordenada de mayor a menor.")
        opcion_escogida = input("Por favor, ingrese el número de la opción que desea ejecutar: ")
        if es_entero(opcion_escogida): 
            match int(opcion_escogida):
                case 1:
                    obtener_existencia()
                    continuar = input("¿Desea realizar otra operación? 'Si/No': ").lower()
                case 2:
                    cantidad_total_de_kilos_de_los_depositos(matriz_de_deposito, filas)
                    continuar = input("¿Desea realizar otra operación? 'Si/No': ").lower()
                case 3:
                    cereales_con_menos_kilos_en_cada_deposito(matriz_de_deposito, filas, cereales)
                    continuar = input("¿Desea realizar otra operación? 'Si/No': ").lower()
                case 4:
                    maxima_cantidad_de_kilos_de_cada_cereal(matriz_de_deposito, filas, cereales)
                    continuar = input("¿Desea realizar otra operación? 'Si/No': ").lower()
                case 5:
                    deposito_con_mayor_recaudacion(matriz_de_deposito, filas, precios)
                    continuar = input("¿Desea realizar otra operación? 'Si/No': ").lower()
                case 6:
                    cantidad_de_depositos_con_mas_de_50000_kilos(matriz_de_deposito)
                    continuar = input("¿Desea realizar otra operación? 'Si/No': ").lower()
                case 7:
                    porcentaje_de_cada_cereal_almacenado(matriz_de_deposito, cereales)
                    continuar = input("¿Desea realizar otra operación? 'Si/No': ").lower()
                case 8: 
                    informe_con_la_recaudación(matriz_de_deposito, precios)
                    continuar = input("¿Desea realizar otra operación? 'Si/No': ").lower()
                case 9: # Está es mía para mostrar la matriz durante el proceso. No aparece como opción al mostrar el menu.
                    for i in range(len(matriz_de_deposito)):
                        for j in range(len(matriz_de_deposito[i])):
                            print(matriz_de_deposito[i][j], end=" ")
                        print("")
                case _:
                    print("El número ingresado no corresponde con ninguna de las opciones dadas.")
        else:
            print("La opción ingresado no correspode a ninguna existente. Por favor, intente denuevo.")  


# print(matriz_de_deposito[0][2])




# Opción 1
# De está manera ingreso uno por uno cada existencia de los granos. Se me hace medio engorroso.

def obtener_existencia():
    """
    Propósito: carga la existencia de cada grano en todos los depositos.
    Return: retorna la matriz de los depositos con los valores de los cereales actualizados.
    """
    for i in range(len(matriz_de_deposito)):
        for j in range(len(matriz_de_deposito[i])):
            if j == 0:
                grano_actual = "maiz"
            elif j == 1:
                grano_actual = "trigo"
            elif j == 2:
                grano_actual = "cebada"
            else:
                grano_actual = "centeno"

            seguir_intentado = "Si"
            while seguir_intentado != "No":
                cantidad_del_grano = input(f"Por favor, ingrese la cantidad de {grano_actual} existente para el deposito {i + 1}, la canitdad debe ser entre 5000 kg y 20000 kg: ")
                if es_entero(cantidad_del_grano) or es_float(cantidad_del_grano) or es_un_numero_negativo(cantidad_del_grano):
                    cantidad_del_grano = int(cantidad_del_grano)
                    if 5000 < cantidad_del_grano < 20000:
                    # if es_un_numero_negativo(cantidad_del_grano) and (cantidad_del_grano <= matriz_de_deposito[i][j]):
                    #     matriz_de_deposito[i][j] -= cantidad_del_grano
                        matriz_de_deposito[i][j] += cantidad_del_grano
                        seguir_intentado = "No"
                    else:
                        print("El número ingresado no está dentro de los valores comprendidos.")
                    
                else:
                    print("El valor ingresado no es valido, por favor vuelva a intentar.")



# obtener_existencia()


for i in range(len(matriz_de_deposito)):
    for j in range(len(matriz_de_deposito[i])):
        print(matriz_de_deposito[i][j], end=" ")
    print("")


# Opción 2

def cantidad_total_de_kilos_de_los_depositos(matriz, cantidad_de_depositos):
    """
    Propósito: Indicar la cantidad de kilos totales de cada deposito.
    Parametro:
        matriz (list): matriz que se tendra en cuenta para realizar la operación.
    Return: Los kilos totales de cada deposito.
    """
    for i in range(cantidad_de_depositos):
        cantidad_total_de_kilos = 0
        for j in range(len(matriz[i])):
            cantidad_total_de_kilos += matriz[i][j]
        print(f"La cantidad total de kilos en el deposito {i + 1} es {cantidad_total_de_kilos} kilos.")


# cantidad_total_de_kilos_de_los_depositos(matriz_de_deposito, filas)



# Opción 3

def cereales_con_menos_kilos_en_cada_deposito(matriz, cantidad_de_depositos, lista_de_cereales):
    """
    Propósito: Indicar cuales son los cereales con más kilos en cada deposito.
    Parametros:
        matriz (list): matriz que se tendra en cuenta para realizar la operación.
        cantidad_de_depositos (int): cantidad de depositos en la matriz
        lista_de_cereales (list): lista de los cereales que contienen los depositos.
    Return: Retorna cual es el cereal con más kilos en cada deposito de la matriz dada.
    """
    for i in range(cantidad_de_depositos):
        cantidad_minima_de_kilos = float("+inf")
        for j in range(len(matriz[i])):
            if matriz[i][j] < cantidad_minima_de_kilos:
                cantidad_minima_de_kilos = matriz[i][j]
                indice_del_cereal = j
        print(f"El cereal con menos kilos en el deposito {i + 1} es: {lista_de_cereales[indice_del_cereal]} ")


# cereales_con_menos_kilos_en_cada_deposito(matriz_de_deposito, filas, cereales)


# Opción 4

def maxima_cantidad_de_kilos_de_cada_cereal(matriz, cantidad_de_depositos, cereales):
    """
    Propósito: Indicar la cantidad máxima de kilos de cada cereal entre los depositos.
    Parametros:
        matriz (list): lista de depositos a tener en cuenta para operar.
        cantidad_de_depositos (int): cantidad de depositos en la matriz
        cereales (list): lista de cereales que hay en los depositos.
    Return: indicar la cantidad máxima de cada cereal almacenado de cada cereal entre todos los depositos.
    """
    for i in range(cantidad_de_depositos):
        max_cantidad_cereal = float("-inf")
        for j in range(len(cereales)):
            if matriz[i][j] > max_cantidad_cereal:
                max_cantidad_cereal = matriz[i][j]
                indice_del_cereal = j
        print(f"El cereal con mayor canitdad en el deposito {i + 1} es {cereales[indice_del_cereal]}")


maxima_cantidad_de_kilos_de_cada_cereal(matriz_de_deposito, filas, cereales)


# Opción 5

def deposito_con_mayor_recaudacion(matriz, cantidad_de_depositos, precios):
    """
    Propóstio: Indicar cual es el deposito que mayor recaudación tuvo.
    Parametro:
        matriz (list): lista de depositos a tener en cuenta para operar.
        cantidad_de_depositos (int): cantidad de depositos en la matriz
        precios (list): lista de precios de cada cereal.
    Return: retorna un str diciendo que cual es el deposito con mayor recaudación.
    """
    recaudaciones = []
    for i in range(cantidad_de_depositos):
        total_del_deposito = 0
        for j in range(len(matriz[i])):
            total_del_cereal = matriz[i][j] * precios[j]
            total_del_deposito += total_del_cereal
        recaudaciones += [total_del_deposito]
    
    recaudacion_mas_grande = float("-inf")
    for i in range(len(recaudaciones)):
        if i > recaudacion_mas_grande:
            deposito_con_mayor_recaudacion = i + 1
    print(f"El deposito con mayor recaudación es el {deposito_con_mayor_recaudacion}")
        

    
deposito_con_mayor_recaudacion(matriz_de_deposito, filas, precios)



# Opción 6

def cantidad_de_depositos_con_mas_de_50000_kilos(matriz):
    """
    Propóstio: Indica la cantidad de deposito que tienen más de 500 kilos entre los cuatro cereales.
    Parametro:
        matriz (list): matriz de depositos con cereales a tener en cuenta.
    Return: retorna un str indicando la cantidad de depositos con más de 500 kilos entre los cuatro cereales.
    """
    cantidad_de_depositos_con_mas_de_50000_kl = 0
    for i in range(len(matriz)):
        if todos_los_cereales_tienen_valores_mayor_a_cero(matriz[i]):
            cantidad_total_del_deposito = 0
            for j in matriz[i]:
                cantidad_total_del_deposito += j
            if cantidad_total_del_deposito > 50000:
                cantidad_de_depositos_con_mas_de_50000_kl += 1
    print(f"La cantidad de depositos con mas de 50000 kl entre los cuatros cereales es: {cantidad_de_depositos_con_mas_de_50000_kl}")


def todos_los_cereales_tienen_valores_mayor_a_cero(deposito):
    """
    Propósito: Indica si todos los cereales tienen un valor mayor a cero
    Parametro:
        deposito (list): lista de cantidades de kilos de los cereales en ese deposito.
    Return: retorna True se todos los cereales tiene valores mayores a cero. En caso contrario retorna False
    """
    todos_tienen_valores_mayores_a_cero = True
    for i in deposito:
        todos_tienen_valores_mayores_a_cero = todos_tienen_valores_mayores_a_cero and (i > 0)
    
    return todos_tienen_valores_mayores_a_cero


# Opción 7

def porcentaje_de_cada_cereal_almacenado(matriz, cereales):
    """
    Propóstio: Indicar el porcentaje almacenado de cara cereal y el nombre del cereal con mayor porcentaje.
    Parametro:
        matriz (list): lista de depositos que se va a tener en cuenta para la operación.
        cereales (list): lista de cereales que contienen los depositos.
    Return: retorna el porcentaje de cada cereal y el nombre del cereal con mayor porcentaje.
    """
    cantidad_total_de_kilos_almacenados = total_de_kilos_almacenados_en(matriz)
    porcentaje_mas_alto = 0
    cereal_con_mayor_porcentaje = 0
    for i in range(len(cereales)):
        cantidad_total_del_cereal = 0
        for j in range(len(matriz)):
            cantidad_total_del_cereal += matriz[j][i]
        porcentaje_del_cereal = (cantidad_total_del_cereal * 100) / cantidad_total_de_kilos_almacenados
        if porcentaje_del_cereal > porcentaje_mas_alto:
            cereal_con_mayor_porcentaje = j
        print(f"{cereales[cereal_con_mayor_porcentaje]}: {round(porcentaje_del_cereal, 2)}%")


def total_de_kilos_almacenados_en(matriz):
    """
    Propósito: indicar la cantidad total de kilos almacenados en la matriz dada.
    Parametro:
        matriz (list): lista de deposito a tener en cuenta
    Return: retorna un int que representa la cantidad total de kilos almacenados.
    """
    cantidad_total = 0
    for i in range(len(matriz)):
        cantidad_total_del_deposito = 0
        for j in matriz[i]:
            cantidad_total_del_deposito += j
        cantidad_total += cantidad_total_del_deposito
    return cantidad_total



# Opción 8

def informe_con_la_recaudación(matriz, precios):
    """
    Propóstio: indicar las recaudaciones de cada deposito.
    Parametro:
        matriz (list): lista de depositos a tener en cuenta para operar.
        precios (list): lista de precios de los cereales.
    Return: retorna las recaudaciones de mayor a menor.
    """

    recaudaciones = []
    for i in range(len(matriz)):
        total_del_deposito = 0
        for j in range(len(matriz[i])):
            total_del_cereal = matriz[i][j] * precios[j]
            total_del_deposito += total_del_cereal
        recaudaciones += [total_del_deposito]

    indices = [i for i in range(len(recaudaciones))]
    for i in range(len(recaudaciones) - 1):
        for j in range(len(recaudaciones) - 1):
            if recaudaciones[j + 1] > recaudaciones[j]:
                valor_actual = recaudaciones[j]
                indice_actual = indices[j]
                recaudaciones[j] = recaudaciones[j + 1]
                recaudaciones[j + 1] = valor_actual
                indices[j] = indices[j + 1]
                indices[j + 1] = indice_actual
                

    print(f"Las recaudaciones de cada deposito son: ")
    for i in range(len(recaudaciones)):
        print(f"La recaudación del deposito {indices[i] + 1} es de: ${recaudaciones[i]}")


# indices = [i for i in range(4)]
# print(indices)

menu_de_opcione()
from funciones import *
datos_cargados = False

while True:
    print("\n--- MENÚ ---")
    print("1. Obtener existencias")
    print("2. Total de kilos por depósito")
    print("3. Cereal con menos kilos en cada depósito")
    print("4. Máxima cantidad de kilos almacenados por cereal")
    print("5. Depósito con mayor recaudación")
    print("6. Depósitos con más de 50.000 kg")
    print("7. Porcentaje de kilos por cereal")
    print("8. Informe de recaudación ordenado")
    print("0. Salir")

    opcion = input("Seleccione una opción: ")

    match opcion:
        case "1":
            cargar_existencias()
            datos_cargados = True
        case "2":
            if datos_cargados:
                i = 0
                while i < NUM_DEPOSITOS:
                    total = total_kilos_deposito(depositos[i])
                    print(f"Depósito {i+1}: {total} kg")
                    i += 1
            else:
                print("Primero debe cargar los datos.")
        case "3":
            if datos_cargados:
                i = 0
                while i < NUM_DEPOSITOS:
                    idx, valor = cereal_menor_en_deposito(depositos[i])
                    print(f"Depósito {i+1}: {NOMBRES_CEREALES[idx]} ({valor} kg)")
                    i += 1
            else:
                print("Primero debe cargar los datos.")
        case "4":
            if datos_cargados:
                i = 0
                while i < NUM_CEREALES:
                    maximo = maximo_por_cereal(i)
                    print(f"{NOMBRES_CEREALES[i]}: máximo = {maximo} kg")
                    i += 1
            else:
                print("Primero debe cargar los datos.")
        case "5":
            if datos_cargados:
                idx, rec = deposito_mayor_recaudacion()
                print(f"Depósito con mayor recaudación: {idx+1} (${rec})")
            else:
                print("Primero debe cargar los datos.")
        case "6":
            if datos_cargados:
                cantidad = contar_depositos_mayores_a_50000()
                print(f"Cantidad de depósitos con más de 50.000 kg: {cantidad}")
            else:
                print("Primero debe cargar los datos.")
        case "7":
            if datos_cargados:
                porcentaje_cereal()
            else:
                print("Primero debe cargar los datos.")
        case "8":
            if datos_cargados:
                informe_recaudaciones()
            else:
                print("Primero debe cargar los datos.")
        case "0":
            print("Fin del programa.")
            break
        case _:
            print("Opción inválida.")

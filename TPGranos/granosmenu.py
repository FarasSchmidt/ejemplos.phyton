from modulogranos import *

# dos depositos y 2 cereales

while True:
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. Cargar existencias")
    print("2. Total por depósito")
    print("3. Cereal con menor cantidad por depósito")
    print("4. Máximo por cereal")
    print("5. Depósito con mayor recaudación")
    print("6. Contar depósitos > 50000 kg")
    print("7. Porcentaje de cada cereal")
    print("8. Informe ordenado de recaudación")
    print("0. Salir")
    
    opcion = input("Seleccione una opción: ")

    match opcion:
        case "1":
            cargar_existencias()
        case "2":
            if depositos: total_por_deposito()
            else: print("⚠️ Primero cargue las existencias.")
        case "3":
            if depositos: cereal_menor_por_deposito()
            else: print("⚠️ Primero cargue las existencias.")
        case "4":
            if depositos: maximo_por_cereal()
            else: print("⚠️ Primero cargue las existencias.")
        case "5":
            if depositos: deposito_mayor_recaudacion()
            else: print("⚠️ Primero cargue las existencias.")
        case "6":
            if depositos: depositos_mayores_50000()
            else: print("⚠️ Primero cargue las existencias.")
        case "7":
            if depositos: porcentaje_por_cereal()
            else: print("⚠️ Primero cargue las existencias.")
        case "8":
            if depositos: informe_recaudacion()
            else: print("⚠️ Primero cargue las existencias.")
        case "0":
            print("Saliendo del programa.")
            break
        case _:
            print("⚠️ Opción inválida.")

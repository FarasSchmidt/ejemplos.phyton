# Constantes
NUM_DEPOSITOS = 20
NUM_CEREALES = 4
NOMBRES_CEREALES = ["maíz", "trigo", "cebada", "centeno"]
VALOR_POR_KILO = [10, 8, 6, 5]  # valores por kilo en orden

# Estructura: lista de listas -> depositos[i][j] = kg del cereal j en el depósito i
depositos = [[0] * NUM_CEREALES for _ in range(NUM_DEPOSITOS)]

def pedir_kg_valido(nombre_cereal):
    while True:
        entrada = input(f"Ingrese los kg de {nombre_cereal} (5000 a 20000): ")
        if entrada.isdigit():
            valor = int(entrada)
            if 5000 <= valor <= 20000:
                return valor
        print("Entrada inválida. Debe ser un número entre 5000 y 20000.")

def cargar_existencias():
    i = 0
    while i < NUM_DEPOSITOS:
        print(f"\nDepósito {i+1}")
        j = 0
        while j < NUM_CEREALES:
            kg = pedir_kg_valido(NOMBRES_CEREALES[j])
            depositos[i][j] = kg
            j += 1
        i += 1

def total_kilos_deposito(dep):
    total = 0
    i = 0
    while i < NUM_CEREALES:
        total += dep[i]
        i += 1
    return total

def cereal_menor_en_deposito(dep):
    min_kg = dep[0]
    min_idx = 0
    i = 1
    while i < NUM_CEREALES:
        if dep[i] < min_kg:
            min_kg = dep[i]
            min_idx = i
        i += 1
    return min_idx, min_kg

def maximo_por_cereal(idx_cereal):
    max_valor = depositos[0][idx_cereal]
    i = 1
    while i < NUM_DEPOSITOS:
        if depositos[i][idx_cereal] > max_valor:
            max_valor = depositos[i][idx_cereal]
        i += 1
    return max_valor

def recaudacion_deposito(dep):
    total = 0
    i = 0
    while i < NUM_CEREALES:
        total += dep[i] * VALOR_POR_KILO[i]
        i += 1
    return total

def deposito_mayor_recaudacion():
    max_rec = 0
    idx = 0
    i = 0
    while i < NUM_DEPOSITOS:
        rec = recaudacion_deposito(depositos[i])
        if rec > max_rec:
            max_rec = rec
            idx = i
        i += 1
    return idx, max_rec

def contar_depositos_mayores_a_50000():
    contador = 0
    i = 0
    while i < NUM_DEPOSITOS:
        if total_kilos_deposito(depositos[i]) > 50000:
            contador += 1
        i += 1
    return contador

def porcentaje_cereal():
    total_por_cereal = [0] * NUM_CEREALES
    total_general = 0
    i = 0
    while i < NUM_DEPOSITOS:
        j = 0
        while j < NUM_CEREALES:
            total_por_cereal[j] += depositos[i][j]
            total_general += depositos[i][j]
            j += 1
        i += 1

    mayor_pct = 0
    idx_mayor = 0
    i = 0
    while i < NUM_CEREALES:
        porcentaje = (total_por_cereal[i] * 100) / total_general
        print(f"{NOMBRES_CEREALES[i]}: {porcentaje:.2f}%")
        if porcentaje > mayor_pct:
            mayor_pct = porcentaje
            idx_mayor = i
        i += 1
    print(f"Cereal con mayor porcentaje: {NOMBRES_CEREALES[idx_mayor]} ({mayor_pct:.2f}%)")

def informe_recaudaciones():
    lista = []
    i = 0
    while i < NUM_DEPOSITOS:
        lista.append((i, recaudacion_deposito(depositos[i])))
        i += 1

    # Ordenar manualmente (burbuja)
    n = len(lista)
    i = 0
    while i < n - 1:
        j = 0
        while j < n - i - 1:
            if lista[j][1] < lista[j+1][1]:
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp
            j += 1
        i += 1

    print("\nRecaudación por depósito (ordenado):")
    for item in lista:
        print(f"Depósito {item[0]+1}: ${item[1]}")

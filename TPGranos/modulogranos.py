CEREALES = ["maíz", "trigo", "cebada", "centeno"]
NUM_DEPOSITOS = 2
VALORES_POR_KILO = {
    "maíz": 10,
    "trigo": 12,
    "cebada": 8,
    "centeno": 9
}

INGRESOS_POR_GRANO = {
    "maíz": 0,
    "trigo": 0,
    "cebada": 0,
    "centeno": 0
}
# def hacerLista():
#     for i in range():

# INGRESOS_POR_GRANO[cerealTipo] += ingresoCereal

def es_entero(int):
    if valor.isdigit():
            valor = int(valor)
    else:
        print("⚠️ Debe ingresar un número válido.")
        
def es_flotante(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False
    

def pedir_num(texto, valorMin, valorMax):
    while True:
        valor = input(f"{texto}")
        if valor.isdigit():
            valor = int(valor)
            if valorMin <= valor <= valorMax:
                return valor
            else:
                print("⚠️ Valor fuera del rango permitido.")
        else:
            print("⚠️ Debe ingresar un número válido.")
    
# 1. Cargar existencias
def cargar_existencias():
    global depositos
    depositos = []
    for i in range(NUM_DEPOSITOS):
        print(f"\n--- Carga para Depósito {i+1} ---")
        deposito = {}
        for cereal in CEREALES:
            ingresoCereal = pedir_num(f"Ingrese kg de {cereal} (5000 a 20000): ", 5000, 20000)
            deposito [cereal] = ingresoCereal
            INGRESOS_POR_GRANO[cereal] += ingresoCereal
        depositos.append(deposito)

# 2. Total por depósito
def total_por_deposito():
    for i, dep in enumerate(depositos):
        total = sum(dep.values())
        print(f"Depósito {i+1}: {total} kg")

# 3. Cereal con menor cantidad por depósito
def cereal_menor_por_deposito():
    for i, dep in enumerate(depositos):
        menor = min(dep, key=dep.get)
        print(f"Depósito {i+1}: menor cantidad = {menor} ({dep[menor]} kg)")

# 4. Máximo por cereal
def maximo_por_cereal():
    for cereal in CEREALES:
        maximo = max(dep[cereal] for dep in depositos)
        print(f"{cereal.capitalize()}: máximo = {maximo} kg")

# 5. Depósito con mayor recaudación
def deposito_mayor_recaudacion():
    mayores = []
    for dep in depositos:
        total = sum(dep[c] * VALORES_POR_KILO[c] for c in CEREALES)
        mayores.append(total)
    mayor_valor = max(mayores)
    pos = mayores.index(mayor_valor)
    print(f"Depósito con mayor recaudación: #{pos+1} - ${mayor_valor}")

# 6. Contar depósitos con más de 50000 kg
def depositos_mayores_50000():
    contador = sum(1 for dep in depositos if sum(dep.values()) > 50000)
    print(f"Cantidad de depósitos con más de 50000 kg: {contador}")

# 7. Porcentaje por cereal y cereal con mayor porcentaje
def porcentaje_por_cereal():
    total_cereal = {c: 0 for c in CEREALES}
    total_general = 0
    for dep in depositos:
        for c in CEREALES:
            total_cereal[c] += dep[c]
            total_general += dep[c]

    print("Porcentaje de cada cereal:")
    for c in CEREALES:
        porc = (total_cereal[c] / total_general) * 100
        print(f"{c.capitalize()}: {porc:.2f}%")
    max_cereal = max(total_cereal, key=total_cereal.get)
    print(f"Cereal con mayor porcentaje: {max_cereal.capitalize()}")

# 8. Informe ordenado por recaudación
def informe_recaudacion():
    lista = []
    for i, dep in enumerate(depositos):
        recaudacion = sum(dep[c] * VALORES_POR_KILO[c] for c in CEREALES)
        lista.append((i + 1, recaudacion))
    lista.sort(key=lambda x: x[1], reverse=True)
    print("Informe de recaudación por depósito (ordenado):")
    for num, rec in lista:
        print(f"Depósito {num}: ${rec}")
        
def ordenar_recaudaciones(lista):
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

      
def encontrar_minimo(lista):
    minimo = lista[0]
    indice = 0
    i = 1
    while i < len(lista):
        if lista[i] < minimo:
            minimo = lista[i]
            indice = i
        i += 1
    return indice

def encontrar_maximo(lista):
    maximo = lista[0]
    i = 1
    while i < len(lista):
        if lista[i] > maximo:
            maximo = lista[i]
        i += 1
    return maximo

lista1 = [1, 3, 5, -8]
numMin = encontrar_minimo(lista1)
print(f"El valor minimo es {lista1[numMin]} en la posicion {numMin+1}")

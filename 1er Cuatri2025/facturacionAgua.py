# Facturación del Servicio de Agua Potable
# El acceso al agua potable es un servicio esencial para hogares, comercios e industrias. Para garantizar un uso eficiente del recurso y establecer una estructura justa de costos, se han definido diferentes tarifas y ajustes según el consumo y el tipo de cliente.
# Este sistema de facturación contempla una tarifa base que incluye un cargo fijo y un costo variable por metro cúbico consumido. Además, se aplican bonificaciones y recargos dependiendo del consumo y la categoría del usuario. En algunos casos especiales, también pueden otorgarse descuentos adicionales.
# A continuación, se detallan las reglas del sistema de facturación y los cálculos necesarios para determinar el monto final a pagar.
# Tarifa base:
# Todas las facturas incluyen un cargo fijo de $7000 además del costo por consumo.
# El costo por metro cúbico (m³) de agua es de $200/m³.
# Bonificaciones y Recargos según tipo de cliente:
# Cliente Residencial:
# Si el consumo es menor a 30 m³, se aplica una bonificación del 10% sobre el costo del consumo.
# Si el consumo supera los 80 m³, se aplica un recargo del 15% sobre el costo del consumo.
# Cliente Comercial:
# Si el consumo es superior a 150 m³, se aplica una bonificación del 8% sobre el costo del consumo.
# Si el consumo supera los 300 m³, la bonificación aumenta al 12%.
# Si el consumo es menor a 50 m³, se aplica un recargo del 5%.
# Cliente Industrial:
# Si el consumo es superior a 500 m³, se aplica una bonificación del 20% sobre el costo del 
# consumo.
# Si el consumo supera los 1,000 m³, la bonificación aumenta al 30%.
# Si el consumo es menor a 200 m³, se aplica un recargo del 10%.
# Casos especiales:
# Si el cliente es Residencial y el total de la factura sin impuestos ni bonificaciones  es menor a $35000, se aplica un descuento adicional del 5%.
# En todos los casos, se aplica el IVA del 21% sobre el total.
# Requerimientos del programa:
# Solicitar al usuario:
# Cantidad de metros consumidos
# Tipo de cliente, que puede ser: Residencial, Comercial o Industrial.
# Calcular:
# Subtotal de consumo.
# Bonificaciones, si corresponde
# Recargos, si corresponde
# Subtotal, con recargos y bonificaciones.
# IVA aplicado (21%), si corresponde.
# Total final a pagar.
# Mostrar en pantalla el desglose de los cálculos.


consumo_m3 = float(input("Ingrese la cantidad de metros cúbicos consumidos: "))
tipo_cliente = input("Ingrese el tipo de cliente (Residencial, Comercial o Industrial): ")


cargo_fijo = 7000
costo_por_m3 = 200

costo_consumo = consumo_m3 * costo_por_m3
tarifa_total = cargo_fijo + costo_consumo

bonificacion = 0
recargo = 0
descuento_especial = 0

if tipo_cliente == "Residencial":
    if consumo_m3 < 30:
        bonificacion = 0.10 * costo_consumo
    elif consumo_m3 > 80:
        recargo = 0.15 * costo_consumo

elif tipo_cliente == "Comercial":
    if consumo_m3 < 50:
        recargo = 0.05 * costo_consumo
    elif consumo_m3 > 300:
        bonificacion = 0.12 * costo_consumo
    elif consumo_m3 > 150:
        bonificacion = 0.08 * costo_consumo

elif tipo_cliente == "Industrial":
    if consumo_m3 < 200:
        recargo = 0.10 * costo_consumo
    elif consumo_m3 > 1000:
        bonificacion = 0.30 * costo_consumo
    elif consumo_m3 > 500:
        bonificacion = 0.20 * costo_consumo

subtotal = tarifa_total - bonificacion + recargo

if tipo_cliente == "Residencial" and tarifa_total < 35000:
    descuento_especial = 0.05 * subtotal
    subtotal = subtotal - descuento_especial

iva = 0.21 * subtotal
total_final = subtotal + iva

print(f"Tipo de Cliente: {tipo_cliente}")
print(f"Consumo: {consumo_m3} m³")
print(f"Cargo fijo: $ {cargo_fijo}")
print(f"Costo por consumo: $ {costo_consumo}")
print(f"Bonificación aplicada: -$ {bonificacion}")
print(f"Recargo aplicado: +$ {recargo}")
if descuento_especial > 0:
    print(f"Descuento especial aplicado: -$ {descuento_especial}")
print(f"Subtotal con ajustes: $ {subtotal}")
print(f"IVA (21%): $ {iva}")
print(f"TOTAL A PAGAR: ${total_final:.2f}")
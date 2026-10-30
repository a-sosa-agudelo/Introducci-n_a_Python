# 1. Variables de tipo texto (str)
nombre = input("Ingresa tu nombre: ")
mes = input("¿Para qué mes es este presupuesto?: ")

# 2. Conversión de datos: el input() devuelve texto (str), 
# usamos float() para convertirlo a números decimales
print("\n--- Ingreso de Datos Financieros ---")
ingresos = float(input("Ingresa tus ingresos totales: $"))
gastos_fijos = float(input("Ingresa tus gastos fijos (renta, servicios, etc.): $"))
gastos_variables = float(input("Ingresa tus gastos variables (comida, salidas, etc.): $"))

# Cálculo de variables
gastos_totales = gastos_fijos + gastos_variables
saldo_disponible = ingresos - gastos_totales

# 3. Variable de tipo booleano (bool): Evalúa si es Verdadero (True) o Falso (False)
# Será True si el saldo es mayor o igual a cero.
presupuesto_saludable = saldo_disponible >= 0

# 4. Salida por pantalla mostrando los diferentes tipos de datos
print(f"\n========== REPORTE DE PRESUPUESTO ==========")
print(f"Usuario: {nombre} | Mes: {mes}")
print(f"--------------------------------------------")
print(f"Ingresos:           ${ingresos}")
print(f"Gastos Totales:     ${gastos_totales}")
print(f"Saldo Disponible:   ${saldo_disponible}")
print(f"--------------------------------------------")

# Mostrar el resultado del booleano y tomar una decisión con él
print(f"¿Presupuesto en números positivos?: {presupuesto_saludable}")

if presupuesto_saludable:
    print("Estado: ¡Excelente! Tus finanzas están bajo control este mes.")
else:
    print("Estado: ¡Alerta roja! Estás gastando más de lo que ganas.")
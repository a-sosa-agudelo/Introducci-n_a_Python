# Solicitar al usuario que ingrese dos números
# Usamos float() para convertir el texto ingresado a números decimales
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

# Realizar las operaciones matemáticas básicas
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2

# Mostrar los resultados en pantalla
print("\n--- Resultados de la Calculadora ---")
print(f"Suma: {numero1} + {numero2} = {suma}")
print(f"Resta: {numero1} - {numero2} = {resta}")
print(f"Multiplicación: {numero1} * {numero2} = {multiplicacion}")

# Validar la división para evitar el error de dividir por cero
if numero2 != 0:
    division = numero1 / numero2
    print(f"División: {numero1} / {numero2} = {division}")
else:
    print("División: No es posible dividir entre cero.")
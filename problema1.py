from datetime import date

# Solicitar el nombre del usuario
nombre = input("Por favor, ingresa tu nombre: ")

# Obtener la fecha actual
fecha_actual = date.today()

# Mostrar el mensaje de bienvenida y la fecha de ejecución
print(f"\n¡Hola, {nombre}! Bienvenido a tu primer programa en Python.")
print(f"La fecha de ejecución de este script es: {fecha_actual}")
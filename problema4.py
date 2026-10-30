# Solicitar la calificación
# Usamos .replace(",", ".") de forma preventiva por si ingresas decimales con coma
entrada = input("Ingresa la calificación obtenida (de 0.0 a 5.0): ").replace(",", ".")
nota = float(entrada)

# Validar el rango y determinar si aprobó o reprobó
print("\n--- Sistema de Calificaciones ---")

# Verificamos primero si la nota se sale del rango permitido (0 a 5)
if nota < 0 or nota > 5:
    print("Error: Calificación inválida. El valor ingresado debe estar entre 0 y 5.")
# Si está en el rango y es mayor o igual a 3.0, aprueba
elif nota >= 3.0:
    print(f"Estado: ¡Aprobado! (Nota final: {nota})")
# Si está en el rango pero es menor que 3.0, reprueba
else:
    print(f"Estado: Reprobado. (Nota final: {nota})")
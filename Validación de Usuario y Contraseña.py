# Solicitar nombre de usuario y contraseña
usuario = input("Ingrese su nombre de usuario: ")
admin = "admin"
contraseña = input("Ingrese su contraseña: ")

# Verificar reglas de validación
regla1 = len(usuario) >= 6  # Longitud del usuario debe ser al menos 6 caracteres
regla2 = usuario.isalpha()  # El usuario debe contener solo letras
regla3 = len(contraseña) >= 8  # Longitud de la contraseña debe ser al menos 8 caracteres
regla4 = not (contraseña.isalpha() or contraseña.isnumeric())  # La contraseña no debe ser solo letras o solo números

# Validar el usuario y la contraseña
if regla1 and regla2:
    print("El usuario es válido")
    if usuario == admin:
        print("El usuario admin no es correcto.")

if regla3 and regla4:
    print("La contraseña es válida")
else:
    if "123" in contraseña or "abc" in contraseña or "hola" in contraseña or "contraseña" in contraseña:
        print(f"La contraseña {contraseña} no es segura. No es posible hacer el registro.")
    else:
        print(f"La contraseña {contraseña} no es válida. No fue posible hacer el registro. intente nuevamente.")


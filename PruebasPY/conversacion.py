import g4f

g4f.debug.logging = True  # enable logging
g4f.check_version = False  # Disable automatic version checking

# Bucle para mantener la conversación
while True:
    # El usuario ingresa un mensaje
    user_input = input("Usuario: ")

    # Salir del bucle si el usuario escribe "salir"
    if user_input.lower() == "salir":
        break

    # Crear un mensaje de usuario y obtener la respuesta del modelo
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}],
        stream=True,
    )

    # Imprimir la respuesta del modelo
    for message in response:
        if isinstance(message, dict) and 'content' in message:
            print("Modelo:", message['content'])

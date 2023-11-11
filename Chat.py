import g4f
from colorama import Fore

class Chat:
    def __init__(self):
        g4f.debug.logging = True  # enable logging
        g4f.check_version = False  # Disable automatic version checking

    def hacerPregunta(self, mensaje):

        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": mensaje}],
            stream=True,
        )

        for message in response:
            print(Fore.BLUE + message, flush=True, end='')
        print(Fore.WHITE+" ")

<<<<<<< HEAD
            # Salir del bucle si el usuario escribe "salir"
            if user_input.lower() == "salir":
                print(Fore.WHITE+" Adios")
                break


            response = g4f.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_input}],
                stream=True,
            )

            for message in response:
                print(Fore.BLUE + message, flush=True, end='')

            
=======
        return response
>>>>>>> 78686d96ea77d832ff2bb9468b3a2ae6d6985c30
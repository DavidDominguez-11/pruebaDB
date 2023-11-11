import g4f
from colorama import Fore

class Chat:
    def __init__(self):
        g4f.debug.logging = True  # enable logging
        g4f.check_version = False  # Disable automatic version checking

    def hacerPregunta(self, mensaje):

        toString = ""

        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": mensaje}],
            stream=True,
        )

        #print("tipo" , type(response))
        for message in response:
            print(Fore.BLUE + message, flush=True, end='')
            toString = toString + message
        print(Fore.WHITE+" ")
        #print("Tipo de to String :",type(toString))
        

        return toString

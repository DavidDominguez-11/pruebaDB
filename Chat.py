import g4f

class Chat:
    def __init__(self):
        g4f.debug.logging = True  # enable logging
        g4f.check_version = False  # Disable automatic version checking

    def hacerPregunta(self, msg):
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": msg}],
            stream=True,
        )

        for message in response:
            print("*********************************************************")
            print(message, flush=True, end='')
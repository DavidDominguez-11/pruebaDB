"""
# este funciona pero solo en ingles y es algo mula
from chatbot import demo
demo()
"""

import g4f

g4f.debug.logging = True # enable logging
g4f.check_version = False # Disable automatic version checking
#print(g4f.version) # check version
#print(g4f.Provider.Ails.params)  # supported args


msg = "¿cuantos huesos tiene el cuerpo humano? Responde en idioma kaqchikel"

response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": msg}],
    stream=True,
)

for message in response:
    print(message, flush=True, end='')

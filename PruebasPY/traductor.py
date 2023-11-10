from google.cloud import *
from google.cloud import translate_v2 as translate

# Crear un cliente
client = translate.Client()

# Traducir texto de inglés a español
result = client.translate('Hello, world!', target_language='es')

# Imprimir el resultado
print(result['input'])
print(result['translatedText'])
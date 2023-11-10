from translate import Translator

"""
def translate_text(text, target_language='zh'):
    translator= Translator(to_lang=target_language)
    translation = translator.translate(text)
    print(f'Texto original: {text}')
    print(f'Traducción ({target_language}): {translation}')

if __name__ == '__main__':
    texto_a_traducir = 'Hello, how are you?'
    idioma_destino = 'zh'
    translate_text(texto_a_traducir, target_language=idioma_destino)
"""

import csv

def translate_text(text, target_language='zh'):
    translator = Translator(to_lang=target_language)
    translation = translator.translate(text)
    print(f'Texto original: {text}')
    print(f'Traducción ({target_language}): {translation}\n')

def test_translations_from_csv(csv_file):
    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        i=0
        for row in reader:
            codigo_iso = row['Código ISO-639-1']
            idioma = row['Idioma']

            texto_a_traducir = 'Hello, how are you?'

            try:
                translate_text(texto_a_traducir, target_language=codigo_iso)
            except Exception as e:
                print(f'Error al traducir al idioma {idioma} ({codigo_iso}): {e}')

if __name__ == '__main__':

    csv_file_path = 'idiomas.csv'
    test_translations_from_csv("CodigoIdiomas.csv")

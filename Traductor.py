from translate import Translator

class Traductor:
    def __init__(self, target_language='zh'):
        self.target_language = target_language

    def traducirTexto(self, text):
        translator = Translator(to_lang=self.target_language)
        translation = translator.translate(text)
        print(f'Texto original: {text}')
        print(f'Traducción ({self.target_language}): {translation}')
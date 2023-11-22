from translate import Translator


class Traductor:
    def __init__(self, target_language='ceb'):
        self.target_language = target_language

    def traducirTexto(self, text):
        translator = Translator(to_lang=self.target_language)
        translation = translator.translate(text)
        return translation

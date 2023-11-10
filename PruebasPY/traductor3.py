from googletrans import Translator

translator = Translator()
translator.translate('안녕하세요.')


translator= Translator(to_lang="zh")
translation = translator.translate("This is a pen.")

# aun hay que probar
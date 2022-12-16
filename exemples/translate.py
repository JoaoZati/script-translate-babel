from translate import Translator

translator = Translator(to_lang="en", from_lang='pt')

translation = translator.translate("Isso é uma caneta")
print(translation)

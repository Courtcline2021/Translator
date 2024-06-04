from translate import Translator

translator = Translator(to_lang ="French")
translation = translator.translate("Good Morning! My name is Courtney.")
print(translation)
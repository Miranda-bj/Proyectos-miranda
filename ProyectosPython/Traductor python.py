from googletrans import Translator

traductor = Translator()
traduccion = traductor.translater("Ajax el mejor de holanda", dest="en")
print(traduccion.origin, '-->' , traduccion.text)



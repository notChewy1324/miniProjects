from googletrans import Translator

translator = Translator()

txt = input("Type anything... ")

usrTXT = translator.translate(f"{txt}", dest='es')
print(f"{usrTXT.origin} ({usrTXT.src}) ---> {usrTXT.text} ({usrTXT.dest})")
from googletrans import Translator

translator = Translator()

usr = input("\nType anything... ")

usrTXT = translator.translate(f"{usr}", dest='es') #change the 'dest' to change the output language
print(f"\nTranslation: {usrTXT.origin} ({usrTXT.src}) ---> {usrTXT.text} ({usrTXT.dest})\n")
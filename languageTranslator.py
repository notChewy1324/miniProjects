from googletrans import Translator

translator = Translator()

txt = input("Type anything... ")

usrTXT = translator.translate(f"{txt}", dest='es') #change the 'dest' to change the output language
print(f"{usrTXT.origin} ({usrTXT.src}) ---> {usrTXT.text} ({usrTXT.dest})")


sentences = [
    "Hello World",
    "Just setting up some code",
    "what the dog doing",
    "Bye World"
]

translations = translator.translate(sentences, dest="ar")
for translation in translations: #translate many different lines at once
    print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

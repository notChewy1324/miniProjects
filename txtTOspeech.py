import gtts
from playsound import playsound

while True:
    
    usrTXT = input("Type anything... ")
    tts = gtts.gTTS(f"{usrTXT}", lang="en") #change the 'lang' to change the output language
    tts.save("tts.mp3")
    playsound("tts.mp3")
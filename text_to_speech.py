import pyttsx3
engine=pyttsx3.init()
s=input("")
engine.setProperty("rate",30)
voice=engine.getProperty("voices")
print(voice[0].id)
engine.setProperty("voices",voice[1].id)
engine.say(s)
engine.runAndWait()
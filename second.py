from gtts import gTTS
import os

mytext = 'Merhaba, ben Python ile yapılmış bir sesli asistanım!'
language = 'tr'

myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("welcome.mp3")
os.system("welcome.mp3")

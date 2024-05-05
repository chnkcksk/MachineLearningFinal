import speech_recognition as sr
from gtts import gTTS
import os

# Ses tanıma için recognizer nesnesi
r = sr.Recognizer()

# Mikrofon ile ses yakaladik
with sr.Microphone() as source:
    print("Bir şeyler söyleyin:")
    audio = r.listen(source)

# Google Web Speech API kullanarak sesi metne çevirdik
try:
    text = r.recognize_google(audio, language='tr-TR')
    print("Söyledikleriniz: " + text)
except sr.UnknownValueError:
    print("Google Web Speech API sesi anlayamadı")
except sr.RequestError as e:
    print(f"Google Web Speech API servisinden yanıt alınamadı; {e}")


# Sese donusturme

#myobj = gTTS(text=text, lang='tr', slow=False)
#myobj.save("welcome.mp3")
#os.system("welcome.mp3")

import tkinter as tk
import speech_recognition as sr
import requests
import webbrowser
from datetime import datetime


def recognize_speech():
    # Ses tanıma için recognizer nesnesi
    r = sr.Recognizer()

    with sr.Microphone() as source:
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language='tr-TR')

        if "web'de ara" in text:
            search_query = text.replace("web'de ara", "").strip()
            url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(url)
            response_text = f"{search_query} için web araması yapılıyor."
        else:

            if "saat kaç" in text:
                now = datetime.now()
                current_time = now.strftime("%H:%M")
                response_text = f"Şu anda saat {current_time}."
            elif "hava kaç derece" in text:
                city = text.split(' ')[0]
                api_key = "b7b6e7e3c4e868a5b18bafb537516668"
                weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
                response = requests.get(weather_url)
                weather_data = response.json()

                if 'main' in weather_data:
                    temp = weather_data['main']['temp']
                    response_text = f"Şu anda {city} şehrinde hava {temp} derece."
                else:
                    response_text = "Hava durumu bilgisi alınamadı."
            else:
                response_text = text

        result_label.config(text=response_text)

    except sr.UnknownValueError:
        result_label.config(text="Google Web Speech API sesi anlayamadı")
    except sr.RequestError as e:
        result_label.config(text=f"Google Web Speech API servisinden yanıt alınamadı; {e}")


# -------------------- GUI oluşturmak icin gereken kodumuz -----------------------
root = tk.Tk()
root.title("Sesli Komut Asistanı")
root.geometry("500x300")

instruction_label = tk.Label(root, text=" Lütfen 'Dinle' düğmesine basın ve mikrofona konuşun.\n", font=("Arial", 22))
instruction_label.pack(padx=10, pady=10)

instruction_label = tk.Label(root, text="Örnek:\n"
                                        "Ankara şehrinde hava kaç derece\n"
                                        "Saat kaç\n"
                                        "Web'de ara Hitit Tarihi", font=("Arial", 22))
instruction_label.pack()

# Sonucu gösteren kisim
result_label = tk.Label(root, text="", wraplength=500, font=("Arial", 25), bg='#fff', fg='#f00')
instruction_label.pack(padx=10, pady=10)
result_label.pack()

listen_button = tk.Button(root,
                          text="Dinle",
                          command=recognize_speech,
                          relief="raised",
                          width=10,
                          height=2)
listen_button.pack(padx=10, pady=10)

root.geometry("800x600")

root.mainloop()

# -----------------------------------------------------------------------------------

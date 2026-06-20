from gtts import gTTS
import os
txt = input("Enter the text you want to convert to speech: ")
print("choose your language :")
print("en = English")
print("fr = French")
print("es = Spanish")
Lang = input("Enter the language code: ").strip().lower()
if Lang not in ['en', 'fr', 'es']:
    print("Invalid language code. Defaulting to English.")
    Lang = 'en'
    print("Converting text to speech...")
res = gTTS(text=txt, lang=Lang)
res.save("audio.mp3")
print("Audio file saved as audio.mp3")
except Exception as e:
    print(f"An error occurred: {e}")
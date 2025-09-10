import speech_recognition as sr
import pyttsx3
import subprocess
import os
import winsound
import threading
import time
from datetime import datetime
import sounddevice as sd
import numpy as np

class VoiceAssistant:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  
        self.engine.setProperty('volume', 0.8)
        
        self.recognizer = sr.Recognizer()
        self.sample_rate = 16000
        self.channels = 1
        
        self.wake_word = "ok garmin"
        
        self.listening = True
        
        print("Dites 'ok garmin' suivi d'une commande.")
        print("Commandes disponibles:")
        print("- 'ouvre notepad'")
        print("- 'ouvre la calculatrice'")
        print("- 'quelle heure est-il'")
        print("- 'arrête-toi' pour quitter")
        print("-" * 50)
    
    def play_beep(self):
        try:
            winsound.Beep(1000, 200) # remplacer par le beep 
        except:
            print("Erreur de son")  
    
    def listen_for_command(self):
        try:
            print("En train d'écouter...")
            
            duration = 6 # secondes
            audio_data = sd.rec(int(duration * self.sample_rate), 
                              samplerate=self.sample_rate, 
                              channels=self.channels, 
                              dtype='int16')
            sd.wait()
            
            audio_data = audio_data.flatten().astype(np.int16)
            audio_bytes = audio_data.tobytes()
            
            audio = sr.AudioData(audio_bytes, self.sample_rate, 2)
            
            command = self.recognizer.recognize_google(audio, language='fr-FR')
            return command.lower()
                
        except sr.UnknownValueError:
            return None
        except sr.RequestError as e:
            print(f"Erreur de service de reconnaissance vocale: {e}")
            return None
        except Exception as e:
            print(f"Erreur d'enregistrement audio: {e}")
            return None

def main():
    try:
        assistant = VoiceAssistant()
        print("Assistant vocal initialisé avec succès.")
    except Exception as e:
        print(f"Erreur lors du démarrage: {e}")

if __name__ == "__main__":
    main()
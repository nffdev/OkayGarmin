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

def main():
    try:
        assistant = VoiceAssistant()
        print("Assistant vocal initialisé avec succès.")
    except Exception as e:
        print(f"Erreur lors du démarrage: {e}")

if __name__ == "__main__":
    main()
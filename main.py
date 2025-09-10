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
    
    def speak(self, text):
        print(f"Assistant: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
    
    def execute_action(self, action):
        action = action.strip()
        
        if "bloc notes" in action or "notepad" in action:
            try:
                subprocess.Popen(["notepad.exe"])
                self.speak("J'ouvre le bloc-notes")
            except Exception as e:
                self.speak("Désolé, je n'ai pas pu ouvrir le bloc-notes")
                print(f"Erreur: {e}")
        
        elif "calculatrice" in action or "calc" in action:
            try:
                subprocess.Popen(["calc.exe"])
                self.speak("J'ouvre la calculatrice")
            except Exception as e:
                self.speak("Désolé, je n'ai pas pu ouvrir la calculatrice")
                print(f"Erreur: {e}")
        
        elif "heure" in action or "temps" in action:
            current_time = datetime.now().strftime("%H heures %M")
            self.speak(f"Il est {current_time}")
        
        elif "arrête" in action or "stop" in action or "quitte" in action:
            self.speak("Au revoir!")
            self.listening = False
        
        else:
            self.speak("Désolé, je n'ai pas compris cette commande")
            print(f"Commande non reconnue: {action}")
    
    def process_command(self, full_command):
        if self.wake_word in full_command:
            action = full_command.replace(self.wake_word, "").strip()
            if action:
                print(f"Action détectée: {action}")
                self.execute_action(action)
            else:
                 self.speak("Oui, je vous écoute. Que puis-je faire pour vous?")
    
    def run(self):
        """Boucle principale de l'assistant"""
        print("Assistant vocal démarré. Parlez maintenant...")
        
        while self.listening:
            try:
                command = self.listen_for_command()
                
                if command:
                    print(f"Commande entendue: {command}")
                    
                    if self.wake_word in command:
                        print(f"Ok garmin '{self.wake_word}' détecté!")
                        
                        threading.Thread(target=self.play_beep, daemon=True).start()
                        
                        self.process_command(command)
                
                time.sleep(0.1)
                
            except KeyboardInterrupt:
                print("\nArrêt demandé par l'utilisateur")
                self.speak("Au revoir!")
                break
            except Exception as e:
                print(f"Erreur inattendue: {e}")
                time.sleep(1)

def main():
    try:
        assistant = VoiceAssistant()
        assistant.run()
    except Exception as e:
        print(f"Erreur lors du démarrage: {e}")

if __name__ == "__main__":
    main()
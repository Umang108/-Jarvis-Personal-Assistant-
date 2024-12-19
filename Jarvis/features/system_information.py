import platform
import psutil
import requests
import json
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def system_check():
   
    system_info = platform.uname()
    cpu_usage = psutil.cpu_percent()
    mem_info = psutil.virtual_memory()

  
    speak("System Information:")
    speak(f"System: {system_info.system}")
    speak(f"Node Name: {system_info.node}")
    speak(f"Release: {system_info.release}")
    speak(f"Version: {system_info.version}")
    speak(f"Machine: {system_info.machine}")
    speak(f"Processor: {system_info.processor}")
    speak(f"CPU Usage: {cpu_usage}%")
    speak(f"Total Memory: {mem_info.total / (1024 ** 3):.2f} GB")
    speak(f"Available Memory: {mem_info.available / (1024 ** 3):.2f} GB")
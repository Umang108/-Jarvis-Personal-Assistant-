import pyautogui
import pyttsx3
import time

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def youtube_control(action):
    if action == "play":
        pyautogui.press('space')
        speak("Playing the video")
    elif action == "pause":
        pyautogui.press('space')
        speak("Pausing the video")
    elif action == "mute":
        pyautogui.press('m')
        speak("Muting the video")
    elif action == "volume up":
        pyautogui.press('up')
        speak("Increasing the volume")
    elif action == "volume down":
        pyautogui.press('down')
        speak("Decreasing the volume")
    else:
        speak("Sorry, I didn't understand that command.")
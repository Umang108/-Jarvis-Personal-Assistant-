from Jarvis import JarvisAssistant
import re
import os
import random
import pprint
from plyer import notification
import datetime
import pyaudio
import wave
import requests
import sys
import urllib.parse  
import pyjokes
import time
import keyboard
import pyautogui
import pyjokes
from pytube import YouTube
import pywhatkit
from pygame import mixer
import wolframalpha
from PIL import Image
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from Jarvis.features.gui import Ui_MainWindow
from Jarvis.features.system_information import system_check
from Jarvis.features.game import game_play, takeCommand
from Jarvis.features.translator import translategl
from Jarvis.config import config

obj = JarvisAssistant()

GREETINGS = ["hello jarvis", "jarvis", "wake up jarvis", "you there jarvis", "time to work jarvis", "hey jarvis",
             "ok jarvis", "are you there"]
GREETINGS_RES = ["always there for you sir", "i am ready sir",
                 "your wish my command", "how can i help you sir?", "i am online and ready sir"]

EMAIL_DIC = {
    'myself': 'akumarmth5@gmail.com',
    'my official email': 'akumarmth5@gmail.com',
    'my second email': 'akumarmth5@gmail.com',
    'my official mail': 'akumarmth5@gmail.com',
    'my second mail': 'akumarmth5@gmail.com'
}

CALENDAR_STRS = ["what do i have", "do i have plans", "am i busy"]



def speak(text):
    obj.tts(text)


app_id = config.wolframalpha_id


def computational_intelligence(question):
    try:
        client = wolframalpha.Client(app_id)
        answer = client.query(question)
        answer = next(answer.results).text
        print(answer)
        return answer
    except:
        speak("Sorry sir I couldn't fetch your question's answer. Please try again ")
        return None
    
def startup():
    speak("Initializing Jarvis")
    speak("Starting all systems applications")
    speak("Now I am online")
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    c_time = obj.tell_time()
    speak("I am Jarvis. Online and ready sir. Please tell me how may I help you")

def WolfRamAlpha(query):
    apikey = "87EH36-VQXKHQHJ97"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("The value is not answerable")

def Calc(query):
    Term = str(query)
    Term = Term.replace("jarvis","")
    Term = Term.replace("multiply","*")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("divide","/")

    Final = str(Term)
    try:
        result = WolfRamAlpha(Final)
        print(f"{result}")
        speak(result)

    except:
        speak("The value is not answerable")

def alarm(command):
    timehere = open("Alarmtext.txt","a")
    timehere.write(command)
    timehere.close()
    os.startfile("alarm.py")

def record_audio(filename, duration=5):
    chunk = 1024
    format = pyaudio.paInt16
    channels = 1
    rate = 44100

    audio = pyaudio.PyAudio()

    stream = audio.open(format=format,
                        channels=channels,
                        rate=rate,
                        input=True,
                        frames_per_buffer=chunk)

    print("Recording...")

    frames = []

    for i in range(0, int(rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    print("Finished recording.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(audio.get_sample_size(format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()

def down_yt_song(url, save_path):
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_stream.download(output_path=save_path)
        speak("Song downloaded successfully!")
    except Exception as e:
        speak(f"An error occurred: {e}")

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    c_time = obj.tell_time()
    speak(f"Currently it is {c_time}")
    speak("I am Jarvis. Online and ready sir. Please tell me how may I help you")

def programming_joke():
    joke = pyjokes.get_joke()
    print(joke)
    speak(joke)
# if __name__ == "__main__":


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    def TaskExecution(self):
        startup()
        wish()

        while True:
            command = obj.mic_input()

            if re.search('date', command):
                date = obj.tell_me_date()
                print(date)
                speak(date)

            elif "time" in command:
                time_c = obj.tell_time()
                print(time_c)
                speak(f"Sir the time is {time_c}")

            
            elif command in GREETINGS:
                speak(random.choice(GREETINGS_RES))

            
            

            elif re.search('tell me about', command):
                topic = command.split(' ')[-1]
                if topic:
                    wiki_res = obj.tell_me(topic)
                    print(wiki_res)
                    speak(wiki_res)
                else:
                    speak(
                        "Sorry sir. I couldn't load your query from my database. Please try again")

            elif "calculate" in command:
                    command = command.replace("calculate","")
                    command = command.replace("jarvis","")
                    Calc(command) 

            elif "open" in command:  
                command = command.replace("open","")
                command = command.replace("jarvis","")
                pyautogui.press("super")
                pyautogui.typewrite(command)
                pyautogui.sleep(2)
                pyautogui.press("enter")

            elif "whatsapp" in command:
                from Jarvis.features.whatsapp import sendMessage
                sendMessage() 

            elif "open" in command:
                from Jarvis.features.dict import openappweb
                openappweb(command)
            elif "close" in command:
                from Jarvis.features.dict import closeappweb
                closeappweb(command)

            elif "schedule my day" in command:
                tasks = []  
                speak("Do you want to clear old tasks (Plzspeak YES or NO)")
                command = takeCommand().lower()
                if "yes" in command:
                    file = open("tasks.txt","w")
                    file.write(f"")
                    file.close()
                    no_tasks = int(input("Enter the no. of tasks :- "))
                    i = 0
                    for i in range(no_tasks):
                        tasks.append(input("Enter the task :- "))
                        file = open("tasks.txt","a")
                        file.write(f"{i}. {tasks[i]}\n")
                        file.close()
                elif "no" in command:
                    i = 0
                    no_tasks = int(input("Enter the no. of tasks :- "))
                    for i in range(no_tasks):
                        tasks.append(input("Enter the task :- "))
                        file = open("tasks.txt","a")
                        file.write(f"{i}. {tasks[i]}\n")
                        file.close()

            elif "translate" in command: 
                command = command.replace("jarvis","")
                command = command.replace("translate","")
                translategl(command)

            elif "show my schedule" in command:
                file = open("tasks.txt","r")
                content = file.read()
                file.close()
                mixer.init()
                mixer.music.load("noti.mp3")
                mixer.music.play()
                notification.notify(
                    title = "My schedule :-",
                    message = content,
                    timeout = 15
                    ) 

            elif "click my photo" in command:
                pyautogui.press("super")
                pyautogui.typewrite("camera")
                pyautogui.press("enter")
                pyautogui.sleep(2)
                speak("SMILE")
                pyautogui.press("enter")

            elif "programming jokes" in command:
                programming_joke()

            elif "voice recording" in command:
                filename = "recorded_audio.wav"
                record_audio(filename)
                print(f"Audio recorded and saved as {filename}")

            if "download song" in command:
                url = input("Enter the YouTube URL of the song: ")
                save_path = input("Enter the directory where you want to save the song: ")
                speak("Downloading the song, please wait.")
                down_yt_song(url, save_path)


            elif "buzzing" in command or "news" in command or "headlines" in command:
                news_res = obj.news()
                speak('Source: The Times Of India')
                speak('Todays Headlines are..')
                for index, articles in enumerate(news_res):
                    pprint.pprint(articles['title'])
                    speak(articles['title'])
                    if index == len(news_res)-2:
                        break
                speak('These were the top headlines, Have a nice day Sir!!..')

            elif "shutdown the system" in command:
                speak("Are You sure you want to shutdown")
                shutdown = input("Do you wish to shutdown yourcomputer? (yes/no)")
                if shutdown == "yes":
                    os.system("shutdown /s /t 1")

                elif shutdown == "no":
                    break 

            

            elif 'youtube' in command:
                video = command.split(' ')[1]
                speak(f"Okay sir, playing {video} on youtube")
                pywhatkit.playonyt(video)

            elif "generate qr code" in command:
                data = input("Enter the data for the QR code: ")
                from Jarvis.features.qrcodes import generate_and_show_qr_code
                generate_and_show_qr_code(data)


            elif "ip address" in command:
                ip = requests.get('https://api.ipify.org').text
                print(ip)
                speak(f"Your ip address is {ip}")
            
            elif "device check" in command:
                system_check()
            
            elif "play a game" in command:
                game_play()

            elif "take screenshot" in command or "take a screenshot" in command or "capture the screen" in command:
                speak("By what name do you want to save the screenshot?")
                name = obj.mic_input()
                speak("Alright sir, taking the screenshot")
                img = pyautogui.screenshot()
                name = f"{name}.png"
                img.save(name)
                speak("The screenshot has been succesfully captured")

            elif "show me the screenshot" in command:
                try:
                    img = Image.open('D://JARVIS//JARVIS_2.0//' + name)
                    img.show(img)
                    speak("Here it is sir")
                    time.sleep(2)

                except IOError:
                    speak("Sorry sir, I am unable to display the screenshot")

            

            elif "wikipedia" in command:
                from Jarvis.features.search import searchWikipedia
                searchWikipedia(command)
            elif "pause" in command:
                pyautogui.press("k")
                speak("video paused")
            elif "play" in command:
                pyautogui.press("k")
                speak("video played")
            elif "mute" in command:
                pyautogui.press("m")
                speak("video muted")

            elif "volume up" in command:
                from keyboard import volumeup
                speak("Turning volume up,sir")
                volumeup()
            elif "volume down" in command:
                from keyboard import volumedown
                speak("Turning volume down, sir")
                volumedown()

            elif "set an alarm" in command:
                print("input time example:- 10 and 10 and 10")
                speak("Set the time")
                a = input("Please tell the time :- ")
                alarm(a)
                speak("Done,sir")
            

            elif "what do i have" in command or "do i have plans" or "am i busy" in command:
                obj.google_calendar_events(command)

            elif "remember that" in command:
                rememberMessage = command.replace("remember that","")
                rememberMessage = command.replace("jarvis","")
                speak("You told me to remember that"+rememberMessage)
                remember = open("Remember.txt","a")
                remember.write(rememberMessage)
                remember.close()

            elif "what do you remember" in command:
                remember = open("Remember.txt","r")
                speak("You told me to remember that" + remember.read())

            elif "goodbye" in command or "offline" in command or "bye" in command:
                speak("Alright sir, going offline. It was nice working with you")
                sys.exit()

            elif "email" in command or "send email" in command:
                sender_email = config.email
                sender_password = config.email_password

                try:
                    speak("Whom do you want to email sir ?")
                    recipient = obj.mic_input()
                    receiver_email = EMAIL_DIC.get(recipient)
                    if receiver_email:

                        speak("What is the subject sir ?")
                        subject = obj.mic_input()
                        speak("What should I say?")
                        message = obj.mic_input()
                        msg = 'Subject: {}\n\n{}'.format(subject, message)
                        obj.send_mail(sender_email, sender_password,
                                      receiver_email, msg)
                        speak("Email has been successfully sent")
                        time.sleep(2)

                    else:
                        speak(
                            "I coudn't find the requested person's email in my database. Please try again with a different name")

                except:
                    speak("Sorry sir. Couldn't send your mail. Please try again")

                       
            elif "what is" in command or "who is" in command:
                question = command
                answer = computational_intelligence(question)
                speak(answer)


            elif "joke" in command:
                from Jarvis.features.jock import tell_joke
                tell_joke()

            elif "system" in command:
                sys_info = obj.system_info()
                print(sys_info)
                speak(sys_info)

            elif "where is" in command:
                place = command.split('where is ', 1)[1]
                current_loc, target_loc, distance = obj.location(place)
                city = target_loc.get('city', '')
                state = target_loc.get('state', '')
                country = target_loc.get('country', '')
                time.sleep(1)
                try:

                    if city:
                        res = f"{place} is in {state} state and country {country}. It is {distance} km away from your current location"
                        print(res)
                        speak(res)

                    else:
                        res = f"{state} is a state in {country}. It is {distance} km away from your current location"
                        print(res)
                        speak(res)

                except:
                    res = "Sorry sir, I couldn't get the co-ordinates of the location you requested. Please try again"
                    speak(res)

            

            elif "switch the window" in command or "switch window" in command:
                speak("Okay sir, Switching the window")
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif "where i am" in command or "current location" in command or "where am i" in command:
                try:
                    city, state, country = obj.my_location()
                    print(city, state, country)
                    speak(
                        f"You are currently in {city} city which is in {state} state and country {country}")
                except Exception as e:
                    speak(
                        "Sorry sir, I coundn't fetch your current location. Please try again")

           

            elif "hide all files" in command or "hide this folder" in command:
                os.system("attrib +h /s /d")
                speak("Sir, all the files in this folder are now hidden")

            elif "visible" in command or "make files visible" in command:
                os.system("attrib -h /s /d")
                speak("Sir, all the files in this folder are now visible to everyone. I hope you are taking this decision in your own peace")

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def __del__(self):
        sys.stdout = sys.__stdout__

    # def run(self):
    #     self.TaskExection
    def startTask(self):
        self.ui.movie = QtGui.QMovie("Jarvis/utils/images/live_wallpaper.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("Jarvis/utils/images/initiating.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())



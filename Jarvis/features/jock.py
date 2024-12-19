import random
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def tell_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!",
        "Parallel lines have so much in common. It's a shame they'll never meet.",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why did the bicycle fall over? Because it was two-tired!",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "Why don't skeletons fight each other? They don't have the guts!",
        "Why couldn't the leopard play hide and seek? Because he was always spotted!",
        "Why don't eggs tell jokes? Because they might crack up!",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "What do you call fake spaghetti? An impasta!",
        "What do you get when you cross a snowman and a vampire? Frostbite!",
        "Why don't oysters donate to charity? Because they're shellfish!",
        "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
        "Why was the math book sad? Because it had too many problems."
    ]

    joke = random.choice(jokes)
    print(joke)
    speak(joke)
    
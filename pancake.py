import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_feedback(joke):
    try:
        with sr.Microphone() as source:
            print("Listening to your feedback")
            voice  = listener.listen(source)
            feed = listener.recognize_google(voice)
            feed =  feed.lower()
            talk("I really appreciate your feedback")
            talk(joke)
    except NameError:
        print("An exception occurred")
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            cmd = listener.recognize_google(voice)
            cmd = cmd.lower()
            if 'pancake' in cmd:
                cmd = cmd.replace('pancake', '')
                print(cmd)
    except NameError:
        print("An exception occurred")
    return cmd


def run_alexa():
    command = take_command()
    try:
        if command == "bonzibuddy":
            talk("Sorry, I didn't get that")
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'open' in command:
            cmd = command.replace('open', '')
            pywhatkit.search(cmd)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        elif 'loco' in command:
            talk('Fuck you too')
        elif 'date' in command:
            talk('sorry, I have a headache')
        elif 'are you single' in command:
            talk("What do u want lol")
            talk('I am in a relationship with wifi')
        elif 'joke' in command:
            joke = pyjokes.get_joke()
            talk(joke)
            talk("Did you enjoy the joke?")
            get_feedback(joke)
    except NameError:
        talk("Can you repeat that please?")

while True:      
    run_alexa()
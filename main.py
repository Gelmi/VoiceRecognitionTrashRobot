import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'robot' in command:
                command = command.replace('robot', '')
                print(command)
    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        pass
    return command

def run_voice_assistant():
    command = take_command()
    if 'help me' in command:
        talk('How can I assist you?')
    else:
        talk('Sorry, I did not understand that.')

while True:
    run_voice_assistant()
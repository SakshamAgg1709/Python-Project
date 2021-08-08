import pyttsx3 #We have to install it
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')#sapi5 is a speech API
voices = engine.getProperty('voices')
# print(voices[1].id)

engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("Good Morning!")
    elif hour >=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening")

    speak("Hello sir, I am Zira, your Personal assistant. Please tell how can I help you!")  


def takeCommand():
    '''
    It takes microphone input and returns string output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said - {query}")

    except Exception as e:
        # print(e)

        print("Say that again please")
        return "None"

    pass

def sendEmail(to, content):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.login('youremail@gmail.com', 'yourpassword_here')
    server.sendmail('youremail@gmail.com', to ,content)
    server.close()



if __name__ == "__main__" :
    # wishMe()

    while True:
        query = takeCommand()
        query = str(query).lower()

        #Logic for executing tasks based on query
        if 'wikipedia' in query :
            speak('Searching in Wikipedia...')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According To Wikipedia")
            speak(results)
            print(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'play music' in query:
            music_dir = 'F:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H%M%S")
            speak(f"Sir the time is {strtime}")

        elif 'open code' in query:
            codepath = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'send mail to' in query:
            try:
                speak("What should I say")
                content = takeCommand()
                to = "sabusiness1709@gmail.com"
                sendEmail(to, content)
                speak("Mail has been sent")

            except Exception as e:
                print(e)
                print("Soory i can't send the email")


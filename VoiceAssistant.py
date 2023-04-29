import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import wikipedia #pip install wikipedia
import datetime #pip install datetime
import os #pip install os
import webbrowser #pip install webbrowser
import pyfiglet #pip install pyfiglet        #if you face any problem email me at perrythehackerrr@gmail.com

print(pyfiglet.figlet_format("VOICE ASSISTANT"))
print("CODED BY - PARTH SHARMA YT - @techyperry_ INSTA - parth._.sharma8")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak(" sir how can i help you.")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("https://youtube.com")

        elif 'open chat gpt' in query:
            speak("opening chat gpt")
            webbrowser.open("https://chat.openai.com/")

        elif 'open my website' in query:
            speak("opening your website")
            webbrowser.open("add any website you want")   

        elif 'open instagram' in query:
            speak("opening instagram")
            webbrowser.open("https://instagram.com")

        elif 'open whatsapp' in query:
            speak("opening whatsapp")
            webbrowser.open("https://web.whatsapp.com")

        #you can add many more features like "open facebook"     

            
        elif 'play music' in query:
            music_dir = 'C:/Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'tell me time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\perry\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open notepad' in query:
            speak("opening notepad")
            os.startfile("notepad.exe")

        elif 'shutdown pc' in query:
            speak("Shutting down the computer")
            os.system("shutdown /s /t 1")

        elif 'open cmd' in query:
            speak("opening cmd")
            os.startfile("cmd.exe")

        elif 'how are you' in query:
            speak("i am fine sir.whats about you")

        elif 'who created you' in query:
            speak("i am coded by perry sir its you! hehe")

        elif 'are you feeling nervous' in query:
            speak("no sir")

        elif 'do you like alexa or google' in query:
            speak("no i am smarter than them")

        elif 'what is your name' in query:
            speak("i am  the personal voice assistant!") # give any name you like

        elif 'what is your aim' in query:
            speak("to make you happy sir")

       #you can also add more command like 'you are good'



            #Techyperry #give star if you like this code

                

        
    

    

    
    


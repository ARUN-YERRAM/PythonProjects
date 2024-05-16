import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import speech_recognition as sr


print("Initializing JARVIS")
MASTER = "ARUN"
# speak("Initializing JARVIS")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#  Speak function will pronounce the string which is passed to it.
def speak(text):

    engine.say(text)
    engine.runAndWait()

# speak("Initializing JARVIS...")
# speak("Arun and BHARATHCHANDRA is Good Boy")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if(hour>=0 and hour<12):
        speak("Good Morning" + MASTER)

    elif hour>=12 and hour<18:
        speak("Good Afternoon" + MASTER)

    else:
        speak("Good Evening" + MASTER)
    
    speak("I am assistant. How may I Help you?")




def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    # import speech_recognition as sr

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
    # Your code to capture audio goes here

        try :
            print("Recognizing...")
            query = r.recognize_google(audio, Language='en-in')
            print(f"user said: {query}\n")

        except Exception as e:
            print("Say that again Please")
            query = "Say that again Please"

        return query


#  Main program starts here...
speak("Initalizing JARVIS...")
# wishMe()
# query = takeCommand()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yerramarun9848@gmail.com', 'password')
    serve.sendmail("yerramarun9848@gmail.com", to, content)
    server.close()

# logic for basic tasks....
def main():

    # speak("Initializing JARVIS...")
    wishMe()
    query = takeCommand()

    if 'wikipedia' in query.lower():

            speak('Searching Wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

    elif 'open youtube' in query.lower():
        # webbrowser.open("youtube.com")
        url = "youtube.com"
        chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif 'open google' in query.lower():
        # webbrowser.open("google.com")
        url = "google.com"
        # chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'
        chrome_path = "C:\Program Files\Google\Chrome\Application"
        webbrowser.get(chrome_path).open(url)

    elif 'open stackoverflow' in query.lower():
        url = "reddit.com"
        chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'
        # webbrowser.open("stackoverflow.com")
        webbrowser.get(chrome_path).open(url)

    elif 'play music' in query.lower():
        # music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
        music_dir = 'C:\\Users\\Yerram Abhilash\\Music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))

    elif 'the time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")

    elif 'open code' in query.lower():
        # codePath = "C:/Users/Yerram Abhilash/AppData/Local/Programs/Microsoft VS Code/Code.exe"
        codePath =  "C:\\Users\\Yerram Abhilash\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe %s"
        
        os.startfile(codePath)

    elif 'email to arun' in query.lower():
        try:
            speak("What should I send")
            content = takeCommand()
            to = "techiegiglover05@gmail.com"
            sendEmail(to,content)
            speak("Email has been sent successfully")
        except Exception as e:
            print(e)

main()





# import pyttsx3
# import datetime
# import wikipedia
# import webbrowser
# import os
# import smtplib
# import speech_recognition as sr

# print("Initializing JARVIS")
# MASTER = "ARUN"

# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# def wishMe():
#     hour = int(datetime.datetime.now().hour)
#     if 0 <= hour < 12:
#         speak("Good Morning " + MASTER)
#     elif 12 <= hour < 18:
#         speak("Good Afternoon " + MASTER)
#     else:
#         speak("Good Evening " + MASTER)
    
#     speak("I am JARVIS. How may I help you?")

# def takeCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         audio = r.listen(source)
#         print("Recognizing...")
        
#         try:
#             query = r.recognize_google(audio, language='en-in')
#             print(f"User said: {query}\n")
#         except Exception as e:
#             print("Say that again, please")
#             query = None

#     return query

# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('your_email@gmail.com', 'your_password')
#     server.sendmail('your_email@gmail.com', to, content)
#     server.close()

# def main():
#     wishMe()
#     query = takeCommand()

#     if 'wikipedia' in query.lower():
#         speak('Searching Wikipedia')
#         query = query.replace("wikipedia", "")
#         results = wikipedia.summary(query, sentences=2)
#         speak("According to Wikipedia")
#         print(results)
#         speak(results)

#     elif 'open youtube' in query.lower():
#         url = "https://www.youtube.com"
#         webbrowser.open(url)

#     elif 'open google' in query.lower():
#         url = "https://www.google.com"
#         webbrowser.open(url)

#     elif 'open stackoverflow' in query.lower():
#         url = "https://www.stackoverflow.com"
#         webbrowser.open(url)

#     elif 'play music' in query.lower():
#         music_dir = 'C:\\Users\\Yerram Abhilash\\Music'
#         songs = os.listdir(music_dir)
#         if songs:
#             os.startfile(os.path.join(music_dir, songs[0]))
#         else:
#             speak("No music files found in the directory.")

#     elif 'the time' in query.lower():
#         strTime = datetime.datetime.now().strftime("%H:%M:%S")
#         speak(f"Sir, the time is {strTime}")

#     elif 'open code' in query.lower():
#         codePath = "C:\\Users\\Yerram Abhilash\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
#         os.startfile(codePath)

#     elif 'email to arun' in query.lower():
#         try:
#             speak("What should I send?")
#             content = takeCommand()
#             to = "techiegiglover05@gmail.com"
#             sendEmail(to, content)
#             speak("Email has been sent successfully")
#         except Exception as e:
#             print(e)

# if __name__ == "__main__":
    # main()

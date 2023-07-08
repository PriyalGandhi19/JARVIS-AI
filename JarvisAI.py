# wikipedia,jokes,news,yuotube,google,time,spotify,code,email,quit

import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import json
# import spotipy
import requests
import random

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait() 

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in') 
            print(f"User said: {query}\n") 

        except Exception as e:
            print("Say that again please...")  
            return "None" 
        return query
    

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('priyal.glsbca21@gmail.com', 'priyal@14')
    server.sendmail('priyal.glsbca21@gmail.com', to, content)
    server.close() 



def get_news_headlines():
    NEWS_API_KEY = 'b0ececc2694c47d0b7fc9c3843c0b6e4'
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    data = json.loads(response.text)
    
    if response.status_code == 200:
        articles = data['articles']
        headlines = [article['title'] for article in articles]
        return headlines
    else:
        return None
    
jokes = [
    {
        'setup': 'Why dont scientists trust atoms?',
        'punchline': 'Because they make up everything!'
    },
    {
        'setup': 'Why did the scarecrow win an award?',
        'punchline': 'Because he was outstanding in his field!'
    },
    {
        'setup': 'What does my dad have in common with Nemo?',
        'punchline': 'They both cant be found.!'
    },
    {
        'setup': 'it turns out a major new study recently found that humans eat more bananas than monkeys.',
        'punchline': 'Its true. I cant remember the last time I ate a monkey.!'
    },
    {
        'setup': 'When does a joke become a dad joke?',
        'punchline': 'When it leaves and never comes back.!'
    },
    {
        'setup': 'Whats the last thing to go through a flys head as it hits the windshield of a car going 70 miles per hour?',
        'punchline': 'Its butt.!'
    }
]

def get_random_joke():
    return random.choice(jokes)

# def playSong():
#     username = 'amh43tjnvqhuj1b0fkuzci6ga'
#     clientID = 'fecbc65e2daa40268af6d1d5d8c9b307'
#     clientSecret = '5d4c72b09fe24aec83532fd3689dc570'
#     redirect_uri = 'http://.com/callback/'
#     oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri)
#     token_dict = oauth_object.get_access_token()
#     token = token_dict['access_token']
#     spotifyObject = spotipy.Spotify(auth=token)
#     user_name = spotifyObject.current_user()

#     # To print the JSON response from
#     # browser in a readable format.
#     # optional can be removed
#     print(json.dumps(user_name, sort_keys=True, indent=4))

# def process_command(command):
#     if "play" in command:
#         # Extract the song or artist name from the command and search in Spotify
#         # Use the spotipy library to play the song using the URI or track ID
#         pass
#     elif "pause" in command:
#         # Pause the currently playing track
#         pass
#     elif "resume" in command:
#         # Resume the playback if paused
#         pass
#     else:
#         print("Invalid command.")


if __name__ == "__main__":
    
    while True:
    
        query = takeCommand().lower() 
        
        if 'wikipedia' in query:  
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "E:/xampp/htdocs/priyal"
            os.startfile(codePath)

        elif 'email to priyal' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "priyal.glsbca21@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email") 

        elif 'play song' in query:
             webbrowser.open("spotify.com")
            #  while True:
            #      playSong()
            #      while True:
            #         command = takeCommand()
            #         process_command(command)

        elif 'news' in query:
            headlines = get_news_headlines()
            if headlines:
                for headline in headlines:
                    print(headline)
            else:
                print('Failed to fetch news headlines.')

        elif 'jokes' in query:
            joke = get_random_joke()
            if joke:
                setup = joke['setup']
                punchline = joke['punchline']
                engine = pyttsx3.init()
                engine.say(setup)
                engine.say(punchline)
                engine.runAndWait()
            else:
                print('No jokes available.')

        elif "quit" in query:
            speak("quit")
            quit()
import re
import urllib.request
import speech_recognition as sr
import os
import vlc
import requests

def listener():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
        print("understanding...")
        command = r.recognize_google(audio).lower()
    return command





def weather(location):
    location=location.title()
    if location == "":
        exit
    else:
        try:
            city = location.replace(" ", "-")
            url = "https://www.weather-forecast.com/locations/"+city+"/forecasts/latest"
            data = urllib.request.urlopen(url).read()
            data1 = data.decode("utf-8")
            m = re.search('span class="phrase">', data1)
            start = m.end()
            end = start + 300
            newString = data1[start:end]
            
            

            x = re.search("</span>", newString)
            end = x.start() 
            final = newString[0:end]
            final=final.replace("&deg;C", " Degrees Celsius")
            return final
            
        except:
            
            return "The city doesn't exist"
            

#########Functions TO DO LIST:


def stream_music():
       
    p = vlc.MediaPlayer('C:\\Users\\Koolkid\\Downloads\\Music\\Pink - Just Give Me A Reason.mp3')#("http://s1.mmdl.xyz/1396/09/22/Eminem%20-%20Revival%20(320)/15.%20Offended.mp3")
    p.play()
    


def scores(sports):
    """ sports code goes here"""
    pass


def news_headlines(country):
    """ news code goes here"""
    pass


def take_notes():
    """notes code goes here"""


    pass


def hide_show(task):
    if task == "hide":
        return wm_state('iconic')
    if task == "show":
        return wm_state('normal')
    




def get_definition(word):
    
    print("looking up: "+word)
    
    
    try:
        url = "https://www.merriam-webster.com/dictionary/"+word
        r = requests.get(url)
        data1 = r.text
        m = re.search('<meta name="description" content="', data1)
        start = m.end()
        end = start + 300
        newString = data1[start:end]
        x = re.search('How to', newString)
        end = x.start()
        define = newString[0:end]
        return define
        
    except:
        
        return "The word doesn't exist"
        





















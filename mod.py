import re
import urllib.request
import speech_recognition as sr

def weather(location):
    location=location.capitalize()
    if location == "":
        exit
    else:
        try:   
            city = location.replace(" ", "-")
            url = "http://www.weather-forecast.com/locations/" + city + "/forecasts/latest"
            
            data = urllib.request.urlopen(url).read()
            data1 = data.decode("utf-8")
            m = re.search('span class="phrase">', data1)
            start = m.end()
            end = start + 300
            newString = data1[start:end]

            

            m = re.search("</span>", newString)
            end = m.start() - 2
            final = newString[0:end]
            
            return final
            
         
            #weather()
        except:
            return "The city doesn't exist"
            #time.sleep(2)
            weather()

def listener():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
        print("understanding...")
        command = r.recognize_google(audio).lower()
    return command

#print(listener())




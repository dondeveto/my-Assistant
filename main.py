import sys
import requests 
import json
import mod, wallpaper
import threading                                    #
from threading import Thread
import pyttsx
import datetime, time

commands = ['weather', 'music']

def speak(x):
    engine = pyttsx.init()
    engine.say(x)
    engine.runAndWait()

def dispatcher(command, arg):
    
    """ Does things """
    #if command in commands:
    if command == "define":
        speak(mod.defination(command))
        
    if command == "wallpaper":
        speak(wallpaper.wallpaper(arg))
        print(wallpaper.wallpaper(arg))
    
    if command == "":
        print("going to sleep...")
        time.sleep(10)
        
    if command == "weather":
        print("Here's the weather forcast for "+arg.capitalize())
        x =mod.weather(arg)
        Thread(target = print(x)).start()
        Thread(target = speak(x)).start()
        
    if command == "music":
        mod.stream_music()
        
    if command == "bye":
        print("Goodbye! Have a good day!")
        return

    if command == "minimize":
       mod.hide_show("hide")
        
    if command == "maximize":
        mod.hide_show("show")
    #prompter()


def prompter():
    command =""
    """ asks for things """
    speak("How may I help you today ?")
    time.sleep(1)
    command =mod.listener()
    if command == "minimize" or command =="maximize":
        dispatcher(command, None)
    
    if command == "weather":
        print("Sure thing! What city? :")
        speak("Sure thing! What city")
        time.sleep(1)
        city = mod.listener()
        dispatcher(command, city)

        
    if command == "music":
        dispatcher(command, "none")

    if command == "wallpaper":
        dispatcher(command, None)
        
    if command == "stocks": # TODO
        pass
    
    else:
        dispatcher(command, "")

def starter(cliargs):
    
    # TODO: Finish up command line interface
    #print("DEBUG: Called with ", cliargs[1:])
    currentTime = datetime.datetime.now()
    if currentTime.hour < 12:
        speak('Good morning.')
    elif 12 <= currentTime.hour < 18:
        speak('Good afternoon.')
    else:
        speak('Good evening.')

    if (len(cliargs) > 1):
        command = cliargs[1]
        arg = cliargs[2]
        # TODO: Call dispatcher with args instead of prompting user. 
        dispatcher(command, arg)
    else:
        prompter()



if __name__ == "__main__":
    starter(sys.argv)

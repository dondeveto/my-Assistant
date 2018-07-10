import sys
import requests 
import json
import mod
import threading                                    #
from threading import Thread
import pyttsx
import datetime, time

def speak(x):
    engine = pyttsx.init()
    engine.say(x)
    engine.runAndWait()

def dispatcher(command, arg):
    """ Does things """
    if command == "weather":
        print("Here's the weather forcast for "+arg.capitalize())
        x =mod.weather(arg)
        x=x.replace("&deg;C", " Degrees Celsius")
        Thread(target = print(x)).start()
        Thread(target = speak(x)).start()
        
    elif command == "bye":
        print("Goodbye! Have a good day!")
        return
    
    prompter()


def prompter():
    command =""
    """ asks for things """
    speak("How may I help you today ?")
    time.sleep(1)
    command =mod.listener()
    if command == "weather":
        print("Sure thing! What city? :")
        speak("Sure thing! What city")
        city = mod.listener()
        dispatcher(command, city)
    if command == "square":
        num = input("I love math! What number?")
        dispatcher(command, num)
    if command == "stocks": # TODO
        pass
    elif command == "dance":
        dance()
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

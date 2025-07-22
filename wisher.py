import time
import pyttsx3
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
datestamp=time.strftime('%d-%m-%Y')
timestamp=time.strftime('%I:%M:%S %p')
# timestamp=time.strftime('%H:%M:%S')
print("Today's Date:",datestamp)
print("Time:",timestamp)
hour=time.strftime('%H')
hour=int(hour)
'''
print("HOURS:",hour)
minute=time.strftime('%M')
print("MINUTES:",minute)
second=time.strftime('%S')
print("SECONDS:",second)
'''
if(hour>= 0 and hour<6):
    print("Good EARLY MORNING sir...!!")
    speak("Good EARLY MORNING sir")
elif(hour>=6 and hour<12):
    print("Good MORNING sir...!!")
    speak("Good MORNING sir")
elif(hour>=12 and hour<16):
    print("Good AFTERNOON sir...!!")
    speak("Good Afternoon sir")
elif(hour>=16 and hour<21):
    print("Good EVENING sir...!!")
    speak("Good EVENING sir")
else:
    print("Good NIGHT sir...!!")
    speak("Good NIGHT sir")

# Play any youtube video using python

import pywhatkit

try:
    
    Song = input("Enter the video name: ") # Enter the video name you want to watch. e.g. "Unstoppable Sia"
    pywhatkit.playonyt(Song)
    print("Successfully played")
    
except:
    print("An error occured.")
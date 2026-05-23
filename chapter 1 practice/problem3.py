# install an external module 
# using this command:  pip install pyttsx3 
# we always usepip install and name of that package we are going to install
# basicallt pip is the package installer for python
# what does pyttsx3 do:
# Converts text → voice (offline, no internet needed)
import pyttsx3
engine = pyttsx3.init()
engine.say("This is my Man")
engine.runAndWait()
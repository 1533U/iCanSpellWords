import pyperclip
from textblob import TextBlob
import keyboard
#avaible 

def on_space():
    #Get last copied word
    print("Doing the thingy")
    badWordOfTerribleSpelling = pyperclip.paste()
    print(badWordOfTerribleSpelling)
    suggestedCorrectedWord = TextBlob(badWordOfTerribleSpelling)
    #Obtain corrected spelling as an output
    print("corrected text: "+str(suggestedCorrectedWord.correct()))
    #copy new corrected word to clip board to past
    pyperclip.copy(str(suggestedCorrectedWord.correct()))

keyboard.add_hotkey('ctrl+c', on_space)
keyboard.wait()
26128
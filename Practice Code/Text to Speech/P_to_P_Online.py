#Text to speech (Online)
# pip install gTTS
#Program description:-
# It uses google translate in order to create
# mp3 file from text

from gtts import gTTS as gt
import os

file = open("text_speech.txt","r")
#print(file.read())

def read(text):
       sound_file="file.mp3"
       a = gt(text,"en")
       a.save(sound_file)
       os.system('mpg123 ' + sound_file)

try:
       print("Generating...")
       read(file.read())
except:
       print("Enter Proper Text")
       print("No connection to Google Translate")
finally:
       print("Done")

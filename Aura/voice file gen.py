from gtts import gTTS
import os
import time

# replace keybind is ctrl + H
# i never remember that one

tts = gTTS('x')                       # text goes here
tts.save('E:/Aura/temp/x.mp3')        # saves it as x.mp3
time.sleep(0.5)
os.startfile('E:/Aura/temp/x.mp3')    # plays x.mp3 to test

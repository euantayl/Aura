#-------------------------------------------------------------------- imports
import urllib.request
import urllib.parse
import wikipediaapi
import os
import os.path
import webbrowser
import getpass
import pandas as pd
import subprocess
import psutil
import ctypes
import time
from gtts import gTTS
from bitlyshortener import Shortener
from selenium import webdriver
from bs4 import BeautifulSoup
from googletrans import Translator
from datetime import datetime
from sound import Sound
from keyboard import Keyboard
from pathlib import Path

#-------------------------------------------------------------------- user defined variables

extPath = 'C:/Users/ethom/Desktop/'                                  # where the user wants to control files from
intPath = 'E:/Aura/'                                                 # where the individual aura files are stored
bitkey = ['']                                                        # bit.ly api key

#-------------------------------------------------------------------- other variables

now = datetime.now()                                                 # make it so i can use datetime.now instead of datetime.datetime.now
gt = Translator()                                                    # define gt as a command for google translate
wiki = wikipediaapi.Wikipedia('en')                                  # define wiki as a command, setting the language
shortener = Shortener(tokens=bitkey, max_cache_size=8192)            # define shortener as a command using the bit.ly key
new = 2                                                              # I haven't found a way to use webbrowser.open() without using variables yet

#-------------------------------------------------------------------- return without variable

def openProgramsCheck():
    EnumWindows = ctypes.windll.user32.EnumWindows
    EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
    GetWindowText = ctypes.windll.user32.GetWindowTextW
    GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
    IsWindowVisible = ctypes.windll.user32.IsWindowVisible
    titles = []
    def foreach_window(hwnd, lParam):
        if IsWindowVisible(hwnd):
            length = GetWindowTextLength(hwnd)
            buff = ctypes.create_unicode_buffer(length + 1)
            GetWindowText(hwnd, buff, length + 1)
            titles.append(buff.value)
        return True
    EnumWindows(EnumWindowsProc(foreach_window), 0)
    listLength = len(titles)
    outp = ''
    for i in range(listLength):
        if titles[i] == 'Microsoft Text Input Application':
            break
        elif titles[i] == '':
            useless = 0
        elif titles[i] == str('C:\WINDOWS\py.exe'):
            outp = (str(outp) + 'Aura Discord' + '\n')            
        else:
            print(titles[i])
            outp = (str(outp) + str(titles[i]) + '\n')
    return outp

def test():
    return True

def getCurrentVolume():
    return Sound.current_volume()

#-------------------------------------------------------------------- return with variable

def wikiSearch(content):                          
    temp = content.lower()                        # convert the entire message into lowercase
    page = temp.replace('what is ', '')           # ]
    page = page.replace('define ', '')            # ]
    page = page.replace('a ', '')                 # ] remove any question semantics
    page = page.replace('an ', '')                # ]
    page = page.replace('?', '')                  # ]
    page_py = wiki.page(page)                     # assigns a new variable to the above worked string using the wikipedia api
    try:
        check = page_py.exists()                  # check the wiki index to see if a page exists with the same name or similar
        if check == True:
            return str(page_py.fullurl)           # return the URL if the article exists
        else:
            return 'Page does not exist'          # return an error message
    except Exception as e:
        return ('error occured' + str(e))         # return an error message

def translate(content):
    if ' from ' in content.lower():       # from known to english
        temp = content.lower()                    # convert given string to lowercase
        content = temp.replace('translate ', '')  # remove commands given from aura_discord
        splitContent = content.split(' from ')    # split the string into 2 parts; x from y
        text = str(splitContent[0])               # assume the first part of the string will be the text to convert
        lang = str(splitContent[1])               # assume the second part of the string will be the languge to convert from
        transMeta = gt.translate(text, src=lang)  # get the data from the translator api, giving the desired text and language
        transText = transMeta.text                # parse the converted text from the data
        outp = lang.capitalize() + ':\n' + text.capitalize() + '\n\nEnglish:\n' + transText.capitalize() # concatenate the outputs, using .capitalize() for aesthetics
        return str(outp)                          # return the string
    elif ' to ' in content.lower():       # from english to known
        temp = content.lower()
        content = temp.replace('translate ', '')
        splitContent = content.split(' to ')
        text = splitContent[0]
        lang = splitContent[1]
        transMeta = gt.translate(text, src='en', dest=lang)
        transText = transMeta.text
        outp = 'English:\n' + text.capitalize() + '\n\n' + lang.capitalize() + ':\n' + transText.capitalize()
        return str(outp)
    else:                                 # from unknown to english
        temp = content.lower()
        text = temp.replace('translate ', '')
        transMeta = gt.translate(text, dest='en')
        transText = transMeta.text
        detectedLang = transMeta.src
        outp = 'Detected: ' + str(detectedLang).capitalize() + '\n' + text.capitalize() + ':\n\nEnglish:\n' + transText.capitalize()
        return str(outp)

def googleSearch(content):
    url = 'https://www.google.com/search?source=hp&q=' # define the base search url
    x = content.replace('?', '')                  # ]
    x = x.replace(',', '')                        # ]_remove the unnecessary characters that come up in search terms
    x = x.replace(' ', '+')                       # ] while replacing spaces with '+' # 
    x = x.replace('search+for+', '')              # ]
    x = x.replace('google+search+', '')           # ]
    x = x.replace('google+', '')                  # ]
    x = x.replace('search+', '')                  # ]
    x = x.replace('look+up+', '')                 # ]
    searchOutput = x.replace('.', '')             # ]
    fullUrl = str(url) + str(searchOutput)        # combine the base url with the search term
    outp = shortenUrl(fullUrl)                    # call the function i made to use the bitly api
    return outp                                   

def imageSearch(content):
    url = 'https://www.google.com/search?tbm=isch&q=' # define the base search url
    x = content.replace('?', '')                  
    x = x.replace(' ', '+')                       
    x = x.replace(',', '')                        
    x = x.replace('image+search+for+', '')
    x = x.replace('image+search+', '')
    x = x.replace('show+me+', '')
    x = x.replace('google+image+', '')
    imageOutput = x.replace('.', '')              
    fullUrl = str(url) + str(imageOutput)
    outp = shortenUrl(fullUrl)
    return outp

#-------------------------------------------------------------------- PC control without variables
                                                                     #   `~>(hardcoded, wouldn't make it's way into the program if i have plans to distribute after improvements)
def openControlPanel():
    os.startfile(extPath + 'control panel.py')                       # open the files linked in extPath, this being the PC desktop folder

def openGoose():
    os.startfile(extPath + 'Goose.lnk')

def stopGoose():
    try:
        os.startfile(extPath + 'DesktopGoose v0.3/Close Goose.bat')
    except:
        os.startfile(extPath + 'Close Goose.lnk')

def openMinecraft():
    os.startfile(intPath + "apps/minecraft.lnk")

def openOverwatch():
    os.startfile(intPath + "apps/overwatch.lnk")

def openFsx():
    os.startfile(intPath + "apps/fsx.lnk")
    
def openTatghoul():
    os.startfile(intPath + "apps/summon.exe")
    
def openFacebook():
    webbrowser.open('https://www.facebook.com/',new=new)

def openYoutube():
    webbrowser.open('https://www.youtube.com/',new=new)

def openReddit():
    webbrowser.open('https://www.reddit.com/',new=new)

def openTwitch():
    webbrowser.open('https://www.twitch.com/', new=new)

def openCleaner():
    os.startfile(intPath + "apps/ccleaner.lnk")

def openSpotify():
    os.startfile(intPath + 'apps/spotify.lnk')

def openStardewValley():
    os.startfile(intPath + 'apps/Stardew Valley.url')

def volumeDown():
    currentVolume = Sound.current_volume()
    desiredVolume = int(currentVolume) - 20
    if desiredVolume < 0:
        desiredVolume = 0
    Sound.volume_set(desiredVolume)

def volumeUp():
    currentVolume = Sound.current_volume()
    desiredVolume = int(currentVolume) + 20
    if desiredVolume > 100:
        desiredVolume = 100
    Sound.volume_set(desiredVolume)

def volumeOff():
    Sound.volume_min()

#-------------------------------------------------------------------- PC control with variables

def openFile(content):
    directs = []                                            # create a list of directories
    path = extPath                                          # set a path string
    fileName = ''                                           # create an empty fleName variable 
    for e in os.walk(path):                                 # for everything found while looking through the path,
        directs.append(str(e))                              # append the result to the directory list
        
    name = str(directs)                                     # set name as a string flattened from the list so i can use string commands
    splitName = name.split(', ')                            # make a list of filenames split by commas
    directory = splitName[0]                                # define directory as the first entry in the list
    for i in range(len(directs)):                           # loop for the amount of entries
        fileName = splitName[i].replace("'", '')            # remove the inverted commas in each filename
        if fileName.lower().startswith(content.lower()):    # if the found filename and the desired filename match, excluding the filetype designation;
            print(fileName)                                 # print to console
            break                                           # break the loop, taking the first found match

    directory = directory.replace("'", '')                  # ]
    directory = directory.replace("[", '')                  # ] remove uneccesary characters
    directory = directory.replace("(", '')                  # ] 
    directory = directory.replace('"', '')                  # ]

    fullFileName = str(directory) + "/" + str(fileName)     # concatenate the directory to the filename with filetype into a full path
    print(fullFileName)                                     # print the path

    try:
        os.startfile(fullFileName)                          # try to open the path
    except:
        print("no.")                                        # or print no to console

def pronounce(content):
    query = content.replace('say', '')                      # remove both probable capitalization variants of the command word without using .lower()
    query = query.replace('Say', '')                        # i don't use .lower() so i can keep any capitalization semantics of the given phrase
    tts = gTTS(query)                                       # give the input to google text to speech
    tts.save(intPath + 'temp/Aura.mp3')                     # save the mp3 in a temporary location
    os.startfile(intPath + 'temp/Aura.mp3')                 # play the mp3 using the OS library

def setVolume(value):
    Sound.volume_set(value)

def textReminder(content):
    text = content.replace('remind me ', '')                # remove both probable capitalization variants of the command word without using .lower()
    text = text.replace('Remind me ', '')                   # i don't use .lower() so i can keep the capitalization of the given reminder
    fileName = (text[0] + text[1] + text[2])                # set the fileName to be the first 3 characters of the reminder
    fullFileName = (str(intPath) + 'reminders/' + str(fileName) + '.txt') # create a directory to a txt file
    fullFileName = Path(fullFileName)                       # convert string into a path object
    if fullFileName.exists():                               # check if the file already exists
        modifier = 1                                        # the number that is added to the end of a file to make it unique                        
        alreadyExists = True                                # start a while loop
        while alreadyExists:
            tempFileName = str(fullFileName).replace('.txt', '') # remove '.txt' from the string
            tempFileName = str(tempFileName) + str(modifier)     # add the modifier number at the end
            tempFileName = str(tempFileName) + '.txt'            # bring '.txt' back
            tempFileName = Path(tempFileName)               # convert to a path object again
            if tempFileName.exists():                       # if this new filename exists too,
                modifier = modifier + 1                     # increase the modifier by one
            else:                                           # else,
                fullFileName = tempFileName                 # move the data to fullFileName
                alreadyExists = False                       # break the loop.
    file = open(fullFileName, 'w')                          # create the new txt file
    file.write(text)                                        # write the data
    file.close()
    os.startfile(fullFileName)                              # open the file to show on screen

def pressKey(keyName):
    keyName = keyName.replace('press ', '')
    keyCode = keyName.upper()
    keyCode = "VK_" + str(keyCode)
    method_to_call = getattr(Keyboard, keyCode)
    Keyboard.key(method_to_call, 0.2)

def typeString(desString):                           
    desString = desString.replace('type ', '')       
    numOfChars = len(desString)                                           
    for i in range(numOfChars):         
        keyCode = desString[i].upper()              
        if keyCode == ' ':           
            keyCode = 'SPACE' 
        keyCode = "VK_" + str(keyCode)                  
        method_to_call = getattr(Keyboard, keyCode)
        Keyboard.key(method_to_call, 0.2)

#-------------------------------------------------------------------- others

def shortenUrl(fullUrl):
    urls = [fullUrl]                                        # bitly api only takes input as list items so it can handle more than one at a time
    biturl = shortener.shorten_urls(urls)                   # use the api to get the shortened link
    return biturl[0]                                        # return the link given
    
#==================================================================== in development area



#====================================================================


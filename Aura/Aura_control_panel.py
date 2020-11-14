#-------------------------------------------------------------------- imports

import os
import sys
import json
import time
import random
import spotipy
import subprocess
import webbrowser
from tkinter import *
import Aura_calc as aura                                    # custom library that handles all of the calculations for each interface to keep parity
import spotipy.util as util              
from datetime import datetime
import tkinter.scrolledtext as tkst
from json.decoder import JSONDecodeError
from spotipy.oauth2 import SpotifyClientCredentials

#-------------------------------------------------------------------- user defined variables

username = ''                                               # spotify username
clientId = ''                                               # spotify client id
clientSecret = ''                                           # spotify client secret
redirectUri = ''                                            # where i get sent as part of the spotify authorisation protocol, made when setting up api access
spotifyPlaylist = ''                                        # The playlist most of the spotify commands use
deviceId = ''                                               # The unique ID of the device spotify is installed. This can be external
extPath = 'C:/Users/ethom/Desktop/'                         # where the user wants to control apps from
intPath = 'E:/Aura/'                                        # where the individual aura files are stored
mainBackground = 'black'                                    # GUI background colour
buttonBackground = 'black'                                  # GUI button colour
buttonForeground = '#BA2AB8'                                # GUI Text colour

#-------------------------------------------------------------------- other variables

now = datetime.now()                                        # redefine 'datetime.datetime.now()' to be 'datetime.now()' for ease of use
new = 2                                                     # I don't know why yet; but I cannot use an integer for 'webbrowser.open()', it has to be an int variable
scope = 'user-read-private user-read-playback-state user-modify-playback-state'
errorMessage = "Not Responding"
global token

#-------------------------------------------------------------------- spotipy setup

try:                                                        # get spotify auth token
    token = util.prompt_for_user_token(username,            # try and get a high quality token
                            scope,
                            client_id = clientId,
                            client_secret = clientSecret,
                            redirect_uri = redirectUri)
except (AttributeError, JSONDecodeError):
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope)     #if not able to get a high quality token, the basics wil do

if token:                                                   # if token exists, redefine the command as sp using the token
    sp = spotipy.Spotify(auth=token)

#-------------------------------------------------------------------- Definitions

#------------------------------------------------- start/open def

def minecraft():
    try:
        aura.openMinecraft()                                # call Aura
    except:
        searchBar.delete(0, END)                            # clear any existing message
        searchBar.insert(0, errorMessage)                   # output error message

def overwatch():
    try:
        aura.openOverwatch()
    except:
        searchBar.delete(0, END)
        searchBar.insert(0, errorMessage)
    
def fsx():
    try:
        aura.openFsx()
    except:
        searchBAr.delete(0, END)
        searchBar.insert(0, errorMessage)

def tatghoul():
    try:
        aura.openTatghoul()
    except:
        searchBar.delete(0, END)
        searchBar.insert(0, errorMessage)

def facebook():
    try:
        aura.openFacebook()
    except:
        searchBar.delete(0, END)
        searchBar.insert(0, errorMessage)

def youtube():
    try:
        aura.openYoutube()
    except:
        searchBar.delete(0, END)
        searchBar.insert(0, errorMessage)

def reddit():
    try:
        aura.openReddit()
    except:
        searchBar.delete(0, END)
        searchBar.insert(0, errorMessage)

def twitch():
    try:
        aura.openTwitch()
    except:
        searchBar.delete(0, END)
        searchBar.insert(0, errorMessage)

def clean():
    try:
        aura.openCleaner()
    except:
        searchBar.delete(0, END)
        searchBar.insert(0, errorMessage)

def stardewValley():
    try:
        aura.openStardewValley()
    except:
        searchBar.delete(0, END)
        searchBar.insert(0, errorMessage)

def spotify():
    try:
        aura.openSpotify()
    except:
        searchBar.delete(0, END)
        searchBar.insert(0, errorMessage)

#------------------------------------------------- functionality def

def q():
    quit()

def miniDef():
    mini.deiconify()                                    # open the mini window
    main.iconify()                                      # minimize the main window

def maxiDef():
    main.deiconify()                                    # open the main window
    mini.iconify()                                      # minimize the mini window

def search():
    query = searchBar.get()                             # define query as what is in the input box
    print(query)                                        # print the query to console
    
    if query.lower() == 'test':                         # check if query equals 'test'
        temp = aura.test()                              # call Aura's test func
        if temp:                                        # if Aura returns True
            searchBar.delete(0, END)                    # clear the input box
            searchBar.insert(0, 'True')                 # insert 'True'
        else:
            searchBar.delete(0, END)                    # clear the input box
            searchBar.insert(0, 'No response')          # insert 'No response'
            
    elif query.startswith('='):                         # check if query starts with an equals
        query = query.replace('=', '')                  # replace the equals with nothing
        tempLen = len(query)                            # get the length of the query
        for i in range (tempLen-1):                     # loop for every character in query
            checkDigit = query[i].isdigit()             # is the character in question a digit?
            if checkDigit == False and query[i] != '.': # if the character is not a digit and not a period
                oper = query[i]                         # define operator as the character then break loop
        var1 = query.split(oper)[0]                     # variable one as what is in front of the operator
        var2 = query.split(oper)[1]                     # variable two as what is behind the operator
        try:
            calculator(var1, oper, var2)                # try plugging both variables and the operator into the calculator function
        except:                                         # if calculator comes across an error
            outp = aura.googleSearch(query)             # call Aura to use query in a google search and give a bit.ly URL
            webbrowser.open(outp,new=new)               # open webbrowser with the given URL
            searchBar.delete(0, END)                    # clear the input box
    else:
        outp = aura.googleSearch(query)                 # call Aura to use query in a google search and give a bit.ly URL
        webbrowser.open(outp,new=new)                   # open webbrowser with the goven URL
        searchBar.delete(0, END)                        # clear the input box

def func(event):                                        # define func() as an event to run search()
    search()

def calculator(var1, oper, var2):                       
    if oper == '+':                                     # if the operator is an addition sign
        outp = float(var1)+float(var2)                  # define the output as the sum of var1 and var2
        if str(outp).endswith('.0'):                    # if the output ends with '.0'
            outp = str(outp).replace('.0', '')          # remove the '.0'
        searchBar.delete(0, END)                        # clear the search box
        searchBar.insert(0, outp)                       # enter the output in the search box
    elif oper == '-':                                   #..........
        outp = float(var1)-float(var2)                  #........
        if str(outp).endswith('.0'):                    #......
            outp = str(outp).replace('.0', '')          #....
        searchBar.delete(0, END)                        #..
        searchBar.insert(0, outp)                       
    elif oper == '*':
        outp = float(var1)*float(var2)
        if str(outp).endswith('.0'):
            outp = str(outp).replace('.0', '')
        searchBar.delete(0, END)
        searchBar.insert(0, outp)
    elif oper == '/':
        outp = float(var1)/float(var2)
        if str(outp).endswith('.0'):
            outp = str(outp).replace('.0', '')
        searchBar.delete(0, END)
        searchBar.insert(0, outp)
    elif oper == '%':
        outp = float(var1)%float(var2)
        if str(outp).endswith('.0'):
            outp = str(outp).replace('.0', '')
        searchBar.delete(0, END)
        searchBar.insert(0, outp)

#------------------------------------------------- spotify def

def getToken():
    global token
    if token:                                               # if the token already exists in cache
        sp = spotipy.Spotify(auth=token)                    # make sure sp is defined correctly
    else:                                                   # if not, call the spotipy api to get a new token
        try:
            token = util.prompt_for_user_token(username,         
                                   scope,
                                   client_id = clientId,
                                   client_secret = clientSecret, 
                                   redirect_uri = redirectUri)
        except (AttributeError, JSONDecodeError):
            os.remove(f".cache-{username}")
            token = util.prompt_for_user_token(username, scope)

        sp = spotipy.Spotify(auth=token)

def spotifyPlay():
    getToken()                                              # make sure token exists and is up to date
    playbackMeta = sp.current_playback()                    # pull the data from spotipy api regarding the current song
    playbackStr = str(playbackMeta)                         # convert data into a string
    splitPlaying = playbackStr.split("'is_playing': ")      # find where the api stores playback status
    isPlaying = splitPlaying[1].replace('}', '')            # remove the '}' from behind the string
    
    if isPlaying == 'False':                                # this is a way i found to get around a problem i had with playing the current song. previously it would shuffle a new song
        sp.next_track(device_id=deviceId)                   # skip to the next song in the queue
        time.sleep(0.2)
        sp.previous_track(device_id=deviceId)               # skip to the previous song
        sp.shuffle(True, device_id=deviceId)                # set shuffle to True
    else:
        sp.pause_playback(device_id=deviceId)               # if a song is currently playing, the button instead causes a pause
    getSongInfo()                                           # call the function 

def spotifyPrevious():
    getToken()                                              # make sure token exists and is up to date
    try:
        sp.previous_track(device_id=deviceId)               # try and skip previous
        getSongInfo()
    except:
        print("error occurred")                             # print to console
        
def spotifyNext():
    getToken()                                              # make sure token exists and is up to date
    try:
        sp.next_track(device_id=deviceId)                   # try to skip next
        getSongInfo()
    except:
        print("error occurred")                             # print to console

def getSongInfo():
    try:                                                    # since this happens every 5 seconds, I don't want a new token to generate each time for performance issues.
                                                            # instead, the function tries to work on the existing token and only if it has expired will generate a new one
        u = sp.current_playback()                           # pull the data from spotipy api regarding the current song
        if u['is_playing']:                                 # if there is a song playing currently
            track = sp.current_user_playing_track()         # pull the song data from the api
            artist = track['item']['artists'][0]['name']    # define the artist name from data dictionary
            track = track['item']['name']                   # define the track name from data dictionary
            songName.delete('1.0', END)                     # clear the song name field
            songName.insert(END, track)                     # insert the playing song name
            songArtist.delete('1.0', END)                   # clear the artist name field
            songArtist.insert(END, artist)                  # insert the playing artist name                   
        else:                                               # if a song is not playing
            songName.delete('1.0', END)                     # clear the song name field
            songArtist.delete('1.0', END)                   # clear the artist name field
    except Exception as e:
        getToken()                                          # most common error is rejected auth token so generate a new one to try next loop
        print(e)                                            # print the error to console so I can check to see the problem

    main.after(5000, getSongInfo)                           # repeat every 5 seconds

#------------------------------------------------- test def

def test():                                                 # testing area for new features
    u = 0
    
#-------------------------------------------------------------------- GUI

main = Tk()                                                 # create the main window
main.geometry('384x260')                                    # size of the window
main.title("Aura - Control Panel")                          # title of the window
main.configure(bg=mainBackground)                           # background colour
main.attributes('-topmost', True)                           # make it stay on top
graphic = PhotoImage(file = intPath+"sys/graphic.gif")      # load the icon image
main.iconphoto(False, graphic)                              # add icon photo to the window
main.bind('<Return>', func)                                 # bind the enter key to func()

mini = Toplevel()                                           # create the mini window
mini.geometry('114x190')                                    # size of the window
mini.title("Aura Mini")                                     # title of the window
mini.configure(bg=mainBackground)                           # background colour
mini.attributes('-topmost', True)                           # make it stay on top
mini.attributes("-toolwindow",1)                            # remove all window tools except X
mini.iconify()                                              # hide the window

#-------------------------------------------------------------------- design

buttonMinecraft = Button(main, text='Minecraft', command=minecraft, fg=buttonForeground, bg=buttonBackground, font=("Calibri", 14, "bold"), width=12, padx=-15, pady=-15)
buttonMinecraftMini = Button(mini, text='MC', command=minecraft, fg=buttonForeground, bg=buttonBackground, font=("Calibri", 14, "bold"), width=3, padx=-15, pady=-15)
buttonOverwatch = Button(main, text='Overwatch', command=overwatch, fg=buttonForeground, bg=buttonBackground, font=("Calibri", 14, "bold"), width=12, padx=-15, pady=-15)
buttonOverwatchMini = Button(mini, text='OW', command=overwatch, fg=buttonForeground, bg=buttonBackground, font=("Calibri", 14, "bold"), width=3, padx=-15, pady=-15)
buttonFsx = Button(main, text='Flight Sim X', command=fsx, fg=buttonForeground, bg=buttonBackground, font=("Calibri", 14, "bold"), width=12, padx=-15, pady=-15)
buttonFsxMini = Button(mini, text='FSX', command=fsx, fg=buttonForeground, bg=buttonBackground, font=("Calibri", 14, "bold"), width=3, padx=-15, pady=-15)

buttonMini = Button(main, text='Minimize', command=miniDef, fg=buttonForeground, bg=buttonBackground, font=("Calibri", 14, "bold"), width=12, padx=-15, pady=-15)
buttonMaxi = Button(mini, text='Max', command=maxiDef, fg=buttonForeground, bg=buttonBackground, font=("Calibri", 14, "bold"), width=3, padx=-15, pady=-15)

buttonFacebook = Button (main, text = 'Facebook', command = facebook, fg=buttonForeground, bg=buttonBackground, font=("Calibri", 14, "bold"), width=12, padx=-15, pady=-15)
buttonFacebookMini = Button (mini, text = 'FB', command = facebook, fg=buttonForeground, bg=buttonBackground, font=("Calibri", 14, "bold"), width=3, padx=-15, pady=-15)
buttonReddit = Button (main, text = 'Reddit', command = reddit, fg=buttonForeground, bg=buttonBackground, font=("Calibri", 14, "bold"), width=12, padx=-15, pady=-15)
buttonRedditMini = Button (mini, text = 'RD', command = reddit, fg=buttonForeground, bg=buttonBackground, font=("Calibri", 14, "bold"), width=3, padx=-15, pady=-15)
buttonYoutube = Button (main, text = 'YouTube', command = youtube, fg=buttonForeground, bg=buttonBackground, font=("Calibri", 14, "bold"), width=12, padx=-15, pady=-15)
buttonYoutubeMini = Button (mini, text = 'YT', command = youtube, fg=buttonForeground, bg=buttonBackground, font=("Calibri", 14, "bold"), width=3, padx=-15, pady=-15)
buttonTwitch = Button (main, text = 'Twitch', command = twitch, fg=buttonForeground, bg=buttonBackground, font=("Calibri", 14, "bold"), width=12, padx=-15, pady=-15)
buttonTwitchMini = Button (mini, text = 'TW', command = twitch, fg=buttonForeground, bg=buttonBackground, font=("Calibri", 14, "bold"), width=3, padx=-15, pady=-15)

buttonGhoul = Button (main, text = 'Tatghoul', command = tatghoul, fg=buttonForeground, bg=buttonBackground, font=("Calibri", 14, "bold"), width=12, padx=-15, pady=-15)
buttonGhoulMini = Button (mini, text = 'STG', command = tatghoul, fg=buttonForeground, bg=buttonBackground, font=("Calibri", 14, "bold"), width=3, padx=-15, pady=-15)
buttonClean = Button (main, text = 'CCleaner', command = clean, fg=buttonForeground, bg=buttonBackground, font=("Calibri", 14, "bold"), width=12, padx=-15, pady=-15)
buttonCleanMini = Button (mini, text = 'CCL', command = clean, fg=buttonForeground, bg=buttonBackground, font=("Calibri", 14, "bold"), width=3, padx=-15, pady=-15)
buttonStardew = Button (main, text = 'SD Valley', command = stardewValley, fg=buttonForeground, bg=buttonBackground, font=("Calibri", 14, "bold"), width=12, padx=-15, pady=-15)
buttonStardewMini = Button (mini, text = 'SDV', command = stardewValley, fg=buttonForeground, bg=buttonBackground, font=("Calibri", 14, "bold"), width=3, padx=-15, pady=-15)
buttonSpotify = Button (main, text = 'Spotify', command = spotify, fg=buttonForeground, bg=buttonBackground, font=("Calibri", 14, "bold"), width=12, padx=-15, pady=-15)
buttonSpotifyMini = Button (mini, text = 'SPO', command = spotify, fg=buttonForeground, bg=buttonBackground, font=("Calibri", 14, "bold"), width=3, padx=-15, pady=-15)

placeholder = Text(main, height=1, width=11, font=(6), fg=mainBackground, bg=mainBackground, borderwidth=0, padx=-15, pady=-15)

searchBar = Entry(main, width=11, font=("Calibri", 14), fg='black', bg='#565656')
searchButton = Button (main, text='Search', command = search, fg=buttonForeground, bg=buttonBackground, font=("Calibri", 14, "bold"), width=6, height=1, padx=-15, pady=-30)
buttonQ = Button(main, text='Quit', command=q, fg=buttonForeground, bg=buttonBackground, font=("Calibri", 14, "bold"), width=10, padx=-15, pady=-15)

songInfo = Label(main, width=11, font=('Calibri', 14), fg=buttonForeground, bg=mainBackground, text='Now playing:')
songName = Text(main, width=11, font=('Calibri', 14), fg=buttonForeground, bg=mainBackground, height=1, borderwidth=0)
songArtist = Text(main, width=11, font=('Calibri', 14), fg=buttonForeground, bg=mainBackground, height=1, borderwidth=0)

buttonSpotifyPlay = Button(main, text='Play/Stop', command=spotifyPlay, fg=buttonForeground, bg=buttonBackground, font=("Calibri", 14, "bold"), width=12, padx=-15, pady=-15)
buttonSpotifyPlayMini = Button(mini, text='P/S', command=spotifyPlay, fg=buttonForeground, bg=buttonBackground, font=("Calibri", 14, "bold"), width=3, padx=-15, pady=-15)
buttonSpotifyPrevious = Button(main, text='<<', command=spotifyPrevious, fg=buttonForeground, bg=buttonBackground, font=("Calibri", 14, "bold"), width=3, padx=-15, pady=-15)
buttonSpotifyPreviousMini = Button(mini, text='<<', command=spotifyPrevious, fg=buttonForeground, bg=buttonBackground, font=("Calibri", 14, "bold"), width=3, padx=-15, pady=-15)
buttonSpotifyNext = Button(main, text='>>', command=spotifyNext, fg=buttonForeground, bg=buttonBackground, font=("Calibri", 14, "bold"), width=3, padx=-15, pady=-15)
buttonSpotifyNextMini = Button(mini, text='>>', command=spotifyNext, fg=buttonForeground, bg=buttonBackground, font=("Calibri", 14, "bold"), width=3, padx=-15, pady=-15)

buttonTest = Button(main, text='Test', command=test, fg=buttonForeground, bg=buttonBackground, font=("Calibri", 14, "bold"), width=10, padx=-15, pady=-15)
buttonTestMini = Button(mini, text='T', command=test, fg=buttonForeground, bg=buttonBackground, font=("Calibri", 14, "bold"), width=10, padx=-15, pady=-15)

#-------------------------------------------------------------------- Positioning Maxi

buttonMinecraft.grid(row=0,column=0)
buttonOverwatch.grid(row=1,column=0)
buttonFsx.grid(row=2,column=0)
buttonStardew.grid(row=3, column=0)        

buttonFacebook.grid(row=0,column=1)
buttonReddit.grid(row=1,column=1)
buttonYoutube.grid(row=2,column=1)
buttonTwitch.grid(row=3,column=1)

buttonGhoul.grid(row=0,column=2)
buttonClean.grid(row=1,column=2)
buttonMini.grid(row=2,column=2)        
buttonSpotify.grid(row=3,column=2)

placeholder.grid(row=4, column=0)
placeholder.insert(END, 'oh hello there')

searchBar.grid(row=5,column=0)
searchButton.grid(row=5, column=1, sticky=W)
buttonQ.grid(row=5,column=2)

songInfo.grid(row=6,column=0,)
songName.grid(row=6,column=1)
songArtist.grid(row=6,column=2)

buttonSpotifyPrevious.grid(row=7,column=0, sticky=E)
buttonSpotifyPlay.grid(row=7,column=1)
buttonSpotifyNext.grid(row=7,column=2, sticky=W)

buttonTest.grid(row=0,column=4)

#-------------------------------------------------------------------- Positioning Mini

buttonMinecraftMini.grid(row=0,column=0)
buttonOverwatchMini.grid(row=1,column=0)
buttonFsxMini.grid(row=2,column=0)
buttonStardewMini.grid(row=3, column=0)        


buttonFacebookMini.grid(row=0,column=1)
buttonRedditMini.grid(row=1,column=1)
buttonYoutubeMini.grid(row=2,column=1)
buttonTwitchMini.grid(row=3,column=1)

buttonGhoulMini.grid(row=0,column=2)
buttonCleanMini.grid(row=1,column=2)
buttonMaxi.grid(row=2,column=2)
buttonSpotifyMini.grid(row=3,column=2)

buttonSpotifyPreviousMini.grid(row=4,column=0)
buttonSpotifyPlayMini.grid(row=4,column=1)
buttonSpotifyNextMini.grid(row=4,column=2)

buttonTestMini.grid(row=0,column=4)

#-------------------------------------------------------------------- Functions on start

getToken()
#test()
getSongInfo()
main.mainloop()

#--------------------------------------------------------------------

keepConsoleOpen = input("\n")




































































#-------------------------------------------------------------------- End












# what are you doing down here?

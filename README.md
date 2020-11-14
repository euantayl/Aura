# Aura
Aura is a small scale personal project designed to help automate common processes in everyday PC use such as; controlling programs, 
scraping the web, and manipulating data.


_________________________________________________
Description

Aura is a project born out of inspiration from A.I. in media and an interest in automation and efficiency. It is designed to be completely modular and to 
provide parity between some personal projects that all use the framework with different input/output methods. Aura has been in development from 2015
when it started as 'Fanqaich', or 'Fully Automated Not Quite Artificial Intelligence Computer Helper'. A typical 16 year old's naming system.


_________________________________________________
Installation



       extPath = ''       # where the user wants to control files from
       intPath = ''        # where the individual aura files are stored
       bitKey = ['']       # bit.ly api key


Edit the program to fill in your details into the required fields, and save aura_calc in the same folder as your project, or in your python scripts folder. This is going to be updated to be more user friendly in future updates.
_________________________________________________
Usage


       import aura_calc

       aura_calc.translate(content)            # Translates a string to or from a given language. If no language is given, it will translate from detected to English 
       aura_calc.openProgramsCheck()     # Returns a string of currently running programs split by '\n' (this returns a string instead of a list to be compatible with aura_discord)
       aura_calc.openFile(content)            # Attempts to find a given file name in the C: directory and runs a file if any is found



_________________________________________________
Future Update Plans

 - Add Spotify controls
 - Add hardware volume controls
 - Add the ability to give a reminder when the user returns to their PC
 - Add the ability to virtually press a key or keys through online commands
 - Update the installation procedure


_________________________________________________
aura_control_panel

The control panel saved here brings Aura's functionality to a GUI. The window can be minimized into a much smaller panel with the same performance
which means it can remain on top of other windows without getting in the way.

_________________________________________________
aura_discord

This program makes use of Discord's bot API to allow me to interface with aura_calc from external sources. A future goal of this project is to create a custom web 
server for less restricted data transfer, a higher level of customisation, and potential higher speeds.


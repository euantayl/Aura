import time
import Aura_calc as aura
import discord
import os

extPath = 'C:/Users/ethom/Desktop/'               # where the user wants to control apps from
intPath = 'E:/Aura/'                              # where the individual aura files are stored

class MyClient(discord.Client):                   # create a client class using the discord api
    async def on_ready(self):                     # define a function to happen when the bot logs in
        print('Logged in as') 
        print(self.user.name)                     # print the bot's username
        print(self.user.id)                       # print the bot's user ID
        print('------\n\n')

    async def on_message(self, message):          # define a function to happen on an incoming message
        print(message.channel.id)                 # ]
        print(message.channel.name)               # ]
        print(message.author.id)                  # print the message information
        print(message.author.name)                # ]
        print(message.content)                    # ]
        print('')
        user = str(message.author)                # set the sender for future functionality
        content = str(message.content)            # set the message contents

        if message.author.id == self.user.id:     # check if the message came from the bot
            return                                # don't reply to itself to prevent loops


        if content.lower() == 'test':             # if the message is 'test'
            try:
                outp = aura.test()                # call Aura's test function
                if outp:                          # if Aura replies True
                    await message.channel.send("Test reply True".format(message)) # reply with the confirmation message
                else:
                    await message.channel.send("unexpected reply gievn".format(message)) # reply with an unexpected error message
            except:                                                                      # (if Aura replies but not with True for some reason)
                await message.channel.send("Couldn't make contact with Aura.calc".format(message)) # reply with an error message
                                                                                                   # (most likely an error with contacting Aura_calc)              

        elif content.lower() == 'check open windows':     # if message is 'check open windows' 
            try:
                outp = aura.openProgramsCheck()           # call Aura's active programs function
                await message.channel.send(outp.format(message))
            except:
                await message.channel.send("Couldn't make contact with Aura.calc".format(message))
        elif content.lower() == 'check open programs':    # or similar
            try:
                outp = aura.openProgramsCheck()           
                await message.channel.send(outp.format(message))
            except:
                await message.channel.send("Couldn't make contact with Aura.calc".format(message))
        elif content.lower() == "what's open?":           # or a less formal use
            try:
                outp = aura.openProgramsCheck()
                await message.channel.send(outp.format(message))
            except:
                await message.channel.send("Couldn't make contact with Aura.calc".format(message))
        elif content.lower() == 'what is open':
            try:
                outp = aura.openProgramsCheck()
                await message.channel.send(outp.format(message))
            except:
                await message.channel.send("Couldn't make contact with Aura.calc".format(message))


        elif content.lower() == 'open control panel':
            try:
                aura.openControlPanel()
            except:
                await message.channel.send("Couldn't make contact with Aura.calc".format(message))
        elif content.lower() == 'close control panel':
            try:
                aura.closeControlPanel()
            except:
                await message.channel.send("Couldn't make contact with Aura.calc".format(message))

                
        elif content.lower() == 'open ccleaner':
            try:
                aura.openCleaner()
            except:
                await message.channel.send("Couldn't make contact with Aura.calc".format(message))
                
        elif content.lower() == 'open spotify':
            try:
                aura.openSpotify()
            except:
                await message.channel.send("Couldn't make contact with Aura.calc".format(message))

        elif content.lower() == 'open youtube':
            try:
                aura.openYoutube()
            except:
                await message.channel.send("Couldn't make contact with Aura.calc".format(message))
                

        elif 'open' in content.lower():
            content = content.replace('Open ', '')  # remove 'open' with both capitalisations options
            content = content.replace('open ', '')  # I could convert the whole message to lowercase but that would get rid of any capitalisation semantics for the files
            try:
                aura.openFile(content)
            except:
                await message.channel.send("Couldn't make contact with Aura.calc".format(message))


        elif (content.lower()).startswith('say'):   # if the message starts with 'say'
            try:
                aura.pronounce(content)
            except:
                await message.channel.send("Couldn't make contact with Aura.calc".format(message))


        elif (content.lower()).startswith('what is'):
            try:
                outp = aura.wikiSearch(content)
                await message.channel.send(outp.format(message))
            except:
                await message.channel.send("Couldn't make contact with Aura.calc".format(message))
        elif (content.lower()).startswith('define'):
            try:
                outp = aura.wikiSearch(content)
                await message.channel.send(outp.format(message))
            except:
                await message.channel.send("Couldn't make contact with Aura.calc".format(message))


        elif (content.lower()).startswith('translate'):
            try:
                outp = aura.translate(content)
                await message.channel.send(outp.format(message))
            except:
                await message.channel.send("Couldn't make contact with Aura.calc".format(message))


        elif (content.lower()).startswith('image search for'):
            try:
                outp = aura.imageSearch(content)
                await message.channel.send(content.format(message))
                await message.channel.send(outp.format(message))
            except:
                await message.channel.send("Couldn't make contact with Aura.calc".format(message))
        elif (content.lower()).startswith('image search'):
            try:
                outp = aura.imageSearch(content)
                await message.channel.send(outp.format(message))
            except:
                await message.channel.send("Couldn't make contact with Aura.calc".format(message))
        elif (content.lower()).startswith('show me'):
            try:
                outp = aura.imageSearch(content)
                await message.channel.send(outp.format(message))
            except:
                await message.channel.send("Couldn't make contact with Aura.calc".format(message))
        elif (content.lower()).startswith('google image'):
            try:
                outp = aura.imageSearch(content)
                await message.channel.send(outp.format(message))
            except:
                await message.channel.send("Couldn't make contact with Aura.calc".format(message))


        elif (content.lower()).startswith('search for'):
            try:
                outp = aura.googleSearch(content)
                await message.channel.send(outp.format(message))
            except:
                await message.channel.send("Couldn't make contact with Aura.calc".format(message))
        elif (content.lower()).startswith('search'):
            try:
                outp = aura.googleSearch(content)
                await message.channel.send(outp.format(message))
            except:
                await message.channel.send("Couldn't make contact with Aura.calc".format(message))
        elif (content.lower()).startswith('google search'):
            try:
                outp = aura.googleSearch(content)
                await message.channel.send(outp.format(message))
            except:
                await message.channel.send("Couldn't make contact with Aura.calc".format(message))
        elif (content.lower()).startswith('google'):
            try:
                outp = aura.googleSearch(content)
                await message.channel.send(outp.format(message))
            except:
                await message.channel.send("Couldn't make contact with Aura.calc".format(message))
        elif (content.lower()).startswith('look up'):
            try:
                outp = aura.googleSearch(content)
                await message.channel.send(outp.format(message))
            except:
                await message.channel.send("Couldn't make contact with Aura.calc".format(message))
                
#======================================================  in development section

#======================================================

client = MyClient()                                                        # redefine as the client class
client.run('api_key_here')                                                 # run the discord client using the api key


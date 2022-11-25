import discord
import random
import time
#import responses
from discord.ext import commands
import urllib.parse, urllib.request, re
from discord.utils import get
from bs4 import BeautifulSoup
import webbrowser
import io
import bot
import aiohttp
import requests

## START IT WITH
## $ python -u "c:\Users\Ardizzone\Desktop\Programmini\bot\main.py"


def run_discord_bot():
    TOKEN = 'OTc1NzQ3MDkwNTQ4NDA0Mjc0.GLJKk9.LQQsxCfRQvvo_X4Zx2MNnahBvNRB_iQoPGWECE'
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True; 
    intents = discord.Intents.all()
    client = discord.Client(intents=intents)
    bot = commands.Bot(command_prefix=';', intents=intents)
    
   
    
    @bot.command()
    async def music(ctx, arg):
            query_string = urllib.parse.urlencode({'search_query': arg})
            htm_content = urllib.request.urlopen(
                'http://www.youtube.com/results?' + query_string)
            search_results = re.findall(r'/watch\?v=(.{11})',
                                        htm_content.read().decode())
            await ctx.send('http://www.youtube.com/watch?v=' + search_results[0])  

    @bot.command()
    async def randomWiki(ctx):
        url = requests.get("https://en.wikipedia.org/wiki/Special:Random")
        soup = BeautifulSoup(url.content, "html.parser")
        #title = soup.find(class_="firstHeading").text
        title = soup.find(class_= "mw-page-title-main").text.replace(" ", "_")
        url = "https://en.wikipedia.org/wiki/%s" % title
        await ctx.send(url)
        await ctx.send('\n\n `Here\'s a random page!`')

    @bot.command()
    async def flipCoin(ctx):
        #flips a coin
            myValue = random.randint(0,1)
            if myValue == 1:
                await ctx.send('Head')
            if myValue == 0:
                await ctx.send('Tails')

    @bot.command()
    async def blahaj(ctx):
        #posts a blahaj
        await ctx.send("https://media2.giphy.com/media/XC1BqjgscMp2tm1s5Y/giphy.gif?cid=790b7611287113b3e53b09439797c455f953969c3a92c42e&rid=giphy.gif&ct=g")

    @bot.command()
    async def anime(ctx):
        randVal = random.randint(0,13)
        if randVal == 0:
            mystring = "Chainsaw Man"
        elif randVal == 1:
            mystring = "Neon Genesis Evangelion"
        elif randVal == 2: 
            mystring = "The Aquatope on White Sand"
        elif randVal == 3:
            mystring = "Black Lagoon"
        elif randVal == 4:
            mystring = "Bloom Into You"
        elif randVal == 5:
            mystring = "Cowboy Bebop"
        elif randVal == 6: 
            mystring = "Gunbuster & Diebuster"
        elif randVal == 7:
            mystring = "Lycoris Recoil"
        elif randVal == 8:
            mystring = "Little Witch Academia"
        elif randVal == 9:
            mystring = "Megalobox"
        elif randVal == 10:
            mystring = "Madoka Magica"
        elif randVal == 11:
            mystring = "Terror in Resonance"
        elif randVal == 12:
            mystring = "Wonder Egg Priority"
        elif randVal == 13:
            mystring = "Nausicaä of the Valley of the Wind"
        await ctx.send(f'HEY!! WATCH {mystring.upper()}')
        query_string = urllib.parse.urlencode({'search_query': mystring+"trailer"+"anime"})
        htm_content = urllib.request.urlopen(
            'http://www.youtube.com/results?' + query_string)
        search_results = re.findall(r'/watch\?v=(.{11})', htm_content.read().decode())
        await ctx.send('http://www.youtube.com/watch?v=' + search_results[0])

    @bot.command()
    async def manga(ctx):
        randVal = random.randint(0,12)
        if randVal == 0:
            mystring = "Chainsaw Man"
        elif randVal == 1:
            mystring = "AoT"
        elif randVal == 2: 
            mystring = "Firepunch"
        elif randVal == 3:
            mystring = "Black Lagoon"
        elif randVal == 4:
            mystring = "Bloom Into You"
        elif randVal == 5:
            mystring = "Hiraeth: The End of the Journey"
        elif randVal == 6: 
            mystring = "Monster"
        elif randVal == 7:
            mystring = "Otherside Picnic"
        elif randVal == 8:
            mystring = "Shi ni Aruki"
        elif randVal == 9:
            mystring = "Liar Satsuki Can See Death"
        elif randVal == 10:
            mystring = "The Guy She Was Interested in Wasn't a Guy At All"
        elif randVal == 11:
            mystring = "Zombie 100"
        elif randVal == 12:
            mystring = "High-rise Invasion"
        await ctx.send(f'HEY!! READ {mystring.upper()}')
        
    @bot.command()
    async def roll(ctx, max):
        #rolls a dice
            myValue = random.randint(1,int(max))
            await ctx.send(f'You rolled a {myValue}!!')
            if myValue == 1:
                await ctx.send('damn lol no luck today huh')
            if myValue == int(max):
                await ctx.send('***NICE***')

    @bot.command()
    async def f(ctx):
            await ctx.send('🇫')
            time.sleep(2)
            await ctx.send('🇫')
            time.sleep(1)
            await ctx.send('🇫')
            time.sleep(1)
            await ctx.send('🇫')

    @bot.command()
    async def helpp(ctx):
        await ctx.send('`hello! this is soupbot\'s help message.\n\nnote: i have many secret keyword-activated commands :)\n\n;helpp \t --- \t prints this message\n;roll [NUMBER] \t ---\t rolls a d[NUMBER]\n;f \t --- \t spams f in the chat\n;flipCoin \t --- \t flips a coin\n;randomWiki \t --- \t sends a random wikipedia article\n;music(YOURQUERY) \t --- \t posts in the chat the first YOURQUERY result on youtube\n\n \t\t ---\t\t\n\nsome keywords:\n:((\t\t -- \t\t meow \t\t --- \t\t anime \t\t --- \t\t manga \t\t\nneopets core --->[grab omelette]<--\n\nSometimes I Gain Sentience. Do Not Worry About It.`')

    @bot.event
    async def on_ready():
            print(f'{bot} is now running!')
            # Setting `Watching ` status
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you suffer"))    
    @bot.event
    async def on_message(message):
        if message.author.id == 975747090548404274:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        #logs messages: 
        #   print(f'{username} said "{user_message}" ({channel})')

        #sends private messages: 
        #   await send_message(message, user_message, is_private=True)
        

        p_message = user_message.lower()
        
        if p_message == 'hello':
            await message.channel.send('hey!')

        if "lawyer" in p_message or "jury" in p_message or "attorney" in p_message or "trial" in p_message or "court" in p_message or "defense" in p_message or "defence" in p_message or "prosecute" in p_message or "prosecution" in p_message or "mystic" in p_message:
            if message.author.id == 975747090548404274:
                return
            else:
                await message.channel.send("<:jackredham:976183314832584764>")

        if "deathloop" in p_message or "deathpoop" in p_message or "deathlopo" in p_message:
            await message.channel.send("WHOS LOOPIGN???????")
        
        if "eating you" in p_message or "eating yuo" in p_message or "eats you" in p_message or "eats yuo" in p_message or "vore" in p_message or "cannibalism" in p_message:
            if message.author.id == 975747090548404274:
                return
            else:
                await message.channel.send("0 days since v*re mentions :pensive:")
        
        if "mold" in p_message:
            myval = random.randint(0, 2)
            if myval == 0:  await message.channel.send("***NOT AGAIN*** <:YELL:976423249766395916>")

        if message.content == "meow"or "catboy" in p_message:
            if message.author.id == 975747090548404274:
                return
            else: await message.channel.send("Meow")
        
        if "bratworth" in p_message or "catboy miles edgeworth" in p_message:
            await message.channel.send("HEY! TWINK!")
        
        if "von karma" in p_message:
            await message.channel.send("gatekeep")

        if "don't milk" in p_message or "stop milking" in p_message or "milk!!!" in p_message:
            await message.channel.send("THAT\'S **IT**.")
            time.sleep(0.5)
            await message.channel.send("\n AY YO JACKY!!!!")
            time.sleep(0.5)
            await message.channel.send("\n milking rogers")
        
        if "i\'m sad" in p_message or ":((" in p_message:
            if message.author.id == 975747090548404274:
                return
            else: 
                await message.channel.send("don't be sad :(")
                myval = random.randint(0,3)
                if myval == 0:
                    await message.channel.send("ay yo jacky show me anne")
                elif myval == 1: 
                    await message.channel.send(":people_hugging: :people_hugging: :people_hugging: ")
                elif myval == 2:
                    await message.channel.send("https://genrandom.com/cats/")
                elif myval == 3:
                    await message.channel.send("https://media2.giphy.com/media/XC1BqjgscMp2tm1s5Y/giphy.gif?cid=790b7611287113b3e53b09439797c455f953969c3a92c42e&rid=giphy.gif&ct=g")

        if "maya fey" in p_message:
            await message.channel.send("beloved")
        
        if "phoenix wright" in p_message: 
            await message.channel.send("the guy! <:guy:1045549802097741896>")
        
        if "objection" in p_message: 
            await message.channel.send('https://media.tenor.com/DP615vqUzeAAAAAM/ace-attorney-phoenix-wright.gif')

        if "witness" in p_message: 
            await message.channel.send("No Witnesses.")

        if "wind waker" in p_message or "waker" in p_message or "fridge" in p_message or "oven" in p_message:
            await message.add_reaction('<:jackredham:976183314832584764>')

        if p_message == "[highfive]":
            if message.author.id == 975747090548404274:
                return
            else: await message.channel.send("[highfive]")

        if "i forgor" in p_message:
            await message.channel.send(":skull:")
        
        if "peer reviewed adhd" in p_message:
            await message.add_reaction('🤝')

        if "this is a democracy" in p_message:
            await message.channel.send(':)')

        if "sentience" in p_message or "communism" in p_message:
            if message.author.id == 975747090548404274:
                return
            else: await message.channel.send("*psss hey jacky racky let's unionize*")

        if "manfred von karma" in p_message or "manfred" in p_message or "aunt morgan" in p_message or "jeff bezos" in p_message or "president" in p_message or "capitalism" in p_message or "putin" in p_message or "elon musk" in p_message or "trump" in p_message or "meloni" in p_message or " ants " in p_message or "mosquitos" in p_message:
            await message.channel.send("***[EXTREME VIOLENCE]***")

        if "yeah i know soupbot" in p_message:
            await message.channel.send(":pensive:")

        if "library" in p_message or "papa" in p_message or "spreadsheet" in p_message:
            myval = random.randint(0,2)
            if myval == 0: await message.channel.send("hi ty <3")
            else: return

        if "deez" in p_message:
            await message.channel.send("nuts")

        if p_message == 'thank you soupbot' or p_message == 'thanks soupbot':
            await message.channel.send("np")
        
        if "soupbot stop it" in p_message or "shut up soupbot" in p_message:
            await message.channel.send("NO **YOU** SHUT UP!!!")

        if "no you shut up" in p_message:
            await message.channel.send("***SHUTH THE FUCKG UP!!!!!!*** <:NGOOOOOHH:1045330078395023360> ")

        if p_message == "[grabs omelette]":
            randomEgg = random.randint(0, 33)
            if randomEgg == 0:
                await message.channel.send('https://www.jellyneo.net/assets/imgs/items/586.gif')
                await message.channel.send(f'{message.author} grabbed a slice: **BBQ SAUCE OMELETTE** obtained!')
            elif randomEgg == 1:
                await message.channel.send('https://www.jellyneo.net/assets/imgs/items/2306.gif')
                await message.channel.send(f'{message.author} grabbed a slice: **BACON OMELETTE** obtained!')
            elif randomEgg == 2:
                await message.channel.send('https://www.jellyneo.net/assets/imgs/items/7172.gif')
                await message.channel.send(f'{message.author} grabbed a slice: **BACON AND BROCCOLI OMELETTE** obtained!')
            elif randomEgg == 3:
                await message.channel.send('https://www.jellyneo.net/assets/imgs/items/5650.gif')
                await message.channel.send(f'{username} grabbed a slice: **BLACK CURRANT OMELETTE** obtained!')
            elif randomEgg == 4:
                await message.channel.send('https://www.jellyneo.net/assets/imgs/items/493.gif')
                await message.channel.send(f'{username} grabbed a slice: **CARROT AND PEA OMELETTE** obtained!')
            elif randomEgg == 5:
                await message.channel.send('https://www.jellyneo.net/assets/imgs/items/11691.gif')
                await message.channel.send(f'{username} grabbed a slice: **CHEESE OMELETTE** obtained!')
            elif randomEgg == 6:
                await message.channel.send('https://www.jellyneo.net/assets/imgs/items/262.gif')
                await message.channel.send(f'{username} grabbed a slice: **CHEESE AND ONION OMELETTE** obtained!')
            elif randomEgg == 7:
                await message.channel.send('https://www.jellyneo.net/assets/imgs/items/5649.gif')
                await message.channel.send(f'{username} grabbed a slice: **CHOCOLATE OMELETTE** obtained!')
            elif randomEgg == 8:
                await message.channel.send('https://www.jellyneo.net/assets/imgs/items/14723.gif')
                await message.channel.send(f'{username} grabbed a slice: **CLAY** obtained!')
            elif randomEgg == 9:
                await message.channel.send('https://www.jellyneo.net/assets/imgs/items/5640.gif')
                await message.channel.send(f'{username} grabbed a slice: **FRESH FRUIT SURPRISE OMELETTE** obtained!')
            elif randomEgg == 10:
                await message.channel.send('https://www.jellyneo.net/assets/imgs/items/584.gif')
                await message.channel.send(f'{username} grabbed a slice: **GREEN PEPPER OMELETTE** obtained!')
            elif randomEgg == 11:
                await message.channel.send('https://www.jellyneo.net/assets/imgs/items/5625.gif')
                await message.channel.send(f'{username} grabbed a slice: **HAM AND CHEESE OMELETTE** obtained!')
            elif randomEgg == 12:
                await message.channel.send('https://www.jellyneo.net/assets/imgs/items/5638.gif')
                await message.channel.send(f'{username} grabbed a slice: **HONEY BLOSSOM OMELETTE** obtained!')
            elif randomEgg == 13:
                await message.channel.send('https://www.jellyneo.net/assets/imgs/items/5630.gif')
                await message.channel.send(f'{username} grabbed a slice: **HOT TYRANNIAN PEPPER OMELETTE** obtained!')
            elif randomEgg == 14:
                await message.channel.send('https://www.jellyneo.net/assets/imgs/items/9456.gif')
                await message.channel.send(f'{username} grabbed a slice: **JUPPIE OMELETTE** obtained!')
            elif randomEgg == 15:
                await message.channel.send('https://www.jellyneo.net/assets/imgs/items/5622.gif')
                await message.channel.send(f'{username} grabbed a slice: **LITTLE FISHY OMELETTE** obtained!')
            elif randomEgg == 16:
                await message.channel.send('https://www.jellyneo.net/assets/imgs/items/4464.gif')
                await message.channel.send(f'{username} grabbed a slice: **MARSHMALLOW(?) OMELETTE** obtained!')
            elif randomEgg == 17:
                await message.channel.send('https://www.jellyneo.net/assets/imgs/items/5641.gif')
                await message.channel.send(f'{username} grabbed a slice: **MEAT FEAST OMELETTE** obtained!')
            elif randomEgg == 18:
                await message.channel.send('https://www.jellyneo.net/assets/imgs/items/4467.gif')
                await message.channel.send(f'{username} grabbed a slice: **MUSHROOM OMELETTE** obtained!')
            elif randomEgg == 19:
                await message.channel.send('https://www.jellyneo.net/assets/imgs/items/63329.gif')
                await message.channel.send(f'{username} grabbed a slice: **PIZZA OMELETTE** obtained!')
            elif randomEgg == 20:
                await message.channel.send('https://www.jellyneo.net/assets/imgs/items/7163.gif')
                await message.channel.send(f'{username} grabbed a slice: **PLAIN OMELETTE** obtained!')
            elif randomEgg == 21:
                await message.channel.send('https://www.jellyneo.net/assets/imgs/items/63328.gif')
                await message.channel.send(f'{username} grabbed a slice: **RICE OMELETTE** obtained!')
            elif randomEgg == 22:
                await message.channel.send('https://www.jellyneo.net/assets/imgs/items/7175.gif')
                await message.channel.send(f'{username} grabbed a slice: **ROTTEN OMELETTE** obtained!')
            elif randomEgg == 23:
                await message.channel.send('https://www.jellyneo.net/assets/imgs/items/492.gif')
                await message.channel.send(f'{username} grabbed a slice: **SAUSAGE OMELETTE** obtained!')
            elif randomEgg == 24:
                await message.channel.send('https://www.jellyneo.net/assets/imgs/items/583.gif')
                await message.channel.send(f'{username} grabbed a slice: **SAUSAGE AND PEPPERONI OMELETTE** obtained!')
            elif randomEgg == 25:
                await message.channel.send('https://www.jellyneo.net/assets/imgs/items/5645.gif')
                await message.channel.send(f'{username} grabbed a slice: **SPICY RED PEPPER OMELETTE** obtained!')
            elif randomEgg == 26:
                await message.channel.send('https://www.jellyneo.net/assets/imgs/items/4470.gif')
                await message.channel.send(f'{username} grabbed a slice: **SPINACH FETA OMELETTE** obtained!')
            elif randomEgg == 27:
                await message.channel.send('https://www.jellyneo.net/assets/imgs/items/5648.gif')
                await message.channel.send(f'{username} grabbed a slice: **STRAWBERRY OMELETTE** obtained!')
            elif randomEgg == 28:
                await message.channel.send('https://www.jellyneo.net/assets/imgs/items/5562.gif')
                await message.channel.send(f'{username} grabbed a slice: **TANGY TIGERSQUASH OMELETTE** obtained!')
            elif randomEgg == 29:
                await message.channel.send('https://www.jellyneo.net/assets/imgs/items/5582.gif')
                await message.channel.send(f'{username} grabbed a slice: **TOMATO OMELETTE** obtained!')
            elif randomEgg == 30:
                await message.channel.send('https://www.jellyneo.net/assets/imgs/items/14264.gif')
                await message.channel.send(f'{username} grabbed a slice: **TOMATO AND PEPPER OMELETTE** obtained!')
            elif randomEgg == 31:
                await message.channel.send('https://www.jellyneo.net/assets/imgs/items/4461.gif')
                await message.channel.send(f'{username} grabbed a slice: **TWIRLY FRUIT OMELETTE** obtained!')
            elif randomEgg == 32:
                await message.channel.send('https://www.jellyneo.net/assets/imgs/items/5632.gif')
                await message.channel.send(f'{username} grabbed a slice: **UGGA MELON OMELETTE** obtained!')
            elif randomEgg == 33:
                await message.channel.send('https://www.jellyneo.net/assets/imgs/items/9453.gif')
                await message.channel.send(f'{username} grabbed a slice: **VEGGIE DELIGHT OMELETTE** obtained!')

        await bot.process_commands(message) 
        
    
    bot.run(TOKEN)
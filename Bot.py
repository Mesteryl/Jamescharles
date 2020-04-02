import discord
import time
import asyncio
import discord.ext
from discord import client
from discord.ext import commands

clinet = discord.Client()

import random

Rage = 0

messages = joined = 0


async def update_stats():
    await clinet.wait_until_ready()
    global messages, joined

    while not clinet.is_closed():

        try:
            with open("States.txt", "a") as f:
                f.write(f"Time: {int(time.time())}, Messages: {messages}, Members Joined: {joined}\n")

            messages = 0
            joined = 0

            await  asyncio.sleep(60)
        except Exception as e:
            print(e)
            await  asyncio.sleep(0)


@clinet.event
async def on_member_update(before, after):
    n = after.nick
    if n:
        if n.lower().count("Fuck" or "Shit" or "Asshole") > 0:
            last = before.nick
            if last:
                await after.edit(nick=last)
            else:
                await after.edit(nick="No. you can't")


@clinet.event
async def on_member_join(member):
    global joined
    joined += 1
    for channel in member.server.channels:
        if str(channel) == "welcome":
            await clinet.send_message(f"""Welcome to the server {member.mention}""")


Fliper = 'Name'
Coin = 0


@clinet.event
async def on_message(message):
    Onrager = "On"
    global messages
    messages += 1
    id = clinet.get_guild(611146625317863435)
    channels = ["general", "📢-announcements", "james-test-chamber"]
    if message.content == ">Help":
        embed = discord.Embed(title="Commands",
                              description="All of the commands avalible (All commands start with a capital letter)")
        embed.add_field(name=">Help", value="Do I have to explain this?")
        embed.add_field(name=">Hello", value="Say hello to James")
        embed.add_field(name=">Age", value="Ask how old he is")
        embed.add_field(name=">Good", value="Tells you a good deed")
        embed.add_field(name=">Bad (Broken)", value="Tells you a bad deed")
        embed.add_field(name=">Gender", value="Ask it's gender")
        embed.add_field(name=">Name", value="Ask it's name")
        embed.add_field(name=">Users", value="Tells you how many people are in this server")
        embed.add_field(name=">Coin", value="Tells you how to flip a coin")
        embed.add_field(name=">Random", value="Opens a menu full of other random commands")
        await message.channel.send(content=None, embed=embed)

    elif str(message.channel) in channels:

        if message.content.find(">Hello") != -1:
            if (str(message.author) == "Mesteryl#4167"):
                await message.channel.send("Sup Mesteryl.")
            else:
                await message.channel.send(random.choice(list(open('RHI.txt', encoding="utf8"))))
        elif message.content.find(">Age") != -1:
            Age = int(random.randint(1,90))
            await message.channel.send(Age)
            await message.channel.send("Is... is discord good for me?")
        elif message.content.find(">Good") != -1:
            await message.channel.send(random.choice(list(open('GD.txt', encoding="utf8"))))
        #elif message.content.find(">Bad") != -1:
            #await message.channel.send(random.choice(list(open('BD.txt', encoding="utf8"))))
        elif message.content.find(">Gender") != -1:
            Gender = random.randint(1, 3)
            if (Gender == 1):
                await message.channel.send("A... Boy")
            elif (Gender == 2):
                await message.channel.send("A... Girl")
            elif (Gender == 3):
                await message.channel.send("Oh... I don't know anymore to be honest")
        elif message.content.find(">Name") != -1:
            await message.channel.send("My name is James Charles. It's right there noob.")
        elif message.content.find("Fuck") != -1:
            await message.channel.send(f"""Don't swear {message.author}""")
            time.sleep(1)
            await message.channel.send("If you swear 3 times, You will be banned")
            f = open("Swearlist.txt", "a")
            f.write(f"""{message.author}\n""")
            f.close()
        elif message.content.find("Shit") != -1:
            await message.channel.send(f"""Don't swear {message.author}""")
            time.sleep(1)
            await message.channel.send("If you swear 3 times, You will be banned")
            f = open("Swearlist.txt", "a")
            f.write(f"""{message.author}\n""")
            f.close()
        elif message.content.find("Dick") != -1:
            await message.channel.send(f"""Don't swear {message.author}""")
            time.sleep(1)
            await message.channel.send("If you swear 3 times, You will be banned")
            f = open("Swearlist.txt", "a")
            f.write(f"""{message.author}\n""")
            f.close()
        elif message.content.find("Asshole") != -1:
            await message.channel.send(f"""Don't swear {message.author}""")
            time.sleep(1)
            await message.channel.send("If you swear 3 times, You will be banned")
            f = open("Swearlist.txt", "a")
            f.write(f"""{message.author}\n""")
            f.close()
        elif message.content.find("Bitch") != -1:
            await message.channel.send(f"""Don't swear {message.author}""")
            time.sleep(1)
            await message.channel.send("If you swear 3 times, You will be banned")
            f = open("Swearlist.txt", "a")
            f.write(f"""{message.author}\n""")
            f.close()
        elif message.content.find("Cunt") != -1:
            await message.channel.send(f"""Don't swear {message.author}""")
            time.sleep(1)
            await message.channel.send("If you swear 3 times, You will be banned")
            f = open("Swearlist.txt", "a")
            f.write(f"""{message.author}\n""")
            f.close()
        elif message.content.find("fuck") != -1:
            await message.channel.send(f"""Don't swear {message.author}""")
            time.sleep(1)
            await message.channel.send("If you swear 3 times, You will be banned")
            f = open("Swearlist.txt", "a")
            f.write(f"""{message.author}\n""")
            f.close()
        elif message.content.find("shit") != -1:
            await message.channel.send(f"""Don't swear {message.author}""")
            time.sleep(1)
            await message.channel.send("If you swear 3 times, You will be banned")
            f = open("Swearlist.txt", "a")
            f.write(f"""{message.author}\n""")
            f.close()
        elif message.content.find("dick") != -1:
            await message.channel.send(f"""Don't swear {message.author}""")
            time.sleep(1)
            await message.channel.send("If you swear 3 times, You will be banned")
            f = open("Swearlist.txt", "a")
            f.write(f"""{message.author}\n""")
            f.close()
        elif message.content.find("asshole") != -1:
            await message.channel.send(f"""Don't swear {message.author}""")
            time.sleep(1)
            await message.channel.send("If you swear 3 times, You will be banned")
            f = open("Swearlist.txt", "a")
            f.write(f"""{message.author}\n""")
            f.close()
        elif message.content.find("bitch") != -1:
            await message.channel.send(f"""Don't swear {message.author}""")
            time.sleep(1)
            await message.channel.send("If you swear 3 times, You will be banned")
            f = open("Swearlist.txt", "a")
            f.write(f"""{message.author}\n""")
            f.close()
        elif message.content.find("cunt") != -1:
            await message.channel.send(f"""Don't swear {message.author}""")
            time.sleep(1)
            await message.channel.send("If you swear 3 times, You will be banned")
            f = open("Swearlist.txt", "a")
            f.write(f"""{message.author}\n""")
            f.close()
        elif message.content.find("FUCK") != -1:
            await message.channel.send(f"""Don't swear {message.author}""")
            time.sleep(1)
            await message.channel.send("If you swear 3 times, You will be banned")
            f = open("Swearlist.txt", "a")
            f.write(f"""{message.author}\n""")
            f.close()
        elif message.content.find("SHIT") != -1:
            await message.channel.send(f"""Don't swear {message.author}""")
            time.sleep(1)
            await message.channel.send("If you swear 3 times, You will be banned")
            f = open("Swearlist.txt", "a")
            f.write(f"""{message.author}\n""")
            f.close()
        elif message.content.find("DICK") != -1:
            await message.channel.send(f"""Don't swear {message.author}""")
            time.sleep(1)
            await message.channel.send("If you swear 3 times, You will be banned")
            f = open("Swearlist.txt", "a")
            f.write(f"""{message.author}\n""")
            f.close()
        elif message.content.find("ASSHOLE") != -1:
            await message.channel.send(f"""Don't swear {message.author}""")
            time.sleep(1)
            await message.channel.send("If you swear 3 times, You will be banned")
            f = open("Swearlist.txt", "a")
            f.write(f"""{message.author}\n""")
            f.close()
        elif message.content.find("BITCH") != -1:
            await message.channel.send(f"""Don't swear {message.author}""")
            time.sleep(1)
            await message.channel.send("If you swear 3 times, You will be banned")
            f = open("Swearlist.txt", "a")
            f.write(f"""{message.author}\n""")
            f.close()
        elif message.content.find("CUNT") != -1:
            await message.channel.send(f"""Don't swear {message.author}""")
            time.sleep(1)
            await message.channel.send("If you swear 3 times, You will be banned")
            f = open("Swearlist.txt", "a")
            f.write(f"""{message.author}\n""")
            f.close()
        elif message.content == ">Users":
            await message.channel.send(f"""There are {id.member_count} people in this server!""")
        elif message.content == ">Random Q":
            await message.channel.send(random.choice(list(open('RS.txt', encoding="utf8"))))
        elif message.content == ">Random S":
            await message.channel.send(random.choice(list(open('RSH.txt', encoding="utf8"))))
        elif message.content == ">Random":
            embed = discord.Embed(title="Random",
                                  description="All of the 'Random' commands avalible(Way more coming soon)")
            embed.add_field(name=">Random Q", value="A Random Quote")
            embed.add_field(name=">Random J (Under maintenance)", value="A Random Joke")
            embed.add_field(name=">Random S", value="A Random Shower Thought")
            await message.channel.send(content=None, embed=embed)
        elif message.content == ">Test" and str(message.author) == "Mesteryl#4167":
            await message.channel.send("Hu... Oh sorry. Let me just write this one last text")
            time.sleep(2)
            await message.channel.send("... and...")
            time.sleep(3)
            await  message.channel.send("**YES** ok so, what do you want?")
        elif message.content == (">Coin"):
            await message.channel.send(
                "You wanna flip a coin? Ok sure. Write '>Flip' if you want to flip a coin.")
        elif message.content == (">Flip"):
            time.sleep(2)
            Coin = random.randint(0, 105)
            if (Coin < 50 and Coin > 0):
                await message.channel.send("Heads!")
            elif (Coin < 100 and Coin > 50):
                await message.channel.send("Tails!")
            elif (Coin < 105 and Coin > 100):
                await message.channel.send("Oh... It landed in the middle... Sorry.")
        elif message.content == (">Dice"):
            time.sleep(2)
            Dice = random.randint(1, 6)
            await message.channel.send("It landed on", Dice)

clinet.loop.create_task(update_stats())

clinet.login(process.env.BOT_TOKEN)

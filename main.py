import discord
from dotenv import load_dotenv
import json
import os
import functions as func

#Create client connection to Discord
client = discord.Client()


@client.event
async def on_ready():
    '''Confirm that connection has been established '''
    print("Logged in".format(client))
    return


@client.event
async def on_message(message):
    # Access JSON file for counting sentences checked and verified
    filename = os.path.dirname(os.path.realpath(__file__)) + '/data.json'
    with open(filename, "r") as file1:
        data = json.load(file1)
        file1.close()

    # Don't check message if written by self
    if message.author == client.user:
        return

    # Update checked messages count
    data["wa"]["checked_total"] += 1
    data["al"]["checked_total"] += 1

    # If words of message are in alphabetical order, update count and print
    if func.words_alphabetical(message.content):
        data["wa"]["checked_fits"] += 1
        wact = data["wa"]["checked_total"]
        wacf = data["wa"]["checked_fits"]
        await message.channel.send(f"Would you look at that, all of the words in your message are in alphabetical order.\nI now have checked {wact} messages so far, and only {wacf} of them are in alphabetical order.")

        # If words of message have all letters of alphabet, update count and print
        if func.all_letters(message.content):
            data["al"]["checked_fits"] += 1
            alcf = data["al"]["checked_fits"]
            await message.channel.send(f"I also noticed that your message has all the letters in the alphabet. Only {alcf} of them are like that.")

    # If words of message have all letters of alphabet, update count and print
    elif func.all_letters(message.content):
        data["al"]["checked_fits"] += 1
        alct = data["al"]["checked_total"]
        alcf = data["al"]["checked_fits"]
        await message.channel.send(f"Would you look at that, your message has all the letters in the alphabet.\nI now have checked {alct} messages so far, and only {alcf} of them have all the letters in the alphabet.")

    # Update JSON file
    with open(filename, "w") as file2:
        json.dump(data, file2, indent=4)
        file2.close()

    return

# Read secret token
load_dotenv()
client.run(os.getenv("TOKEN"))

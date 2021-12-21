import discord
import json
import functions as func

client = discord.Client()

@client.event
async def on_ready():
    print("Logged in".format(client))
    return


@client.event
async def on_message(message):
    with open("data.json") as file1:
        data = json.load(file1)
        file1.close()

    data["wa"]["checked_total"] += 1
    data["al"]["checked_total"] += 1

    if message.author == client.user:
        return

    if func.words_alphabetical(message.content):
        data["wa"]["checked_fits"] += 1
        wact = data["wa"]["checked_total"]
        wacf = data["wa"]["checked_fits"]
        await message.channel.send(f"Would you look at that, all of the words in your message are in alphabetical order.\nI now have checked {wact} messages so far, and only {wacf} of them are in alphabetical order.")
        if func.all_letters(message.content):
            data["al"]["checked_fits"] += 1
            alcf = data["al"]["checked_fits"]
            await message.channel.send(f"I also noticed that your message has all the letters in the alphabet. Only {alcf} of them are like that.")

    elif func.all_letters(message.content):
        data["al"]["checked_fits"] += 1
        alct = data["al"]["checked_total"]
        alcf = data["al"]["checked_fits"]
        await message.channel.send(f"Would you look at that, your message has all the letters in the alphabet.\nI now have checked {alct} messages so far, and only {alcf} of them have all the letters in the alphabet.")

    with open("data.json") as file2:
        json.dump(data, file2, "")
        file2.close()

client.run("TOKEN")

import os
import discord
from dotenv import load_dotenv

load_dotenv()   #?
token = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True


class DevPSUBot(discord.Client):
    async def on_ready(self):       #async does ?
        print("logged on!")
    async def on_message(self, message):
        print(f"message found: {message.content} from {message.author} in {message.channel}")
        if message.author == client.user:
            return

        if message.content.lower() == "hello": #when someone says hello
            await message.channel.send("Hello!")    #bot sends this message 

        if client.user in message.mentions:
            print("bot mentioned!")
            await message.channel.send("I was mentioned") #bot sends this message
        
        if message.content == "react":
            print("react command recognized")
            await message.add_reaction("👍") #you can add another line so that the bot can do more than one reaction

    async def on_typing(self, channel, user, when):
        print(f"{user} is typing in {channel} at {when}")
        await channel.send(f"I see you typing, {user}")


client = DevPSUBot(intents=intents) #difference betweent intents and intents=intents?
client.run(token)

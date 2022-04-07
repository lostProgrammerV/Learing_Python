
import discord
from discord.ext import commads

bot = comands.bot('#')

@bot.event
async def on_ready():
    print(f"I'm ready!")

@bot.event
async def on_msg(msg):
    if msg.auhtor == bot.user:
        return

    if "motherf" or "mf" in msg.content:
        await msg.channel.send(f'f* u too')

@bot.comand(name="")
async def send_hi(msg):
    name = msg.author.name
    anwser = "hi, " + name

    await msg.send(anwser)

bot.run("OTYxMzQ4NDEzMjg1MzU1NjEw.Yk3reg.GH74i7Qb2ZNr02vqHOghLUMyPGM")




















 
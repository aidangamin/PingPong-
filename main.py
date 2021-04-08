# Imports Python Modules
import discord
from discord.ext import commands
from discord_slash import SlashCommand , SlashCommandOptionType , SlashContext
from discord_slash.utils.manage_commands import create_option
import random
import ctypes

# Changes The Window Name
ctypes.windll.kernel32.SetConsoleTitleW("Discord.py Bot By : AidanGamin")

client = commands.Bot(command_prefix='!')
slash = SlashCommand(client , sync_commands=True)

# Sets Activity To "Playing MeowMeow VI"
# And Prints "Ready!" When Bot Is Active
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='MeowMeow VI' ))
    print ("Ready!")

# Makes A Ping Command.
@client.command()
async def ping(ctx):
    embed=discord.Embed(title="Ping", description="!ping", color=0xfb00ff)
    embed.set_author(name="PingPong")
    embed.add_field(name="Pong!",value=f"You Got Ponged ({client.latency}s)", inline=False)
    embed.set_footer(text=f"Requested By {ctx.author.name}")
    await ctx.send(embed=embed)

# A Random Number Genarator Slash Command
@client.command()
async def rand(ctx):
# Generates A Number From 1 - 100
    result = random.randint(1, 100)
    embed=discord.Embed(title="Random Number", description="!rand", color=0xfb00ff)
    embed.set_author(name="PingPong")
    embed.add_field(name="You're Random Number is...", value=f"{result}", inline=False)
    embed.set_footer(text=f"Requested By {ctx.author.name}")
    await ctx.send(embed=embed)

#Source Code Command
@slash.slash(name = 'Source' ,description = 'source code' , guild_ids = [680199822329774092] )
async def source(ctx : SlashContext ):
    embed=discord.Embed(title="Source Code", description="/source", color=0xfb00ff)
    embed.set_author(name="PingPong")
    embed.add_field(name="My GitHub is... https://github.com/AidanProgramiz/PingPong-",value=f"Check Out My Source Code If You Want To Make A Bot Like Me", inline=False)
    embed.set_footer(text=f"Requested By {ctx.author.name}, Bot Made By AidanGamin")
    await ctx.send(embed=embed)


# Token
client.run("Insert Token Here")

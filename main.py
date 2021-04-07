import discord
from discord.ext import commands
from discord_slash import SlashCommand , SlashCommandOptionType , SlashContext
from discord_slash.utils.manage_commands import create_option
import random

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
        await ctx.send(content=ff"Pong! ({client.latency} seconds)")

# A Random Number Genarator Slash Command
@slash.slash(name="randomnumber",
             description="Makes A Random Number",
             options=[
               create_option(
                 name="num1",
                 description="Starting Number",
                 option_type=3,
                 required=False,
                 name="num2",
                 description="Ending Number",
                 option_type=3,
                 required=False
               )
             ])
async def test(ctx, optone: str):
    result = random.randint(num1, num2)
    embed=discord.Embed(title="Random Number", description="/randomnumber", color=0xfb00ff)
    embed.set_author(name="PingPong")
    embed.add_field(name="You're Random Number is...", value=f"{result}", inline=False)
    embed.set_footer(text=f"Requested By {ctx.author.name}")
    await ctx.send(embed=embed)



client.run("[ Insert Token Here ]")

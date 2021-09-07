import os
import discord
import gasprice
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

bot = commands.Bot(command_prefix='g!')
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

#-----------------------------------------------------------------------------#
# Commands #

@bot.command(name='price', help='Gets the current Ethereum gas price')
async def price(ctx, *args): 
    

#-----------------------------------------------------------------------------#
# Basic Stuff #

@bot.command(name='info', help='Displays information about the bot.')
async def info(ctx):
    info_embed = discord.Embed(
        title="Info",
        description=f'This is gasbot, a small personal bot that tracks and displays Ethereum gas prices! This bot is currently in **{len(bot.guilds)}** servers!', 
        color=discord.Color.purple()
    )
    info_embed.set_footer(text='Made with <3 by ABlazingEBoy#7375')
    await ctx.send(embed=info_embed)

@bot.command(name='help', help='Shows this page.')
async def help(ctx, args=None):
    help_embed = discord.Embed(title="Command Usage", color=discord.Color.purple())
    command_names_list = [x.name for x in bot.commands]

    if not args:
        help_embed.add_field(
            name="List of supported commands:",
            value="\n".join([str(i+1)+".  `"+x.name+"`" for i,x in enumerate(bot.commands)]),
            inline=False
        )
        help_embed.set_footer(
            text="Type \'g!help <command name>\' for more details about each command."
        )

    elif args in command_names_list:
        help_embed.add_field(
            name='`=' + args + '`',
            value=bot.get_command(args).help
        )

    else:
        help_embed.add_field(
            name="Sorry!",
            value="That command doesn't exist."
        )

    await ctx.send(embed=help_embed)

@bot.command(name='ping', help='Basically useless, just tells you if the bot is running.')
async def ping(ctx):
    if round(bot.latency * 1000) <= 50:
        embed=discord.Embed(title="Pong!", description=f"The ping is **{round(bot.latency *1000)}** milliseconds!", color=0x44ff44)
    elif round(bot.latency * 1000) <= 100:
        embed=discord.Embed(title="Pong!", description=f"The ping is **{round(bot.latency *1000)}** milliseconds!", color=0xffd000)
    elif round(bot.latency * 1000) <= 200:
        embed=discord.Embed(title="Pong!", description=f"The ping is **{round(bot.latency *1000)}** milliseconds!", color=0xff6600)
    else:
        embed=discord.Embed(title="Pong!", description=f"The ping is **{round(bot.latency *1000)}** milliseconds!", color=0x990000)
    await ctx.send(embed=embed)

# @bot.command(name='invite', help='Provides a link to invite this bot to your server!')
# async def invite(ctx):
#     invite_embed = discord.Embed(
#         title='Add this bot to your server!',
#         url='placeholder',
#         color=discord.Color.red()
#     )
#     invite_embed.set_footer(text=f'Currently in {len(bot.guilds)} servers! | Made with <3 by ablazingeboy#7375')
#     await ctx.send(embed=invite_embed)

#-----------------------------------------------------------------------------#

bot.run(TOKEN)
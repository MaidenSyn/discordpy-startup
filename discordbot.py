from discord.ext import commands

import os

import traceback

import random



bot = commands.Bot(command_prefix='/')

token = os.environ['BOT_TOKEN']




@bot.event

async def on_command_error(ctx, error):

    orig_error = getattr(error, "original", error)

    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())

    await ctx.send(error_msg)




@bot.command()

async def challenge(ctx):
    
    chas = ['cha1', 'cha2', 'cha3', 'cha4', 'cha5', 'cha6', 'cha7']

    random_chas = random.choice(chas)

    await ctx.send(random_chas)



bot.run(token)

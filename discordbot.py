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



challenges = ['challenge1', 'challenge2', 'challenge3', 'challenge4', 'challenge5', 'challenge6', 'challenge7']

random_challenge = random.choice(challenges)





@bot.command()

async def challenge(ctx):

    await ctx.send(random_challenge)







bot.run(token)

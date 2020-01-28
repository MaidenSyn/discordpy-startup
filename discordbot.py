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

names = ['Sam', 'Paul', 'Mark', 'Simon', 'Sean', 'Samantha', 'Ellen']
random_name = random.choice(names)

print(random_name)

@bot.command()
async def ping(ctx):
    await ctx.send(random_name)
    


bot.run(token)

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
    
Sam = 'Hi my name is Sam'
Paul = 'Hi my name is Paul'
Mark = 'Hi my name is Mark'
Simon = 'Hi my name is Simon'
Sean = 'Hi my name is Sean'
Samantha = 'Hi my name is Samantha'
Ellen = "Hi my name is Ellen'


names = [ Sam, Paul, Mark, Simon, Sean, Samantha, Ellen]
random_name = random.choice(names)


@bot.command()
async def ping(ctx):
    await ctx.send(random_name)
    


bot.run(token)

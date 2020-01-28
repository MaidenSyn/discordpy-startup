from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
    
    
@bot.event
async def on_member_join(member):
    print(f'(member) has joined a server.')
    
    
    

@bot.event
async def on_member_remove(member):
    print(f'(member) has left a server.')


bot.run(token)

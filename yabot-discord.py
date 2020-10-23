# -*- coding: utf-8 -*-

import discord
from discord.ext import commands, tasks
#from itertools import cycle

import os
import random
import settings

client = commands.Bot(command_prefix = "/") #prefixo de comando
#status = cycle(['Bom Dia','Boa Tarde','Boa Noite'])

@client.event
async def on_ready():
#    change_status.start()
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('/Yabolso!'))
    print('Bot is ready')

#----------------------------------ERRORS-------------------------------------#
  
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Esse comando não existe.')
        
#---------------------------------CHECKS--------------------------------------#

def is_it_me(ctx):
    return ctx.author.id == 345661266305744896
    
@client.command()
@commands.check(is_it_me)
async def example(ctx):
    await ctx.send(f'Hi im {ctx.author}.')
    
#-----------------------------BACKGROUND TASK---------------------------------#
    
#@tasks.loop(seconds=21600)
#async def change_status():
#    await client.change_presence(activity=discord.Game(next(status)))
    
#------------------------------------COGS-------------------------------------#
    
@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")

@client.command()    
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    
@client.command()    
async def reload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")
    
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')

#---------------------------------COMANDO CLEAR-------------------------------#   
    
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit = amount + 1)
 
#-----------------------COMANDOS PRO BOT--------------------------------------#

@client.command(aliases=['8ball','teste'])
async def _8ball(ctx, *, question):
    responses = ["Sim.",
                 "Com certeza!",
                 "Talvez?",
                 "Acho que não...",
                 "Talvez sim, talvez não de verdade nsei."]
    
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
    
#------------------------EVENTOS DE ENTRADA E SAIDA---------------------------#
    
@client.event                              
async def on_member_join(member):
    print(f"{member} entrou no servidor.")
    
@client.event
async def on_member_remove(member):
    print(f"{member} saiu do servidor.")
    
#-------------------------COMANDOS KICK, BAN E UNBAN--------------------------#
    
#@client.command()
#async def kick(ctx, member : discord.Member, *, reason=None):
#    await member.kick(reason=reason)
#    
#@client.command()
#async def ban(ctx, member : discord.Member, *, reason=None):
#    await member.ban(reason=reason)
#    await ctx.send(f"Banned {member.mention}")
#    
#@client.command()
#async def unban(ctx, *, member):
#    bannedUsers = await ctx.guild.bans()
#    memberName, memberDiscriminator = member.split('#')
#    
#    for banEntry in bannedUsers:
#        user = banEntry.user
#        
#        if (user.name, user.discriminator) == (memberName, memberDiscriminator):
#            await ctx.guild.unban(user)
#            await ctx.send(f"Unbanned {user.mention}")
#            return


    
client.run(f"{settings.token}")






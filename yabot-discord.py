# -*- coding: utf-8 -*-

import settings
import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = "/") #prefixo de comando

@client.event
async def on_ready():
    print("Bot ta pronto.")
    
#@client.command()
#async def unban():
    
    
#-------------------------COMANDOS KICK E BAN---------------------------------#
    
#@client.command()
#async def kick(ctx, member: discord.Member, *, reason=None):
#    await member.kick(reason=reason)
    
#@client.command()
#async def ban(ctx, member: discord.Member, *, reason=None):
#    await member.ban(reason=reason)
 
#---------------------------------COMANDO CLEAR-------------------------------#   
    
@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit = amount + 1)
   
#-----------------------COMANDOS PRO BOT--------------------------------------#
    
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! Latência: {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball','test'])
async def _8ball(ctx, *, question):
    responses = ["Sim.",
                 "Com certeza!",
                 "Talvez?",
                 "Acho que não...",
                 "Talvez sim, talvez não de verdade nsei."]
    
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
    
#------------------------EVENTOS DE ENTRADA E SAIDA---------------------------#
#@client.event                              
#async def on_member_join(member):
#    print(f"{member} entrou no servidor.")
#    
#@client.event
#async def on_member_remove(member):
#    print(f"{member} saiu do servidor.")
     
client.run(f"{settings.token}")























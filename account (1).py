import discord
import youtube_dl
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
from youtube_dl import YoutubeDL
import time
import asyncio
from discord.utils import get
import discord.utils
import os

token = 'NzAwNzY5NTY3MDk3NzQ5NjQ0.Xpnxwg.ktPibqtl6hknGg5Uz2F2x9p8yBc'
client = discord.Client()
client = commands.Bot(command_prefix = '.')



@client.event
async def on_ready():
    print('Bot is ready.')
    
    


@client.event
async def on_message(message):
    guild = client.get_guild(634513158593052683)
    channel = client.get_channel(691449697864515614)
    r = 0
    for i in ctx.guild.voice_channels:
        if message.content == "show":
            channel = discord.utils.get(guild.voice_channels,id=i.id)
            
            r+=len(channel.members)
        await channel.send(r)
    
    
    
    
@client.event
async def on_message(message):
    channel = client.get_channel(700772608030933135)
    channel2 = client.get_channel(700772357220073524)
    guild = client.get_guild(633775363683647552)#Versace
    guild2 = client.get_guild(633031988735115274)#infinity
    guild3 = client.get_guild(692164850553454613)#Hush
    guild4 = client.get_guild(692199921616683028)#venice
    guild5 = client.get_guild(646399083015045138)#rain
    guild6 = client.get_guild(644709521834639360)#Ls
    guild7 = client.get_guild(675732905548578820)#OneRoof
    guild8 = client.get_guild(693262651807236137)#Future
    guild9 = client.get_guild(651982013863297024)#Enigma
    guild10 = client.get_guild(365852388617093130)#Vision Omg
    voice = discord.utils.get(guild.voice_channels, id=641807146756866078)
    voice2 = discord.utils.get(guild2.voice_channels, id=633033309735223316)
    voice3 = discord.utils.get(guild3.voice_channels, id=692164850553454617)
    voice4 = discord.utils.get(guild4.voice_channels, id=693996068265787612)
    voice5 = discord.utils.get(guild5.voice_channels, id=685260590624800809)
    voice6 = discord.utils.get(guild6.voice_channels, id=645121012060389386)
    voice7 = discord.utils.get(guild7.voice_channels, id=677108534336290818)
    voice8 = discord.utils.get(guild8.voice_channels, id=693669739742101585)
    voice9 = discord.utils.get(guild9.voice_channels, id=675780805423005718)
    voice10 = discord.utils.get(guild10.voice_channels, id=620348106013147166)
    r = 0
    r2 = 0
    r3 = 0
    r4 = 0
    r5 = 0
    r6 = 0
    r7 = 0
    r8 = 0
    r9 = 0
    r10 = 0
    b = 0
    b2 = 0
    b3 = 0
    b4 = 0
    b5 = 0
    b6 = 0
    b7 = 0
    b8 = 0
    b9 = 0
    b10 = 0
    if message.content == "show" and str(message.author) == "tester23#0152":
        for i in guild.voice_channels:
            channels = discord.utils.get(guild.voice_channels,id=i.id)
            for i in channels.members:
                if i.bot:
                    b+=1
                else:
                    r+=1
        for i in guild2.voice_channels:
            channels2 = discord.utils.get(guild2.voice_channels,id=i.id)
            for i in channels2.members:
                if i.bot:
                    b2+=1
                else:
                    r2+=1
        for i in guild3.voice_channels:
            channels3 = discord.utils.get(guild3.voice_channels,id=i.id)
            for i in channels3.members:
                if i.bot:
                    b3+=1
                else:
                    r3+=1
        for i in guild4.voice_channels:
            channels4 = discord.utils.get(guild4.voice_channels,id=i.id)
            for i in channels4.members:
                if i.bot:
                    b4+=1
                else:
                    r4+=1

        for i in guild5.voice_channels:
            channels5 = discord.utils.get(guild5.voice_channels,id=i.id)
            for i in channels5.members:
                if i.bot:
                    b5+=1
                else:
                    r5+=1

        for i in guild6.voice_channels:
            channels6 = discord.utils.get(guild6.voice_channels,id=i.id)
            for i in channels6.members:
                if i.bot:
                    b6+=1
                else:
                    r6+=1

        for i in guild7.voice_channels:
            channels7 = discord.utils.get(guild7.voice_channels,id=i.id)
            for i in channels7.members:
                if i.bot:
                    b7+=1
                else:
                    r7+=1

        for i in guild8.voice_channels:
            channels8 = discord.utils.get(guild8.voice_channels,id=i.id)
            for i in channels8.members:
                if i.bot:
                    b8+=1
                else:
                    r8+=1

        for i in guild9.voice_channels:
            channels9 = discord.utils.get(guild9.voice_channels,id=i.id)
            for i in channels9.members:
                if i.bot:
                    b9+=1
                else:
                    r9+=1

        for i in guild10.voice_channels:
            channels10 = discord.utils.get(guild10.voice_channels,id=i.id)
            for i in channels10.members:
                if i.bot:
                    b10+=1
                else:
                    r10+=1




        await channel.send(
        f"**Versace:**\n**{voice}**, **Bot's: {b}**\n"
        "===================== \n"
        f"**Infinity:**\n**{voice2}**, **Bot's: {b2}**\n"
        "===================== \n"
        f"**Hush:**\n**{voice3}**, **Bot's: {b3}**\n"
        "===================== \n"
        f"**Venice:**\n**{voice4}**, **Bot's: {b4}**\n"
        "===================== \n"
        f"**Rain:**\n**{voice5}**, **Bot's: {b5}**\n"
        "===================== \n"
        f"**Lordliness:**\n**{voice6}**, **Bot's: {b6}**\n"
        "===================== \n"
        f"**OneRoof:**\n**{voice7}**, **Bot's: {b7}**\n"
        "===================== \n"
        f"**Future:**\n**{voice8}**, **Bot's: {b8}**\n"
        "===================== \n"
        f"**Roma:**\n**{voice9}**, **Bot's: {b9}**\n"
        "===================== \n"
        f"**Vision Omg:**\n **{voice10}**, **Bot's: {b10}**\n"

        )
        await channel2.send("show")
        
    
    
    


client.run(token, bot=False)
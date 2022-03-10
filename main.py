from calendar import c
from distutils.command.config import config
from operator import truediv
from re import X
from traceback import print_tb
from unicodedata import name
import random
import os

from click import pass_context
import keep_alive
import discord
import datetime, time
import json
from discord.ext import commands
from discord.utils import get
from discord import Webhook, RequestsWebhookAdapter

TOKEN = os.getenv("TOKEN")

"""Load JSON"""
cwd = os.getcwd()
with open(cwd + "/configs.json") as data_file:    
    configs = json.load(data_file)

client = discord.Client
client = commands.Bot(command_prefix=">", help_command=None, intents = discord.Intents.all())
randomchoise10 = ["slow dikit", "bentar", "bentaran jangan dispam", "stop dulu", "bentar cayang ku"]

"""Coldown Handler"""
@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandOnCooldown):
		await ctx.send(f"{random.choice(randomchoise10)}, tunggu {round(error.retry_after, 2)} detik lagi!")

@client.event
async def on_ready():
    print('has been loaded') 
    global startTime #global variable to be used later in cog
    startTime = time.time() # snapshot of time when listener sends on_ready
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=">help"),status=discord.Status.do_not_disturb)


@client.command(name='apakah')
@commands.cooldown(1, 10, commands.BucketType.guild)
async def apakah(ctx):
    """Check Guild Id"""
    if ctx.guild.id == 864789922233057300:
        """Check Room Request"""
        if ctx.channel.id == 950603060823064616:
            randomchoise = ["kayaknya iya", "ga", "ga tau", "enggak juga", "kurang tau", "kurang yakin", "bisa jadi", "mungkin aja", "iya kayaknya", "bisa dibilang iya", "kata siapa?", "fek", "ril", "engga lah", "ngga kayaknya", "ga mungkin"]
            if (ctx.message.content in [">apakah bot aja", ">apakah iya", ">apakah", ">apakah aku", "apakah doang", ">apakah akan"]):
                print("canceling..")
                randomchoise1 = ["ga jelas", "apakah apaan kanjut", "apakah apanya", "yang bener anjime", "lluwh gjls"]
                await ctx.send(f"{random.choice(randomchoise1)}")
            else:
                await ctx.send(f"{random.choice(randomchoise)}")
    else:
            randomchoise = ["kayaknya iya", "ga", "ga tau", "enggak juga", "kurang tau", "kurang yakin", "bisa jadi", "mungkin aja", "iya kayaknya", "bisa dibilang iya", "kata siapa?", "fek", "ril", "engga lah", "ngga kayaknya", "ga mungkin"]
            if (ctx.message.content in [">apakah bot aja", ">apakah iya", ">apakah", ">apakah aku", "apakah doang", ">apakah akan"]):
                print("canceling..")
                randomchoise1 = ["ga jelas", "apakah apaan kanjut", "apakah apanya", "yang bener anjime", "lluwh gjls"]
                await ctx.send(f"{random.choice(randomchoise1)}")
            else:
                await ctx.send(f"{random.choice(randomchoise)}")

@client.command(name='kapan')
@commands.cooldown(1, 10, commands.BucketType.guild)
async def kapan(ctx):
    """Check Guild Id"""
    if ctx.guild.id == 864789922233057300:
        """Check Room Request"""
        if ctx.channel.id == 950603060823064616:
            randomchoise = ["ga tau", "nanti", "mungkin 4 bulan", "kurang tau", "emang bakalan jadi?", "bulan depan", "bentar lagi", "taun depan", "minggu ini", "dibulan ini", "gtw"]
            if (ctx.message.content in [">kapan-kapan", ">kapan aja", ">kapan kapan", ">kapan", ">kapan aku", "kapan doang"]):
                print("canceling..")
                randomchoise1 = ["ga jelas", "kapan apaan kanjut", "kapan apanya", "yang bener anjime", "lluwh gjls"]
                await ctx.send(f"{random.choice(randomchoise1)}")
            else:
                await ctx.send(f"{random.choice(randomchoise)}")             
    else:
            randomchoise = ["ga tau", "nanti", "mungkin 4 bulan", "kurang tau", "emang bakalan jadi?", "bulan depan", "bentar lagi", "taun depan", "minggu ini", "dibulan ini", "gtw"]
            if (ctx.message.content in [">kapan-kapan", ">kapan aja", ">kapan kapan", ">kapan", ">kapan aku", "kapan doang"]):
                print("canceling..")
                randomchoise1 = ["ga jelas", "kapan apaan kanjut", "kapan apanya", "yang bener anjime", "lluwh gjls"]
                await ctx.send(f"{random.choice(randomchoise1)}")
            else:
                await ctx.send(f"{random.choice(randomchoise)}")


@client.command(name='kapanClone')
@commands.cooldown(1, 10, commands.BucketType.guild)
async def kpn(ctx):
    """Check Guild Id"""
    if ctx.guild.id == 864789922233057300:
        """Check Room Request"""
        if ctx.channel.id == 950603060823064616:
            randomchoise = ["tunggu aja","ga tau", "nanti", "mungkin 4 bulan", "kurang tau", "emang bakalan jadi?", "bulan depan", "bentar lagi", "taun depan", "minggu ini", "dibulan ini", "gtw"]
            if (ctx.message.content in [">kapan-kapan", ">kapan aja", ">kapan kapan", ">kapan", ">kapan aku", "kapan doang"]):
                print("canceling..")
                randomchoise1 = ["ga jelas", "kapan apaan kanjut", "kapan apanya", "yang bener anjime", "lluwh gjls"]
                await ctx.send(f"{random.choice(randomchoise1)}")
            else:
                await ctx.send(f"{random.choice(randomchoise)}")
    else:
            randomchoise = ["tunggu aja","ga tau", "nanti", "mungkin 4 bulan", "kurang tau", "emang bakalan jadi?", "bulan depan", "bentar lagi", "taun depan", "minggu ini", "dibulan ini", "gtw"]
            if (ctx.message.content in [">kapan-kapan", ">kapan aja", ">kapan kapan", ">kapan", ">kapan aku", "kapan doang"]):
                print("canceling..")
                randomchoise1 = ["ga jelas", "kapan apaan kanjut", "kapan apanya", "yang bener anjime", "lluwh gjls"]
                await ctx.send(f"{random.choice(randomchoise1)}")
            else:
                await ctx.send(f"{random.choice(randomchoise)}")

@client.command(name='siapa')
@commands.cooldown(1, 10, commands.BucketType.guild)
async def siapa(ctx, *, keterangan):
    print("used")
    if ctx.guild.id == 864789922233057300:
        print("yes1")
        """Check Room Request"""
        if ctx.channel.id == 950603060823064616:
            user = random.choice(ctx.guild.members)

                    # Just do it over if it is a bot
            while (user.bot):
                user = random.choice(ctx.guild.members)
            Matches = ["gua", "aku", "gw", "saya", "sy", "sya"]
            print("psaja yes2")
            if any (X in keterangan for X in Matches):
                print("psaja yes3")
                """Matches Handler"""
                keterangan2 = None
                if 'gua' in keterangan:
                    keterangan2 = keterangan.replace("gua", ctx.message.author.mention)
                if 'gw' in keterangan:
                    keterangan2 = keterangan.replace("gw", ctx.message.author.mention)
                if 'aku' in keterangan:
                    keterangan2 = keterangan.replace("aku", ctx.message.author.mention)
                if 'saya' in keterangan:
                    keterangan2 = keterangan.replace("saya", ctx.message.author.mention)
                if 'sya' in keterangan:
                    keterangan2 = keterangan.replace("sya", ctx.message.author.mention)
                if 'sy' in keterangan:
                    keterangan2 = keterangan.replace("sy", ctx.message.author.mention)
                """Close"""

                await ctx.send("si " + user.mention + f" {keterangan2}")                    
            else:
                print("psaja used3")                
                if 'yang' in keterangan:
                    await ctx.send("si " + user.mention + f" {keterangan}")
                else:
                    await ctx.send("si " + user.mention + f" yang {keterangan}")
    else:
        user = random.choice(ctx.guild.members)

                # Just do it over if it is a bot
        while (user.bot):
            user = random.choice(ctx.guild.members)
        Matches = ["gua", "aku", "gw", "saya", "sy", "sya"]
        print("yes2")
        if any (X in keterangan for X in Matches):
            print("yes3")
            """Matches Handler"""
            keterangan2 = None
            if 'gua' in keterangan:
                keterangan2 = keterangan.replace("gua", ctx.message.author.mention)
            if 'gw' in keterangan:
                keterangan2 = keterangan.replace("gw", ctx.message.author.mention)
            if 'aku' in keterangan:
                keterangan2 = keterangan.replace("aku", ctx.message.author.mention)
            if 'saya' in keterangan:
                keterangan2 = keterangan.replace("saya", ctx.message.author.mention)
            if 'sya' in keterangan:
                keterangan2 = keterangan.replace("sya", ctx.message.author.mention)
            if 'sy' in keterangan:
                keterangan2 = keterangan.replace("sy", ctx.message.author.mention)
            """Close"""

            await ctx.send("si " + user.mention + f" {keterangan2}")                    
        else:
            print("used3")                
            if 'yang' in keterangan:
                await ctx.send("si " + user.mention + f" {keterangan}")
            else:
                await ctx.send("si " + user.mention + f" yang {keterangan}")

@client.command(name='hide', pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.guild)
async def hide(ctx, *, keterangan):
    """Check If Psaja"""
    if ctx.guild.id == 864789922233057300:
        """Check Room Request"""
        if ctx.channel.id == 950603060823064616:
            member = ctx.message.author
            randomchoise = ["kamu di-hide", "kamu ter-hide", "kamu berhasil di-hide sesuai request", "udah", "udah coba cek"]
            if keterangan == "general":
                """General"""
                role = get(member.guild.roles, name="❀ General                        ⁣                            ⁣")
                await member.add_roles(role)
                await ctx.send(f"{random.choice(randomchoise)}")
            if keterangan == "roleroom":
                """Role Room"""
                role = get(member.guild.roles, name="❀ Role Room                          ⁣                            ⁣")
                await member.add_roles(role)
                await ctx.send(f"{random.choice(randomchoise)}")
            if keterangan == "bot":
                """BotRequest Role"""
                role = get(member.guild.roles, name="❀ Bot Request                            ⁣                            ⁣")
                await member.add_roles(role)
                await ctx.send(f"{random.choice(randomchoise)}")
            if keterangan == "meme":
                """Shitpost Role"""
                role = get(member.guild.roles, name="❀ Shitpost                            ⁣                            ⁣")
                await member.add_roles(role)
                await ctx.send(f"{random.choice(randomchoise)}")


@client.command(name='unhide', pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.guild)
async def unhide(ctx, *, keterangan):
    """Check If Psaja"""
    if ctx.guild.id == 864789922233057300:
        """Check Room Request"""
        if ctx.channel.id == 950603060823064616:
            member = ctx.message.author
            randomchoise = ["kamu di-unhide", "kamu ter-unhide", "kamu berhasil di-unhide sesuai request", "udah", "udah coba cek"]
            if keterangan == "general":
                """General"""
                role = get(member.guild.roles, name="❀ General                        ⁣                            ⁣")
                await member.remove_roles(role)
                await ctx.send(f"{random.choice(randomchoise)}")
            if keterangan == "roleroom":
                """Role Room"""
                role = get(member.guild.roles, name="❀ Role Room                          ⁣                            ⁣")
                await member.remove_roles(role)
                await ctx.send(f"{random.choice(randomchoise)}")
            if keterangan == "bot":
                """BotRequest Role"""
                role = get(member.guild.roles, name="❀ Bot Request                            ⁣                            ⁣")
                await member.remove_roles(role)
                await ctx.send(f"{random.choice(randomchoise)}")
            if keterangan == "meme":
                """Shitpost Role"""
                role = get(member.guild.roles, name="❀ Shitpost                            ⁣                            ⁣")
                await member.remove_roles(role)
                await ctx.send(f"{random.choice(randomchoise)}")

@client.command(name='saran', pass_context=True)
async def saran(ctx, *, keterangan):
    print("saran used")
    webhook = Webhook.from_url("WEBHOOK", adapter=RequestsWebhookAdapter()) # Initializing webhook
    embed = discord.Embed(title="Saran! ✨", description=f"👋 **{ctx.author.name}#{ctx.author.discriminator}**\n{keterangan}") # Initializing an Embed
    webhook.send(embed=embed) # Executing webhook and sending embed.
    await ctx.send("Pesan mu telah dikirim! *saranmu akan segera direalisasikan*")
    
@client.command()
@commands.cooldown(1, 10, commands.BucketType.guild)
async def poll(ctx, *, question):
    question2 = None
    Matches = ["gua", "aku", "gw", "saya", "sy", "sya"]
    if any (X in question for X in Matches):
        print("Matches true")

    """Matches Handler"""
    if 'gua' in question:
        question2 = question.replace("gua", ctx.message.author.mention)
    if 'gw' in question:
        question2 = question.replace("gw", ctx.message.author.mention)
    if 'aku' in question:
        question2 = question.replace("aku", ctx.message.author.mention)
    if 'saya' in question:
        question2 = question.replace("saya", ctx.message.author.mention)
    if 'sya' in question:
        question2 = question.replace("sya", ctx.message.author.mention)
    if 'sy' in question:
        question2 = question.replace("sy", ctx.message.author.mention)
        """Close"""
    message = await ctx.send(f"**POLL!**✅❎\n{question2}")        
    await message.add_reaction('❎')        
    await message.add_reaction('✅')      

@client.event
@commands.cooldown(1, 10, commands.BucketType.guild)
async def on_message(ctx):
    randomchoise = ["sok dingin kanjut", "dingin cuy dingin", "dingin amat", "berusaha menjadi dingin"]
    if(ctx.content  == "pagi"):
        await ctx.channel.send(configs["pagi"])
    if(ctx.content  == "sore"):
        await ctx.channel.send(configs["sore"])        
    if(ctx.content  == "malam"):
        await ctx.channel.send(configs["malam"])

    if(ctx.content in ["ok","sip","Ok","Sip","o","O","👍", "y", "Y", "k", "K"]):
        await ctx.channel.send(random.choice(randomchoise), reference=ctx)

    if(ctx.content == "sange sama kartun"):
        await ctx.channel.send("https://cdn.discordapp.com/attachments/880509666482860042/884722248303403008/video0-18.mp4", reference=ctx)
    await client.process_commands(ctx)        

@client.command(name='help')
@commands.cooldown(1, 10, commands.BucketType.guild)
async def help(ctx):
    clientCMDS = "**help** <- kamu sedang memakai commandnya sekarang\n\n**poll ``[kalimat]``**: Membuat polling[alias: quickvote, vote, voting, polling]\n\n**kapan ``[kalimat]``**: Menanyakan kapan akan terjadi(Tidak Serius)\n\n**apakah ``[kalimat]``**: Menanyakan apakah [kalimat] benar atau tidak(tidak serius)\n\n**siapa ``[kalimat]``**: Memberi nama+tags secara acak\n\n**saran ``[kalimat]``**: Saran atau tambahan harus jelas sehingga staff mengerti, jika tidak sesuai format/tidak jelas, maka admin berhak menghapus atau menolak saran/tambahan."
    PYVERS = "Python 10.5.10"
    UPTIME = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
    STAT = f"**Ping**: {round(client.latency, 1)}      **Uptime**: {UPTIME}\n**Python**: {PYVERS}      **BotID**: {client.user.id}"
    embed=discord.Embed(title="BabuPsaja | Help", url="https://github.com/Encham10/BabuPsajaHost/tree/main", description="BotPrefix: > | Woho#1010510", color=discord.Color.blue())
    embed.add_field(name="Bot Commands",value=f"{clientCMDS}",inline=True)
    embed.add_field(name="Random Commands",value="**pagi**: pagi kencroters\n**sore**: sore kencroters\n**malam**: malam kencroters\n\n**sange sama kartun**: mengirim video dedi kobuzer",inline=True)
    embed.add_field(name="Psaja Config",value="**hide/unhide** ``[general/roleroom/bot/meme]``: Memberi role khusus untuk hide/unhide room",inline=False)
    embed.add_field(name="Bot Info",value=f"{STAT}",inline=False)
    await ctx.send(embed=embed)

TOKEN = os.getenv("TOKEN")

client.run("TOKEN")


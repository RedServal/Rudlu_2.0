#id = 592275943406436373
#Token = NTkyMjc1OTQzNDA2NDM2Mzcz.XQ8--w.WGVrHo_4wdf0krYyyLm9TiKDtGI
#permission = 129088
#https://discordapp.com/oauth2/authorize?client_id=592275943406436373&scope=bot&permissions=8

import asyncio
import random
import os
from PIL import Image
import requests
import ffmpeg

import weeb
import modif_image

import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get


def compress_image(path) :
    img = Image.open(path)
    img= img.convert('RGB')

    #rot = random.random()*10

    img = img.resize((img.size[0]//15,img.size[1]//15))
    #img = img.rotate(rot, expand=True)
    img = img.resize((img.size[0]*15,img.size[1]*15))
    #img = img.rotate(360 + rot, expand=True)

    img.save(path, quality=1)


global victimisation, p, t, identifiant

victimisation = False
p = 0.5
identifiant = 246738655832571904
t = 1

client = commands.Bot(command_prefix=':', help_command=None)



@client.event
async def on_ready():
    print('Connexion en tant que {0.user}'.format(client))
    activity = discord.Activity(name=':help', type=discord.ActivityType.listening)
    await client.change_presence(activity=activity)

@client.event
async def on_message(message):
    print(f"{message.author}: {message.content}")


    if message.author == client.user:
        return

    if message.content.startswith(':noweeb'):
        await message.channel.send(weeb.choose_weeb())

    if message.content.startswith(':blaguevalide'):
        await message.channel.send('https://www.youtube.com/watch?v=eW4c3vTdU54')

    if message.content.startswith(':is ') and (message.content.endswith('gay?') or message.content.endswith('gay ?')):
        await message.channel.send('yes')

    if message.content.startswith(':yeet_tonin') :
        serv = client.get_guild(470974497781186560)
        afk_channel = client.get_channel(472857563873017856)
        victime = serv.get_member(246738655832571904)
        await victime.edit(voice_channel=afk_channel)

    if message.content.startswith(':yeet') and message.content.endswith('random') :
        serv = client.get_guild(470974497781186560)
        afk_channel = client.get_channel(472857563873017856)
        k=0
        while True :
            try :
                victime = random.choice(serv.members)
                print(victime)
                await victime.edit(voice_channel=afk_channel)
                break
            except :
                k+=1
                if k>20 :
                    await message.channel.send('Bruh moment')
                    break
                pass


    if message.content.startswith(':test') :
        serv = client.get_guild(470974497781186560)
        afk_channel = client.get_channel(472857563873017856)
        victime = serv.get_member(184622316792184832)
        print(victime)


    #On ne dit pas chocolatine mais pain au chocolat

    for i in message.content.split() :  #parcourt le message mot par mot
        mot=i.lower()
        old_mot=i.lower()
        if mot.endswith("ïnes") :
            mot=i.replace("ïnes","ine")
            old_mot=i.replace("ïnes","ïne")
        elif mot.endswith("ines") :
            mot=i.replace("ines","ine")
            old_mot=i.replace("ines","ine")
        elif mot.endswith("ïne") :
            mot=i.replace("ïne","ine")
            old_mot=i

        if mot.endswith("ine") :
            reponse="On ne dit pas " + old_mot + " mais pain au " + mot.replace("ine", "") + " !"
            await message.channel.send(reponse)

    if "juif" in message.content :
        await message.add_reaction("🔥")

    if message.content.startswith(':jpg') :
        success = False
        messages = await message.channel.history(limit=5).flatten() #recupere les 5 derniers messages du channel
        for msg in messages :   #les parcours

            if msg.attachments != [] or msg.content.endswith('.jpg') or msg.content.endswith('.png') or msg.content.endswith('.gif') or msg.content.endswith('.jpeg') :
                #enregistrement de l'image
                try :
                    url = msg.attachments[0].url
                except :
                    url = msg.content
                img_data = requests.get(url).content
                with open('img.jpg', 'wb') as handler:
                    handler.write(img_data)

                #modification de l'image

                compress_image('img.jpg')
                #envoi
                await msg.channel.send(file=discord.File('img.jpg'))
                #suppression
                os.remove('img.jpg')
                success = True
                break
            else :
                pass

        if success :
            success = False
            pass
        else :
            await message.add_reaction('❌')


#await message.channel.send('Bruh moment')

    if message.content.startswith(':victimisation') :       #victimisation True/False proba temps id_victime
        msg = message.content.split()
        if len(msg) == 1 :
            await message.channel.send('victimisation True/False proba temps id_victime')
        elif len(msg) == 5 :
            global victimisation, p, t, identifiant
            victimisation = bool(msg[1])
            p = int(msg[2])
            t = int(msg[3])
            identifiant = msg[4]
            await message.channel.send('victimisation de ' + str(identifiant) + ' toutes les ' + str(t) + ' secondes avec une proba de ' + str(p) + ' --> ' + str(victimisation))
        else :
            await message.channel.send('Mauvais paramètres. Format = :victimisation True/False proba temps id_victime')


    await client.process_commands(message)



async def background_loop() :
    await asyncio.sleep(5)
    while not client.is_closed() :
        serv = client.get_guild(470974497781186560)
        print(serv)
        afk_channel = client.get_channel(472857563873017856)
        print(afk_channel)
        victime = serv.get_member(identifiant)
        print(victime)
        print('victimisation de ' + str(identifiant) + ' toutes les ' + str(t) + ' secondes avec une proba de ' + str(p) + ' --> ' + str(victimisation))
        if random.random()>1-p :
            if victimisation==True :
                print('yeet')
                await victime.edit(voice_channel=afk_channel)
        await asyncio.sleep(t)




@client.command(pass_context=True)
async def yeet(ctx, member : discord.Member, *, reason=None):
    afk_channel = client.get_channel(472857563873017856)
    await member.edit(voice_channel=afk_channel)

@client.command(pass_context=True)
async def tg(ctx) :
    await ctx.message.channel.send('Fermes ta gueule', tts=True)

@client.command(pass_context=True)
async def groscerveau(ctx) :
    success = False
    messages = await ctx.message.channel.history(limit=5).flatten() #recupere les 5 derniers messages du channel
    for msg in messages :   #les parcours

        if msg.attachments != [] or msg.content.endswith('.jpg') or msg.content.endswith('.png') or msg.content.endswith('.gif') or msg.content.endswith('.jpeg') :
            #enregistrement de l'image
            try :
                url = msg.attachments[0].url
            except :
                url = msg.content
            try :
                force = int(ctx.message.content.split()[1])
            except :
                force = 1.6
            img_data = requests.get(url).content
            with open('img.png', 'wb') as handler:
                handler.write(img_data)
            coord = modif_image.detection('img.png')
            try :
                if coord == () :
                    await ctx.message.add_reaction('❌')
                    return
            except :
                pass
            modif_image.groscerveau('img.png',coord, force)
            await msg.channel.send(file=discord.File('img.png'))
            #suppression
            os.remove('img.png')
            success = True
            break
        else :
            pass
    if success :
        success = False
        pass
    else :
        await ctx.message.add_reaction('❌')

@client.command(pass_context=True)
async def swirl(ctx) :
    success = False
    messages = await ctx.message.channel.history(limit=5).flatten() #recupere les 5 derniers messages du channel
    for msg in messages :   #les parcours

        if msg.attachments != [] or msg.content.endswith('.jpg') or msg.content.endswith('.png') or msg.content.endswith('.gif') or msg.content.endswith('.jpeg') :
            #enregistrement de l'image
            try :
                url = msg.attachments[0].url
            except :
                url = msg.content
            img_data = requests.get(url).content
            with open('img.png', 'wb') as handler:
                handler.write(img_data)
            try :
                force = int(ctx.message.content.split()[1])
            except :
                force = 5
            modif_image.tourbillion('img.png', force)
            await msg.channel.send(file=discord.File('img.png'))
            #suppression
            os.remove('img.png')
            success = True
            break
        else :
            pass
    if success :
        success = False
        pass
    else :
        await ctx.message.add_reaction('❌')

@client.command(pass_context=True)
async def help(ctx) :
    await ctx.message.channel.send(open("help.txt", "r").read())

@client.command(pass_context=True)
async def indignite(ctx):
    chan = ctx.message.author.voice.channel
    vc = await chan.connect()
    vc.play(discord.FFmpegPCMAudio('indignite.mp3'), after=lambda e: print('done', e))
    await asyncio.sleep(5)
    await vc.disconnect()

@client.command(pass_context=True)
async def leave(ctx) :
    voicechannel = discord.utils.get(ctx.guild.channels, name='Général')
    server = ctx.message.guild
    await vc.disconnect()


"""
@client.command(pass_context=True)
async def rename(ctx, member : discord.Member,*, nickname):
    print("yoy")
    await member.change_nickname(member, nickname)
"""


#client.loop.create_task(background_loop())
client.run("NTkyMjc1OTQzNDA2NDM2Mzcz.XQ8--w.WGVrHo_4wdf0krYyyLm9TiKDtGI")

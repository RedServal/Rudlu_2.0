#id = XXXXXXXXXXXXXXX
#Token = XXXXXXXXXXXXXXX
#permission = 8
#https://discordapp.com/oauth2/authorize?client_id=XXXXXXXXXXXXXXX&scope=bot&permissions=8

import asyncio
import random
import os
from PIL import Image
import requests
import json

import modif_image
import yt_dl
import tweet
import scrapper

import discord
from discord.ext import commands
from discord.ext.commands import Bot, CommandNotFound
from discord.utils import get

global partie_en_cours, cplus_channel, cplus_nbr, pepe_count, weeb_count

partie_en_cours = False

pepe_count = random.randint(0, len(os.listdir("data/images/pepe")))
weeb_count = 0

bot_id = 0000000000

client = commands.Bot(command_prefix=('$'), help_command=None)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:77.0) Gecko/20100101 Firefox/77.0' }

@client.event
async def on_ready():
    print('Connexion en tant que {0.user}'.format(client))
    activity = discord.Activity(name='$help', type=discord.ActivityType.listening)
    await client.change_presence(activity=activity)

@client.event
async def on_message(message):
    print(f"{message.author.name} sur {message.guild} | {message.channel} : {message.content}")

    global cplus_channel, cplus_nbr, partie_en_cours

    if message.author == client.user:
        return

    #partie de cplus
    try :
        if partie_en_cours == True :
            if message.channel == cplus_channel :
                #process
                if int(message.content) == cplus_nbr :
                    partie_en_cours = False
                    await message.add_reaction('🥇')
                elif int(message.content) > cplus_nbr :
                    await message.add_reaction('➖')
                else :
                    await message.add_reaction('➕')
    except :
        pass

    if message.content.startswith('pierre') :
        await message.channel.send("feuille")
        await message.channel.send("J'ai gagné !")
    if message.content.startswith('feuille') :
        await message.channel.send("ciseaux")
        await message.channel.send("J'ai gagné !")
    if message.content.startswith('ciseaux') :
        await message.channel.send("pierre")
        await message.channel.send("J'ai gagné !")

    if message.content.lower().startswith("merci") :
        await message.channel.send("de rien frère")

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

    await client.process_commands(message)

#Commandes

@client.command(pass_context=True, name='is')
async def is_gay(ctx) :
    if (ctx.message.content.endswith('gay?') or ctx.message.content.endswith('gay ?')):
        master = ['RUDLU', 'YOURMASTER', 'NICOLAS']
        if ctx.message.content.replace(' ','').replace('gay?', '').replace('$is', '').upper() in master :
            await ctx.message.channel.send('no')
        else :
            if random.random() > 0.8 :
                await ctx.message.channel.send('yes')
            else :
                await ctx.message.channel.send("oh boy i can't tell you how much")

"""
@client.command(pass_context=True)
async def yeet(ctx, member : discord.Member, *, reason=None):
    afk_channel = client.get_channel(472857563873017856)
    await member.edit(voice_channel=afk_channel)
"""

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
    else :
        await ctx.message.add_reaction('❌')

@client.command(pass_context=True)
async def jpg(ctx) :
    success = False
    messages = await ctx.message.channel.history(limit=5).flatten() #recupere les 5 derniers messages du channel
    for msg in messages :   #les parcours

        if msg.attachments != [] or msg.content.endswith('.jpg') or msg.content.endswith('.png') or msg.content.endswith('.gif') or msg.content.endswith('.jpeg') :
            #enregistrement de l'image
            async with ctx.channel.typing() :
                await msg.add_reaction('✅')
                try :
                    url = msg.attachments[0].url
                except :
                    url = msg.content
                img_data = requests.get(url).content
                with open('img.jpg', 'wb') as handler:
                    handler.write(img_data)

                #modification de l'image
                modif_image.compress_image('img.jpg')
                #envoi
                await msg.channel.send(file=discord.File('img.jpg'))
            serv = ctx.channel.guild
            await msg.remove_reaction('✅', serv.get_member(bot_id))
            #suppression
            os.remove('img.jpg')
            success = True
            break
        else :
            pass

    if success :
        success = False
    else :
        await ctx.message.add_reaction('❌')

@client.command(pass_context=True, aliases=["s","siwrl","swilr"])
async def swirl(ctx) :
    success = False
    messages = await ctx.message.channel.history(limit=5).flatten() #recupere les 5 derniers messages du channel
    for msg in messages :   #les parcours

        if msg.content.startswith("https://tenor.com/") :
            msg.content += ".gif"

        if msg.attachments != [] or msg.content.endswith('.jpg') or msg.content.endswith('.png') or msg.content.endswith('.gif') or msg.content.endswith('.jpeg') :
            #enregistrement de l'image
            try :
                url = msg.attachments[0].url
            except :
                url = msg.content
            if url.endswith(".gif") :
                async with ctx.channel.typing() :
                    await msg.add_reaction('🔄')
                    img_data = requests.get(url).content
                    with open('anim.gif', 'wb') as handler:
                        handler.write(img_data)
                    try :
                        force = ctx.message.content.split()[1]
                    except :
                        force = "2"
                    nbFrames = modif_image.tourbillion('anim.gif', force)
                    await msg.channel.send(file=discord.File('anim.gif'))
                    serv = ctx.channel.guild
                    await msg.remove_reaction('🔄', serv.get_member(bot_id))
                #suppression
                os.remove('anim.gif')
                for frame in range(0, nbFrames) :
                    try :
                        os.remove(str(frame)+".gif")
                    except :
                        print("failed to delete")
                success = True
                break
            else :
                async with ctx.channel.typing() :
                    await msg.add_reaction('🔄')
                    img_data = requests.get(url).content
                    with open('img.png', 'wb') as handler:
                        handler.write(img_data)
                    try :
                        force = int(ctx.message.content.split()[1])
                    except :
                        force = 2
                    modif_image.tourbillion('img.png', force)
                    await msg.channel.send(file=discord.File('img.png'))
                serv = ctx.channel.guild
                await msg.remove_reaction('🔄', serv.get_member(bot_id))
                #suppression
                os.remove('img.png')
                success = True
                break
        else :
            pass
    if success :
        success = False
    else :
        await ctx.message.add_reaction('❌')


@client.command(pass_context=True, aliases=["h", "aide"])
async def help(ctx) :
    await ctx.send(open("data/help.txt", "r",encoding='utf-8').read())

@client.command(pass_context=True)
async def blague(ctx) :
   await ctx.send(random.choice(open("data/blagues.txt", "r",encoding='utf-8').read().split('\n\n')))

@client.command(pass_context=True)
async def heenok(ctx) :
    await ctx.send(random.choice(list(open('data/heenok.txt','r',encoding='utf-8'))))
    await ctx.message.delete()

@client.command(pass_context=True)
async def noweeb(ctx) :
    global weeb_count
    await ctx.send(file=discord.File('data/images/weeb/' + os.listdir("data/images/weeb")[weeb_count]))
    if weeb_count >= len(os.listdir("data/images/weeb"))-1 :
        weeb_count = 0
    else :
        weeb_count += 1
    await ctx.message.delete()


@client.command(pass_context=True)
async def pepe(ctx) :
    global pepe_count
    await ctx.send(file=discord.File('data/images/pepe/' + os.listdir("data/images/pepe")[pepe_count]))
    if pepe_count >= len(os.listdir("data/images/pepe"))-1 :
        pepe_count = 0
    else :
        pepe_count += 1
    await ctx.message.delete()

@client.command(pass_context=True)
async def blaguevalide(ctx) :
    await ctx.send(file=discord.File('data/images/autre/blague.gif'))

@client.command(pass_context=True)
async def morse(ctx) :
    ctx.message.content.replace(ctx.prefix + ctx.invoked_with + ' ', "")
    msg=""
    msg_util=ctx.message.content.upper()
    with open('data/morse.json') as json_file:
        morse = json.load(json_file)
    for i in msg_util :
        if i not in morse :
            msg+=" "
        else :
            msg+=morse[i]
            msg+=" "
    await ctx.message.channel.send(msg)

@client.command(pass_context=True)
async def glitch(ctx) :
    success = False
    messages = await ctx.message.channel.history(limit=5).flatten() #recupere les 5 derniers messages du channel
    for msg in messages :   #les parcours

        if msg.attachments != [] or msg.content.endswith('.jpg') or msg.content.endswith('.png') or msg.content.endswith('.gif') or msg.content.endswith('.jpeg') :
            #enregistrement de l'image
            try :
                url = msg.attachments[0].url
            except :
                url = msg.content
            async with ctx.channel.typing():
                await msg.add_reaction('✅')
                img_data = requests.get(url).content
                with open('img.png', 'wb') as handler:
                    handler.write(img_data)
                try :
                    force = int(ctx.message.content.split()[1])
                except :
                    force = 2
                modif_image.glitch('img.png', force)
                await msg.channel.send(file=discord.File('glitched.gif'))
            serv = ctx.channel.guild
            await msg.remove_reaction('✅', serv.get_member(bot_id))
            #suppression
            os.remove('img.png')
            os.remove('glitched.gif')
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
async def nightcore(ctx) :
    await ctx.message.add_reaction('⏩')
    msg = ctx.message.content.split(' ')
    path = msg[1]
    try :
        spood = float(msg[2])
    except :
        spood = 2.0
    yt_dl.nightcore(path, spood)
    size = os.path.getsize('audio_' + str(spood) + '.mp3')
    if size > 8e+6 :
        await ctx.send("Fichier trop gros ! Il fait %.2f Mo le bougre ! Merci de couper l'audio pour qu'il soit plus court ou gueuler sur Rudlu pour qu'il règle ça" % (size/1048576))
    else :
        await ctx.send(file=discord.File('audio_' + str(spood) + '.mp3'))
    serv = ctx.channel.guild
    await ctx.message.remove_reaction('⏩', serv.get_member(bot_id))
    os.remove('audio_' + str(spood) + '.mp3')
    os.remove('audio.webm')

@client.command(pass_context=True)
async def rank(ctx) :
    text = "Vous pouvez vous attribuez des roles avec la commande :rank NOM DU ROLE (sen fair 2 fote et avec les bonnes majuscules). Liste des rôles attribuables : \n \n"
    role_non_dispo = ["Commandant","Député","Officier","Sergent","Membre","everyone","Groovy","Robot","Rudlu 2.0"]
    member = ctx.message.author
    role_user = ctx.message.content.replace(ctx.prefix + ctx.invoked_with + ' ', "")
    print(role_user)

    if ctx.message.content == ctx.prefix + ctx.invoked_with + ' ' :
        for i in range(len(member.guild.roles)) :
            if member.guild.roles[i].name.replace("@","") not in role_non_dispo :
                text += member.guild.roles[i].name.replace("@","") + " | "
        await ctx.send(text)
    elif role_user in role_non_dispo :
        await ctx.message.add_reaction('❌')
        print("pas dispo")
    else :
        role = discord.utils.get(member.guild.roles, name=role_user)
        print(role)
        if role == None :
            await ctx.message.add_reaction('❌')
            print("invalide")
        else :
            if role in member.roles :
                await member.remove_roles(role)
                await ctx.message.add_reaction('✅')
                await ctx.send('Rôle retiré !')
            else :
                await member.add_roles(role)
                await ctx.message.add_reaction('✅')
                await ctx.send('Rôle ajouté !')

@client.command(pass_context=True)
async def blob(ctx) :
    success = False
    messages = await ctx.message.channel.history(limit=5).flatten() #recupere les 5 derniers messages du channel
    for msg in messages :   #les parcours

        if msg.attachments != [] or msg.content.endswith('.jpg') or msg.content.endswith('.png') or msg.content.endswith('.gif') or msg.content.endswith('.jpeg') :
            #enregistrement de l'image
            try :
                url = msg.attachments[0].url
            except :
                url = msg.content
            await msg.add_reaction('✅')
            img_data = requests.get(url).content
            with open('img.png', 'wb') as handler:
                handler.write(img_data)
            modif_image.blob('img.png')
            await msg.channel.send(file=discord.File('img.png'))
            serv = ctx.channel.guild
            await msg.remove_reaction('✅', serv.get_member(bot_id))
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
async def trump(ctx) :
    id = tweet.trump()
    await ctx.send('https://twitter.com/generikb/status/' + str(id))

@client.command(pass_context=True)
async def cplus(ctx) :
    global partie_en_cours, cplus_channel, cplus_nbr
    if ctx.message.content.replace(ctx.prefix + ctx.invoked_with + ' ', "").lower() == "stop" :
        partie_en_cours = False
        await ctx.send('fin de partie')
    elif partie_en_cours == True :
        await ctx.message.add_reaction('❌')
    elif ctx.message.content.replace(ctx.prefix + ctx.invoked_with, "").replace(' ', '') == "" :
        await ctx.send("Jeu du c'est plus c'est moins. Une partie se lance avec la commande $cplus x:y avec x et y les nombres minimum et maximum.")
    else :
        #try :
        cplus_min, cplus_max = ctx.message.content.replace(ctx.prefix + ctx.invoked_with + ' ', "").split(':')[0], ctx.message.content.replace(ctx.prefix + ctx.invoked_with + ' ', "").split(':')[1]
        print(cplus_min,cplus_max)
        cplus_channel = ctx.channel
        cplus_nbr = random.randint(int(cplus_min), int(cplus_max))
        partie_en_cours = True
        await ctx.send("Partie commencée !")
        print(cplus_channel, ctx.channel, cplus_nbr, partie_en_cours)
        #except :
            #await ctx.message.add_reaction('❌')

@client.command(pass_context=True, name='def')
async def definition(ctx) :
    try :
        if ctx.message.content.replace(ctx.prefix + ctx.invoked_with, '').replace(" ", "") == "" :
            await ctx.send(embed = scrapper.urban())
        else :
            mot = ctx.message.content.replace(ctx.prefix + ctx.invoked_with + ' ', "").replace(' ', '%20')
            await ctx.send(embed = scrapper.urban(mot))
    except :
        await ctx.message.add_reaction('❌')

@client.command(pass_context=True)
async def qqn(ctx) :
    img_data = requests.get("https://www.thispersondoesnotexist.com/image.jpg", headers = headers).content
    with open('img.jpg', 'wb') as handler:
        handler.write(img_data)
    await ctx.send(file=discord.File('img.jpg'))
    os.remove('img.jpg')

@client.command(pass_context=True)
async def cat(ctx) :
    img_data = requests.get("https://thiscatdoesnotexist.com/", headers = headers).content
    with open('img.jpg', 'wb') as handler:
        handler.write(img_data)
    await ctx.send(file=discord.File('img.jpg'))
    os.remove('img.jpg')

@client.command(pass_context=True)
async def horse(ctx) :
    img_data = requests.get("https://thishorsedoesnotexist.com/", headers = headers).content
    with open('img.jpg', 'wb') as handler:
        handler.write(img_data)
    await ctx.send(file=discord.File('img.jpg'))
    os.remove('img.jpg')

@client.command(pass_context=True)
async def stock(ctx) :
    async with ctx.channel.typing() :
        recherche = 'stock image ' + ctx.message.content.replace(ctx.prefix + ctx.invoked_with + ' ', "")
        link = scrapper.stock(recherche)
        if link != None :
            img_data = requests.get(link).content
            with open('img.png', 'wb') as handler:
                handler.write(img_data)
            await ctx.send(file=discord.File('img.png'))
            os.remove('img.png')
        else :
            await ctx.send("Hm, <@184622316792184832> ca se passe mal ici, probablement à cause de l'API qui limite à 100 le nombre de requêtes par jour. Réessayez et si ca ne marche toujours pas... niquez vous.")

#quand commande inconnue
@client.event
async def on_command_error(ctx, error) :
    if isinstance(error, CommandNotFound) :
        await ctx.message.add_reaction('❓')
    else :
        raise error

"""
#a toutes commande
@client.event
async def on_command(ctx) :
    pass

@client.command(pass_context=True)
async def audio(ctx):
    chan = ctx.message.author.voice.channel
    vc = await chan.connect()
    vc.play(discord.FFmpegPCMAudio('audio.mp3'), after=lambda e: print('done', e))
    await asyncio.sleep(5)
    await vc.disconnect()


@client.command(pass_context=True)
async def leave(ctx) :
    voicechannel = discord.utils.get(ctx.guild.channels, name='Général')
    server = ctx.message.guild
    await vc.disconnect()
"""

#client.loop.create_task(background_loop())
client.run("XXXXXXXXXXXXXXXXXXXXXXX")

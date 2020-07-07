import requests
from bs4 import BeautifulSoup
import json
import random
import discord

#Google CSE
API_key = "AIzaSyD5I9DDwiIFIL2aNMzovsYeie7yce9JGE8"
cx = "002143315822336798488:wiqqznfe5po"

def stock(mot) :
    r = requests.get("https://www.googleapis.com/customsearch/v1?key=" + API_key + "&cx=" + cx + "&q=" + mot + "&searchType=image&imgSize=xlarge&num=10&start=1")
    if r.status_code == 200:
        return(r.json()['items'][random.randint(0,9)]['link'])
    else :
        return None

def urban(mot='') :
    if mot == '' :
        page = random.randint(2,1000)
        url = 'https://www.urbandictionary.com/random.php?page=' + str(page)

    else :
        url = 'https://www.urbandictionary.com/define.php?term=' + mot

    data = requests.get(url)

    soup = BeautifulSoup(data.text, 'html.parser')

    def_embed = discord.Embed(
            description = soup.find('div', {'class': 'def-panel'}).find('div', {'class': 'meaning'}).text,
            colour = discord.Colour.red(),
            title = soup.find('div', {'class': 'def-panel'}).find('div', {'class': 'def-header'}).find('a', {'class': 'word'}).text,
            url = url
        )

    def_embed.add_field(name = 'Example', value = soup.find('div', {'class': 'def-panel'}).find('div', {'class': 'example'}).text)

    return(def_embed)
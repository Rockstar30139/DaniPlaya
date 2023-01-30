#Script by NΘISS
#https://github.com/Noisec/DaniPlaya

#----------imports----------
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

from os import system, name
import discord
import youtube_dl
from pytube import YouTube
import random
import requests
import json
import base64
import time
from bs4 import BeautifulSoup
import asyncio
import os
from youtubesearchpython.__future__ import VideosSearch
import os.path
from os import path
from urllib.parse import urlparse
colorama_init()
#----------variables----------

key=""
queue=[]
song=""
semmi=""
song_publisher=""
current_requester = ""
client = discord.Client(intents=discord.Intents.all())

#get-random-songs
page_url = "https://beats-rhymes-lists.com/lists/50-greatest-rappers-of-all-time/"
page_response = requests.get(page_url)
page_html = page_response.text
soup = BeautifulSoup(page_html, "html.parser")
song_elements = soup.select("strong:contains('Best song:')")
song_names = []
for element in song_elements:
  song_name = element.text.replace("Best song: “", "").replace("”", "").strip()
  song_names.append(song_name)
page_url = "https://beats-rhymes-lists.com/lists/top-50-best-west-coast-rappers-of-all-time/"
page_response = requests.get(page_url)
page_html = page_response.text
soup = BeautifulSoup(page_html, "html.parser")
song_elements = soup.select("p em")
for element in song_elements:
  song_name = element.text.strip()
  song_names.append(song_name)
s = os.get_terminal_size()

def logo():
        print(f"""{Fore.GREEN}{Style.BRIGHT} _____              _ _____  _                   """.center(int(s.columns)," "))
        print(f"""{Fore.GREEN}{Style.BRIGHT}|  __ \            (_)  __ \| |                  """.center(int(s.columns)," "))
        print(f"""{Fore.GREEN}{Style.BRIGHT}| |  | | __ _ _ __  _| |__) | | __ _ _   _  __ _ """.center(int(s.columns)," "))
        print(f"""{Fore.GREEN}{Style.BRIGHT}| |  | |/ _` | '_ \| |  ___/| |/ _` | | | |/ _` |""".center(int(s.columns)," "))
        print(f"""{Fore.GREEN}{Style.BRIGHT}| |__| | (_| | | | | | |    | | (_| | |_| | (_| |""".center(int(s.columns)," "))
        print(f"""{Fore.GREEN}{Style.BRIGHT}|_____/ \__,_|_| |_|_|_|    |_|\__,_|\__, |\__,_|""".center(int(s.columns)," "))
        print(f"""{Fore.GREEN}{Style.BRIGHT}             _____       _     _ _    __/ |      """.center(int(s.columns)," "))
        print(f"""{Fore.GREEN}{Style.BRIGHT}            |  __ \     | |   | (_)  |___/       """.center(int(s.columns)," "))
        print(f"""{Fore.GREEN}{Style.BRIGHT}      ______| |__) |   _| |__ | |_  ___          """.center(int(s.columns)," "))
        print(f"""{Fore.GREEN}{Style.BRIGHT}     |______|  ___/ | | | '_ \| | |/ __|         """.center(int(s.columns)," "))
        print(f"""{Fore.GREEN}{Style.BRIGHT}            | |   | |_| | |_) | | | (__ X        """.center(int(s.columns)," "))
        print(f"""{Fore.GREEN}{Style.BRIGHT}            |_|    \__,_|_.__/|_|_|\___|         """.center(int(s.columns)," "))
        print(f"""{Fore.GREEN}{Style.BRIGHT}""")
        print(f"""{Fore.GREEN}{Style.BRIGHT}{Style.RESET_ALL}""")

 
# define our clear function
def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

clear()
clear()
clear()
clear()
logo()
print()

print(("-"*60).center(int(s.columns)," "))
print(f"{Style.BRIGHT}"+"Script by NΘISS#6149 | https://github.com/Noisec/DaniPlaya".center(s.columns," ")+f"{Style.RESET_ALL}",end="")
print(("-"*60).center(int(s.columns)," "))
print()
print(f"{Fore.YELLOW}Me, as the creator of this script I don't take any responsibility for anything you do with this script. This is for education purposes only. (Discord music bots are not align with the YouTube Terms of Service and/or the YouTube API Terms of Service){Style.RESET_ALL}")
print()
if input(f'Type {Style.BRIGHT}"accept"{Style.RESET_ALL}, to accept it:') != "accept":
    raise SystemExit

clear()

logo()

from os.path import exists

if exists("dani.conf")==True:
    
    f1=open("dani.conf","r")
    key=f1.read()
else:
    
    key=input("Enter BOT token:")
    clear()
    logo()
    for i in range(9):
        key = base64.b64encode(key.encode()).decode() #very basic token protection

    f1=open("dani.conf","w")
    print(key,file=f1)
    f1.close()
print("Songs Loaded:",len(song_names))
@client.event
async def on_ready():

    try:
            voice_client = client.voice_clients[0]
    except:semmi=1
    
    print('{|} Logged in')
    #print(client.user.name)
    #print(client.user.id)
    #bot_user = client.user 
    activity_text = "d {youtube url or song title}"
    activity_text = discord.utils.escape_markdown(activity_text)
    activity_text = "\n" + activity_text + "\n"
    await client.change_presence(activity=discord.Activity(name=activity_text, type=discord.ActivityType.playing))
    print("{|}  Servers:")

    for guild in client.guilds:
        # get the first text channel in the server
        channel = guild.text_channels[0]
        # create a new invite for the channel that expires after 30 seconds and can only be used once
        invite = await channel.create_invite(max_age=30, max_uses=1)
        # print the server name, ID, and invite link
        print(f"  - {guild.name} ({guild.id}): {invite.url} | Member count: {guild.member_count}")   

@client.event
async def on_message(message):
    
     server = message.guild
     user_voice_channel = message.author.voice.channel
     bitratex = server.bitrate_limit

     # Increase the bitrate of the voice channel
     await user_voice_channel.edit(bitrate=bitratex)
    
    
     global current_requester
     # Set the current requester to the name of the user who sent the message
     current_requester = message.author.name

    
     try:
            voice_client = client.voice_clients[0]
            # try to deafen the bot
            try:
                voice_client.deaf = True
            except Exception as e:
                print(f"Error deafening the bot: {e}")
     except:semmi=1
    


     # Log the message to the console
     print(f"> {message.author}: {message.content}")
     # ignore messages from the bot itself
     if message.author == client.user:
        return
    
     # check if the message starts with "dani"
     if message.content.startswith("d"):
        
        current_requester = str(message.author)
        # split the message into words
        words = message.content.split()
        # check if an URL was provided
        if len(words) > 1:
            query= " ".join(words[1:])  
            parsed_url = urlparse(query)
            if parsed_url.scheme:
                # If the query is a URL, print it
                #print(query)
                semmi=1
            else:
                if query == "random":
                    random_song_name = random.choice(song_names)
                    print("> Random song:",random_song_name)
                    query=random_song_name

                videosResult = await vids(query)
                # Print the results
                urls = [video['link'] for video in videosResult['result'][:1]]
                #print(urls[0])

                urls = [video['link'] for video in videosResult['result'][:1]]
                video_title = videosResult['result'][0]['title']
                # Get the channel where the message was originally sent
                channel = message.channel
                # Send a message with the video's title and url
                #await channel.send(f"Video title: {video_title}\nVideo url: {urls[0]}")
                
                #if not client.voice_clients:
                    #await play_next(urls[0])
                words[1]=str(urls[0])
                print("{|} Song requested:",words[1])
                
            ytvids = words[1:]
            
            
            
            # add the URLs to the queue
            for ytvid in ytvids:
                queue.append(ytvid)
            # check if the bot is not already playing an audio file
            if not client.voice_clients or not client.voice_clients[0].is_playing():
                # play the next audio file in the queue
                #print(message)
                await play_next(message)

     # check if the message is "skip"
     elif message.content == "skip":
        # check if the bot is connected to a voice channel
        if client.voice_clients:
            # get the voice client object
            vc = client.voice_clients[0]
            # check if the bot is in the same voice channel as the user
            if vc.channel.id == message.author.voice.channel.id:
                # stop playing the audio file
                vc.stop()
                # play the next audio file in the queue
                await play_next(message)


@client.event
async def on_voice_state_update(member, before, after):
    

    
    if client.voice_clients:
        # get the voice client object
        voice_client = client.voice_clients[0]
        # try to deafen the bot
        try:
            voice_client.deaf = True
        except Exception as e:
            print(f"Error deafening the bot: {e}")
    else:
        try:
            voice_client = client.voice_clients[0]
            # try to deafen the bot
            try:
                voice_client.deaf = True
            except Exception as e:
                print(f"Error deafening the bot: {e}")
        except:semmi=1
    
    
    
    
    print(".")
    if member.name == current_requester and after.channel is not None and before.channel != after.channel:
        
        # get the voice channel the user joined
        channel = after.channel
        # get the server that the voice channel belongs to
        server = channel.guild
        # check if the bot is a member of the server
        if server in client.guilds:
        # check if the bot is already in the voice channel
            if not client.voice_clients:
            # connect the bot to the voice channel
                await channel.connect()
            else:
                voice_client = client.voice_clients[0]
                # check if the bot is in the same voice channel as the user
                if voice_client.channel.id != channel.id:
                # disconnect from the current voice channel
                    await voice_client.disconnect()
                # connect to the new voice channel
                    await channel.connect()
                    


    if before.channel is not None and after.channel is None:
        # get the voice channel the member left
        channel = before.channel
        # check if the bot is the only member left in the voice channel
        if len(channel.members) == 1 and client.user in channel.members:
            # get the voice client object
            voice_client = client.voice_clients[0]
            # disconnect from the voice channel
            await voice_client.disconnect()
            
    
    
    # check if the user has joined a voice channel
    if before.channel is None and after.channel is not None:
        # get the voice channel the user joined
        channel = after.channel
        # get the server that the voice channel belongs to
        server = channel.guild
        # check if the bot is a member of the server
        if server in client.guilds:
            # check if the bot is already in the voice channel
            if not client.voice_clients or client.voice_clients[0].channel.id != channel.id:
                # join the voice channel
                await channel.connect()
    # check if the user has left a voice channel or moved to a different voice channel
    elif before.channel is not None and after.channel is not None:
        # check if the user has moved to a different voice channel
        if before.channel != after.channel:
            # get the voice channel the user left
            channel = before.channel
            # check if the voice channel is empty
            # get the voice client for the voice channel
                #voice_client = client.voice_clients[0]
            # disconnect the bot from the voice channel
                #await voice_client.disconnect()
    # check if the user's voice state has not changed
    elif before.channel == after.channel:
        # check if the voice channel is empty
        semmi=1



@client.event
async def on_reaction_add(reaction, user):
    # Check if the reaction is the "next track" emoji
    if reaction.emoji == "⏭️":
        # Check if the user is not the bot
        if not user.bot:
            semmi=1
            
        # Skip the song
        
        
        
        
        # Get the voice client and stop the audio
        voice_client = client.voice_clients[0]
        voice_client.stop()
        # Clear the queue
        queue.clear()
        os.remove("base.mp3")
        # Check if there are any songs in the queue
        while len(queue) > 0:
            # Get the first song in the queue
            song = queue[0]
            # Play the song
            await play_song(song)
            # Remove the song from the queue
            queue.pop(0)
    else:semmi=1


async def vids(xxquery):
    videosSearch = VideosSearch(xxquery, limit = 2)
    videosResult = await videosSearch.next()
    return videosResult

async def play_next(message): 

    # check if the queue is empty
    if not queue:
        return
    # get the next URL from the queue
    ytvid = queue.pop(0)
    # download the video to the local folder
    yt = YouTube(ytvid)
    
    
    '''
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path='.')'''
    
    video = max(yt.streams.filter(only_audio=True), key=lambda s: s.bitrate)

    # Download the audio
    out_file = video.download(output_path='.')
    
    # delete the "base.mp3" file if it already exists
    if os.path.exists("base.mp3"):
        os.remove("base.mp3")
    # rename the file to "base.mp3"
    song=out_file
    os.rename(out_file, "base.mp3")
    # result of success
    print(yt.title + " downloaded as base.mp3")
    # play the audio file in the voice channel
    voice_channel = message.author.voice.channel
    
    if voice_channel:
        
        # check if the bot is already connected to a voice channel
        if client.voice_clients:
            # get the voice client object
            vc = client.voice_clients[0]
            # check if the bot is already connected to the same voice channel
            if vc.channel.id != voice_channel.id:
                # disconnect from the old voice channel
                await vc.disconnect()
                # connect to the new voice channel
                voice_client = await voice_channel.connect()
            else:
                # reuse the existing voice client object
                voice_client = vc
        else:
            # connect to the voice channel
            voice_client = await voice_channel.connect()
        # play the audio file
        source = discord.FFmpegPCMAudio("base.mp3", executable='ffmpeg.exe')
        vc = client.voice_clients[0]
        server = message.guild
        channel = message.channel
        
        #making the song title readable
        song_title = os.path.basename(song)
        song_title = song_title.replace("mp4"," ")
        song_title = song_title.replace("webm"," ")
        song_title = song_title.replace("flv"," ")
        song_title = song_title.replace("mp3"," ")
        song_title = song_title.replace("_"," ")
        
        song_title, file_extension = os.path.splitext(song_title)
        message = await message.channel.send(f"**{current_requester}** 🎸 {song_title}")   
        print(f"> {server}/{channel}: {song_title} ({current_requester})")  
        await message.add_reaction("⏭️")
        vc.play(source)#playing the song
        
    else:
        print("! The user not in a voice channel !")



#run bot client
def bx(string):
    keyd = base64.b64decode(string)
    return keyd.decode('utf-8')

keyd=key
for i in range(9):
    keyd = bx(keyd)

client.run(keyd)

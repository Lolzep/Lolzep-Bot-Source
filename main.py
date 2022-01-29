import os #used to write/read files
import csv #used to make copy data file
import time #used to know how long a commmand takes (zp!copy)
import discord
import asyncio #used for sleeping the bot (waittimers)
import re #used for stupid im thing
import string #fixes stupid im thing for capitalizing the phrase
import youtube_dl #for playing youtube videos in voice chat
import shutil #moves data file to "Copy Data" folder

from random import randint #used for roll, used for im probability
from datetime import datetime
from discord.ext import commands
from keepalive import keep_alive #used to keep bot alive on server
from itertools import groupby #used to make rows/columns on copy data file

if os.path.exists("file.csv"):
  os.remove("file.csv") #if no command is ran, the file.csv stays, this deletes it
if os.path.exists("messages.txt"):
  os.remove("messages.txt") #if no command is ran, the msg.txt stays, this deletes it
if os.path.exists("boosters.txt"):
  os.remove("boosters.txt")
if os.path.exists("members.csv"):
  os.remove("members.csv")
os.mknod("file.csv") #makes new file.csv

intents = discord.Intents.default() #intents to allow reading member list (boost cmd)
intents.members = True
intents.emojis = True
intents.reactions = True

bot = commands.Bot(command_prefix='zp!',intents=intents) #using a bot
bot.remove_command('help') #make my own help command
TOKEN = os.getenv('TOKEN') #environment variables

#ideas
#replys smug emotes back at sent smug emotes
#talks like josh in emote spam
#assforce ranking (holy fuck this would be hard)
#recognize that two messages are identical and repeat messages (kinda working? tobefixedlater)
#(can't get range on list to work and also bot-commands)
#responds to the reginald image
#ah i see you're a man of culture.jpg if you say a list of keywords like thicc and etc
#post reginald image every two weeks
#"My idea is to have a command to send photos for verification of SDVX/IIDX skill levels, so they send an image with like zp!verify and it copies the photo/message to somewhere like here so we can sort them out"

#fixes

#START OF EVENTS (don't need a command to trigger)

@bot.event
async def on_ready():
    print("Bot is ready!")
    activity = discord.Game(name="zp!help || bork", type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)

@bot.event  
async def on_message(message): #returns different messages based on what is sent by users
  if message.author == bot.user or str(message.channel.id) == "749844960194330714" or str(message.channel.id) == "751618333912072219": #ignores itself, bot-commands, and announcements
    return

  dumb = str(message.content).strip().lower() #message with punctuation
  dumb_letters = re.sub(r'([^\s\w]|_)+', '', dumb) #message with no punctuation
  if "https" in dumb_letters: #ignore links
    return
  if dumb[0:3] == "zp!": #ignores zp! commands
    await bot.process_commands(message)

  dumb_phrases = {"number 15": "burger king foot lettuce", "drop kick": "React Roles", "if god had wanted me to live":"he would not have created me", "this is so sad":"https://www.youtube.com/watch?v=kJQP7kiw5Fk", "yandev":"I may be coded with many if-else statements, but it's not by someone with over a decade of coding experience.", "if else":"I may be coded with many if-else statements, but it's not by someone with over a decade of coding experience.", "furry":"It's art owo", "single core":"Wait... I'm only using a single core?", "prozep":"take prozep if you are experiencing prolonged heart pains\nside effects may include these sick fucking scores", "amogus":"ඞ", "ඞ":"amogus", "apple":"apple bottom jeans", "fuck off":"Who's Off?", "mayo":"mayo is bad", "bad bot":"sorry... :c"} #for simple text replies

  dumb_images = {"god i wish that was me":"wishthatwereme.jpg", "god i wish that were me":"wishthatwereme.jpg","salt":"salt.jpg","motivation":"motivation.png","wack":"wack.jpg","good bot":"happiness.jpg"} #for simple image replies

  for key in dumb_phrases: #sends simple text replies
    if key in dumb_letters:
      await message.channel.send(dumb_phrases.get(key))
      return
  
  for key in dumb_images: #sends simple image replies
    if dumb_letters == key:
      await message.channel.send(file=discord.File("Images/" + dumb_images.get(key)))
      return

  #more complicated replies

  #ping people if a certain string is sent in a channel

  michael = message.guild.get_member(195748601639600128)
  if "love live" in dumb_letters:
    await message.channel.send(f"{michael.mention}")

  miku = message.guild.get_member(693294060143640586)
  if "miku" in dumb_letters:
    await message.channel.send(f"{miku.mention}")

  lolzep = "126068015094693888"
  if lolzep == dumb_letters:
    await message.delete()
    await message.channel.send(message.author.mention + " fuck u")


  #the im message, the best thing ive ever made (1 in [probability] chance)

  probability = randint(1,5)

  if "im " == dumb_letters[0:3] and probability == 3:
    await message.channel.send("Hi \"" + string.capwords(dumb[3:]) + "\", I'm Lolzep Bot!")
  if "i am " == dumb_letters[0:5] and probability == 3:
    await message.channel.send("Hi \"" + string.capwords(dumb[5:]) + "\", I'm Lolzep Bot!")

  #the bork message, for every sent "bork", link a random video from "Best of Gabe" playlist.
  if dumb_letters == "bork":
    with open("Best of Gabe.txt", "r") as f:
      videos = [(line.strip()).split() for line in f]
      f.close()
    rand = str(videos[randint(1,271)])
    rand = rand[2:-2]
    await message.channel.send(rand)

  #if 2 messages are identical, repeat the message (make channel specific, fix 4+ messages)

  #counter = 0

  #with open("messages.txt", "a") as f:
    #f.write(dumb + "a" + "\n")
  
  #with open("messages.txt", "r+") as f:   
    #CoList = f.read().split("\n")
    #for i in CoList: 
      #if i: 
        #counter += 1  

  #with open("messages.txt", "r+") as f:
    #same = list(f)
    #msg3 = ""
    #msg1 = same[-1:]
    #msg2 = same[-2:-1]
    #if msg3 == msg1:
      #return
    #if msg1 == msg2:
      #msg3 = msg1
      #await message.channel.send(message.content)
      #same.clear()
      #os.remove("messages.txt")
    #if counter > 100:
      #os.remove("messages.txt")

#START OF COMMANDS
#the help command

@bot.command()
async def help(ctx):
  contents = ["`Lolzep Bot Help (Page 1, Main Commands)`\n**zp!help**\n> Displays this message\n**zp!verify** [**Image**]\n> Send a scorepost image to mod-chat to verify skill level and give skill roles\n**zp!vf** [**score** | first 3-4 digits | 1 for PUC] [**clear** | PUC,UC,etc.] [**level** | 20,19,etc.]\n> Calculates Volforce for a SDVX chart when given variables\n**zp!poll** [**question** | surrounded by quotes] [**answers** | up to 4 | surrounded by quotes]\n> Creates a poll for a question that has between 2 and 4 answers\n**zp!play** [**YouTube URL**], **zp!stop**\n> Play and stop YouTube videos in voice chat\n**zp!roll** [**value**]\n> Rolls a number 1-[value], default=100\n**zp!old**\n> Shows your account age\n**zp!oldlb**\n> Leaderboard of oldest account members (why? cause why not?)\n**zp!joined**\n> Create a list of users sorted by the date they joined the server\n**Certain Messages**\n> Peak comedy", "`Lolzep Bot Help (Page 2, Admin Commands)`\n**zp!bonk // zp!bonk** [**user**]\n> Sends a user to horny jail (leave [**user**] blank for user of last message)\n**zp!unbonk** [**user**]\n> Save a user from the depths of horny jail, once the horniness has passed\n**zp!boost**\n> Makes ar!member command to add levels for boosted members via AR bot (YggBasil only)\n**zp!copy**\n> Creates a data file for messages in a server channel (Lolzep only)\n**zp!say**\n> Sends a message as the bot (Lolzep only)"]
  pages = 2
  cur_page = 1
  message = await ctx.send(f"`Page {cur_page}/{pages}:`\n{contents[cur_page-1]}")

  await message.add_reaction("◀️")
  await message.add_reaction("▶️")

  def check(reaction, user):
    return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]

  while True:
    try:
      reaction, user = await bot.wait_for("reaction_add", timeout=60, check=check)
       # waiting for a reaction to be added - times out after x seconds, 60 in this
       # example

      if str(reaction.emoji) == "▶️" and cur_page != pages:
        cur_page += 1
        await message.edit(content=f"`Page {cur_page}/{pages}:`\n{contents[cur_page-1]}")
        await message.remove_reaction(reaction, user)

      elif str(reaction.emoji) == "◀️" and cur_page > 1:
        cur_page -= 1
        await message.edit(content=f"`Page {cur_page}/{pages}:`\n{contents[cur_page-1]}")
        await message.remove_reaction(reaction, user)

      else:
        await message.remove_reaction(reaction, user)
        # removes reactions if the user tries to go forward on the last page or
        # backwards on the first page
    except asyncio.TimeoutError:
      break
        # ending the loop if user doesn't react after x seconds

#account age leaderboard

@bot.command()
async def old(ctx, user=None):  
    created_at = str(ctx.author.created_at.strftime("%m/%d/%Y"))
    user = str(ctx.author.name)
    await ctx.send(user + " joined on " + created_at)

@bot.command()
async def oldlb(ctx):
  if os.path.exists("members.csv"):
    os.remove("members.csv")
  createddate = []
  boys = []

  for members in ctx.guild.members:
    boys.append(members.name) #puts them in a list
    createddate.append(members.created_at.strftime("%m/%d/%Y"))
      
    both = zip(boys, createddate) #sort the overall messages list
    sorted_both = sorted(both, key = lambda row: datetime.strptime(row[1], "%m/%d/%Y"), reverse=False)

  with open("members.csv", "a", newline='') as f:
    writer = csv.writer(f,delimiter='\t')
    writer.writerows(sorted_both) #write the overall messages list

  with open("members.csv", "r+", newline='') as f:
    counter = 0
    for lines in f:
      if counter == 10:
        break
      counter += 1

  boys, createddate = zip(*sorted_both)

  embed = discord.Embed(title = "Oldest Account Members (why not?) ¯\_(ツ)_/¯", color = discord.Color.purple())

  embed.set_thumbnail(url="https://i.imgur.com/rH1Tq0k.png")
  embed.add_field(name=":first_place: " + str(boys[0]), value=str(createddate[0]), inline=False)
  embed.add_field(name=":second_place: " + str(boys[1]), value=str(createddate[1]), inline=False)
  embed.add_field(name=":third_place: " + str(boys[2]), value=str(createddate[2]), inline=False)
  embed.add_field(name="#4 " + str(boys[3]), value=str(createddate[3]), inline=False)
  embed.add_field(name="#5 " + str(boys[4]), value=str(createddate[4]), inline=False)
  embed.add_field(name="#6 " + str(boys[5]), value=str(createddate[5]), inline=False)
  embed.add_field(name="#7 " + str(boys[6]), value=str(createddate[6]), inline=False)
  embed.add_field(name="#8 " + str(boys[7]), value=str(createddate[7]), inline=False)
  embed.add_field(name="#9 " + str(boys[8]), value=str(createddate[8]), inline=False)
  embed.add_field(name="#10 " + str(boys[9]), value=str(createddate[9]), inline=False)

  await ctx.send(embed=embed)

#voice chat player

@bot.command()
async def play(ctx, url=None):
  suburl = "https://www.youtube.com/watch?v="
  if suburl not in url:
    await ctx.send("Please enter a valid link")
    return
  if not ctx.author.voice:
    await ctx.send("Please connect to a voice channel.")
    return
  if ctx.author.voice.channel:
    await ctx.send("File is being downloaded...")
    if not ctx.guild.voice_client:
        player = await ctx.author.voice.channel.connect()
    else:
        player = ctx.guild.voice_client
    options = {
          "postprocessors":[{
              "key": "FFmpegExtractAudio", # download audio only
              "preferredcodec": "mp3", # other acceptable types "wav" etc.
              "preferredquality": "192" # 192kbps audio
          }],
          "format": "bestaudio/best",
          "outtmpl": "yt_song.mp3" # downloaded file name
      }
    with youtube_dl.YoutubeDL(options) as dl:
      dl.download([url])
    player.play(discord.FFmpegPCMAudio("yt_song.mp3"))
    await ctx.send("Now playing!") 
    playing = player.is_playing()
    while playing: # not compulsory
      await asyncio.sleep(1)
      playing = player.is_playing()
    if os.path.exists("yt_song.mp3"):
      os.remove("yt_song.mp3") # delete the file after use
      await asyncio.sleep(3)
      await ctx.guild.voice_client.disconnect()
      await ctx.send("Song has finished")  

@bot.command()
async def stop(ctx):
  if os.path.exists("yt_song.mp3"):
    os.remove("yt_song.mp3")
  if ctx.voice_client: # If the bot is in a voice channel 
    await ctx.guild.voice_client.disconnect() # Leave the channel
    await ctx.send("Sorry you don't like my music... I'll leave now :c")   
  else: # But if it isn't
    await ctx.send("I'm not in a voice channel yet, play some tunes with \"zp!play\"!")
          
#say a message as the bot

@bot.command()
async def say(ctx):
  author = ctx.message.author
  say = str(ctx.message.content)
  if str(author) != "Lolzep#5723": #checks to see if im running the bot
    await ctx.send(".-.", delete_after=5)
    await ctx.message.delete()
  else:
    await ctx.send(say[7:])
    await ctx.message.delete()

#calculates volforce for a song when given variables

@bot.command()
async def vf(ctx, score, clear, level):
  score = str(score[0:4]).strip().ljust(4,"0") #filter score value
  if score != "1000":
    score = score[:3] + '.' + score[3:]
  score = float(score)

  clear = str(clear).strip().upper() #filter clear value

  level = str(level[0:2]).strip() #filter level value
  if int(level) > 20 or int(level) < 0: #if out of range level, return error message
    await ctx.send("`Level out of range (" + level + ")! Using a level of 20`")
    level = 20

  #select correct medal coefficient for clear given

  medal = 0
  clear_medal = {"PUC":1.10,"UC":1.05,"EC":1.02,"C":1.00,"F":0.50}
  for key in clear_medal: 
    if clear == key:
      medal = clear_medal.get(key)
  if clear == "PUC" or clear == "UC" or clear == "EC" or clear == "C" or clear == "F":
    pass
  else: #if unknown clear is given, return error message
    await ctx.send("`Unknown clear value (" + clear + "). Acceptable values are PUC, UC, EC, C, and F. C has been used instead`")
    clear = "C"
    medal = 1.00

  #selects the correct grade coefficient and grade based on score given

  grade = 0 
  letter = ""
  counter = -1
  score_range = [1000 >= score >= 990, 990 > score >= 980, 980 > score >= 970, 970 > score >= 950, 950 > score >= 930, 930 > score >= 900, 900 > score >= 870, 870 > score >= 750, 750 > score >= 650, 650 > score]
  for item in score_range:
    if item == False:
      counter += 1
    if item == True:
      counter += 1
      break

  grade_letter = {"S":1.05, "AAA+":1.02, "AAA":1.00, "AA+":0.97, "AA":0.94, "A+":0.91, "A":0.88, "B":0.85, "C":0.82, "D":0.80}
  correct = list(grade_letter.items())[counter]
  letter = correct[0]
  grade = correct[1]
  
  #calculate eg/vw volforce

  eg_volforce = float(level) * (score/1000) * float(grade) * float(medal) * 2 / 100
  vw_volforce = eg_volforce

  factor = 1 / (10 ** 3) #round down
  eg_volforce = (eg_volforce // factor) * factor
  eg_volforce = "{:.3f}".format(eg_volforce) #formatting

  factor = 1 / (10 ** 2) #round down
  vw_volforce = (vw_volforce // factor) * factor
  vw_volforce = "{:.2f}".format(vw_volforce) #formatting
 
  #making of the embed that's posted by the bot

  embed = discord.Embed(title = "Volforce for " + str(ctx.message.author.name), color = discord.Color.purple())

  embed.set_thumbnail(url=ctx.author.avatar_url)
  embed.add_field(name="Exceed Gear Volforce", value=eg_volforce, inline=False)
  embed.add_field(name="Vivid Wave Volforce", value=vw_volforce, inline=False)
  embed.add_field(name="Level", value=level, inline=False)
  embed.add_field(name="Grade Coefficient", value=str(grade) + " (" + str(letter) + ")", inline=False)
  embed.add_field(name="Clear Coefficient", value=str(medal) + " (" + str(clear) + ")", inline=False)

  await ctx.send(embed=embed)

  #send all command outputs to a csv (useful if wanting to save for submitting things (yggbasil))

  author_list = []
  eg_volforce_list = []
  vw_volforce_list = []
  letter_list = []
  level_list = []
  score_list = []

  with open("vf.csv", "a", newline='') as f:
    author_list.append(ctx.message.author)
    eg_volforce_list.append(eg_volforce)
    vw_volforce_list.append(vw_volforce)
    level_list.append(level)
    letter_list.append(letter)
    score_list.append(score)
      
    both = zip(author_list, eg_volforce_list, vw_volforce_list, level_list, letter_list, score_list) #sort the overall messages list
    sorted_both = sorted(both, reverse=True)

    writer = csv.writer(f,delimiter='\t')
    writer.writerows(sorted_both) #write the overall messages list

#rolls a number 1-(number specified, default=100)

@bot.command()
async def roll(ctx, number=100):
  rng = randint(1,int(number))
  await ctx.send(str(ctx.message.author.name) + " rolled a " + str(rng) + "!")

#makes ar!member command to add levels for boosted members via AR Bot

@bot.command()
async def boost(ctx):
  boosters = []
  author = ctx.message.author
  if str(author) != "YggBasil#0573" and str(author) != "Lolzep#5723": #checks to see if correct people are running the bot
    await ctx.send("You're not YggBasil... command not executed.", delete_after=5)
  else:
    await ctx.send("just copy these xd")
    for members in ctx.guild.premium_subscribers: #checks all boosted members
      boosters.append(members.name + "#" + members.discriminator) #puts them in a list
    with open("boosters.txt", "w") as f:
      for item in boosters:
        f.write("ar!member " + item + " give 1000\n")
    await ctx.send(file=discord.File("boosters.txt"))
  
#creates a data file for channels in a server

@bot.command()
async def copy(ctx):
  start = time.time()
  author = ctx.message.author
  if str(author) != "Lolzep#5723": #checks to see if im running the bot
    await ctx.send("You're not my father... command not executed.", delete_after=5)
    if os.path.exists("file.csv"):
      os.remove("file.csv")
  else:
    #counter that starts at 0 for counting amount of messages
    overallcount = 0
    #list for every variable tracked
    lines = []
    counter = []
    authors = []
    made_at = []
    #react = []
    await ctx.send("Processing channel... this might take awhile (or fail)")
    with open("file.csv", "w") as f:
      async for message in ctx.history(limit=20000): #for every msg in channel (up to limit)
        msg_author = message.author.name
        lines.append(msg_author) #lines list used for sorting
        counter.append(str(overallcount + 1))
        authors.append(msg_author)
        made_at.append(message.created_at.strftime("%m/%d/%Y")) #append each message's content to each list
        #react.append(message.reactions)
        overallcount = overallcount + 1 #increase counter by 1 each for-loop

      channel_name = message.channel.name #variables to limit api requests
      server_name = message.guild.name
      f.write(str(server_name) + " #" + str(channel_name) + "\n") #first line inside csv file
      
      lines.sort() #sort usernames and then find the frequency to count amount of messages from each user
      results = {value: len(list(freq)) for value,freq in groupby(sorted(lines))}

      numbers = [] #used to write the results of frequency of usernames
      users = []
      for value in results.values():
        numbers.append(value)
      for key in results.keys():
        users.append(key)
      
      both = zip(numbers,users) #sort the overall messages list
      sorted_both = sorted(both, reverse=True)

      writer = csv.writer(f,delimiter='\t')
      writer.writerows(sorted_both) #write the overall messages list

      f.write(str(overallcount) + " total messages\n\n") #total messages

      for w in range(overallcount):
        writer.writerow([counter[w], authors[w], made_at[w]]) #write the appended lists

      os.rename("file.csv", str(server_name) + " #" + str(channel_name) + ".csv") #rename csv
      end = time.time()
      shutil.move(str(server_name) + " #" + str(channel_name) + ".csv","Copy Data/" + str(server_name) + " #" + str(channel_name) + ".csv")
      totaltime = end - start
      totaltime = "{:.2f}".format(totaltime)
      await ctx.send("Done! Data file made! Time taken was " + str(totaltime) + " seconds") #confirm that file was made successfully

#polls

@bot.command()
async def poll(ctx,question=None,*answers):
  await ctx.message.delete()
  poll_answers = list(answers)
  len_answers = len(poll_answers)
  settime = 60
  embed = discord.Embed(title = question, color = discord.Color.purple())
  reactions = ["1️⃣", "2️⃣", "3️⃣", "4️⃣"]
  percents = []

  if len_answers >=5:
    embed.add_field(name="My god... you're full of answers...", value="Too many answers! Please limit amount of answers to 4 or less. Make sure that you are using quotes to separate each entry!", inline=False)
    poll = await ctx.send(embed=embed)
    await poll.add_reaction("❓")    
  if len_answers == 0:
    embed.add_field(name="Bro, it's a question not a statement...", value='Please add answers for your question! Example: zp!poll "Favorite Monkey?" "SDVX Gorilla" "The Great Ape"', inline=False)
    poll = await ctx.send(embed=embed)
    await poll.add_reaction("❓")
  elif len_answers == 1:
    embed.add_field(name="This ain't a dictatorship...", value='Please add more than one answer for your question! Example: zp!poll "Favorite Monkey?" "SDVX Gorilla" "The Great Ape"', inline=False)
    poll = await ctx.send(embed=embed)
    await poll.add_reaction("❓")
  elif len_answers == 2:
    embed.add_field(name=str("1️⃣ " + poll_answers[0]), value="?", inline=False)
    embed.add_field(name=str("2️⃣ " + poll_answers[1]), value="?", inline=False)
    initial = await ctx.send("Vote now! " + str(settime) + " seconds until results.")
    poll = await ctx.send(embed=embed)

    for items in range(len_answers):
      await poll.add_reaction(reactions[items])

    await asyncio.sleep(settime)

    message = await ctx.fetch_message(poll.id)

    count_reactions = {react.emoji: react.count for react in message.reactions}
    no_bot_count_reactions = {key: count_reactions[key] - 1 for key in count_reactions}
    keys, values = zip(*no_bot_count_reactions.items())

    total = values[0] + values[1]
    for item in values:
      percents.append("{:.0%}".format(item / total))

    await asyncio.sleep(1)
    await initial.delete()
    await poll.delete()
    embed.clear_fields()

    embed.add_field(name=poll_answers[0], value=percents[0], inline=False)
    embed.add_field(name=poll_answers[1], value=percents[1], inline=False)
    poll = await ctx.send(embed=embed)

  elif len_answers == 3:
    embed.add_field(name=str("1️⃣ " + poll_answers[0]), value="?", inline=False)
    embed.add_field(name=str("2️⃣ " + poll_answers[1]), value="?", inline=False)
    embed.add_field(name=str("3️⃣ " + poll_answers[2]), value="?", inline=False)
    initial = await ctx.send("Vote now! " + str(settime) + " seconds until results.")
    poll = await ctx.send(embed=embed)

    for items in range(len_answers):
      await poll.add_reaction(reactions[items])

    await asyncio.sleep(1)

    message = await ctx.fetch_message(poll.id)

    count_reactions = {react.emoji: react.count for react in message.reactions}
    no_bot_count_reactions = {key: count_reactions[key] - 1 for key in count_reactions}
    keys, values = zip(*no_bot_count_reactions.items())

    total = values[0] + values[1] + values[2]
    for item in values:
      percents.append("{:.0%}".format(item / total))

    await asyncio.sleep(settime)
    await initial.delete()
    await poll.delete()
    embed.clear_fields()

    embed.add_field(name=poll_answers[0], value=percents[0], inline=False)
    embed.add_field(name=poll_answers[1], value=percents[1], inline=False)
    embed.add_field(name=poll_answers[2], value=percents[2], inline=False)
    poll = await ctx.send(embed=embed)

  elif len_answers == 4:
    embed.add_field(name=str("1️⃣ " + poll_answers[0]), value="?", inline=False)
    embed.add_field(name=str("2️⃣ " + poll_answers[1]), value="?", inline=False)
    embed.add_field(name=str("3️⃣ " + poll_answers[2]), value="?", inline=False)
    embed.add_field(name=str("4️⃣ " + poll_answers[3]), value="?", inline=False)
    initial = await ctx.send("Vote now! " + str(settime) + " seconds until results.")
    poll = await ctx.send(embed=embed)

    for items in range(len_answers):
      await poll.add_reaction(reactions[items])

    await asyncio.sleep(1)

    message = await ctx.fetch_message(poll.id)

    count_reactions = {react.emoji: react.count for react in message.reactions}
    no_bot_count_reactions = {key: count_reactions[key] - 1 for key in count_reactions}
    keys, values = zip(*no_bot_count_reactions.items())

    total = values[0] + values[1] + values[2] + values[3]
    for item in values:
      percents.append("{:.0%}".format(item / total))

    await asyncio.sleep(settime)
    await initial.delete()
    await poll.delete()
    embed.clear_fields()

    embed.add_field(name=poll_answers[0], value=percents[0], inline=False)
    embed.add_field(name=poll_answers[1], value=percents[1], inline=False)
    embed.add_field(name=poll_answers[2], value=percents[2], inline=False)
    embed.add_field(name=poll_answers[3], value=percents[3], inline=False)
    print(max(percents))
    poll = await ctx.send(embed=embed)

#take sent image, post to mod-chat for verification, say what dan?

@bot.command()
async def verify(ctx):
  user = ctx.guild.get_member(ctx.message.author.id)
  channel = bot.get_channel(752960043275780224)
  if not ctx.message.attachments:
    await ctx.send("Please attach your image when sending the command. Example: zp!verify [Image]")
    return
  for attachment in ctx.message.attachments:
    await attachment.save(f'VerifyImages/{attachment.filename}')
    await channel.send(file=discord.File(f"VerifyImages/{attachment.filename}"))
    os.remove(f'VerifyImages/{attachment.filename}')
  await channel.send(f"{user.mention}" + " is attempting to verify a skill level. Give the appropriate role as shown in the image.")
  await ctx.send("This skill level claim is now being verified. Your role will be updated if approved.")

#add the "horny jail" role to someone

@bot.command()
@commands.has_any_role("Admin", "Mod", "A Person")
async def bonk(ctx, user: discord.Member):
  role = discord.utils.get(ctx.guild.roles, name="horny jail")
  name = user.name
  if role in user.roles:
    await ctx.send(str(name) + " is already horny.")
    return
  if name == "Lolzep Bot" or name == "Lolzep":
    await ctx.send("Nice try.")
    return
  await user.add_roles(role)
  await ctx.send(":boom: :hammer: " + str(name) + " has been sent to horny jail. Let this be lesson for you.") 

@bonk.error
async def bonk_error(ctx, error):
  if isinstance(error, commands.MissingAnyRole):
    await ctx.send("You're not a mod/admin.")
  if isinstance(error, commands.MissingRequiredArgument):
    role = discord.utils.get(ctx.guild.roles, name="horny jail")
    async for message in ctx.history(limit=2):
      name = message.author
      respond = message.author.name
    if respond == "Lolzep Bot" or respond == "Lolzep":
      await ctx.send("Nice try.")
      return
    await name.add_roles(role)
    await ctx.send(":boom: :hammer: " + str(respond) + " has been sent to horny jail. Let this be lesson for you.")

@bot.command()
@commands.has_any_role("Admin", "Mod", "A Person")
async def unbonk(ctx, user: discord.Member):
  role = discord.utils.get(ctx.guild.roles, name="horny jail")
  name = user.name
  if role not in user.roles:
    await ctx.send(str(name) + " is not horny.")
    return
  await user.remove_roles(role)
  await ctx.send(str(name) + " does not wish to be horny anymore. They just want to be happy.")

@unbonk.error
async def unbonk_error(ctx, error):
  if isinstance(error, commands.MissingAnyRole):
    await ctx.send("You're not a mod/admin.")
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("Please input a horny user.")

#make list of users based on join date

@bot.command()
async def joined(ctx):
  if os.path.exists("joined.csv"):
    os.remove("joined.csv")
  joineddate = []
  boys = []

  for members in ctx.guild.members:
    boys.append(members.name) #puts them in a list
    joineddate.append(members.joined_at.strftime("%m/%d/%Y"))
      
    both = zip(boys, joineddate) #sort the overall messages list
    sorted_both = sorted(both, key = lambda row: datetime.strptime(row[1], "%m/%d/%Y"), reverse=False)

  with open("joined.csv", "a", newline='') as f:
    writer = csv.writer(f,delimiter='\t')
    writer.writerows(sorted_both) #write the overall messages list

  boys, createddate = zip(*sorted_both)

  await ctx.send("User list created.")
  await ctx.send(file=discord.File("joined.csv"))  

keep_alive() #used to keep the bot alive and not timeout from server

bot.run(os.getenv('TOKEN'))

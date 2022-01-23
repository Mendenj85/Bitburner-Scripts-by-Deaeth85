import os
import discord
from keep_alive import keep_alive
from discord.ext import commands
from github import Github
g = Github()
repo = g.get_repo("danielyxie/bitburner")
contents = repo.get_contents("markdown")
paths = [x.path for x in contents if x.path != "markdown/index.md" or x.path !='markdown/bitburner.md']
paths.sort(key=lambda x: len(x))
bot = commands.Bot(command_prefix='!',help_command=None)

botUrl = "https://i.ibb.co/LSbWqj0/Bitburner-Logo.png"
botName = "Bitburner Help Bot"

commandDescriptions = {
    'help':'Displays possible commands (wow what a shocker)',
    'md':'<arg> Link to Bitburner Markdown pages based on the args you supply',
}
guideDirectory = os.getcwd()+'/guides/'
#Get list of files for guides without the extension
fileList = [os.path.splitext(file)[0] for file in os.listdir(guideDirectory)]

guideContents = {}
for guide in os.listdir(guideDirectory):
    file = open(guideDirectory+guide,'r')
    content = file.read()
    guideContents.update({guide:content})

@bot.command()
async def guide(ctx, arg=""):
    file = open(guideDirectory+arg+'.txt','r')
    fileContent = file.read().splitlines()
    
    embedTitle = fileContent[1]
    content = fileContent[3:] #Everything from 4th line onwards, previous lines are reserved for title and description

    fieldTitles = []
    for lineNum,line in enumerate(content):
        if '{FIELD}' in line:
            fieldTitles.append([line.replace('{FIELD}',''),lineNum])

    fieldValues = []
    for index in range(len(fieldTitles)):
        #This breaks down everything between {FIELD}s into individual entries
        startIndex = fieldTitles[index][1]+1
        #Check if this is the last {FIELD}
        if index != len(fieldTitles)-1:
            endIndex = fieldTitles[index+1][1]
            fieldValues.append('\n'.join(content[startIndex:endIndex]))
        #If this is the last {FIELD} get everything after it as an entry
        else:
            fieldValues.append('\n'.join(content[startIndex:]))
            
    embed = discord.Embed(title=embedTitle, url=botUrl,color=0x00bc38)
    #for every {FIELD} add an embed field with the corresponding value
    if len(fieldTitles) > 0:
        for index in range(len(fieldTitles)):
            embed.add_field(name=fieldTitles[index][0],value=fieldValues[index],inline=False)
    else:
        embed.description = '\n'.join(content)
        
    embed.set_author(name=botName, icon_url=botUrl)
    if(len(''.join(content)) > 600): #Check if guide's character count exceeds 600
        return await ctx.author.send(embed=embed)
    return await ctx.channel.send(embed=embed)


@bot.command()
async def help(ctx, args=""):
    
    if args == "":
        stringBuilder = ''
        for key in commandDescriptions:
            stringBuilder += '**!{command}** - {description}\n'.format(
                command=key, description=commandDescriptions[key])
        
        for guide in guideContents:
            name = os.path.splitext(guide)[0] #get rid of the file extension
            fileContent = guideContents[guide].splitlines()
            description = fileContent[0]
            stringBuilder += f"**!{name}** - {description}\n"
            
        stringBuilder += '\nIf you have any ideas for other commands that could be added, please submit a PR on the git-hub'
        embed = discord.Embed(title="Command list",description=stringBuilder, url = botUrl,color=0x00bc38)
        embed.set_author(name=botName, icon_url=botUrl)
        await ctx.author.send(embed=embed)
        
    else:
        if args in commandDescriptions.keys():
            await ctx.channel.send("{command} - {description}".format(command=args,description=commandDescriptions[args]))
        elif args in fileList:
            file = open(guideDirectory+args+'.txt','r')
            fileContents = file.read().splitlines()
            argDescription = fileContents[0]
            content = fileContents[3:]
            if(len(''.join(content)) > 600):
                await ctx.channel.send("{args} - {description} (Will pm user)".format(args=args,description=argDescription))
            else:
                await ctx.channel.send("{args} - {description}".format(args=args,description=argDescription))
        else:
            await ctx.channel.send("Command doesn't exist!")
            
@bot.command()
async def md(ctx, args=""):
    allowedSpoilerList = ["endgame","help","coding-contract"]
    spoilersAllowed = False
    
    for channel in allowedSpoilerList:
        if ctx.channel.name.startswith(channel): spoilersAllowed = True
        
    if args == "":
        return await ctx.channel.send("Usage: !md <arg>")
    userInput = args
    linkList = []
    #Check if user wants namespace specific function
    if '.' not in userInput:
        for path in paths:
            function = path.split('.')[-2]
            if userInput.lower() == function:
                #Spoiler links if spoilers aren't allowed (except ns functions)
                if spoilersAllowed or path.split('.')[-3] == 'ns':
                    linkList.append("<https://github.com/danielyxie/bitburner/blob/dev/" + path +">\n")
                else: linkList.append("ENDGAME SPOILER: ||<https://github.com/danielyxie/bitburner/blob/dev/" + path +">||\n")
    else:
        nameSpace = userInput.lower().split('.')[0]
        functionName = userInput.lower().split('.')[1]
        for path in paths:
            print(path)
            function = path.split('.')[-2]
            if functionName == function and path.split('.')[-3] == nameSpace:
                if spoilersAllowed or nameSpace == 'ns':
                    linkList.append("<https://github.com/danielyxie/bitburner/blob/dev/" + path +">\n")
                else: linkList.append("ENDGAME SPOILER: ||<https://github.com/danielyxie/bitburner/blob/dev/" + path +">||\n")
            
    if(len(linkList) > 0):
        return await ctx.channel.send(''.join(linkList))
    await ctx.channel.send("That page does not exist!")
    
    
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    activity = discord.Activity(name="!help || Possible Spoilers", type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("Bot is ready!")

@bot.event
async def on_message(message):
    content = message.content[1:].split(' ')
    if message.author == bot.user:
        return
    if not message.content.startswith(bot.command_prefix):
        return
    if len(message.content)==1:
        return
    if content[0] in fileList:
        message.content = '!guide ' + content[0]
        return await bot.process_commands(message)
    if content[0] not in commandDescriptions.keys():
        return await message.channel.send("Command doesn't exist! Type `!help` for a list of commands!")
    await bot.process_commands(message)


my_secret = os.environ['token']
keep_alive()
bot.run(my_secret)

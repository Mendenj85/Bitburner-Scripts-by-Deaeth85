import discord
import os
from keep_alive import keep_alive
from discord.ext import commands
from github import Github
g = Github()
repo = g.get_repo("danielyxie/bitburner")
contents = repo.get_contents("markdown")
paths = [x.path for x in contents if x.path != "markdown/index.md"]
paths.sort(key=lambda x: len(x))
bot = commands.Bot(command_prefix='!',help_command=None)


commandDescriptions = {
    'help':'Displays possible commands (wow what a shocker)',
    'md':'<arg> Link to Bitburner Markdown pages based on the args you supply',
}
guideDirectory = os.getcwd()+'/guides/'
#Get list of files for guides without the extension
fileList = [os.path.splitext(file)[0] for file in os.listdir(guideDirectory)]



@bot.command()
async def guide(ctx, arg=""):
    file = open(guideDirectory+arg+'.txt','r')
    contents = '\n'.join(file.read().splitlines()[2:])
    await ctx.channel.send(contents)

@bot.command()
async def help(ctx,args=""):

    if args == "":
        stringBuilder = ''
        for key in commandDescriptions:
            stringBuilder += '!{command} - {description}\n'.format(command=key,description=commandDescriptions[key])
            
        for guide in os.listdir(guideDirectory):
            file = open(guideDirectory+guide,'r')
            description = file.read().splitlines()[0]
            stringBuilder += '!'+description +'\n'
        
        stringBuilder += '\nIf you have any ideas for other commands that could be added, please submit a PR on the git-hub'
        await ctx.author.send(stringBuilder)
    else:
        if args in commandDescriptions.keys():
            await ctx.channel.send("{command} - {description}".format(command=args,description=commandDescriptions[args]))
        elif args in fileList:
            file = open(guideDirectory+args+'.txt','r')
            argDescription = file.read().splitlines()[0]
            await ctx.channel.send("{description}".format(description=argDescription))
        else:
            await ctx.channel.send("Command doesn't exist!")
            
@bot.command()
async def md(ctx, args=""):
    if args == "":
        return await ctx.channel.send("Usage: !md <arg>")
    userInput = args
    linkList = []
    for path in paths:
        function = path.split('.')[-2]
        if userInput.lower() == function:
            linkList.append("<https://github.com/danielyxie/bitburner/blob/dev/" + path +">\n")
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

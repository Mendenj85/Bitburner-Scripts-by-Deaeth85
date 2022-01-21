import os
import discord
from discord.ext import commands
from github import Github
from keep_alive import keep_alive

g = Github()
repo = g.get_repo("danielyxie/bitburner")
contents = repo.get_contents("markdown")
paths = [x.path for x in contents if x.path != "markdown/index.md"]

bot = commands.Bot(command_prefix='!', help_command=None)

commandList = {
    'ascend': 'General advice on when to ascend gang members',
    'batch': 'Link to Batch Algorithms section of Hacking Algorithms on "Read the Docs"',
    'bn3': 'Pulls a startup guide written by Angr for BN3(Corps)',
    'bn4': 'Explains the updates to BN4',
    'cores': 'Gives a description of what core upgrades do',
    'escape': 'Gives assistance to players "still lost" right before, or after, installing TRP',
    'favor': 'Gives a breakdown of earning favor',
    'format': 'shows how to format .js code in Discord',
    'formulas': 'Link to basic Formulas API',
    'gang': 'Link to Bitburner Markdown Gang Interface page',
    'inject': 'Link to Injecting HTML from Advanced Gameplay in "Read The Docs',
    'karma':'Shows the undocumented function as a spoiler',
    'md':'<arg> Link to Bitburner Markdown pages based on the args you supply',
    'ns': 'same as md, for those who prefer ns over md',
    'order':'Pulls the Recommended Bit Node Order page from "Read The Docs"',
    'rep': 'Gives a list of ways to earn rep',
    'rss': 'Link to #resources channel in Bitburner Discord',
    'singularity': 'Link to Bitburner Markdown Singularity page',
    'source': 'Link to source code for the bot',
    'spoiler': 'Shows how to format spoilers for text in Discord',
    'startgang': 'Tells the requirments to start a gang outside of BN2',
    'stats': 'Link to Insights custom stats script',
}


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    activity = discord.Activity(name="!help || Possible Spoilers", type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("Bot is ready!")


@bot.command()
async def help(ctx, args=""):

    if args == "":
        stringBuilder = ''
        for key in commandList:
            stringBuilder += '!{command} - {description}\n'.format(
                command=key, description=commandList[key])
        stringBuilder += '\nIf you have any ideas for other commands that could be added, please submit a PR on the git-hub'
        await ctx.author.send(stringBuilder)
    else:
        if args in commandList.keys():
            await ctx.channel.send("{command} - {description}".format(command=args, description=commandList[args]))
        else:
            await ctx.channel.send("Command doesn't exist!")


@bot.command()
async def ascend(ctx):
    embed = discord.Embed(title="Gang Member Ascending", url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png",
                          description='General rule of thumb is to ascend when the ascension multiplier is at 1.6, slowly working your way to a 1.1 multiplier', color=0x00bc38)
    embed.set_author(name="Bitburner Help Bot ",
                     icon_url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png")
    embed.set_thumbnail(url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png")
    await ctx.send(embed=embed)


@bot.command()
async def batch(ctx):
    embed = discord.Embed(title="Batching Algorithms", url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png",
                          description="Here's a link that gives an overview on batching within Bitburner - https://bitburner.readthedocs.io/en/latest/advancedgameplay/hackingalgorithms.html#batch-algorithms-hgw-hwgw-or-cycles", color=0x00bc38)
    embed.set_author(name="Bitburner Help Bot ",
                     icon_url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png")
    embed.set_thumbnail(url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png")
    await ctx.send(embed=embed)


@bot.command()
async def bn3(ctx):
    embed = discord.Embed(title="Bit Node 3 Startup Guide", url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png",
                          description="Follow this link for a startup guide to corporations - <https://docs.google.com/document/d/e/2PACX-1vTzTvYFStkFjQut5674ppS4mAhWggLL5PEQ_IbqSRDDCZ-l-bjv0E6Uo04Z-UfPdaQVu4c84vawwq8E/pub>", color=0x00bc38)
    embed.set_author(name="Bitburner Help Bot ",
                     icon_url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png")
    embed.set_thumbnail(url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png")
    await ctx.send(embed=embed)


@bot.command()
async def bn4(ctx):
    embed = discord.Embed(title="Bit Node 4 Completion Info", url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png",
                          description="The following is what you get for completing BN4 - ram multiplier applies to singularity based scripts only", color=0x00bc38)
    embed.set_author(name="Bitburner Help Bot ",
                     icon_url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png")
    embed.set_thumbnail(url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png")
    embed.add_field(
        name="BN 4.1", value="All Singularities & 16x ram cost multiplier", inline=False)
    embed.add_field(
        name="BN 4.2", value="4x ram cost multiplier", inline=False)
    embed.add_field(
        name="BN 4.3", value="1x ram cost multiplier", inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def cores(ctx):
    embed = discord.Embed(title="Cores", url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png",
                          description='The effect of cores on grow and weaken scripts', color=0x00bc38)
    embed.set_author(name="Bitburner Help Bot ",
                     icon_url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png")
    embed.set_thumbnail(url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png")
    embed.add_field(name="Calculating the additive effect to grow and weaken scripts",
                    value="((cores-1)/16) * 100 : or 6.25% increase per core", inline=False)
    embed.add_field(name="Effect on timings", value="no effect", inline=False)
    embed.add_field(name="Servers affected",
                    value='only "home" and Endgame: ||hacknet servers||', inline=False)
    embed.set_footer(
        text='Only works on mentioned server(s) as all other servers only have one core')
    await ctx.send(embed=embed)


@bot.command()
async def escape(ctx):
    embed = discord.Embed(title="Escape", url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png",
                          description='How to "Find what you are looking for"', color=0x00bc38)
    embed.set_author(name="Bitburner Help Bot ",
                     icon_url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png")
    embed.set_thumbnail(url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png")
    embed.add_field(
        name="Step 1", value='||Purchase The "Special Aug" from an end-game faction and install augs||', inline=False)
    embed.add_field(
        name="Step 2", value='||Look "around" the cave to find what you are looking for||', inline=False)
    embed.add_field(name="Step 2.5 - if you're still lost",
                    value='||The "cave" is generally found deep in the network beyond `scan-analyze 10` range||')
    embed.add_field(name="Step 3", value="If you are still lost, maybe this clue from Zea might help - https://discord.com/channels/415207508303544321/415207923506216971/929207305612951592'", inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def favor(ctx):
    embed = discord.Embed(title="Earning Favor", url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png",
                          description="Here's a few different ways to earn favor", color=0x00bc38)
    embed.set_author(name="Bitburner Help Bot ",
                     icon_url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png")
    embed.set_thumbnail(url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png")
    embed.add_field(name="Export Save",
                    value="You can get 1 every 24 hours by backing up your save via the Augments tab in-game", inline=False)
    embed.add_field(name="Augmentation Install",
                    value="You gain favor based on earned rep after an aug install", inline=False)
    embed.add_field(name="How much on install?",
                    value="You can mouse over the reputation on main page of the faction to see how much favor you will earn on aug install", inline=False)
    embed.add_field(name="Getting 150 Favor/Donation Ability",
                    value="If you do it in one shot, it takes roughly 462.5k rep to get the 150 favor needed for donations", inline=False)
    embed.add_field(name="Getting Donation Status Faster",
                    value="This is easier to achieve by earning roughly 70k - 100k rep, then doing an aug install, as the next run you will earn more favor, and faster", inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def format(ctx):
    embed = discord.Embed(title="How to format code blocks in Discord", url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png",
                          description='This is how to formate code blocks', color=0x00bc38)
    embed.set_author(name="Bitburner Help Bot ",
                     icon_url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png")
    embed.set_thumbnail(url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png")
    embed.add_field(
        name="This:", value='\`\`\`js\nwhile (true) {\n ns.exec(my_script.js, "home");\n await ns.sleep(100);\n}\n\`\`\`', inline=False)
    embed.add_field(name="Turns into:",
                    value='```js\nwhile (true) {\n ns.exec(my_script.js, "home");\n await ns.sleep(100)\n}\n```', inline=False)
    embed.set_footer(
        text="NOTE: There are tabs in the top part, they just don't show up on embed formatting, but you see them in the code block")
    await ctx.send(embed=embed)


@bot.command()
async def formulas(ctx):
    embed = discord.Embed(title="Where to find the Formulas API", url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png",
                          description="Click this link: <https://github.com/danielyxie/bitburner/blob/dev/markdown/bitburner.formulas.md>", color=0x00bc38)
    embed.set_author(name="Bitburner Help Bot ",
                     icon_url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png")
    embed.set_thumbnail(url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png")
    await ctx.send(embed=embed)


@bot.command()
async def gang(ctx):
    embed = discord.Embed(title="Where to find the Gangs API", url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png",
                          description="Click this link: <https://github.com/danielyxie/bitburner/blob/master/markdown/bitburner.gang.md>", color=0x00bc38)
    embed.set_author(name="Bitburner Help Bot ",
                     icon_url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png")
    embed.set_thumbnail(url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png")
    await ctx.send(embed=embed)


@bot.command()
async def inject(ctx):
    embed = discord.Embed(title="How to Inject commands into the terminal", url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png",
                          description="Click this link: <https://bitburner.readthedocs.io/en/latest/netscript/advancedfunctions/inject_html.html>", color=0x00bc38)
    embed.set_author(name="Bitburner Help Bot ",
                     icon_url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png")
    embed.set_thumbnail(url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png")
    await ctx.send(embed=embed)


@bot.command()
async def karma(ctx):
    embed = discord.Embed(title="Here's how to find your Karma", url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png",
                          description="You can find your Karma with the undocumented function ||`ns.heart.break()`||", color=0x00bc38)
    embed.set_author(name="Bitburner Help Bot ",
                     icon_url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png")
    embed.set_thumbnail(url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png")
    await ctx.send(embed=embed)


@bot.command(aliases=['ns'])
async def md(ctx, args):
    linkPrefix = "<https://github.com/danielyxie/bitburner/blob/dev/"
    linkPostfix = ">\n"
    userInput = args
    userInputArray = userInput.lower().split('.')
    linkList = []
    if len(userInputArray) > 1:
        for path in paths:
            pathArray = path.split('.')
            if len(pathArray) == 2: # We already know it's more than 1, and the followin IF works if it's 3 or more
                continue
            if userInputArray[-2] == pathArray[-3] and userInputArray[-1] == pathArray[-2]:
                linkList.append(
                    linkPrefix + path + linkPostfix)
    else:
        for path in paths:
            pathArray = path.split('.')
            function = pathArray[-2]
            if userInputArray[0] == function:
                linkList.append(
                    linkPrefix + path + linkPostfix)
    if(len(linkList) > 0):
        return await ctx.channel.send(''.join(linkList))
    await ctx.channel.send("That page does not exist!")

    
@bot.command()
async def order(ctx):
    embed = discord.Embed(title="Here's a Generalized Bit Node Order Guide", url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png",
                          description="Click this link - <https://bitburner.readthedocs.io/en/latest/guidesandtips/recommendedbitnodeorder.html>", color=0x00bc38)
    embed.set_author(name="Bitburner Help Bot ",
                     icon_url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png")
    embed.set_thumbnail(url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png")
    await ctx.send(embed=embed)


@bot.command()
async def rep(ctx):
    embed = discord.Embed(title="Different Ways to Earn Rep", url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png",
                          description="Here's a list of the ways to earn reputation", color=0x00bc38)
    embed.set_author(name="Bitburner Help Bot ",
                     icon_url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png")
    embed.set_thumbnail(url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png")
    embed.add_field(name="Work at a Company",
                    value="higher stats increase rep gain", inline=False)
    embed.add_field(name="Augmentations",
                    value="Auguments with reputation bonus (includes Neuroflux Governor)", inline=False)
    embed.add_field(
        name="Favor", value="1 favor = 1% faster rep gain", inline=False)
    embed.add_field(
        name="Donations", value="unlocked at 150 favor, 1 rep per $1m donated, before bonuses", inline=False)
    embed.add_field(name="Infiltrations",
                    value="Successful infiltrations can earn rep", inline=False)
    embed.add_field(name="Coding Contracts",
                    value="give rep to a single joined faction, or spread across all joined factions", inline=False)
    embed.add_field(
        name="Endgame", value="||high Intelligence has an effect on reputation gain||", inline=False)
    embed.add_field(
        name="Endgame", value="||Corps can directly add rep with Corp funds||", inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def rss(ctx):
    embed = discord.Embed(title="Resources Channel", url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png",
                          description="Click this to see the suggested resources  - <#921223819375575050>", color=0x00bc38)
    embed.set_author(name="Bitburner Help Bot ",
                     icon_url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png")
    embed.set_thumbnail(url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png")
    await ctx.send(embed=embed)


@bot.command()
async def singularity(ctx):
    embed = discord.Embed(title="Singularity API", url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png",
                          description="Click this link - <https://github.com/danielyxie/bitburner/blob/master/markdown/bitburner.singularity.md>", color=0x00ff00)
    embed.set_author(name="Bitburner Help Bot ",
                     icon_url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png")
    embed.set_thumbnail(url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png")
    await ctx.send(embed=embed)

@bot.command()
async def source(ctx):
    embed=discord.Embed(title="Bitburner Help Bot Source Code", url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png", description="Click this link - <https://github.com/Mendenj85/Bitburner-Scripts-by-Deaeth85/blob/main/Bitburner%20Help%20Bot.py>", color=0x00ff00)
    embed.set_author(name="Bitburner Help Bot ", icon_url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png")
    embed.set_thumbnail(url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png")
    await ctx.send(embed=embed)

@bot.command()
async def spoiler(ctx):
    embed = discord.Embed(title="How to format Spoilers in Discord", url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png",
                          description="This is how you format spoilers", color=0x00bc38)
    embed.set_author(name="Bitburner Help Bot ",
                     icon_url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png")
    embed.set_thumbnail(url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png")
    embed.add_field(name="This:", value="\|\|text\|\|", inline=False)
    embed.add_field(name="Turns into:", value="||text||", inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def startgang(ctx):
    embed = discord.Embed(title="Gang Startup", url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png",
                          description="How to start up a gang", color=0x00bc38)
    embed.set_author(name="Bitburner Help Bot ",
                     icon_url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png")
    embed.set_thumbnail(url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png")
    embed.add_field(name="While in BN 2.x",
                    value="Join any gang related faction, then click 'Manage Gang'", inline=False)
    embed.add_field(name="Outside of BN 2",
                    value="You need -54k Karma to start a gang", inline=False)
    embed.add_field(name="How to get the Karma",
                    value="This equates to 15 hours of 100% success rate homicide", inline=False)
    embed.add_field(name="How to get the Karma faster",
                    value="Sleeves can help reduce this time drastically", inline=True)
    await ctx.send(embed=embed)


@bot.command()
async def stats(ctx):
    embed = discord.Embed(title="Stats", url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png",
                          description="Click this link for Insights custom stats script - <https://github.com/bitburner-official/bitburner-scripts/blob/master/custom-stats.js>", color=0x00bc38)
    embed.set_author(name="Bitburner Help Bot ",
                     icon_url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png")
    embed.set_thumbnail(url="https://i.ibb.co/LSbWqj0/Bitburner-Logo.png")
    await ctx.send(embed=embed)

my_secret = os.environ['token']
keep_alive()
bot.run(my_secret)

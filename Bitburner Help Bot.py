import discord
import os
from keep_alive import keep_alive
from discord.ext import commands
from github import Github

g = Github()
repo = g.get_repo("danielyxie/bitburner")
contents = repo.get_contents("markdown")
paths = [x.path for x in contents if x.path != "markdown/index.md"]

bot = commands.Bot(command_prefix='!',help_command=None)

commandList = {
    'ascend':'General advice on when to ascend gang members',
    'batch':'Link to Batch Algorithms section of Hacking Algorithms on "Read the Docs"',
    'bn3':'Pulls a startup guide written by Angr for BN3(Corps)',
    'bn4':'Explains the updates to BN4',
    'cores':'Gives a description of what core upgrades do',
    'escape':'Gives assistance to players "still lost" right before, or after, installing TRP',
    'favor':'Gives a breakdown of earning favor',
    'format':'shows how to format .js code in Discord',
    'formulas':'Link to basic Formulas API',
    'gang':'Link to Bitburner Markdown Gang Interface page',
    'inject':'Link to Injecting HTML from Advanced Gameplay in "Read The Docs',
    'karma':'Shows the undocumented function as a spoiler',
    'md':'<arg> Link to Bitburner Markdown pages based on the args you supply',
    'order':'Pulls the Recommended Bit Node Order page from "Read The Docs"',
    'rep':'Gives a list of ways to earn rep',
    'rss':'Link to #resources channel in Bitburner Discord',
    'singularity':'Link to Bitburner Markdown Singularity page',
    'spoiler':'Shows how to format spoilers for text in Discord',
    'startgang':'Tells the requirments to start a gang outside of BN2',
    'stats':'Link to Insights custom stats script',    
}

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    activity = discord.Activity(name="!help || Possible Spoilers", type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("Bot is ready!")

@bot.command()
async def help(ctx,args=""):

    if args == "":
        stringBuilder = ''
        for key in commandList:
            stringBuilder += '!{command} - {description}\n'.format(command=key,description=commandList[key])
        stringBuilder += '\nIf you have any ideas for other commands that could be added, please submit a PR on the git-hub'
        await ctx.author.send(stringBuilder)
    else:
        if args in commandList.keys():
            await ctx.channel.send("{command} - {description}".format(command=args,description=commandList[args]))
        else:
            await ctx.channel.send("Command doesn't exist!")

@bot.command()
async def ascend(ctx):
    await ctx.channel.send("General rule of thumb is to ascend when the ascension multiplier is at 1.6, slowly working your way to a 1.1 multiplier")

@bot.command()
async def batch(ctx):
    await ctx.channel.send("Here's a link that gives an overview on batching within Bitburner - <https://bitburner.readthedocs.io/en/latest/advancedgameplay/hackingalgorithms.html#batch-algorithms-hgw-hwgw-or-cycles>")

@bot.command()
async def bn3(ctx):
    await ctx.channel.send("Follow this link for a startup guide to corporations - <https://docs.google.com/document/d/e/2PACX-1vTzTvYFStkFjQut5674ppS4mAhWggLL5PEQ_IbqSRDDCZ-l-bjv0E6Uo04Z-UfPdaQVu4c84vawwq8E/pub>")

@bot.command()
async def bn4(ctx):
    await ctx.channel.send("The updated SF4.1 gives all Singularity functions now. The other change is the ram cost of singularity based scripts outside of BN4\n4.1 = 16x ram cost\n4.2 = 4x ram cost\n4.3 = 1x ram cost")

@bot.command()
async def cores(ctx):
    await ctx.channel.send("(cores-1)/16 additive effect to grow/weaken\nTimings don't change\nOnly works on 'home' server")

@bot.command()
async def escape(ctx):
    await ctx.channel.send('Step 1: ||Purchase The "Special Aug" from an end-game faction and install augs||\nStep 2: ||Look "around" the cave to find what you are looking for||\nStep 3: If you are still lost, maybe this clue from Zea might help - https://discord.com/channels/415207508303544321/415207923506216971/929207305612951592')

@bot.command()
async def favor(ctx):
    await ctx.channel.send("Favor is earned by:\nYou can get 1 every 24 hours by backing up your save via the Augments tab in-game\nYou gain favor based on earned rep after an aug install\nYou can mouse over the reputation on main faction page to see how much favor you will earn on aug install\nIf you go do it all at once, it takes roughly 462.5k rep to get the 150 favor needed for donations\nThis is easier to achieve by earning roughly 70k - 100k rep, then doing an install, as the next run you will earn more favor, faster")

@bot.command()
async def format(ctx):
    await ctx.channel.send("This:\n\`\`\`js\nawait ns.sleep(100);\n\`\`\`\nTurns into this:\n```js\nawait ns.sleep(100)\n```")

@bot.command()
async def formulas(ctx):
    await ctx.channel.send("<https://github.com/danielyxie/bitburner/blob/dev/markdown/bitburner.formulas.md>")

@bot.command()
async def gang(ctx):
    await ctx.channel.send("<https://github.com/danielyxie/bitburner/blob/master/markdown/bitburner.gang.md>")

@bot.command()
async def inject(ctx):
    await ctx.channel.send("<https://bitburner.readthedocs.io/en/latest/netscript/advancedfunctions/inject_html.html>")

@bot.command()
async def karma(ctx):
    await ctx.channel.send("You can find your Karma with the undocumented function ||`ns.heart.break()`||")

@bot.command()
async def md(ctx, args):
    userInput = args
    linkList = []
    for path in paths:
        function = path.split('.')[-2]
        if userInput.lower() == function:
          linkList.append("<https://github.com/danielyxie/bitburner/blob/dev/" + path +">\n")
    if(len(linkList) > 0):
        return await ctx.channel.send(''.join(linkList))
    await ctx.channel.send("That page does not exist!")

@bot.command()
async def order(ctx):
    await ctx.channel.send("<https://bitburner.readthedocs.io/en/latest/guidesandtips/recommendedbitnodeorder.html>")

@bot.command()
async def rep(ctx):
    await ctx.channel.send("Methods of gaining rep:\n1. Job: higher stats increase rep gain\n2. Auguments with reputation bonus (includes Neuroflux Governor)\n3. Faction favor, 1 favor = 1% faster gain\n4. Donations (unlocked at 150 favor, 1 rep per $1m donated, before bonuses)\n5. Infiltrations\n6. Coding Contracts can give rep to a single joined faction, or spread across all joined factions\n7. Endgame: ||high Intelligence has an effect on reputation gain||\n8. Endgame: ||Corps can directly add rep with Corp funds||")

@bot.command()
async def rss(ctx):
    await ctx.channel.send("<#921223819375575050>")

@bot.command()
async def singularity(ctx):
    await ctx.channel.send("<https://github.com/danielyxie/bitburner/blob/master/markdown/bitburner.singularity.md>")

@bot.command()
async def spoiler(ctx):
    await ctx.channel.send("This is how you format spoilers:\n\|\|text\|\|\nWill turn into this:\n||text||")

@bot.command()
async def startgang(ctx):
    await ctx.channel.send("You need -54k Karma to start a gang outside of BN2\nThis equates to 15 hours of 100% homicide\nSleeves can help reduce this time drastically")

@bot.command()
async def stats(ctx):
    await ctx.channel.send("<https://github.com/bitburner-official/bitburner-scripts/blob/master/custom-stats.js>")

my_secret = os.environ['token']
keep_alive()
bot.run(my_secret)

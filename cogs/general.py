import discord
from discord.ext import commands
import datetime
import functions
from functions import data_dict, keys


class General:
    def __init__(self, bot):
        self.bot = bot

    async def on_member_join(self, member):
        await member.send('Hello & welcome to Team Paradox discord server\n'
                          'If you are new to our community you can check out our application process'
                          ' with "!app".\nIf you are already part of Team Paradox, please message '
                          f'one of the council in game with your discord tag ({member})'
                          '\nBy using our discord you agree to abide by our rules\n'
                          'for more information on commands and rules '
                          'type "!help" and "!rules" respectively')

    @commands.command()
    async def rules(self, ctx):
        """Shows Rules"""
        embed = discord.Embed(title="Rules", colour=discord.Colour(0x14d2fd),
                              url="http://team-paradox.com/index.php?/topic/4-rules/",
                              description="\nNO excessive flaming, including religion, racism, and homophobia."
                                          "\n\nNO talk of Staking/Gambling within the Clan Chat/ TPx Discord"
                                          "\n\nNO Scamming/Hacking/Phishing/DDoSing"
                                          "\n\nLENDS & LOANS are to be made on your own terms."
                                          "\n\nNO Pking other clan members unless mutually agreed",
                              timestamp=datetime.datetime.utcfromtimestamp(1439636401))
        embed.set_thumbnail(url="http://team-paradox.com/uploads/monthly_2017_06/58c5e3e643f4e_oldlogo.png."
                                "929cdfce6dd1113c40497e2633517a8d.png.30328b34ac18b81e4fa23544608c23f9.png")
        embed.set_author(name="Team Paradox", url="http://team-paradox.com")
        embed.set_footer(text="Team Paradox", icon_url="http://team-paradox.com/favicon.ico")
        await ctx.send(content="Summary of TPx Rules", embed=embed)

    # @commands.command()
    # async def about(self, ctx):
    #     """Brings up github page on TPx Bot"""
    #     await ctx.send(functions.recall_json(data_dict['reference'], keys["commands"]))

    @commands.command()
    async def app(self, ctx):
        """Application information for new members"""
        await ctx.send('Apply at <http://www.team-paradox.com/index.php?/forum/28-applications> \n'
                       'Requirements: <http://team-paradox.com/index.php?/topic/1324-requirements>')

    @commands.command()
    async def event(self, ctx):
        """Upcoming event information"""
        await ctx.send(functions.recall_json(data_dict['small'], keys['small'][1]))

    @commands.command()
    async def item(self, ctx):
        """Current Item of the Week"""
        await ctx.send(functions.recall_json(data_dict['small'], keys['small'][0]))

    @commands.command()
    async def rotations(self, ctx):
        """Shows raids rotations"""
        await ctx.send('https://i.gyazo.com/d303883c8f2ef2a5679dc7f28ef0b800.png')

    @commands.command()
    async def drop(self, ctx, drop_rate: int, *, kills: int):
        """Work out % chance to of recieved atleast 1 drop in 1/<drop rate> <Kills>"""
        await ctx.send(functions.drop_rate(drop_rate, kills) + ' chance to have received the drop')

    @commands.command()
    async def pointvalues(self, ctx):
        """links TPx's Pvm Point values"""
        await ctx.send('Point values can be found at:\n'
                       '<http://team-paradox.com/index.php?/topic/246-drop-competition-point-values/>')

    @commands.command()
    async def submit(self, ctx):
        """links TPx's forums to submit drops"""
        await ctx.send('Drops can be submitted for PvM Points!\n'
                       'New drops can be submitted under member boards, '
                       '[Month] drop competition, Week [x]'
                       '\nhttp://team-paradox.com/index.php?/forum/43-member-boards/\n'
                       "Drops that you had forgotten about or didn't "
                       "post in time for the competition are still "
                       'eligible for points and can be submitted here \n'
                       'http://team-paradox.com/index.php?/forum/127-point-appeals/')

    @commands.command()
    async def rsn(self, ctx, *, message: str):
        """Search TPx member database by RSN and Forum name"""
        message = message.replace(' ', '%20')
        await ctx.send('By RSN:\n'
                       f'<http://team-paradox.com/index.php?/search/&type=core_members&core_pfield_11={message}>\n'
                       'By Forum Name:\n'
                       f'<http://team-paradox.com/index.php?/search/&q={message}&type=core_members>')

    @commands.command()
    async def rankup(self, ctx):
        """Displays rank up information"""
        embed = discord.Embed(title="Want to rank up?!", colour=discord.Colour(0x14d2fd),
                              url="https://team-paradox.com",
                              description="You can check out the forums for information.\nNew members should use "
                                          "!app to see the appropriate information\n\n"
                                          "For existing members here are the requirements for "
                                          "[Member](http://team-paradox.com/index.php?/topic/2232-"
                                          "member-requirements/), "
                                          "[Experienced](http://team-paradox.com/index.php?/topic/"
                                          "2233-experienced-requirements/) and "
                                          "[Elite](http://team-paradox.com/index.php?/"
                                          "topic/2234-elite-requirements/)\n\n"
                                          "Once you have all the requirements for"
                                          " your next rank please create a new topic "
                                          "[here](http://team-paradox.com/index.php?/forum/83-rankup-applications/)")
        embed.set_thumbnail(url="http://team-paradox.com/uploads/monthly_2017_06/58c5e3e643f4e_oldlogo.png.929cdfce6d"
                                "d1113c40497e2633517a8d.png.30328b34ac18b81e4fa23544608c23f9.png")
        embed.set_footer(text="Team Paradox", icon_url="http://team-paradox.com/favicon.ico")
        await ctx.send(embed=embed)



    @commands.command()
    async def info(self, ctx):
        """Displays info about the bot"""
        embed = discord.Embed(title="Team Paradox Bot",
                              colour=discord.Colour(0x00aa08),
                              url="https://github.com/SourSpoon/TPxBot-Cogs",
                              description="A discord bot written in Python 3, with the aid of the discord.py library."
                                          "\nWritten & Hosted by <@120636888418615300>/ Spoon#7805"
                                          "\n[GitHub](https://github.com/SourSpoon/TPxBot-Cogs)")

        embed.set_footer(text="\N{SPOON} Sour Spoon")
        await ctx.send(embed=embed)

    @commands.command(aliases=['hc'])
    async def hotandcold(self, ctx):
        """
        Posts link to the Hot & Cold Map

        Can also use hc
        """
        await ctx.send('<https://vignette.wikia.nocookie.net/2007scape/images/5/50/Strange_device_dig_locations.png'
                       '/revision/latest?cb=20170711150204>')


def setup(bot):
    bot.add_cog(General(bot))

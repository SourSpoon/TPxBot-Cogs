import discord
from discord.ext import commands
import functions
from functions import data_dict


class Admin:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def init_small(self, ctx):
        """resets item & event data"""
        small = {
            'item': '',
            'event': '',
        }
        functions.init_small(small)
        await ctx.send('Small Initialised')

    @init_small.error
    async def init_small_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.CheckFailure):
            await ctx.message.add_reaction('\N{Cross Mark}')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def init_ref(self, ctx):
        ref = {'commands': ''}
        functions.init_reference(ref)
        await ctx.send('Reference Initialised')

    @init_ref.error
    async def init_ref_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.CheckFailure):
            await ctx.message.add_reaction('\N{Cross Mark}')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def init_queue(self, ctx):
        boss_list = ['bandos', 'sara', 'arma', 'zammy', 'raids', 'corp', 'dks']
        functions.init_queues(data_dict['queues'], boss_list)

    @init_queue.error
    async def init_queue_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.CheckFailure):
            await ctx.message.add_reaction('\N{Cross Mark}')


def setup(bot):
    bot.add_cog(Admin(bot))

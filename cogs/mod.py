import discord
from discord.ext import commands
from testtokens import admin_channel_id
import functions
from functions import data_dict, keys


class Mod:
    def __init__(self, bot):
        self.bot = bot

    # @commands.command()
    # @commands.has_permissions(manage_messages=True)
    # @commands.guild_only()
    # async def purge(self, ctx, mention, *, reason: str=None):
    #     """Deletes the last 20 messages from mentioned user"""


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def setevent(self, ctx, *, message: str):
        """Sets Event information - Manage Messages req"""
        functions.rewrite_json(data_dict['small'], keys['small'][1], message)
        await ctx.send('Event set!')
        await ctx.send(functions.recall_json(data_dict['small'], keys['small'][1]))

    @setevent.error
    async def setevent_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.CheckFailure):
            await ctx.message.add_reaction('\N{Cross Mark}')

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def setitem(self, ctx, *, message: str):
        """Sets Item of the week information - Manage Messages req"""
        functions.rewrite_json(data_dict['small'], keys['small'][0], message)
        await ctx.send('Item set!')
        await ctx.send(functions.recall_json(data_dict['small'], keys['small'][0]))

    @setitem.error
    async def setitem_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.CheckFailure):
            await ctx.message.add_reaction('\N{Cross Mark}')

    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.guild_only()
    async def kick(self, ctx, target: discord.Member, *, reason: str=None):
        """Kicks a pleb - Requires Kick perms"""
        await ctx.guild.kick(target, reason=reason)
        await ctx.message.delete()
        admin = self.bot.get_channel(admin_channel_id)
        embed = functions.punish(target, 'Kick', ctx.author, reason)
        await admin.send(embed=embed)

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.CheckFailure):
            await ctx.message.add_reaction('\N{Cross Mark}')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.guild_only()
    async def ban(self, ctx, target: discord.Member, *, reason):
        """Bans a pleb - Requires Ban perms"""
        await ctx.guild.ban(target, reason=reason)
        await ctx.message.delete()
        admin = self.bot.get_channel(admin_channel_id)
        embed = functions.punish(target, 'Ban', ctx.author, reason)
        await admin.send(embed=embed)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.CheckFailure):
            await ctx.message.add_reaction('\N{Cross Mark}')

    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.guild_only()
    async def soft(self, ctx,  target: discord.Member, *, reason: str=None):
        """Bans then unbans a pleb to delete all their messages - Requires Kick perms"""
        await ctx.guild.ban(target, reason=reason)
        await ctx.guild.unban(target)
        await ctx.message.delete()
        admin = self.bot.get_channel(admin_channel_id)
        embed = functions.punish(target, 'Soft Ban', ctx.author, reason)
        await admin.send(embed=embed)

    @soft.error
    async def soft_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.errors.CheckFailure):
            await ctx.message.add_reaction('\N{Cross Mark}')


def setup(bot):
    bot.add_cog(Mod(bot))

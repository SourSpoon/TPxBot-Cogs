from discord.ext import commands
import functions
from functions import Boss


bandos = Boss('bandos', 3)
arma = Boss('arma', 2)
sara = Boss('sara', 3)
zammy = Boss('zammy', 2)
raids = Boss('raids', 3)
corp = Boss('corp', 3)
dks = Boss('dks', 2)
boss_list = [bandos, sara, arma, zammy, raids, corp, dks]


class Queue:
    def __init__(self, bot):
        self.bot = bot

    @commands.group(has_subcommands=True, aliases=['q'])
    async def queue(self, ctx):
        """Has subcommands use !help queue for more details."""
        if ctx.invoked_subcommand is None:
            await ctx.send('Invalid Queue command')

    @queue.command()
    async def arma(self, ctx):
        full, list_ = functions.append_queue(arma, ctx.author.mention)
        if full is True:
            await ctx.send(f'{list_[0]} & {list_[1]} are ready to kill Armadyl')
        elif full is False:
            await ctx.message.add_reaction('\N{White Heavy Check Mark}')

    @queue.command()
    async def bandos(self, ctx):
        full, list_ = functions.append_queue(bandos, ctx.author.mention)
        if full is True:
            await ctx.send(f'{list_[0]} & {list_[1]} are ready to kill Bandos')
        elif full is False:
            await ctx.message.add_reaction('\N{White Heavy Check Mark}')

    @queue.command()
    async def sara(self, ctx):
        full, list_ = functions.append_queue(sara, ctx.author.mention)
        if full is True:
            await ctx.send(f'{list_[0]} & {list_[1]} are ready to kill Saradomin')
        elif full is False:
            await ctx.message.add_reaction('\N{White Heavy Check Mark}')

    @queue.command()
    async def zammy(self, ctx):
        full, list_ = functions.append_queue(zammy, ctx.author.mention)
        if full is True:
            await ctx.send(f'{list_[0]} & {list_[1]} are ready to kill Zammy')
        elif full is False:
            await ctx.message.add_reaction('\N{White Heavy Check Mark}')

    @queue.command()
    async def dks(self, ctx):
        full, list_ = functions.append_queue(dks, ctx.author.mention)
        if full is True:
            await ctx.send(f'{list_[0]} & {list_[1]} are ready to kill Dagannoth Kings')
        elif full is False:
            await ctx.message.add_reaction('\N{White Heavy Check Mark}')

    @queue.command()
    async def corp(self, ctx):
        full, list_ = functions.append_queue(corp, ctx.author.mention)
        if full is True:
            await ctx.send(f'{list_[0]} & {list_[1]} are ready to kill Corporeal Beast')
        elif full is False:
            await ctx.message.add_reaction('\N{White Heavy Check Mark}')

    @queue.command(aliases=['raids'])
    async def raid(self, ctx):
        full, list_ = functions.append_queue(raids, ctx.author.mention)
        if full is True:
            await ctx.send(f'{list_[0]} & {list_[1]} are ready to Raid the Chambers Of Xeric')
        elif full is False:
            await ctx.message.add_reaction('\N{White Heavy Check Mark}')

    @queue.command(aliases=['remove'])
    async def rem(self, ctx):
        functions.remove_from_queue(ctx.author.mention)
        await ctx.message.add_reaction('\N{White Heavy Check Mark}')

    @queue.command()
    async def status(self, ctx):
        status_d = functions.get_queue_info()
        await ctx.send("```"
                       f"dks has {status_d['dks']} player(s) in the queue \n"
                       f"bandos has {status_d['bandos']} player(s) in the queue \n"
                       f"corp has {status_d['corp']} player(s) in the queue \n"
                       f"raids has {status_d['raids']} player(s) in the queue \n"
                       f"zammy has {status_d['zammy']} player(s) in the queue \n"
                       f"sara has {status_d['sara']} player(s) in the queue \n"
                       f"arma has {status_d['arma']} player(s) in the queue \n```")


def setup(bot):
    bot.add_cog(Queue(bot))

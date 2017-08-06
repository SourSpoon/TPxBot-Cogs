from discord.ext import commands
import discord
from testtokens import token

tpx = commands.Bot(command_prefix='!')
# tpx.remove_command('help')
description = 'this thing'
startup_extensions = ['cogs.general', 'cogs.queue', 'cogs.mod']



@tpx.event
async def on_ready():
    print('Logged In As')
    print(tpx.user.name)
    print(tpx.user.id)
    print(discord.__version__)
    print('---------')


@tpx.event
async def on_message(message):
    if message.author.bot:
        return
    if message.author == tpx.user:
        return
    await tpx.process_commands(message)


@tpx.command(hidden=True)
@commands.has_permissions(administrator=True)
async def load(ctx, extension_name: str):
    """Loads an extension."""
    try:
        tpx.load_extension(extension_name)
    except (AttributeError, ImportError) as err:
        x = type(err).__name__
        y = str(err)
        await ctx.send(f"```py\n{x}: {y}\n```")
        return
    await ctx.send(f"{extension_name} loaded.")


@load.error
async def load_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CheckFailure):
        await ctx.message.add_reaction('\N{Cross Mark}')


@tpx.command(hidden=True)
@commands.has_permissions(administrator=True)
async def unload(ctx, extension_name: str):
    """Unloads an extension."""
    tpx.unload_extension(extension_name)
    await ctx.send(f"{extension_name} unloaded.")


@unload.error
async def unload_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CheckFailure):
        await ctx.message.add_reaction('\N{Cross Mark}')


if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            tpx.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    tpx.run(token)

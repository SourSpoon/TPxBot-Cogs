from discord.ext import commands
import discord
import datetime
import aiohttp
import json


def _read_json(item):
    with open('data/items.json', 'r') as doc:
        data = json.load(doc)
        if item in data:
            item_id = data[item]["id"]
            return item_id
        return None


class Exchange:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def price(self, ctx, *, item: str):
        message = await ctx.send('Fetching price')
        item = item.lower()
        item_id = _read_json(item)
        if item_id is None:
            await message.edit(content='Item not found')
            return
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.rsbuddy.com/grandExchange",
                                   params=f"a=guidePrice&i={item_id}") as price_data:
                content = (await price_data.json())
        embed = discord.Embed()
        embed.colour = discord.Colour(0x14d2fd)
        embed.title = item.title()
        embed.url = f"https://rsbuddy.com/exchange?id={item_id}"
        embed.add_field(name="Buying Price", value="{:,}gp".format(content["buying"]))
        embed.add_field(name="Selling Price", value="{:,}gp".format(content["selling"]))
        embed.add_field(name="Buying Quantity", value="{:,}/hr".format(content["buyingQuantity"]))
        embed.add_field(name="Selling Quantity", value="{:,}/hr".format(content["sellingQuantity"]))
        await message.edit(embed=embed)


def setup(bot):
    bot.add_cog(Exchange(bot))

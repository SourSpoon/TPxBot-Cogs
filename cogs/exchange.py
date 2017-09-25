from discord.ext import commands
import discord
import async_timeout
import json


class Exchange:
    def __init__(self, bot):
        self.bot = bot
        self.session = bot.session
        self.rsb_api = 'https://api.rsbuddy.com/grandExchange?a=guidePrice&i='

    async def _fetch(self, url):
        with async_timeout.timeout(10):
            async with self.session.get(url) as resp:
                return await resp.json()

    def _build_url(self, item):
        with open('data/item.json') as file:
            item_db = json.load(file)
            item = item.lower()
            if item in item_db:
                item_id = item_db[item]['id']
                url = (1, self.rsb_api + item_id)
                return url
            else:
                failed = (0, "failed")
                return failed

    @commands.command()
    async def price(self, ctx, *, item):
        """looks up price of item against RSBuddy Exchange"""
        status, url = self._build_url(item)
        if status == 0:
            return await ctx.send(f"unable to find item: {item}")
        content = await self._fetch(url)

        # build embed
        em = discord.Embed()
        em.colour = discord.Colour(0x13c116)
        em.title = item.title()
        em.url = url
        em.add_field(name="Buying Price", value="{:,}gp".format(content["buying"]))
        em.add_field(name="Selling Price", value="{:,}gp".format(content["selling"]))
        em.add_field(name="Buying Quantity", value="{:,}/hr".format(content["buyingQuantity"]))
        em.add_field(name="Selling Quantity", value="{:,}/hr".format(content["sellingQuantity"]))
        await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(Exchange(bot))

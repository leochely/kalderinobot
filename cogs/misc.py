import asyncio
import datetime
import logging
import os

import humanize
from twitchio.ext import commands


class Misc(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="no")
    async def no(self, ctx: commands.Context):
        await ctx.send("Oh noooo kalder4Pliz")

    @commands.command(name="yes")
    async def yes(self, ctx: commands.Context):
        await ctx.send("Haha yes kalder4Yes")

    @commands.command(name="skip")
    async def skip(self, ctx: commands.Context):
        await ctx.send(f"Je te dedicace ce skip @{ctx.author.name} kalder4Speed")

    @commands.command(name="day", aliases=["jour"])
    async def day(self, ctx: commands.Context):
        week_days = ["Lundoom", "Mardoom", "Mercredoom",
                     "Jeudoom", "Vendredoom", "Samedoom", "Doomanche"]
        week_day = week_days[datetime.datetime.now().weekday()]
        await ctx.send(f"Aujourd'hui c'est {week_day}! kalder4Love")

    @commands.command(name="pb")
    async def pb(self, ctx: commands.Context):
        await ctx.send("1h 13m 54s 090ms kalder4Speed")

    @commands.command(name="moon")
    async def moon(self, ctx: commands.Context):
        humanize.i18n.activate("fr_FR")
        time = datetime.datetime(2021, 12, 22, 8, 41) - datetime.datetime.now()
        await ctx.send(f"Il reste {humanize.precisedelta(time, minimum_unit='seconds')} à Kald et ses camarades de project moon pour finir leurs runs avant que le jour ne se lève! Kalder4No")


def prepare(bot: commands.Bot):
    bot.add_cog(Misc(bot))

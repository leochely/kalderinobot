# bot.py
import asyncio
import logging
import os  # for importing env vars for the bot to use
import random
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path

from twitchio import Channel, Client, User
from twitchio.ext import commands, pubsub, routines


class KalderinoBot (commands.Bot):

    def __init__(self):
        super().__init__(
            token=os.environ['ACCESS_TOKEN'],
            prefix=os.environ['BOT_PREFIX'],
            initial_channels=os.environ['INITIAL_CHANNELS'].split(', '),
            case_insensitive=True
        )
        self.channel = None
        self._cogs_names: t.Dict[str] = [
            p.stem for p in Path(".").glob("./cogs/*.py")
        ]

    def setup(self):
        random.seed()

        print("Chargement des cogs...")

        for cog in self._cogs_names:
            logging.info(f"Loading `{cog}` cog.")
            self.load_module(f"cogs.{cog}")

        # logging.info("Starting timers")
        # self.loop.create_task(self.timers())

        logging.info("Chargement terminé")

    def run(self):
        self.setup()
        super().run()

    async def event_ready(self):
        # Notify us when everything is ready!

        # Starting timers
        # self.links.start()

        # We are logged in and ready to chat and use commands...
        logging.info(f'Logged in as | {self.nick}')

    async def event_message(self, message):
        # Messages with echo set to True are messages sent by the bot...
        # For now we just want to ignore them...
        if message.echo:
            return

        # Print the contents of our message to console...
        logging.info(
            f'{message.author.name} on channel {message.author.channel.name}: '
            f'{message.content}'
        )

        if "@kalderinobot" in message.content.lower():
            await self.random_reply(message)

        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands...
        await self.handle_commands(message)

    ## GENERAL FUNCTIONS ##

    @commands.command(name="git")
    async def git(self, ctx: commands.Context):
        await ctx.send(
            f'Here the source code of my bot dad LeixBot : https://github.com/leochely/LeixBot MrDestructoid'
        )

    @commands.command(name="list")
    async def list(self, ctx: commands.Context):
        list = ""
        for command in self.commands:
            list += command + ", "

        # Remove last comma and space
        list = list[:-2]
        await ctx.send(f'La liste des commandes de KalderinoBot: {list}')

    async def random_reply(self, message):
        compiled_msg = re.compile(re.escape("@KalderinoBot "), re.IGNORECASE)
        msg_clean = compiled_msg.sub("", message.content)
        reply_pool = [
            "Redis ca et je gold split", "Oh nooo", "Haha yes kalder4Yes",
            "Est-ce que ce monde est sérieux?", "Kalderinoskip incoming kalder4Yes",
            "Ici Goldospliteru, fils du grand @Kalderinofeross MrDestructoid"
        ]
        reply = random.choice(reply_pool)
        await message.author.channel.send(f"@{message.author.name} {reply}")


if __name__ == "__main__":
    logging.basicConfig(
        encoding='utf-8',
        level=logging.INFO,
        handlers=[
            logging.FileHandler("debug.log"),
            logging.StreamHandler()
        ]
    )

    bot = KalderinoBot()

    bot.run()

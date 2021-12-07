import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Discord stuff
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


class DoggersClient(discord.Client):
    """The custom client for the doggers boi bot."""

    async def on_message(self, message):
        """Filter messages and direct them to their proper functions.

        Fires for every message in the discord."""

        # The bot should not check messages from itself
        if message.author.id == self.id:
            return

    @staticmethod
    async def on_ready():
        """Things that happen when the bot boots up."""
        print(f'{client.user} has connected to Discord!')


client = DoggersClient()
client.run(TOKEN)

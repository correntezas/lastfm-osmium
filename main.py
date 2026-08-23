"""Last.fm bot for Osmium.
Loads configuration, sets up logging and connects to the Osmium gateway.
"""

import os
from asyncio import run
from logging import DEBUG, Formatter, StreamHandler, getLogger

from dotenv import load_dotenv
from osmium_chat import Bot

from modules import core, lastfm

load_dotenv()
TOKEN = os.getenv("OSMIUM_TOKEN")
CLIENT_ID = int(os.getenv("OSMIUM_CLIENT_ID"))
LASTFM_API_KEY = os.getenv("LASTFM_API_KEY")
LASTFM_SECRET = os.getenv("LASTFM_SECRET")


logger = getLogger("osmium_chat")
logger.setLevel(DEBUG)
_handler = StreamHandler()
_handler.setFormatter(Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s"))
logger.addHandler(_handler)

bot = Bot(prefix=".", client_id=CLIENT_ID, logger=logger)

bot.add_commands(core.CoreCommands)
bot.add_commands(lastfm.LastFMCommands)

if __name__ == "__main__":
    run(bot.connect(token=TOKEN))

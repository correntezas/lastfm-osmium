"""Hello world bot — minimal starting point.

See the other examples for focused feature demos:
  invites.py   -- invite creation, listing, lookup
  channels.py  -- channel create / rename / delete
  categories.py -- category create / manage / delete
  messages.py  -- sending, formatting, editing, DMs
"""

from asyncio import run
from logging import DEBUG, Formatter, StreamHandler, getLogger
from osmium_chat import Bot, Context, Message, commands
from os import getenv
from dotenv import load_dotenv
import os
from commands import general, lastfm

load_dotenv()
TOKEN = os.getenv('OSMIUM_TOKEN')
CLIENT_ID = int(os.getenv('OSMIUM_CLIENT_ID'))
LASTFM_API_KEY = os.getenv('LASTFM_API_KEY')
LASTFM_SECRET = os.getenv('LASTFM_SECRET')


logger = getLogger("osmium_chat")
logger.setLevel(DEBUG)
_handler = StreamHandler()
_handler.setFormatter(Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s"))
logger.addHandler(_handler)

bot = Bot(prefix=".", client_id=CLIENT_ID, logger=logger)


bot.add_commands(general.GeneralCommands)
bot.add_commands(lastfm.LastFMCommands)

if __name__ == "__main__":
    run(bot.connect(token=TOKEN))

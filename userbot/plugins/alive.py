import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet nibba, add your name in heroku var ALIVE_NAME"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.client.send_message(
            alive.chat_id,
            f"Python: 3.7.3\n`Database Status: Databases functioning normally!\n\nAlways with you, my master!\n`My owner`: {DEFAULTUSER}`",
            file="https://i.imgur.com/pU8BE9B.png"
        )
    await alive.delete()

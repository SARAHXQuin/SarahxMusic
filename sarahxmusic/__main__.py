import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from sarahxmusic import LOGGER, app, userbot
from sarahxmusic.core.call import SARAH
from sarahxmusic.misc import sudo
from sarahxmusic.plugins import ALL_MODULES
from sarahxmusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("sarahxmusic.plugins" + all_module)
    LOGGER("sarahxmusic.plugins").info("sᴜᴄᴄᴇssғᴜʟʟʏ ɪᴍᴘᴏʀᴛᴇᴅ ᴀʟʟ ᴍᴏᴅᴜʟᴇs...")
    await userbot.start()
    await SARAH.start()
    try:
        await SARAH.stream_call("https://telegra.ph/file/26541097b8833e61f603d.mp4")
    except NoActiveGroupCall:
        LOGGER("sarahxmusic").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await SARAH.decorators()
    LOGGER("sarahxmusic").info(
        "Music bot Started Successfully, Power By @we_are_universee"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("sarahxmusic").info("Stopping sarah x music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())

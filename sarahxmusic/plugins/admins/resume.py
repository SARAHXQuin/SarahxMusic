from pyrogram import filters
from pyrogram.types import Message

from sarahxmusic import app
from sarahxmusic.core.call import SARAH
from sarahxmusic.utils.database import is_music_playing, music_on
from sarahxmusic.utils.decorators import AdminRightsCheck
from sarahxmusic.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(filters.command(["resume", "cresume"]) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def resume_com(cli, message: Message, _, chat_id):
    if await is_music_playing(chat_id):
        return await message.reply_text(_["admin_3"])
    await music_on(chat_id)
    await SARAH.resume_stream(chat_id)
    photo_url = "https://te.legra.ph/file/c444d70431989b4c6cee4.jpg"  # Replace with the URL of the photo you want to send
    await message.reply_photo(
        photo=photo_url        
    )
    await message.reply_text(
        _["admin_4"].format(message.from_user.mention), disable_web_page_preview=True
    )

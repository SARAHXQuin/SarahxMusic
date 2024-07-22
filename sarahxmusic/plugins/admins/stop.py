from pyrogram import filters
from pyrogram.types import Message

from sarahxmusic import app
from sarahxmusic.core.call import SARAH
from sarahxmusic.utils.database import set_loop
from sarahxmusic.utils.decorators import AdminRightsCheck
from sarahxmusic.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(
    filters.command(["end", "stop", "cend", "cstop"]) & filters.group & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return
    await SARAH.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    photo_url = "https://te.legra.ph/file/5f3347d579c92e984521f.jpg"  # Replace with the URL of the photo you want to send    
    await message.reply_photo(
        photo=photo_url          
    )
    await message.reply_text(
        _["admin_5"].format(message.from_user.mention), reply_markup=close_markup(_)
    )

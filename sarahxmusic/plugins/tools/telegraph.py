from telegraph import upload_file
from pyrogram import filters
from sarahxmusic import app


@app.on_message(filters.command('tgm'))
def ul(_, message):
    reply = message.reply_to_message
    if reply.media:
        i = message.reply("𝐌aking 𝐀 𝐋ink 𝐎f 𝐘our 𝐃ocument 𝐁aby....")
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://telegra.ph" + x

        i.edit(f'🇾ᴏᴜʀ🇹ᴇʟᴇɢʀᴀᴘʜ 👉 {url}')

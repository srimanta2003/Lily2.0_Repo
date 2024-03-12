from pyrogram import filters
from pyrogram.types import Message
from unidecode import unidecode

from LilyXMusic import app
from LilyXMusic.misc import SUDOERS
from LilyXMusic.utils.database import (
    get_active_chats,
    get_active_video_chats,
    remove_active_chat,
    remove_active_video_chat,
)


@app.on_message(filters.command(["activevc", "av"]) & SUDOERS)
async def activevc(_, message: Message):
    mystic = await message.reply_text("» 𝐆ᴇᴛᴛɪɴɢ 𝐀ᴄᴛɪᴠᴇ 𝐕ᴏɪᴄᴇ 𝐂ʜᴀᴛs 𝐋ɪsᴛ...")
    served_chats = await get_active_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except:
            await remove_active_chat(x)
            continue
        try:
            if (await app.get_chat(x)).username:
                user = (await app.get_chat(x)).username
                text += f"<b>{j + 1}.</b> <a href=https://t.me/{user}>{unidecode(title).upper()}</a> [<code>{x}</code>]\n"
            else:
                text += (
                    f"<b>{j + 1}.</b> {unidecode(title).upper()} [<code>{x}</code>]\n"
                )
            j += 1
        except:
            continue
    if not text:
        await mystic.edit_text(f"» 𝐍ᴏ 𝐀ᴄᴛɪᴠᴇ 𝐕ᴏɪᴄᴇ 𝐂ʜᴀᴛs 𝐎ɴ {app.mention}.")
    else:
        await mystic.edit_text(
            f"<b>» 𝐋ɪsᴛ 𝐎ғ 𝐂ᴜʀʀᴇɴᴛʟʏ 𝐀ᴄᴛɪᴠᴇ 𝐕ᴏɪᴄᴇ 𝐂ʜᴀᴛs :</b>\n\n{text}",
            disable_web_page_preview=True,
        )


@app.on_message(filters.command(["activev", "av"]) & SUDOERS)
async def activevi_(_, message: Message):
    mystic = await message.reply_text("» 𝐆ᴇᴛᴛɪɴɢ 𝐀ᴄᴛɪᴠᴇ 𝐕ɪᴅᴇᴏ 𝐂ʜᴀᴛs 𝐋ɪsᴛ...")
    served_chats = await get_active_video_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except:
            await remove_active_video_chat(x)
            continue
        try:
            if (await app.get_chat(x)).username:
                user = (await app.get_chat(x)).username
                text += f"<b>{j + 1}.</b> <a href=https://t.me/{user}>{unidecode(title).upper()}</a> [<code>{x}</code>]\n"
            else:
                text += (
                    f"<b>{j + 1}.</b> {unidecode(title).upper()} [<code>{x}</code>]\n"
                )
            j += 1
        except:
            continue
    if not text:
        await mystic.edit_text(f"» 𝐍ᴏ 𝐀ᴄᴛɪᴠᴇ 𝐕ɪᴅᴇᴏ 𝐂ʜᴀᴛs 𝐎ɴ {app.mention}.")
    else:
        await mystic.edit_text(
            f"<b>» 𝐋ɪsᴛ 𝐎ғ 𝐂ᴜʀʀᴇɴᴛʟʏ 𝐀ᴄᴛɪᴠᴇ 𝐕ɪᴅᴇᴏ 𝐂ʜᴀᴛs :</b>\n\n{text}",
            disable_web_page_preview=True,
        )

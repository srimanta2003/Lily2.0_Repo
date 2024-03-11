from pyrogram.enums import ParseMode

from LilyXMusic import app
from LilyXMusic.utils.database import is_on_off
from config import LOGGER_ID


async def play_logs(message, streamtype):
    if await is_on_off(2):
        logger_text = f"""
<b>{app.mention} ᴘʟᴀʏ ʟᴏɢ</b>

<b>𝐂ʜᴀᴛ 𝐈ᴅ :</b> <code>{message.chat.id}</code>
<b>𝐂ʜᴀᴛ 𝐍ᴀᴍᴇ :</b> {message.chat.title}
<b>𝐂ʜᴀᴛ 𝐔sᴇʀɴᴀᴍᴇ :</b> @{message.chat.username}

<b>𝐔sᴇʀ 𝐈ᴅ :</b> <code>{message.from_user.id}</code>
<b>𝐍ᴀᴍᴇ :</b> {message.from_user.mention}
<b>𝐔sᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}

<b>𝐒ᴏɴɢ :</b> {message.text.split(None, 1)[1]}
<b>𝐒ᴛʀᴇᴀᴍᴛʏᴘᴇ :</b> {streamtype}"""
        if message.chat.id != LOGGER_ID:
            try:
                await app.send_message(
                    chat_id=LOGGER_ID,
                    text=logger_text,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return

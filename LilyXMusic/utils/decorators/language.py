from strings import get_string

from LilyXMusic import app
from LilyXMusic.misc import SUDOERS
from LilyXMusic.utils.database import get_lang, is_maintenance


def language(mystic):
    async def wrapper(_, message, **kwargs):
        if await is_maintenance() is False:
            if message.from_user.id not in SUDOERS:
                return await message.reply_text(
                    text=f"{app.mention} 𝐈s 𝐔ɴᴅᴇʀ 𝐌ᴀɪɴᴛᴇɴᴀɴᴄᴇ, 𝐕ɪsɪᴛ <a href={SUPPORT_CHAT}>𝐒ᴜᴘᴘᴏʀᴛ 𝐂ʜᴀᴛ</a> 𝐅ᴏʀ 𝐊ɴᴏᴡɪɴɢ 𝐓ʜᴇ 𝐑ᴇᴀsᴏɴ.",
                    disable_web_page_preview=True,
                )
        try:
            await message.delete()
        except:
            pass

        try:
            language = await get_lang(message.chat.id)
            language = get_string(language)
        except:
            language = get_string("en")
        return await mystic(_, message, language)

    return wrapper


def languageCB(mystic):
    async def wrapper(_, CallbackQuery, **kwargs):
        if await is_maintenance() is False:
            if CallbackQuery.from_user.id not in SUDOERS:
                return await CallbackQuery.answer(
                    f"{app.mention} 𝐈s 𝐔ɴᴅᴇʀ 𝐌ᴀɪɴᴛᴇɴᴀɴᴄᴇ, 𝐕ɪsɪᴛ 𝐒ᴜᴘᴘᴏʀᴛ 𝐂ʜᴀᴛ 𝐅ᴏʀ 𝐊ɴᴏᴡɪɴɢ 𝐓ʜᴇ 𝐑ᴇᴀsᴏɴ.",
                    show_alert=True,
                )
        try:
            language = await get_lang(CallbackQuery.message.chat.id)
            language = get_string(language)
        except:
            language = get_string("en")
        return await mystic(_, CallbackQuery, language)

    return wrapper


def LanguageStart(mystic):
    async def wrapper(_, message, **kwargs):
        try:
            language = await get_lang(message.chat.id)
            language = get_string(language)
        except:
            language = get_string("en")
        return await mystic(_, message, language)

    return wrapper

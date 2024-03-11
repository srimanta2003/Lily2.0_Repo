import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from LilyXMusic import LOGGER, app, userbot
from LilyXMusic.core.call import Anony
from LilyXMusic.misc import sudo
from LilyXMusic.plugins import ALL_MODULES
from LilyXMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("𝐀ssɪsᴛᴀɴᴛ 𝐂ʟɪᴇɴᴛ 𝐕ᴀʀɪᴀʙʟᴇs 𝐍ᴏᴛ 𝐃ᴇғɪɴᴇᴅ, 𝐄xɪᴛɪɴɢ...")
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
        importlib.import_module("LilyXMusic.plugins" + all_module)
    LOGGER("LilyXMusic.plugins").info("𝐒ᴜᴄᴄᴇssғᴜʟʟʏ 𝐈ᴍᴘᴏʀᴛᴇᴅ 𝐌ᴏᴅᴜʟᴇs...")
    await userbot.start()
    await Anony.start()
    try:
        await Anony.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("LilyXMusic").error(
            "𝐏ʟᴇᴀsᴇ 𝐓ᴜʀɴ 𝐎ɴ 𝐓ʜᴇ 𝐕ᴄ 𝐎ғ 𝐘ᴏᴜʀ 𝐋ᴏɢ 𝐆ʀᴏᴜᴘ\𝐂ʜᴀɴɴᴇʟ.\n\n𝐒ᴛᴏᴘᴘɪɴɢ 𝐁ᴏᴛ..."
        )
        exit()
    except:
        pass
    await Anony.decorators()
    LOGGER("LilyXMusic").info(
        "𝐌𝙴𝚁𝙸 𝐉𝙰𝙰𝙽 𝐌𝙰𝚉𝙴 𝐊𝙰𝚁𝙾 𝐀𝙱 𝐉𝙰𝙺𝙴 𝐀𝙶𝙰𝚁 𝐊𝙾𝙸 𝐈𝚂𝚂𝚄𝙴 𝐇𝚄𝙰 𝐓𝙾𝙷 @its_Aryaan 𝐘𝙰𝙷𝙰 𝐃𝙼 𝐊𝙰𝚁 𝐋𝙴𝙽𝙰"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("LilyXMusic").info("𝐒ᴛᴏᴘᴘɪɴɢ 𝐋𝚒𝚕𝚢𝚇𝐌𝚞𝚜𝚒𝚌 𝐌ᴜsɪᴄ 𝐁ᴏᴛ...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())

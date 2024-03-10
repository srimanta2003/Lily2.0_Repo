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
        LOGGER(__name__).error("ᴀssɪsᴛᴀɴᴛ ᴄʟɪᴇɴᴛ ᴠᴀʀɪᴀʙʟᴇs ɴᴏᴛ ᴅᴇғɪɴᴇᴅ, ᴇxɪᴛɪɴɢ...")
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
    LOGGER("LilyXMusic.plugins").info("sᴜᴄᴄᴇssғᴜʟʟʏ ɪᴍᴘᴏʀᴛᴇᴅ ᴍᴏᴅᴜʟᴇs...")
    await userbot.start()
    await Anony.start()
    try:
        await Anony.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("LilyXMusic").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await Anony.decorators()
    LOGGER("LilyXMusic").info(
        "𝙼𝙴𝚁𝙸 𝙹𝙰𝙰𝙽 𝙼𝙰𝚉𝙴 𝙺𝙰𝚁𝙾 𝙰𝙱 𝙹𝙰𝙺𝙴 𝙰𝙶𝙰𝚁 𝙺𝙾𝙸 𝙸𝚂𝚂𝚄𝙴 𝙷𝚄𝙰 𝚃𝙾𝙷 @its_Aryaan 𝚈𝙰𝙷𝙰 𝙳𝙼 𝙺𝙰𝚁 𝙻𝙴𝙽𝙰"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("LilyXMusic").info("Stopping 𝙻𝚒𝚕𝚢𝚇𝙼𝚞𝚜𝚒𝚌 Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())

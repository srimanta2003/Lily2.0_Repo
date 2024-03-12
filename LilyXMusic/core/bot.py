from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config

from ..logging import LOGGER


class Anony(Client):
    def __init__(self):
        LOGGER(__name__).info(f"𝐋ɪʟʏ𝐱𝐌ᴜsɪᴄ 𝐒ᴛᴀʀᴛ 𝐇ᴏ 𝐑ᴀʜᴀ 𝐁ᴀʙᴇ...")
        super().__init__(
            name="LilyXMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            parse_mode=ParseMode.HTML,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

        try:
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=f"<u><b>» {self.mention} 𝐁ᴏᴛ 𝐒ᴛᴀʀᴛ 𝐇ᴏ 𝐆ʏᴀ 𝐁ᴀʙᴇ :</b><u>\n\n𝐁ᴏᴛ 𝐊ɪ 𝐈ᴅ: <code>{self.id}</code>\n𝐁ᴏᴛ 𝐊ᴀ 𝐍ᴀᴍᴇ: {self.name}\n𝐁ᴏᴛ 𝐊ᴀ 𝐔sᴇʀɴᴀᴍᴇ : @{self.username}",
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid):
            LOGGER(__name__).error(
                "𝐁𝐬ᴅᴋ 𝐁ᴏᴛ 𝐊ᴏ 𝐋ᴏɢ 𝐆ʀᴏᴜᴘ 𝐌ᴇ 𝐀ᴅᴍɪɴ 𝐁ᴀɴᴀʏᴀ 𝐘ᴀ 𝐍ʜɪ."
            )
            exit()
        except Exception as ex:
            LOGGER(__name__).error(
                f"𝐁ᴏᴛ 𝐊ᴏ 𝐊ᴏɴ 𝐓ᴇʀᴀ 𝐁ᴀᴀᴘ 𝐀ᴅᴍɪɴ 𝐁ᴀɴᴀʏᴇɢᴀ? .\n  𝐄ʀʀᴏʀ : {type(ex).__name__}."
            )
            exit()

        a = await self.get_chat_member(config.LOGGER_ID, self.id)
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error(
                "𝐁sᴅᴋ 𝐁ᴏᴛ 𝐊ᴏ 𝐋ᴏɢ 𝐆ʀᴏᴜᴘ 𝐌ᴇ 𝐀ᴅᴍɪɴ 𝐁ᴀɴᴀʏᴀ 𝐘ᴀ 𝐍ʜɪ?."
            )
            exit()
        LOGGER(__name__).info(f"𝐋ɪʟʏ𝐱𝐌ᴜsɪᴄ 𝐒ᴛᴀʀᴛᴇᴅ{self.name}")

    async def stop(self):
        await super().stop()

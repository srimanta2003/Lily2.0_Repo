from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_DB_URI

from ..logging import LOGGER

LOGGER(__name__).info("𝐂ᴏɴɴᴇᴄᴛɪɴɢ 𝐓ᴏ 𝐘ᴏᴜʀ 𝐌ᴏɴɢᴏ 𝐃ʙ 𝐃ᴀᴛᴀʙᴀsᴇ...")
try:
    _mongo_async_ = AsyncIOMotorClient(MONGO_DB_URI)
    mongodb = _mongo_async_.Anon
    LOGGER(__name__).info("𝐂ᴏɴɴᴇᴄᴛᴇᴅ 𝐓ᴏ 𝐘ᴏᴜʀ 𝐌ᴏɴɢᴏ 𝐃ʙ 𝐃ᴀᴛᴀʙᴀsᴇ.")
except:
    LOGGER(__name__).error("𝐅ᴀɪʟᴇᴅ 𝐓ᴏ 𝐂ᴏɴɴᴇᴄᴛ 𝐓ᴏ 𝐘ᴏᴜʀ 𝐌ᴏɴɢᴏ 𝐃ʙ 𝐃ᴀᴛᴀʙᴀsᴇ.")
    exit()

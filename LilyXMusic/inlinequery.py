from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="𝐏ᴀᴜsᴇ",
            description=f"𝐏ᴀᴜsᴇ 𝐓ʜᴇ 𝐂ᴜʀʀᴇɴᴛ 𝐏ʟᴀʏɪɴɢ 𝐒ᴛʀᴇᴀᴍ 𝐎ɴ 𝐕ɪᴅᴇᴏᴄʜᴀᴛ.",
            thumb_url="https://graph.org/file/1f05ea59a08727a9ea01e.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="𝐑ᴇsᴜᴍᴇ",
            description=f"𝐑ᴇsᴜᴍᴇ 𝐓ʜᴇ 𝐏ᴀᴜsᴇᴅ 𝐒ᴛʀᴇᴀᴍ 𝐎ɴ 𝐕ɪᴅᴇᴏᴄʜᴀᴛ.",
            thumb_url="https://graph.org/file/1f05ea59a08727a9ea01e.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="𝐒ᴋɪᴩ",
            description=f"𝐒ᴋɪᴩ 𝐓ʜᴇ 𝐂ᴜʀʀᴇɴᴛ 𝐏ʟᴀʏɪɴɢ 𝐒ᴛʀᴇᴀᴍ 𝐎ɴ 𝐕ɪᴅᴇᴏᴄʜᴀᴛ 𝐀ɴᴅ 𝐌ᴏᴠᴇs 𝐓ᴏ 𝐓ʜᴇ 𝐍ᴇxᴛ 𝐒ᴛʀᴇᴀᴍ.",
            thumb_url="https://graph.org/file/1f05ea59a08727a9ea01e.jpg",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="𝐄ɴᴅ",
            description="𝐄ɴᴅ 𝐓ʜᴇ 𝐂ᴜʀʀᴇɴᴛ 𝐏ʟᴀʏɪɴɢ 𝐒ᴛʀᴇᴀᴍ 𝐎ɴ 𝐕ɪᴅᴇᴏᴄʜᴀᴛ.",
            thumb_url="https://graph.org/file/1f05ea59a08727a9ea01e.jpg",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="𝐒ʜᴜғғʟᴇ",
            description="𝐒ʜᴜғғʟᴇ 𝐓ʜᴇ 𝐐ᴜᴇᴜᴇᴅ 𝐒ᴏɴɢs 𝐈ɴ 𝐏ʟᴀʏʟɪsᴛ.",
            thumb_url="https://graph.org/file/1f05ea59a08727a9ea01e.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="𝐋ᴏᴏᴩ",
            description="𝐋ᴏᴏᴩ 𝐓ʜᴇ 𝐂ᴜʀʀᴇɴᴛ 𝐏ʟᴀʏɪɴɢ 𝐓ʀᴀᴄᴋ 𝐎ɴ 𝐕ɪᴅᴇᴏᴄʜᴀᴛ.",
            thumb_url="https://graph.org/file/1f05ea59a08727a9ea01e.jpg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)



import os
from pyexpat.errors import messages
import re

import yt_dlp
from pykeyboard import InlineKeyboard
from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaAudio,
                            InputMediaVideo, Message ,InputMediaPhoto)

from config import (BANNED_USERS, SONG_DOWNLOAD_DURATION,
                    SONG_DOWNLOAD_DURATION_LIMIT)
from strings import get_command
from LogiMusic import YouTube, app
from LogiMusic.utils.decorators.language import language, languageCB
from LogiMusic.utils.formatters import convert_bytes
from LogiMusic.utils.inline.song import song_markup

ABOUT_LOGI = get_command("ABOUT_LOGI")

@app.on_message(
    filters.command(ABOUT_LOGI)
    & filters.group
    & ~filters.edited
)
async def about_logi(client, message:Message):
    
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text= " 🦋 ᴍʏ ᴋɪɴɢ 🦋",
                    url=f"https://t.me/iMzaynKING",
                ),
            ]
        ]
    )
    await message.reply_text("👨‍💻**ᴀʙᴏᴜᴛ ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ :** \n🦋 ʜɪ ᴍʏ ɴᴀᴍᴇ ɪꜱ 🇰 🇮 🇳 🇬  \n🦋 ᴀʙᴏᴜᴛ ᴍᴇ - [KING](https://t.me/iMzaynKING) \n🦋 ᴍʏ ᴄʜᴀɴɴᴇʟꜱ \n\n ❤️ [KING BIOz](https://t.me/KING_BIOz) \n💙 [GROUP](https://t.me/TAMIL_CHATBOX)\n💜 [PRIVATE PARTY](https://t.me/PRIVATE_PARTY)\nᴛʜᴀɴᴋꜱ ꜰᴏʀ ʀᴇᴀᴅ ɪᴛ ❤ ", reply_markup=upl)
    await InputMediaPhoto.media("https://te.legra.ph/file/fc96390beb168c19b1788.jpg")
    




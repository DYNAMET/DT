import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app
from config import BANNED_USERS, MUSIC_BOT_NAME

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

BOT_USERNAME = getenv("BOT_USERNAME")


@app.on_message(
    command(["سورس ديمو","سورس","السورس","يا سورس"])
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_video(
        video=f"https://t.me/SYYYYP/192",
        caption=f"""**╭── • [⌯ ѕᴏᴜʀᴄᴇ ᴅʏɴᴍᴇᴛ⌯](https://t.me/SYYYYP) • ──╮**

**[⌯𝗗𝗘𝗩⌯](https://t.me/DYNMET)**

**[⌯𝗦𝗨𝗣𝗣𝗨𝗥𝗧⌯](https://t.me/AC_XR)**

**[⌯𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ⌯](https://t.me/SYYYYP)**

**╰── • [⌯ѕᴏᴜʀᴄᴇ ᴅʏɴᴍᴇᴛ⌯](https://t.me/SYYYYP) • ──╯**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "صانع ميوزك مجانا ◍", url=f"https://t.me/MAKER_MUSIC_ELNGOOM_BOT"), 
                ],[
                    InlineKeyboardButton(
                        "𝗗𝗘𝗩 𝐃𝐄𝐍𝐌𝐄𝐓 ◍", url=f"https://t.me/DYNMET"),
                ],[
                    InlineKeyboardButton(
                        "أضغط لاضافه ألبوت لمجموعتك ◍", url=f"https://t.me/FVVVVBOT?startgroup=true"),
                ],

            ]

        ),

    )
    
    
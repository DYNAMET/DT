import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from typing import Union
from YukkiMusic import app

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

BOT_USERNAME = getenv("BOT_USERNAME")

OWNER = getenv("OWNER")

NAME_BOT = getenv("NAME_BOT")



@app.on_message(
    command(["بوت"])
    & ~filters.edited
)
async def madison(client: Client, message: Message):
    async for photo in client.iter_profile_photos(BOT_USERNAME, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"اسمي {NAME_BOT} يا قمر 💗 ˣ", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• مطور البوت 🤖", url=f"https://t.me/{OWNER}")
                ],[
                    InlineKeyboardButton(
                       "• اضف البوت الي مجموعتك ✅", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
                ],
            ]
        ),
    )
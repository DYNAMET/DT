import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from aiohttp import ClientSession
import re
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from traceback import format_exc
from YukkiMusic import app
from typing import Union
from pyrogram.types import *


@app.on_message(
     command(["سيمو","احمد","مبرمج"])
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/4323873295f4dc1668a68.jpg",
caption=f"""**ꔷѕᴏᴜʀᴄᴇ ᴅʏɴᴍᴇᴛ**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(
                    "تواصل ◍", url=f"https://t.me/ac_xr"
                ),
                ],
                [
                    InlineKeyboardButton(
                        " ᴅʏɴᴍᴇᴛ ◍", url=f"https://t.me/dynmet"),
                ],
            ]
        ),
    )
    
@app.on_message(command(["الاوامر"])
    & filters.group
    & ~filters.edited
)
@app.on_message(command(["الاوامر"])
    & filters.channel
    & ~filters.edited
)
async def ahmad(client: Client, message: Message): 
  await message.reply_photo(
    photo="https://telegra.ph/file/4323873295f4dc1668a68.jpg",
    caption=f"""**ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ѕᴏᴜʀᴄᴇ ᴅʏɴᴍᴇᴛ◍**
    
🎵 | اوامر الموسيقي ⇊
⩹⌯⊷★父⸢ᴅʏɴᴍᴇᴛ⸥父★⊶⌯⩺
▶️╖ تشغيل «» ريلاي علي اغنيه او فديو
🎶╢ تشغيل + اسم الاغنيه
📹╢ تشغيل فديو + اسم الفديو
🔴╢ تشغيل + لينك بث مباشر
💢╢ ايقاف
💫╢ تخطي
😵╢ كتم
👷‍♂️╢ تحميل + اسم الاغنيه
💥╢ سورس «» سيمو
👮╜ ايدي «» احصا
⩹⌯⊷★父⸢ᴅʏɴᴍᴇᴛ⸥父★⊶⌯⩺
💎 « المطور الاساسي » ⇊
⩹⌯⊷★父⸢ᴅʏɴᴍᴇᴛ⸥父★⊶⌯⩺
⚡╖ حظر «» ريلاي علي الشخص
🐾╢ فك «» ريلاي علي الشخص
💎╢ عام «» ريلاي علي الشخص
✨╢ الغلي «» ريلاي علي الشخص
🗣️╢ رفع «» ريلاي علي الشخص
👥╢ تنزيل «» ريلاي علي الشخص
🌀╢ العام
🐣╢ الادمنيه
🚧╢ ذيع «» ريلاي علي الكلمه
🗽╜ ذيع بالمساعد «» ريلاي علي الكلمه
⩹⌯⊷★父⸢ᴅʏɴᴍᴇᴛ⸥父★⊶⌯⩺""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(f"قناة السورس  ◍", url=f"https://t.me/SYYYYP"),
                ],[
                InlineKeyboardButton(f"◍ اضفني الي قناتك", url=f"https://t.me/fvvvvbot?startchannel=true"),
                ],[
                InlineKeyboardButton("◍ أضفني الى مجموعتك", url=f"https://t.me/fvvvvbot?startgroup=true"),
                ]
            ]
        ),
    )

@app.on_message(command(["قول"])
    & filters.group
    & ~filters.channel
    & ~filters.edited
)
def echo(client, msg):
    text = msg.text.split(None, 1)[1]
    msg.reply(text)
    
@app.on_message(command(["ترجمة","/tr"]))
async def tr(_, message):
    trl = Translator()
    if message.reply_to_message and (message.reply_to_message.text or message.reply_to_message.caption):
        if len(message.text.split()) == 1:
            target_lang = "ar"
        else:
            target_lang = message.text.split()[1]
        if message.reply_to_message.text:
            text = message.reply_to_message.text
        else:
            text = message.reply_to_message.caption
    else:
        if len(message.text.split()) <= 2:
            return await message.reply_text("أرسل الامر على هذا الشكل :\n[Available options](https://telegra.ph/Lang-Codes-02-22).\n<b>Usage:</b> <code>/tr ar</code>",disable_web_page_preview=True)
        target_lang = message.text.split(None, 2)[1]
        text = message.text.split(None, 2)[2]
    detectlang = await trl.detect(text)
    try:
        data = requests.get(f"https://api.safone.tech/translate?text={text}&target={target_lang}").json()
        tekstr = await trl(text, targetlang=target_lang)
    except ValueError as err:
        return await message.reply_text(f"Error: <code>{str(err)}</code>")
    return await message.reply_text(f"<b>Translated:</b> from {data['origin']} to {data['target']} \n<code>{data['translated']}</code>")

def ReplyCheck(message: Message):
    reply_id = None
    if message.reply_to_message:
        reply_id = message.reply_to_message.message_id
    elif not message.from_user.is_self:
        reply_id = message.message_id
    return reply_id


session = ClientSession()
pattern = re.compile(r"^text/|json$|yaml$|xml$|toml$|x-sh$|x-shellscript$")
BASE = "https://batbin.me/"

async def post(url: str, *args, **kwargs):
    async with session.post(url, *args, **kwargs) as resp:
        try:
            data = await resp.json()
        except Exception:
            data = await resp.text()
    return data

async def paste(content: str):
    resp = await post(f"{BASE}api/v2/paste", data=content)
    if not resp["success"]:
        return
    return BASE + resp["message"]


@app.on_message(command(["طباعة","/pr"]))
async def paste_func(_, message: Message):
    if not message.reply_to_message:
        return await message.reply_text("الرد على رسالة ب  `/pr`")
    r = message.reply_to_message
    if not r.text and not r.document:
        return await message.reply_text("يتم دعم النصوص والمستندات فقط ")
    m = await message.reply_text("لصق ...")
    if r.text:
        content = str(r.text)
    elif r.document:
        if r.document.file_size > 40000:
            return await m.edit("يمكنك فقط لصق ملفات أصغر من 40 كيلوبايت .")
        if not pattern.search(r.document.mime_type):
            return await m.edit("يمكن لصق الملفات النصية فقط .")
        doc = await message.reply_to_message.download()
        async with aiofiles.open(doc, mode="r") as f:
            content = await f.read()
        os.remove(doc)
    link = await paste(content)
    kb = [[InlineKeyboardButton(text="رابط اللصق", url=link)]]
    try:
        if m.from_user.is_bot:
            await message.reply_photo(photo=link,quote=False,caption="تم نسخ النص",reply_markup=InlineKeyboardMarkup(kb),)
        else:
            await message.reply_photo(photo=link,quote=False,caption="تم نسخ النص",reply_markup=InlineKeyboardMarkup(kb),)
        await m.delete()
    except Exception:
        await m.edit("فتح الرابط", reply_markup=InlineKeyboardMarkup(kb))

        
@app.on_message(filters.voice_chat_started)
async def brah(client, message):
       await message.reply("تم بدا محادثة صواتية جديدة.")
       
@app.on_message(filters.voice_chat_ended)
async def brah2(client, message):
       await message.reply("تم انهاء المحادثه الصواتيه.")
       
@app.on_message(filters.voice_chat_members_invited)
async def fuckoff(client, message):
           text = f"قام : {message.from_user.mention}\nبدعوة : "
           x = 0
           for user in message.voice_chat_members_invited.users:
             try:
               text += f"{user.mention} "
               x += 1
             except Exception:
               pass
           try:
             await message.reply(f"{text} .")
           except:
             pass
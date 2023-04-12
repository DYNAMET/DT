from config import LOG, LOG_GROUP_ID
from YukkiMusic import app
from YukkiMusic.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "Private Group"
        if message.from_user:
            useri = message.from_user.id
            users = f"@{message.from_user.username}"
            user = message.from_user.mention
        else:
            useri = "Channel Player"
            users = "Channel Player"
            user = "Channel Player"
        logger_text = f"""
**تـم طـلـب اغـنـيـة جـديـدة مـن الـبـوت : 🤖**

**الجروب:** {message.chat.title} [`{message.chat.id}`]
**اسم الطالب:** {user}
**معرف المستخدم:** {users}
**ايدي المستخدم:** {useri}
**لنك الجروب:** {chatusername}

**طريقه البحث:** {message.text}

**تم تشغيل من:** {streamtype}"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
            except:
                pass
        return

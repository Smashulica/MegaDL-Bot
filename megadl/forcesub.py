# (c) Asm Safone
# A Part of MegaDL-Bot <https://github.com/AsmSafone/MegaDL-Bot>

import asyncio
from config import Config
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


async def handle_force_subscribe(bot, message):
    try:
        invite_link = await bot.create_chat_invite_link(int(Config.UPDATES_CHANNEL))
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return 400
    try:
        user = await bot.get_chat_member(int(Config.UPDATES_CHANNEL), message.from_user.id)
        if user.status == "kicked":
            await bot.send_message(
                chat_id=message.from_user.id,
                text="🖕🏻 Sugi pula, ai luat BAN ! 🤬 Scoatel singur [UNBAN](https://www.thisworldthesedays.com/ai-luat-ban.html).",
                parse_mode="markdown",
                disable_web_page_preview=True,
                reply_to_message_id=message.message_id,
            )
            return 400
    except UserNotParticipant:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="**Intra pe @OTRofficial ca sa ma poti utiliza!**\n\nDin cauza limitari de utilizatori, Doar cine este intrat pe canal ma poate utiliza!",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Join 🇦🇱 🏴‍☠️ 🅞🅣🅡 ᴏғғɪᴄɪᴀʟ 🏴‍☠️ 🇦🇱 🇹🇩", url=invite_link.invite_link)
                    ],
                    [
                        InlineKeyboardButton("🔄 Refresh 🔄", callback_data="refreshmeh")
                    ]
                ]
            ),
            parse_mode="markdown",
            reply_to_message_id=message.message_id,
        )
        return 400
    except Exception:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Ceva nu e bine. Contact My [Developer](https://t.me/iarbadevanzare).",
            parse_mode="markdown",
            disable_web_page_preview=True,
            reply_to_message_id=message.message_id,
        )
        return 400

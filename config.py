# (c) Asm Safone
# A Part of MegaDL-Bot <https://github.com/AsmSafone/MegaDL-Bot>


import os

class Config:
    API_ID = int(os.environ.get("API_ID", 123))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    TG_MAX_SIZE = 2040108421
    OWNER_ID = int(os.environ.get("OWNER_ID", 828779943))
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)


class TEXT:
  ABOUT = """
🤖 **Nume:** {bot_name}

📝 **Am fost programat in:** [Python](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Sunt Hostat pe:** [Heroku](https://heroku.com)

🧑‍💻 **Developer:** [Safone](https://t.me/iarbadevanzare)

👥 **Grup Support:** [SafoTheBot](https://t.me/otrofficial)

📢 **Canalele noastre si boti:** [🇦🇱 🏴‍☠️ 🅞🅣🅡 ᴏғғɪᴄɪᴀʟ 🏴‍☠️ 🇦🇱 🇹🇩](https://t.me/OTRportal)
"""

  HELP_USER = """
Eu sunt **{bot_name}**\n\nAcest bot poate descarca fisiere & video de pe linkurile Mega si sa le incarce pe Telegram.\nDoar trimite un link Mega.nz (nu folder) si asteapta sa vezi magia🔮\n\n**Poti oricand sa adaugi sau sa modifici un text:** doar alege un tip de fisier sau video deja trimis de mine dupa care poti face forward la un **telegraph cu textul dorit** ca raspuns la acesta si el va aparea sub video 😁!\n**Made With 💪🏻 By @OTRportal! 🔥**
"""

  START_TEXT = """
👋🏻 **Salut/Buna** {user_mention},\n\nEu sunt **{bot_name}**\n**Pot descarca fisiere & video de pe Mega.nz** & le pot incarca la tine pe Telegram.\n**Te rog sa apesi pe AJUTOR** pentru a putea afla mai multe 😉!\n\n**BOT Owner: {bot_owner}**🍁!
"""

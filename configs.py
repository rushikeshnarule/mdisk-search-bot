# (c) @KGN_OFFICIAL

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 4565499))
    API_HASH = os.environ.get("API_HASH", "3d5392714ba6ea6ed61b70d8d61cf4ec")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5338812482:AAFp5QMLor9bhV4Cadh2h5KHuH74wSgwwTY")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MdiskSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "BQArEd_Iv08hsWIin_XisuI-d7ej0RJUHbpDI8ZVfiJSDUZZLKI_zMkNcplKjGf7ha1Jz837vKc6UW_-IGgE5YN7udquxxKEX6Wh4MrGlTDluh-Cpp3QsXHjipwMR5iK7yj_U72TLvF5uiAghzpjQUjMzCs_vfuHs_WqZS5ObEZJdIDNF484JUgKlkenwGuDRerddRhRIG0OjoCbqlVJFoahOS-UhW62kfdnCAIQhjQEcWfm0JMSjDSUVKW1mk7E_6ZOoWUSA1oGMXm-ontHJHr_s7nthfUwsNTBRczv1hnzA139V-Az2syPRc2jVUPlXGkzmCnyaXUBd50hZhNMz65TbqeyAQA")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -1001741439328))
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b>This is Mdisk Search Bot.

🤖 My Name: <a href='https://t.me/DTG_BOTS'>Mdisk Search Robot</a>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

📡 Server: <a href='https://heroku.com'>Heroku</a>

👨‍💻 Created By: <a href='https://t.me/DTG_TV'>DTG TV</a></b>
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 Developer : <a href='https://t.me/DTG_Admin_bot'>DTG TV</a>

If You Want Your Own Bot Like This Then You Can Contact Our Developer.</b>
"""

    HOME_TEXT = """
<b>Hey! {}😅,

I'm Mdisk Search Robot.🤖</a>

I Can Search!🔍 What You Want?😜

<a>Deploy ❤ By @DTG_TV</a></b>
"""


    START_MSG = """
<b>Hey! {}😅,

I'm Mdisk Search Robot.🤖</a>

I Can Search!🔍 What You Want?😜

<a>Deploy ❤ By @DTG_TV</a></b>
"""



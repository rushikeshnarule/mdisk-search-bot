import os
Fromm configs.py import  BOT_USERNAME

class temp(object):
    BANNED_USERS = []
    BANNED_CHATS = []
    ME = None
    CURRENT=int(os.environ.get("SKIP", 2))
    CANCEL = False
    MELCOW = {}
    U_NAME = config.py(BOT_USERNAME)
    B_NAME = None
    SETTINGS = {}

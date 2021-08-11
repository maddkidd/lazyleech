from lazyleech import BOT_USERNAME
import os

class Config(object):
    DB_URL = os.environ.get("DB_URL", "xxxxxxxxxxxx")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1938468087:AAEAi5DMnn_Tc6xYmNS5qguFuMEAadEFQkU")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@lazyleechsk_bot")
    EVERYONE_CHATS = os.environ.get("EVERYONE_CHATS", "-1001550345714")
    API_ID = int(os.environ.get("API_ID", 2469592))
    API_HASH = os.environ.get("API_HASH", "c62df1c04a516765f468f86e30c6680a")
    LICHER_CHAT = os.environ.get("LICHER_CHAT", "-1001550345714")
    ADMIN_CHATS = os.environ.get('ADMIN_CHATS', "-1001550345714")

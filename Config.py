import os


class Config():
# LEXPER VE RAHMET TARAFINDAN BAŞTAN AŞŞAĞIYA DÜZELTİLİRMİŞTİR!

    API_ID = int(os.environ.get("API_ID", "25114508"))
    API_HASH = os.environ.get("API_HASH", "993ccdfe81548dade420e81bcd6807ce")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6004868881:AAFsyDIoYHhpyDI6kUC9ZPLoiVU393Rjorc")
    BOT_USERNAME = os.environ.get("BOT_USERNAME" , "denizinkizitag_bot")
    BOT_NAME = os.environ.get("BOT_NAME" , "Denizin Kızı Tagger")
    BOT_ID = int(os.environ.get("BOT_ID" , "6004868881"))
    SUDO_USERS = os.environ.get("SUDO_USERS" , "6481578614").split()
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT" , "sohbetsirius")
    OWNER_ID = int(os.environ.get("OWNER_ID" , "6481578614"))
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME" , "deniziinkizi")

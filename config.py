import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    API_HASH = os.environ.get("API_HASH" , "92315b2cb9d11132dbb9d12d6fd3c0d4")
    BOT_TOKEN = os.environ.get("BOT_TOKEN" , "6796815952:AAEwoy1MgxYFiwOah8qhL8XHt0KLr2StjG8")
    TELEGRAM_API = os.environ("TELEGRAM_API" , "21993419")
    OWNER = os.environ.get("OWNER" , "6500361116")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME" , "master_champ")
    PASSWORD = os.environ.get("PASSWORD" , "vik")
    DATABASE_URL = os.environ.get("DATABASE_URL" , "mongodb+srv://surya2519990:feQJjOemwKKsIBti@cluster0.atjrk5v.mongodb.net/?retryWrites=true&w=majority")
    LOGCHANNEL = os.environ.get("LOGCHANNEL" , "-1002042816119")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]

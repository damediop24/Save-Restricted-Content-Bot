
from os import getenv

API_ID = int(getenv("API_ID", "24363932"))
API_HASH = getenv("API_HASH", "d84176e864496c3cd2542c1a0de42c4a")
BOT_TOKEN = getenv("BOT_TOKEN", "7920155198:AAEWhAaW3sNMfIZzILwjCYRMIifjRK3yqVQ")
OWNER_ID = list(map(int, getenv("OWNER_ID", "8086008476").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://damealorica:damealorica@saverbot.znrlqwc.mongodb.net/?retryWrites=true&w=majority&appName=SaverBot")
LOG_GROUP = getenv("LOG_GROUP", "-1002553314227")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002842488275"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "100000"))
WEBSITE_URL = getenv("WEBSITE_URL", "")
AD_API = getenv("AD_API", "")
STRING = getenv("STRING", "")
YT_COOKIES = getenv("YT_COOKIES", "")
INSTA_COOKIES = getenv("INSTA_COOKIES", "")

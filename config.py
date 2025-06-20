
from os import getenv

API_ID = int(getenv("API_ID", "24856774"))
API_HASH = getenv("API_HASH", "c67513889c9d838ed41bf12155bc8bf3")
BOT_TOKEN = getenv("BOT_TOKEN", "7542850907:AAELDDb7hV9D3SfLtlz5GE1CSL_LeGcRybk")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5118708665").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://damealorica:moitiere2A@saverbot.znrlqwc.mongodb.net/?retryWrites=true&w=majority&appName=SaverBot")
LOG_GROUP = getenv("LOG_GROUP", "-1002842488275")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002842488275"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "100000"))
WEBSITE_URL = getenv("WEBSITE_URL", "")
AD_API = getenv("AD_API", "")
STRING = getenv("STRING", "")
YT_COOKIES = getenv("YT_COOKIES", "")
INSTA_COOKIES = getenv("INSTA_COOKIES", "")

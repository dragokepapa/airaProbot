import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# ==========================
# HIDDEN VARIABLES (ENV)
# ==========================

API_ID = int(getenv("API_ID", 0))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")
BOT_ID = int(getenv("BOT_ID", 0))

BOT_USERNAME = getenv("BOT_USERNAME")
OWNER_USERNAME = getenv("OWNER_USERNAME")

BOT_NAME = getenv("BOT_NAME")
ASSUSERNAME = getenv("ASSUSERNAME")

MONGO_DB_URI = getenv("MONGO_DB_URI")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT_MIN", 60))

LOGGER_ID = int(getenv("LOGGER_ID", 0))
DISASTER_LOG = int(getenv("DISASTER_LOG", 0))

OWNER_ID = int(getenv("OWNER_ID", 0))
SPECIAL_USER = int(getenv("SPECIAL_USER", 0))

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# ==========================
# ✅ ONLY VISIBLE VALUE
# ==========================

UPSTREAM_REPO = "https://github.com/slayer123700/zenitsu-music-main"
UPSTREAM_BRANCH = "master"

# ==========================
# HIDDEN AGAIN
# ==========================

GIT_TOKEN = getenv("GIT_TOKEN")

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL")
SUPPORT_CHAT = getenv("SUPPORT_CHAT")

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET")

STRING1 = getenv("STRING1")
STRING2 = getenv("STRING2")
STRING3 = getenv("STRING3")
STRING4 = getenv("STRING4")
STRING5 = getenv("STRING5")
STRING6 = getenv("STRING6")
STRING7 = getenv("STRING7")

# ==========================
# OTHER SETTINGS
# ==========================

AUTO_LEAVING_ASSISTANT = False
AUTO_LEAVE_ASSISTANT_TIME = 9000

PLAYLIST_FETCH_LIMIT = 25

TG_AUDIO_FILESIZE_LIMIT = 2147483648
TG_VIDEO_FILESIZE_LIMIT = 2147483648

SONG_DOWNLOAD_DURATION = 9999999
SONG_DOWNLOAD_DURATION_LIMIT = 9999999

filter = filters.user()
BANNED_USERS = filter

adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ==========================
# IMAGES (ENV SAFE)
# ==========================

START_IMG_URL = getenv("START_IMG_URL")
PLAYLIST_IMG_URL = getenv("PLAYLIST_IMG_URL")
STATS_IMG_URL = getenv("STATS_IMG_URL")
TELEGRAM_AUDIO_URL = getenv("TELEGRAM_AUDIO_URL")
TELEGRAM_VIDEO_URL = getenv("TELEGRAM_VIDEO_URL")
STREAM_IMG_URL = getenv("STREAM_IMG_URL")
SOUNCLOUD_IMG_URL = getenv("SOUNCLOUD_IMG_URL")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL")
SPOTIFY_ARTIST_IMG_URL = getenv("SPOTIFY_ARTIST_IMG_URL")
SPOTIFY_ALBUM_IMG_URL = getenv("SPOTIFY_ALBUM_IMG_URL")
SPOTIFY_PLAYLIST_IMG_URL = getenv("SPOTIFY_PLAYLIST_IMG_URL")

# ==========================
# FUNCTIONS
# ==========================

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# ==========================
# VALIDATION
# ==========================

if SUPPORT_CHANNEL and not re.match("(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] SUPPORT_CHANNEL must start with https://")

if SUPPORT_CHAT and not re.match("(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] SUPPORT_CHAT must start with https://")
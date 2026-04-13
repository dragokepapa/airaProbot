import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters
load_dotenv()


API_ID = 25955854

API_HASH = "2ede59823a90cb31442a74f5ae01f675"

BOT_TOKEN = "8287492525:AAHgkD4zbbRk_4937966-WVObyrmIqVPnuw"

BOT_ID = 8287492525

BOT_USERNAME = "rion_xbot"

OWNER_USERNAME = "SLAYER1237"

BOT_NAME = "Shigaraki"

ASSUSERNAME = "DEATH_WISH"


MONGO_DB_URI = "mongodb+srv://shigarakisan:demnkin@cluster0.cxt4iov.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DURATION_LIMIT_MIN = 500000

LOGGER_ID = -1003791371177

DISASTER_LOG = -1003791371177

OWNER_ID = 6018803920

SPECIAL_USER = 7933208850

HEROKU_APP_NAME = None

HEROKU_API_KEY = None

UPSTREAM_REPO = "https://github.com/slayer123700/zenitsu-music-main"

UPSTREAM_BRANCH = "master"

GIT_TOKEN = ""


SUPPORT_CHANNEL = "https://t.me/MBT_UPDATES"

SUPPORT_CHAT = "https://t.me/+Fy_y61SmobdkYWRl"

AUTO_LEAVING_ASSISTANT = False
AUTO_LEAVE_ASSISTANT_TIME = 9000


SPOTIFY_CLIENT_ID = "22b6125bfe224587b722d6815002db2b"

SPOTIFY_CLIENT_SECRET = "c9c63c6fbf2f467c8bc68624851e9773"

PLAYLIST_FETCH_LIMIT = 25

TG_AUDIO_FILESIZE_LIMIT = 2147483648
TG_VIDEO_FILESIZE_LIMIT = 2147483648

SONG_DOWNLOAD_DURATION = 9999999
SONG_DOWNLOAD_DURATION_LIMIT = 9999999

TG_AUDIO_FILESIZE_LIMIT = 2147483648
TG_VIDEO_FILESIZE_LIMIT = 2147483648

STRING1 = "BQJZsZ4Ad1EkXlwucmeoqqcpgB0gr3xK1yMMNnAWxQYZ8Hgd18hHEhzpz-etWfSEVMrR_tSOK3_l5IjvB9Elv_gWc-lcpnRFG109XCE_nLRcOX0w343DuK9Q2cCw1FVfgBwyHuip0iRBM9tzpFj5WciIjvGnpAEhnQ3LieLm9YzOHFU3tLzkBx3Sy08BYLAt3EUWRP3vQL5wN5Vqz-QX4lxx9wHGYHjzxtvL92vhQpoiyKffGoTHYqaCV3jh3tUePMuYVA3int6FIClXFYvM0ch1LaEQ7ixAwpoSVFskmqg6ckwioyVJJ8ZKerzQQ766B4HgKF89mbrBCW6bU7u3LXQWx9VvIAAAAAHqaaalAA"
STRING2 = None 
STRING3 = None 
STRING4 = None
STRING5 = None
STRING6 = None
STRING7 = None


filter = filters.user()
BANNED_USERS = filter
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

START_IMG_URL =  "https://files.catbox.moe/iffmnv.jpg"
PLAYLIST_IMG_URL = "https://files.catbox.moe/bggrlh.jpg"
STATS_IMG_URL = "https://files.catbox.moe/iffmnv.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/f3yuiy.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/urv7wi.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/6khxhw.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/2tcim5.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/bggrlh.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/iffmnv.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/6khxhw.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/jkqyg2.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )

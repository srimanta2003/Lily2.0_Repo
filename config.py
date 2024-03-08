import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH") 

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Get Your bot username
BOT_USERNAME = getenv("BOT_USERNAME" , "")

# Don't Add style font 
BOT_NAME = getenv("BOT_NAME" , "")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 900000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", None))

# Get this value from @BRANDRD_ROBOT on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 6680361392))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Venom-X-Bots/SuperFast-New-Music",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/thecchub")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+eOndzGjht5FhNGY1")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False)) 


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "d42345c23b204f05a8495809545a640b")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "01f2f6b75c004ef0a0d1c73139ec97d2")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/ba0d1cd6fa6dc871b45a7.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/4a72c60cab00853718087.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/89e1c3a393e7115ab76ff.jpg"
STATS_IMG_URL = "https://graph.org/file/89e1c3a393e7115ab76ff.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/a52584b57a0dd44f62c8f.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/a52584b57a0dd44f62c8f.jpg"
STREAM_IMG_URL = "https://graph.org/file/89e1c3a393e7115ab76ff.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/2a0840ee7b5ef1c0ed511.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/f2d8de51c5a313f82359e.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/4b11c10cf7c7bdf1b5fe5.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/4b11c10cf7c7bdf1b5fe5.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/4b11c10cf7c7bdf1b5fe5.jpg"


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

from LilyXMusic.core.bot import Anony
from LilyXMusic.core.dir import dirr
from LilyXMusic.core.git import git
from LilyXMusic.core.userbot import Userbot
from LilyXMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

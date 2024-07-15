from sarahxmusic.core.bot import SARAH
from sarahxmusic.core.dir import dirr
from sarahxmusic.core.git import git
from sarahxmusic.core.userbot import Userbot
from sarahxmusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = SARAH()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

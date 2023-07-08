from dataclasses import dataclass
from environs import Env
import simplematrixbotlib as botlib
from .handlers import setup

env = Env()
env.read_env()

USERNAME = env('USERNAME')
PASSWORD = env('PASSWORD')
SERVER = env('SERVER')


@dataclass
class MyConfig(botlib.Config):
    _admin_id: str = 'unknown'
    _lang: str = 'en'

    @property
    def admin_id(self) -> str:
        return self._admin_id

    @admin_id.setter
    def admin_id(self, value: str) -> None:
        self._admin_id = value


config = MyConfig()
config.load_toml('config.toml')
config.encryption_enabled = True
config.emoji_verify = True
config.ignore_unverified_devices = True
config.store_path = './crypto_store/'

creds = botlib.Creds(SERVER, USERNAME, PASSWORD)
bot = botlib.Bot(creds, config)
PREFIX = '!'

setup(bot, prefix=PREFIX)
bot.run()

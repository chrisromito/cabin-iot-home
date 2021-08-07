import os
from dotenv import load_dotenv, find_dotenv
import pathlib


load_dotenv(find_dotenv())

THIS_DIR = pathlib.Path(__file__).parent.absolute()
MEDIA_PATH = os.path.join(THIS_DIR, 'media')
DOORBELL_AUDIO_PATH = os.path.join(MEDIA_PATH, 'doorbell.wav')

debug = os.getenv('DEBUG', False)
DEBUG = debug == 'true' or debug == 'True'

# DB Settings
########################
SQLITE_FILE_NAME = os.getenv('SQLITE_FILE_NAME', 'sqlite.db')
DB_PATH = os.path.join(
    pathlib.Path(THIS_DIR).parent.absolute(),
    'db',
    SQLITE_FILE_NAME
)


class Settings:
    DB_PATH = DB_PATH
    DOORBELL_AUDIO_PATH = DOORBELL_AUDIO_PATH

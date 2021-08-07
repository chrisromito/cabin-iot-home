import os
from dotenv import load_dotenv, find_dotenv
import pathlib

load_dotenv(find_dotenv())

THIS_DIR = pathlib.Path(__file__).parent.absolute()
UPLOAD_FOLDER = os.path.join(THIS_DIR, 'media')
STATIC_PATH = os.path.join(THIS_DIR, 'static')
TEMPLATE_PATH = os.path.join(THIS_DIR, 'templates', 'base.html')

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

# MQTT
########################
BROKER_HOST = os.getenv('BROKER_HOST')
BROKER_PORT = int(os.getenv('BROKER_PORT'))


# Web Server Settings
########################
class WebServer:
    STATIC_URL = '/static'
    STATIC_PATH = STATIC_PATH
    HOST = os.getenv('SERVER_HOST', '0.0.0.0')
    PORT = os.getenv('SERVER_PORT', '5000')
    WORKERS = 4
    DEBUG = DEBUG
    ACCESS_LOG = DEBUG


class Settings(WebServer):
    DB_PATH = DB_PATH
    SECRET_KEY = os.getenv('SECRET_KEY', None)
    BROKER_HOST = BROKER_HOST
    BROKER_PORT = BROKER_PORT
    TEMPLATE_PATH = TEMPLATE_PATH

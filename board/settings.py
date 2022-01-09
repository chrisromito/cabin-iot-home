import os
import pathlib


THIS_DIR = pathlib.Path(__file__).parent.absolute()
MEDIA_PATH = os.path.join(THIS_DIR, 'media')
DOORBELL_AUDIO_PATH = os.path.join(MEDIA_PATH, 'doorbell.wav')
DEBUG = False
MQTT_HOST = '192.168.0.194'


class Settings:
    DOORBELL_AUDIO_PATH = DOORBELL_AUDIO_PATH
    MQTT_HOST = MQTT_HOST
    DEBUG = DEBUG


def debug(message: str):
    if DEBUG:
        print(message)



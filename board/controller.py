from pydub import AudioSegment
from datetime import datetime
from pydub.playback import play
from asyncio import sleep

from shared import Component, State
from settings import DOORBELL_AUDIO_PATH
from db.queries import resident_is_home


SLEEP_SECONDS = 5


async def handle_button_press(state: State, component: Component):
    state.update({'last_pressed': datetime.now()})
    is_home = resident_is_home()
    led = component.green_led if is_home else component.red_led
    led.on()
    if is_home:
        try:
            play_doorbell_audio()
        except Exception as err:
            print('Caught exception trying to play doorbell audio')
            print(err)
            raise err
    else:
        await sleep(SLEEP_SECONDS)
    led.off()


def play_doorbell_audio():
    print('Playing audio...')
    play(
        AudioSegment.from_file(DOORBELL_AUDIO_PATH, format='wav')
    )

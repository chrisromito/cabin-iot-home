from gpiozero import Button
from signal import pause
from pydub.playback import play

from pin_config import BUTTON
from settings import DOORBELL_AUDIO_PATH


def play_doorbell_audio():
    write_component_status('button', {'pressed': True})
    play(
        AudioSegment.from_file(DOORBELL_AUDIO_PATH, format='wav')
    )
    write_component_status('button', {'pressed': False})


button = Button(BUTTON)
button.when_pressed = play_doorbell_audio
pause()

from asyncio import get_event_loop, sleep
from datetime import datetime

from gpiozero import Button, LED

from controller import handle_button_press, SLEEP_SECONDS
from pin_config import GREEN_LED, BUTTON, RED_LED
from shared import Component, State


def run():
    loop = get_event_loop()
    try:
        loop.run_until_complete(run_app())
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()


async def run_app():
    print('Starting cabin-iot-home board...')
    app = App()
    while True:
        try:
            await app.loop()
        except Exception as err:
            print('run_app() caught an error')
            raise err


class App:
    def __init__(self):
        self.components = Component(button=Button(BUTTON), red_led=LED(RED_LED), green_led=LED(GREEN_LED))
        self.state = State({'pressed': False, 'last_pressed': None})

    async def loop(self):
        was_pressed = self.state.value.get('pressed', False)
        pressed = self.components.button.is_pressed
        if pressed:
            print('button was pressed')
        if was_pressed != pressed:
            self.state.update({'pressed': pressed})
            if self.can_handle_button_press():
                print('Handling button press')
                await handle_button_press(self.state, self.components)
        await sleep(1 / 1000)

    def can_handle_button_press(self) -> bool:
        if not self.state.value.get('pressed'):
            return False
        last_pressed = self.state.value.get('last_pressed', None)
        return (
            True if last_pressed is None
            else (datetime.now() - last_pressed).total_seconds() > SLEEP_SECONDS
        )


if __name__ == '__main__':
    run()

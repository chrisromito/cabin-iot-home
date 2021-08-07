from typing import Dict

from gpiozero import Button, LED


class State:
    def __init__(self, initial_value=None):
        self.value: Dict = initial_value or {}

    def update(self, new_state: Dict) -> Dict:
        value = {**self.value, **new_state}
        self.value = value
        return value


class Component:
    def __init__(self, button: Button, red_led: LED, green_led: LED):
        self.button: Button = button
        self.red_led: LED = red_led
        self.green_led: LED = green_led

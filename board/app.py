from datetime import datetime
import paho.mqtt.client as mqtt
from pydub import AudioSegment
from pydub.playback import play
from settings import Settings, debug


def play_doorbell_audio():
    time_str = datetime.now().strftime("%c")
    print(f'Doorbell pressed: {time_str}')
    debug('Playing doorbell audio...')
    play(
        AudioSegment.from_file(Settings.DOORBELL_AUDIO_PATH, format='wav')
    )
    debug('Doorbell audio complete')


def on_connect(client, userdata, flags, rc):
    debug('on_connect()')
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe('doorbell')


def on_message(client, userdata, msg):
    # The callback for when a PUBLISH message is received from the server.
    topic: str = msg.topic
    body: bytes = msg.payload
    if 'doorbell' in topic:
        try:
            if int(body) == 1:
                play_doorbell_audio()
                # No matter what, set the value to '0'
                mqtt_client.publish('doorbell', '0')
        except ValueError:
            pass
    debug(f'on_message -> {msg.topic} {msg.payload}')


mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

mqtt_client.connect(Settings.MQTT_HOST, port=1883, keepalive=60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
mqtt_client.loop_forever()

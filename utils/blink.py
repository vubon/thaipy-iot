import time
from machine import Pin


def blink(n):
    """
    :description: This function perform when data is sending to server. It could be a local MQTT or Internet MQTT
    :functionality: Checking the number is interger then LED light on and Go sleep for 0.5 second and Trun off the LED light
    :params: n: integer
    :raise: No raise case
    :return: None
    :rtype: None
    """
    led = Pin(2, Pin.OUT)
    if type(n) is int:
        led.value(True)
        time.sleep(0.5)
        led.value(False)

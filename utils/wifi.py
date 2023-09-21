import network
import time


def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)

    if not wlan.isconnected():
        print("Connecting to Wi-Fi...")
        wlan.active(True)
        wlan.connect(ssid, password)

        while not wlan.isconnected():
            time.sleep(1)

    print("Connected to Wi-Fi")
    print("IP address:", wlan.ifconfig()[0])

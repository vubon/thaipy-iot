import dht
import machine


class DHT11Sensor:
    """
    DHT11 Sensor class
    """

    def __init__(self, pin):
        self.dht_pin = dht.DHT11(machine.Pin(pin))

    def read_temperature_humidity(self):
        """
        :description: A basic temperature collect function
        :functionality: Temperature, Humidity
        :params: None
        :raise: No raise case
        :return: {"temperature": 25, "humidity": 80}
        :rtype: dict

        """
        retry = 3
        for _ in range(retry):
            try:
                self.dht_pin.measure()
                return {"temperature": self.dht_pin.temperature(), "humidity": self.dht_pin.humidity()}
            except OSError as e:
                print("Can't read sensor data: ", e)
                print("Retrying....")
        return {"temperature": 0, "humidity": 0}

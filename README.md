# MicroPython DHT11 AWS IoT Project

This project showcases how to utilize MicroPython on an ESP32 to retrieve temperature and humidity data from a DHT11 sensor. The collected data is then published to AWS IoT Core using MQTT.

## Table of Contents

- [Features](#features)
- [Hardware Requirements](#hardware-requirements)
- [Software Requirements](#software-requirements)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Reads temperature and humidity from a DHT11 sensor using MicroPython.
- Publishes sensor data (temperature and humidity) to AWS IoT Core using MQTT.
- Subscribe IoT Topic
- Easy to configure and adapt for other IoT projects.

## Hardware Requirements

- ESP32 microcontroller (e.g., ESP32 DevKit V1)
- DHT11 temperature and humidity sensor
- Power supply
- Connecting wires

## Software Requirements

- MicroPython firmware flashed onto the ESP32 (You can get the file in BIN folder)
- AWS Account
- AWS IoT Core endpoint, device certificate, and private key

## Setup

1. Flash MicroPython firmware onto your ESP32. Refer to the official MicroPython documentation for instructions.

2. Configure your AWS IoT Core:
   - Create an AWS IoT Thing for your device.
   - Generate device certificates and keys for authentication.
   - Note down your AWS IoT endpoint.

3. Update the `config.py` file with your AWS IoT endpoint, certificates and Wi-Fi credentials.

4. Upload the required files (`aws_iot.py`, `dht11.py`, `blink.py`, `wifi.py`, `config.py`, `msg.py`,`main.py`) to your ESP32 using Thonny IDE.

## Usage

1. Connect the DHT11 sensor to the ESP32 based on the wiring specified in `dht11.py`.

2. Power on the ESP32.

3. The ESP32 will read temperature and humidity from the DHT11 sensor and publish the data to AWS IoT Core using MQTT.

4. Check the AWS IoT Core console to see the incoming sensor data.

## Contributing

Contributions are welcome! Fork the repository and submit a pull request to propose changes.

## License

This project is licensed under the [MIT License](LICENSE).

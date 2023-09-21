from umqtt.simple import MQTTClient


class AwsIoTClient:
    def __init__(self, endpoint, client_id, cert_path, key_path):
        self.endpoint = endpoint
        self.client_id = client_id
        self.cert_path = cert_path
        self.key_path = key_path
        self.client = None
        self.msg_handler = None

    def read_file(self, path):
        with open(path, 'r') as key:
            return key.read()

    def set_msg_handler(self, handler_func):
        self.msg_handler = handler_func

    def _on_message(self, topic, message):
        # Handle incoming message
        if self.msg_handler:
            self.msg_handler(topic, message)

    def initialize(self):
        self.client = MQTTClient(self.client_id, self.endpoint, port=8883,
                                 keepalive=120,
                                 ssl=True,
                                 ssl_params={
                                     "certfile": self.read_file(self.cert_path),
                                     "keyfile": self.read_file(self.key_path)
                                 }
                                 )
        self.client.set_callback(self._on_message)

    def connect(self):
        self.client.connect()

    def disconnect(self):
        self.client.disconnect()

    def publish(self, topic, payload):
        self.client.publish(topic.encode(), payload.encode())

    def subscribe(self, topic):
        self.client.subscribe(topic.encode())

    def check_for_messages(self):
        self.client.check_msg()

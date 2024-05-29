"""Mqtt subscriber implementation for specified settings"""
from paho.mqtt import client as mqtt_client
from mqtt.communication_settings import CommunicationSettings
from mqtt.configuration import Configuration
from gpiozero import OutputDevice

from utils.logger import Logger


class MqttSubscriber:
    """Mqtt subscriber implementation"""
    def __init__(self, yaml: dict):
        """
        @param: yaml parameter file as parsed dictionary
        """
        self.communication_settings = CommunicationSettings(yaml[CommunicationSettings.section_key()])
        self.configuration = Configuration(yaml[Configuration.section_key()])
        global output
        output = OutputDevice(self.configuration.output_pin)
        output.off()

    def connect_mqtt(self) -> mqtt_client:
        """Connect to mqtt client function"""
        client = mqtt_client.Client(
            self.get_subscriber_id(
                self.communication_settings.client_id,
                self.communication_settings.topic,
            ),
        )
        client.on_connect = self.on_connect
        client.connect(self.communication_settings.broker, self.communication_settings.port)
        return client

    def subscribe(self, client: mqtt_client):
        """
        Subscriber to mqtt_client
        @param: client: mqtt_client. Client to connect to.
        """
        client.subscribe(self.communication_settings.topic)
        client.on_message = self.on_message

    def run(self):
        """Run mqtt subscriber"""
        client = self.connect_mqtt()
        self.subscribe(client)
        Logger.get_logger().info('Mqtt subscriber initialized')
        client.loop_forever()

    @staticmethod
    def get_subscriber_id(client_id: int, topic: str) -> str:
        """Get specifically formatted client id"""
        return f"subscriber-{topic}-{client_id}"

    # pylint: disable=W0613
    @staticmethod
    def on_connect(client, userdata, flags, rc):
        """On connect event for mqtt subscriber"""
        if rc == 0:
            Logger.get_logger().info("Connected to MQTT Broker!")
        else:
            Logger.get_logger().info("Failed to connect, return code %d\n", rc)

    @staticmethod
    def on_message(client, userdata, msg):
        """On received message event function"""
        received = bool(msg.payload.decode())
        Logger.get_logger().info("Received %s from %s topic", msg.payload.decode(), msg.topic)
        
        if received:
            output.on()
        else:
            output.off()
"""Definition of communication settings for """


class CommunicationSettings:
    """Communication settings storing class"""
    def __init__(self, communication_settings: dict):
        self.broker = communication_settings[self.broker_key()]
        self.port = communication_settings[self.port_key()]
        self.topic = communication_settings[self.topic_key()]
        self.client_id = communication_settings[self.client_id_key()]

    @staticmethod
    def section_key():
        """Section key for communication"""
        return "communication"

    @staticmethod
    def broker_key():
        """Section key for broker"""
        return "broker"

    @staticmethod
    def port_key():
        """Section key for port"""
        return "port"

    @staticmethod
    def topic_key():
        """Section key for topic"""
        return "topic"

    @staticmethod
    def client_id_key():
        """Section key for client id"""
        return "clientId"

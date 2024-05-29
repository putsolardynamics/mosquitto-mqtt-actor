"""Definition of configuration of RPI"""


class Configuration:
    """Class for storing RPI configuration"""
    def __init__(self, configuration: dict) -> None:
        self.output_pin = configuration[self.pin_key()]

    @staticmethod
    def section_key():
        """Section key for communication"""
        return "configuration"

    @staticmethod
    def pin_key():
        """Section key for broker"""
        return "output_pin"

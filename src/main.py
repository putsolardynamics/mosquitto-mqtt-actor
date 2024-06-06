"""Main script"""
import argparse

from utils.yaml_parser import YamlParser
from mqtt.mqtt_subscriber import MqttSubscriber


def main(args):
    """Main executable script"""
    config = YamlParser.load_config(args.config)
    mqtt_subscriber = MqttSubscriber(config)
    mqtt_subscriber.run()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='ProgramName',
        description='What the program does',
        epilog='Text at the bottom of help')
    parser.add_argument('-c', '--config', action='store', default='../config.yaml')
    args_parsed = parser.parse_args()
    main(args_parsed)

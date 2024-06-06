"""Module providing helpers for simple functionalities not related to internal logic"""
from pathlib import Path
import yaml


class YamlParser:
    """Yaml parser for parsing yaml files"""
    @staticmethod
    def load_config(path: Path) -> dict:
        """
        :param path: path to config file
        :rtype: dictionary of parameters specified in yaml file
        """
        with open(path, 'r', encoding="utf-8") as file:
            config = yaml.safe_load(file)
        return config

    @staticmethod
    def get_section(yaml_parser: dict, section_name: str) -> dict:
        """
        :param yaml_parser: dictionary with yaml content parsed
        :param section_name: name of section to extract data from
        :rtype dict: dictionary of section values
        """
        return yaml_parser[section_name]

from camel_converter import dict_to_snake, dict_to_camel
from .logger import logging
import json


class SnakeToCamelConverter:
    @staticmethod
    def convert(data):
        try:
            if data:
                if isinstance(data, str):
                    return dict_to_camel(json.loads(data))
                return dict_to_camel(data)
        except Exception as e:
            logging.error(e)
            raise e


class CamelToSnakeConverter:
    @staticmethod
    def convert(data):
        try:
            if data:
                if isinstance(data, str):
                    return dict_to_snake(json.loads(data))
                return dict_to_snake(data)
        except Exception as e:
            logging.error(e)
            raise e

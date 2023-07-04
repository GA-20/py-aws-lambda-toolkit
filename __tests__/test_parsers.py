import unittest
from py_sls_lambda_toolkit.parsers import (
    convert_camel_to_snake,
    convert_snake_to_camel,
)


class TestParsers(unittest.TestCase):

    def test_convert_camel_to_snake(self):
        data = {
            "testKey": "testValue",
            "testKey2": "testValue2",
            "testKey3": "testValue3",
        }
        expected = {
            "test_key": "testValue",
            "test_key2": "testValue2",
            "test_key3": "testValue3",
        }
        self.assertEqual(convert_camel_to_snake(data), expected)

    def test_convert_snake_to_camel(self):
        data = {
            "test_key": "testValue",
            "test_key2": "testValue2",
            "test_key3": "testValue3",
        }
        expected = {
            "testKey": "testValue",
            "testKey2": "testValue2",
            "testKey3": "testValue3",
        }
        self.assertEqual(convert_snake_to_camel(data), expected)


if __name__ == '__main__':
    unittest.main()

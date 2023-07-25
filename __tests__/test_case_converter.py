import unittest
from py_aws_lambda_toolkit.case_converter import CaseConverter


class TestParsers(unittest.TestCase):
    case_converter = CaseConverter()

    def test_recursive_to_camel(self):
        data = {
            'test_key': 'test_value',
            'test_list': [
                {
                    'test_key': 'test_value'
                }
            ]
        }
        expected = {
            'testKey': 'test_value',
            'testList': [
                {
                    'testKey': 'test_value'
                }
            ]
        }
        actual = self.case_converter._recursive_to_camel(data)
        self.assertEqual(actual, expected)

    def test_recursive_to_snake(self):
        data = {
            'testKey': 'test_value',
            'testList': [
                {
                    'testKey': 'test_value'
                }
            ]
        }
        expected = {
            'test_key': 'test_value',
            'test_list': [
                {
                    'test_key': 'test_value'
                }
            ]
        }
        actual = self.case_converter._recursive_to_snake(data)
        self.assertEqual(actual, expected)

    def test_to_camel_str(self):
        data = 'test_key'
        expected = 'testKey'
        actual = self.case_converter._to_camel_str(data)
        self.assertEqual(actual, expected)

    def test_to_snake_str(self):
        data = 'testKey'
        expected = 'test_key'
        actual = self.case_converter._to_snake_str(data)
        self.assertEqual(actual, expected)

    def test_camelize(self):
        data = {
            'test_key': 'test_value',
            'test_list': [
                {
                    'test_key': 'test_value'
                }
            ]
        }
        expected = {
            'testKey': 'test_value',
            'testList': [
                {
                    'testKey': 'test_value'
                }
            ]
        }
        actual = self.case_converter.camelize(data)
        self.assertEqual(actual, expected)

    def test_snakeify(self):
        data = {
            'testKey': 'test_value',
            'testList': [
                {
                    'testKey': 'test_value'
                }
            ]
        }
        expected = {
            'test_key': 'test_value',
            'test_list': [
                {
                    'test_key': 'test_value'
                }
            ]
        }
        actual = self.case_converter.snakeify(data)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()

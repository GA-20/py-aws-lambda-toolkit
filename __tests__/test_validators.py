import unittest
from py_sls_lambda_toolkit.validators import (
    validate_path,
    validate_data,
)


class TestValidators(unittest.TestCase):

    def test_validate_multiple_type(self):
        schema = {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "title": "Validate multiple type",
            "type": "object",
            "properties": {
                "integer": {
                    "type": ["integer", "string"]
                },
                "string": {
                    "type": ["string", "integer"]
                },
                "boolean": {
                    "type": ["boolean", "integer"]
                },
                "number": {
                    "type": ["number", "integer"]
                },
                "array": {
                    "type": ["array", "integer"]
                },
                "object": {
                    "type": ["object", "integer"]
                },
                "null": {
                    "type": ["null", "integer"]
                },
            }
        }

        data = {
            "integer": 1,
            "string": "1",
            "boolean": True,
            "number": 1.0,
            "array": [1],
            "object": {"integer": 1},
            "null": None,
        }
        result = validate_data(data, schema)
        self.assertIsNone(result)

    def test_validate_path(self):
        path = {
            "id": "00000000-0000-0000-0000-000000000000"
        }
        result = validate_path(path)
        self.assertIsNone(result)

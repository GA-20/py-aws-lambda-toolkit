import unittest
from py_sls_lambda_toolkit.http_event import process_event


class TestProcessEvent(unittest.TestCase):
    def test_process_event(self):
        event = {
            'body': '{"name": "John", "age": 30}',
            'headers': {'Content-Type': 'application/json'},
            'httpMethod': 'POST',
            'isBase64Encoded': False,
            'multiValueHeaders': {'Accept': ['*/*']},
            'path': '/users',
            'pathParameters': {'id': '123'},
            'queryStringParameters': {'sort': 'desc'},
            'requestContext': {
                'accountId': '123456789012', 'resourceId': '123456', 'stage': 'prod'},
            'resource': '/users/{id}',
            'stageVariables': {'env': 'prod'}
        }

        expected_output = {
            'body': {'name': 'John', 'age': 30},
            'headers': {'Content-Type': 'application/json'},
            'httpMethod': 'POST',
            'isBase64Encoded': False,
            'multiValueHeaders': {'Accept': ['*/*']},
            'path': '/users',
            'pathParameters': {'id': '123'},
            'queryStringParameters': {'sort': 'desc'},
            'requestContext': {
                'accountId': '123456789012',
                'resourceId': '123456',
                'stage': 'prod'
            },
            'resource': '/users/{id}',
            'stageVariables': {'env': 'prod'}
        }

        try:
            output = process_event(event)
        except Exception as e:
            self.fail(e)

        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()

from .logger import logging
from typing import Dict
from .case_converter import CaseConverter

case_converter = CaseConverter()


def process_event(event: Dict) -> Dict:
    try:
        body = event.get('body')
        headers = event.get('headers')
        http_method = event.get('httpMethod')
        is_base64_encoded = event.get('isBase64Encoded')
        multi_value_headers = event.get('multiValueHeaders')
        path = event.get('path')
        path_parameters = event.get('pathParameters')
        query_string_parameters = event.get('queryStringParameters')
        request_context = event.get('requestContext')
        resource = event.get('resource')
        stage_variables = event.get('stageVariables')

        logging.info({
            'requestContext': request_context,
            'httpMethod': http_method,
            'path': path,
            'headers': headers
        })

        query_string_parameters = case_converter.snakeify(
            query_string_parameters)
        path_parameters = case_converter.snakeify(path_parameters)
        body = case_converter.snakeify(body)

        return {
            'body': body,
            'headers': headers,
            'httpMethod': http_method,
            'isBase64Encoded': is_base64_encoded,
            'multiValueHeaders': multi_value_headers,
            'path': path,
            'pathParameters': path_parameters,
            'queryStringParameters': query_string_parameters,
            'requestContext': request_context,
            'resource': resource,
            'stageVariables': stage_variables
        }
    except Exception as e:
        logging.error(e)
        raise e

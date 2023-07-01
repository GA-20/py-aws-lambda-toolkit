from py_sls_lambda_toolkit.logger import logging
from typing import Dict
from py_sls_lambda_toolkit.parsers import CamelToSnakeConverter


def process_event(event: Dict) -> Dict:
    """
    Converts the keys in the `query_string_parameters`, `path_parameters`, and `body` dictionaries from camel case to snake case.

    Args:
        event (Dict): A dictionary representing the input event.

    Returns:
        Dict: A dictionary with the same keys as the input dictionary, but with the keys in the `query_string_parameters`, `path_parameters`, and `body` dictionaries converted from camel case to snake case.

    Raises:
        Exception: If an exception occurs during the conversion process.
    """
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

        query_string_parameters = CamelToSnakeConverter.convert(
            query_string_parameters)
        path_parameters = CamelToSnakeConverter.convert(path_parameters)
        body = CamelToSnakeConverter.convert(body)

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

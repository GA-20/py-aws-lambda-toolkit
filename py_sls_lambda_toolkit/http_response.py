import json
from .parsers import (
    convert_snake_to_camel
)
from .settings import (
    ACCESS_CONTROL_ALLOW_ORIGIN,
    ACCESS_CONTROL_ALLOW_CREDENTIALS,
    CONTENT_TYPE,
    ACCESS_CONTROL_ALLOWED_METHODS,
    ACCESS_CONTROL_ALLOWED_HEADERS
)


def create_response(
    response,
    status_code=200,
    custom_headers=None,
    content_type=CONTENT_TYPE
):
    """
        Creates an HTTP response object.

        Parameters:
            response (dict): The response body.
            status_code (int): The HTTP status code to be returned.
            headers (dict): The headers to be returned with the response.
            content_type (str): The content type of the response.

        Returns:
            dict: The HTTP response object with keys statusCode, headers, and body.
    """
    # TODO: Add support for binary data
    # TODO: Add to global config
    headers = {
        'Access-Control-Allow-Origin': ACCESS_CONTROL_ALLOW_ORIGIN,
        'Access-Control-Allow-Credentials': ACCESS_CONTROL_ALLOW_CREDENTIALS,
        'Content-Type': content_type,
        'Access-Control-Allow-Methods': ACCESS_CONTROL_ALLOWED_METHODS,
        'Access-Control-Allow-Headers': ACCESS_CONTROL_ALLOWED_HEADERS,
    }

    if custom_headers is not None:
        headers.update(custom_headers)

    body = convert_snake_to_camel(response)

    return {
        'statusCode': status_code,
        'headers': headers,
        'body': json.dumps(body) if body is not None else None
    }

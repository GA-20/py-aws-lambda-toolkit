ALLOW_METHODS = [
    'GET',
    'POST',
    'OPTIONS',
    'PUT',
    'PATCH',
    'DELETE'
]

ALLOW_HEADERS = [
    'Origin',
    'X-Requested-With',
    'Content-Type',
    'Accept',
    'X-API-AUTH',
    'X-Amz-Date',
    'X-Api-Key',
    'X-Amz-Security-Token',
    'X-Amz-User-Agent'
]

ACCESS_CONTROL_ALLOW_ORIGIN = '*'
ACCESS_CONTROL_ALLOW_CREDENTIALS = True
CONTENT_TYPE = 'application/json'
ACCESS_CONTROL_ALLOWED_METHODS = ', '.join(ALLOW_METHODS)
ACCESS_CONTROL_ALLOWED_HEADERS = ', '.join(ALLOW_HEADERS)

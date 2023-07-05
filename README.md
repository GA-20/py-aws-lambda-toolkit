# Py SLS Lambda Toolkit

This is a lightweight Python toolkit for easily and quickly creating AWS Lambda functions with the Serverless Framework. It includes the following features:

- DynamoDB shortcuts: Avoid boilerplate code for DynamoDB operations.
- HTTP event processing: Get the event of the HTTP request and parse it, splitting it into the path, query string, body, headers, etc.
- HTTP response shortcuts: Create HTTP responses with the correct format and status code.
- JWT authentication: Create and verify JWT tokens as easily as possible.
- Logger: Log messages with a format that is easy to read.
- Mappers: Remove specified fields from a dictionary or list of dictionaries.
- Parser: Convert dictionary keys to snake case or camel case.
- Password hashing: Hash passwords with salt and verify them.
- DynamoDB scan builder: Build a scan query with specified filters.
- Validator: Validate a dictionary with specified rules.

## Installation

Install the package with pip:

```bash
pip install py-aws-lambda-toolkit
```

## Usage

Use the package in your code:

```python
import logging
from py_sls_lambda_toolkit.http_event import process_event
from py_sls_lambda_toolkit.http_response import create_response
from py_sls_lambda_toolkit.status_code import StatusCode
from py_sls_lambda_toolkit.logger import logging

status_code = StatusCode()

def handler(event, context):
    # Process the event
    event_data = process_event(event)
    event_body = event_data.get("body", {})

    logging.info("Event body: %s", event_body)

    # Create a response
    response = create_response(
        { "ok": True, "message": "Processed event successfully" },
        status_code=status_code.code_200_success,
    )

    return response

```

## Contributing

Contributions are welcome! For bug reports or requests please [submit an issue](https://github.com/0riion/py-aws-lambda-toolkit/issues). For code contributions please create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Further Reading

This project is in an starting phase. More documentation will be added soon and the project will be improved with more features.

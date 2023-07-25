from jsonschema import validate
from jsonschema.exceptions import ValidationError


path_id_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Validate id comes in the object path",
    "type": "object",
    "properties": {
        "id": {
            "type": "string",
            "format": "uuid"
        }
    },
    "required": [
        "id"
    ]
}


def validate_path(path):
    """
    Validates the path object.

    Args:
        path (dict): The path object to be validated.

    Raises:
        ValidationError: If the path is invalid.
    """

    if not path:
        raise ValidationError("Path is empty")

    try:
        validate(path, path_id_schema)
    except ValidationError as err:
        raise ValidationError(err.message)


def validate_data(data, schema):
    """
    Validates the data object against the schema.

    Args:
        data (dict): The data object to be validated.
        schema (dict): The schema to be used for validation.

    Raises:
        ValidationError: If the data is invalid.
    """

    if not data or not schema:
        raise ValidationError("Data or schema is empty")

    try:
        validate(data, schema)
    except ValidationError as err:
        raise ValidationError(err.message)

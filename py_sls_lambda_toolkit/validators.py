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
    try:
        if not path:
            raise ValidationError("Path is empty")

        validate(path, path_id_schema)
    except ValidationError as err:
        raise ValidationError(err.message)


def validate_data(data, schema):
    try:

        if not data or not schema:
            raise ValidationError("Data or schema is empty")

        validate(data, schema)
    except ValidationError as err:
        raise ValidationError(err.message)

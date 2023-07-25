from camel_converter import (
    to_camel,
    to_snake,
    dict_to_camel,
    dict_to_snake
)


class CaseConverter:

    """
    This class provides methods for converting strings and dictionaries to CamelCase
    and snake_case.

    Methods:
        _recursive_to_camel: Recursively converts a dictionary or list of dictionaries
        to CamelCase.
        _recursive_to_snake: Recursively converts a dictionary or list of dictionaries
        to snake_case.
        _to_camel_str: Converts a string to CamelCase.
        _to_snake_str: Converts a string to snake_case.
        camelize: Converts a string, dictionary, or list of dictionaries to CamelCase.
        snakeify: Converts a string, dictionary, or list of dictionaries to snake_case.
    """

    def _to_camel_str(self, data):
        """
        Converts a string to CamelCase.

        Args:
            data (str): The string to convert.

        Returns:
            str: The converted string.

        Raises:
            TypeError: If the data is not a string.
        """

        if not isinstance(data, str):
            raise TypeError('_to_camel_str: Data must be a string.')
        return to_camel(data)

    def _to_snake_str(self, data):
        """
        Converts a string to snake_case.

        Args:
            data (str): The string to convert.

        Returns:
            str: The converted string.

        Raises:
            TypeError: If the data is not a string.
        """

        # if the data is a single word like "Hello", "hello", "hellO", "HELLO"
        # return data

        if not isinstance(data, str):
            raise TypeError('_to_snake_str: Data must be a string.')

        return to_snake(data)

    def _recursive_to_camel(self, data):
        """
        Recursively converts a dictionary or list of dictionaries to CamelCase.

        Args:
            data (dict or list): The data to convert.

        Returns:
            dict or list: The converted data.

        Raises:
            TypeError: If the data is not a dictionary or list.
        """

        if isinstance(data, dict):
            return dict_to_camel(data)
        elif isinstance(data, list):
            return [self._recursive_to_camel(item) for item in data]
        elif isinstance(data, str) or isinstance(data, int):
            return data
        else:
            raise TypeError(
                '_recursive_to_camel: Data must be a dict or a list of dicts.')

    def _recursive_to_snake(self, data):
        """
        Recursively converts a dictionary or list of dictionaries to snake_case.

        Args:
            data (dict or list): The data to convert.

        Returns:
            dict or list: The converted data.

        Raises:
            TypeError: If the data is not a dictionary or list.
        """

        if isinstance(data, dict):
            return dict_to_snake(data)
        elif isinstance(data, list):
            return [self._recursive_to_snake(item) for item in data]
        elif isinstance(data, str) or isinstance(data, int):
            return data
        else:
            raise TypeError(
                '_recursive_to_snake: Data must be a dict or a list of dicts.')

    def camelize(self, data):
        """
        Converts a string, dictionary, or list of dictionaries to CamelCase.

        Args:
            data (str or dict or list): The data to convert.

        Returns:
            str or dict or list: The converted data.

        Raises:
            TypeError: If the data is not a string, dictionary, or list.
        """

        if isinstance(data, str) or isinstance(data, int):
            return data

        if isinstance(data, dict) or isinstance(data, list):
            return self._recursive_to_camel(data)

        raise TypeError(
            'camelize: Data must be a string, a dict, or a list of dicts.')

    def snakeify(self, data):
        """
        Converts a string, dictionary, or list of dictionaries to snake_case.

        Args:
            data (str or dict or list): The data to convert.

        Returns:
            str or dict or list: The converted data.

        Raises:
            TypeError: If the data is not a string, dictionary, or list.
        """
        if isinstance(data, str) or isinstance(data, int):
            return data

        if isinstance(data, dict) or isinstance(data, list):
            return self._recursive_to_snake(data)

        raise TypeError(
            'camelize: Data must be a string, a dict, or a list of dicts.')


def mapper(data, fields):
  """
    Removes the specified fields from the dictionary or list of dictionaries.

    Args:
    - data: a dictionary or list of dictionaries.
    - fields: a list of strings with the names of the fields to remove.

    Returns:
    - The dictionary or list of dictionaries with the specified fields removed.
    """

  if isinstance(data, dict):
    data = {key: value for key, value in data.items() if key not in fields}
  elif isinstance(data, list):
    for item in data:
      for field in fields:
        item.pop(field, None)
  else:
    raise TypeError("'data' must be a dictionary or a list")

  return data

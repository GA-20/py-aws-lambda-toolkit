import logging
from boto3.dynamodb.conditions import Attr


def list_all(table, scan_params):
    """
    Lists all the items in the table.

    Args:
        table (boto3.resource('dynamodb').Table): The DynamoDB table.
        scan_params (dict): The scan parameters.

    Returns:
        dict: A dictionary of the items in the table.
    """

    try:
        response = table.scan(**scan_params)
        data = response['Items']

        while 'LastEvaluatedKey' in response:
            scan_params['ExclusiveStartKey'] = response['LastEvaluatedKey']
            response = table.scan(**scan_params)
            data.extend(response['Items'])

        return {'items': data, 'total': len(data)}
    except Exception as err:
        raise err


def exits_by_attr(table, attribute, value):
    """
    Checks if a resource exists with the given attribute and value.

    Args:
        table (boto3.resource('dynamodb').Table): The DynamoDB table.
        attribute (str): The attribute to check.
        value (any): The value to check.

    Returns:
        bool: True if the resource exists, False otherwise.
    """

    try:

        if not attribute or not value:
            raise Exception('Attribute and value are required')

        response = table.scan(
            FilterExpression=Attr(attribute).eq(value)
        )

        return response['Count'] > 0

    except Exception as err:
        logging.error(f"Error while checking: {err}")
        raise


def exits_by_key(table, partition_key, partition_value, sort_key=None, sort_value=None):
    """
    Checks if a resource exists with the given partition key and sort key (if any).

    Args:
        table (boto3.resource('dynamodb').Table): The DynamoDB table.
        partition_key (str): The partition key.
        partition_value (any): The partition value.
        sort_key (str): The sort key (optional).
        sort_value (any): The sort value (optional).

    Returns:
        bool: True if the resource exists, False otherwise.
    """

    try:

        if not partition_value or not partition_value:
            raise Exception('Partition key and value are required')

        if sort_key and sort_value:
            response = table.get_item(
                Key={
                    partition_key: partition_value,
                    sort_key: sort_value
                }
            )

        else:
            response = table.get_item(
                Key={
                    partition_key: partition_value
                }
            )

        return response['Item'] is not None

    except Exception as err:
        logging.error(f"Error while checking {partition_value} : {err}")
        raise

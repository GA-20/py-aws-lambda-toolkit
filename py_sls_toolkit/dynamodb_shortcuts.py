import logging
from boto3.dynamodb.conditions import Attr


def exits_by_attr(table, attribute, value):
    try:

        if not attribute or not value:
            raise Exception('Attribute and value are required')

        response = table.scan(
            FilterExpression=Attr(attribute).eq(value)
        )

        if response['Count'] > 0:
            raise Exception(f'Resource with same {attribute} already exists')

    except Exception as err:
        logging.error(f"Error while checking: {err}")
        raise


def exits_by_key(table, partition_key, partition_value, sort_key=None, sort_value=None):
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

        if response['Item'] is None:
            raise Exception('Resource not found.')

        return response['Item']

    except Exception as err:
        logging.error(f"Error while checking {partition_value} : {err}")
        raise

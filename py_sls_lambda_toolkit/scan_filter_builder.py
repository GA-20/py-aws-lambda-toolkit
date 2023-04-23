from boto3.dynamodb.conditions import Attr

def equal(filter_expression, attribute, value):
    if bool(filter_expression):
        filter_expression &= Attr(attribute).eq(value)
    else:
        filter_expression = Attr(attribute).eq(value)

    return filter_expression


def less_than(filter_expression, attribute, value):
    if bool(filter_expression):
        filter_expression &= Attr(attribute).lt(value)
    else:
        filter_expression = Attr(attribute).lt(value)

    return filter_expression


def less_than_or_equal(filter_expression, attribute, value):
    if bool(filter_expression):
        filter_expression &= Attr(attribute).lte(value)
    else:
        filter_expression = Attr(attribute).lte(value)

    return filter_expression


def greater_than(filter_expression, attribute, value):
    if bool(filter_expression):
        filter_expression &= Attr(attribute).gt(value)
    else:
        filter_expression = Attr(attribute).gt(value)

    return filter_expression


def greater_than_or_equal(filter_expression, attribute, value):
    if bool(filter_expression):
        filter_expression &= Attr(attribute).gte(value)
    else:
        filter_expression = Attr(attribute).gte(value)

    return filter_expression


def between(filter_expression, attribute, value):
    if bool(filter_expression):
        filter_expression &= Attr(attribute).between(value[0], value[1])
    else:
        filter_expression = Attr(attribute).between(value[0], value[1])

    return filter_expression


def in_list(filter_expression, attribute, value):
    if bool(filter_expression):
        filter_expression &= Attr(attribute).is_in(value)
    else:
        filter_expression = Attr(attribute).is_in(value)

    return filter_expression


def contains(filter_expression, attribute, value):
    if bool(filter_expression):
        filter_expression &= Attr(attribute).contains(value)
    else:
        filter_expression = Attr(attribute).contains(value)

    return filter_expression


def not_exists(filter_expression, attribute, value):
    if bool(filter_expression):
        filter_expression &= Attr(attribute).not_exists()
    else:
        filter_expression = Attr(attribute).not_exists()

    return filter_expression


def exists(filter_expression, attribute, value):
    if bool(filter_expression):
        filter_expression &= Attr(attribute).exists()
    else:
        filter_expression = Attr(attribute).exists()

    return filter_expression


actions = {
    'eq': equal,
    'lt': less_than,
    'lte': less_than_or_equal,
    'gt': greater_than,
    'gte': greater_than_or_equal,
    'between': between,
    'in': in_list,
    'contains': contains,
    'not_exists': not_exists,
    'exists': exists,
}


def apply_filter_expression(filters):
    filter_expression = {}

    for key, value in filters.items():

        if '__' not in key:
            raise Exception('Invalid filter key')

        action, attribute = key.split('__')
        filter_expression = actions[action](
            filter_expression, attribute, value)

    return filter_expression

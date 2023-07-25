import jwt
import time


def create_token(user_id, exp_time, jwt_secret):
    """
    Creates a JWT token.
    Args:
        user_id (str): The user ID to be included in the token.
        exp_time (int): The expiration time of the token, in seconds.
        jwt_secret (str): The secret used to sign the token.
    Returns:
        str: The JWT token.
    """
    payload = {'sub': user_id, 'exp': int(time.time()) + exp_time}
    token = jwt.encode(payload, jwt_secret, algorithm='HS256')
    return token


def verify_token(token, jwt_secret):
    """
    Verifies a JWT token.
    Args:
        token (str): The JWT token to be verified.
        jwt_secret (str): The secret used to sign the token.
    Returns:
        str: The user ID from the token.
    Raises:
        ExpiredSignatureError: If the token has expired.
        InvalidTokenError: If the token is invalid.
    """
    try:
        decoded_token = jwt.decode(token, jwt_secret, algorithms=['HS256'])
        return decoded_token['sub']
    except jwt.ExpiredSignatureError:
        raise Exception('Token has expired')
    except jwt.InvalidTokenError:
        raise Exception('Invalid token')

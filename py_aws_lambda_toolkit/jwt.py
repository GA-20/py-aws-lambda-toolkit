import jwt
import time

def create_token(user_id, exp_time, jwt_secret):
  payload = {'sub': user_id, 'exp': int(time.time()) + exp_time}
  token = jwt.encode(payload, jwt_secret, algorithm='HS256')
  return token


def verify_token(token, jwt_secret):
  try:
    decoded_token = jwt.decode(token, jwt_secret, algorithms=['HS256'])
    return decoded_token['sub']

  except jwt.ExpiredSignatureError:
    raise Exception('Token has expired')

  except jwt.InvalidTokenError:
    raise Exception('Invalid token')

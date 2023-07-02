import unittest
from py_sls_lambda_toolkit.jwt import create_token, verify_token
import jwt

class TestJWT(unittest.TestCase):

    def test_create_token(self,):
        user_id = 12345
        exp_time = 3600
        jwt_secret = 'secret'
        token = create_token(user_id, exp_time, jwt_secret)
        decoded_token = jwt.decode(token, jwt_secret, algorithms=['HS256'])
        self.assertEqual(decoded_token['sub'], user_id)

    def test_verify_token(self,):
        user_id = 12345
        exp_time = 3600
        jwt_secret = 'secret'
        token = create_token(user_id, exp_time, jwt_secret)
        decoded_token = verify_token(token, jwt_secret)
        self.assertEqual(decoded_token, user_id)


if __name__ == '__main__':
    unittest.main()

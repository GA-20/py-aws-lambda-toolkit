import unittest
from py_sls_lambda_toolkit.password import (
    hash_password,
    verify_password,
)


class TestPassword(unittest.TestCase):

    password = "testPassword"
    salt = "testSalt"
    hashed_password_regex = r"^[a-f0-9]{64}$"

    def test_hash_password(self):
        hashed_password = hash_password(self.password, self.salt)
        self.assertRegex(hashed_password, self.hashed_password_regex)
    
    def test_verify_password(self):
        hashed_password = hash_password(self.password, self.salt)
        self.assertTrue(verify_password(self.password, hashed_password, self.salt))
        self.assertFalse(verify_password("wrongPassword", hashed_password, self.salt))

if __name__ == '__main__':
    unittest.main()

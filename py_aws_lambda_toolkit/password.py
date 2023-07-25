import hashlib

def hash_password(password, salt):
  """Hashes a password using SHA-256"""
  password = password.encode('utf-8')
  salt = salt.encode('utf-8')
  hashed_password = hashlib.sha256(password + salt).hexdigest()
  return hashed_password


def verify_password(password, hashed_password, salt):
  """Verifies a password by comparing the hashed password to the provided password"""
  password = password.encode('utf-8')
  salt = salt.encode('utf-8')
  hashed_password_to_check = hashlib.sha256(password + salt).hexdigest()
  return hashed_password == hashed_password_to_check

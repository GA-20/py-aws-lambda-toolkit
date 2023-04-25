import bcrypt


def encrypt_password(password):
  """Encrypts a password using bcrypt"""
  password_bytes = password.encode('utf-8')
  salt = bcrypt.gensalt()
  hashed_password = bcrypt.hashpw(password_bytes, salt)
  return hashed_password


def decrypt_password(password, hashed_password):
  """Decrypts a password using bcrypt"""
  password_bytes = password.encode('utf-8')
  return bcrypt.checkpw(password_bytes, hashed_password)

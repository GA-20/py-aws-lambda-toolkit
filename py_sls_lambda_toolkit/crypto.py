import bcrypt
import re


def validate_password(password):
    """Validates a password against a pattern"""
    if not isinstance(password, str):
        raise TypeError("Password must be a string.")
    
    # Define a pattern for a valid password
    # At least 8 characters
    # At least one uppercase letter
    # At least one lowercase letter
    # At least one digit
    # At least one special character
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()_+\\-=[\]{};':\"\\|,.<>/?]).{8,}$"
    
    if not re.match(pattern, password):
        raise ValueError("Invalid password.")
        

def encrypt_password(password):
    """Encrypts a password using bcrypt"""
    if not isinstance(password, str):
        raise TypeError("Password must be a string.")
    
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    return hashed_password


def decrypt_password(password, hashed_password):
    """Decrypts a password using bcrypt"""
    if not isinstance(password, str):
        raise TypeError("Password must be a string.")
    if not isinstance(hashed_password, bytes):
        raise TypeError("Hashed password must be bytes.")
    
    password_bytes = password.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_password)


def validate_decrypted_password(password, hashed_password):
    """Validates a password against a hashed password"""
    if not decrypt_password(password, hashed_password):
        raise ValueError("Invalid password.")

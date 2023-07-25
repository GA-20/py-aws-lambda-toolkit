import hashlib


def hash_password(password, salt):
    """
    Hashes a password using SHA-256.

    Args:
        password (str): The password to be hashed.
        salt (str): A random salt to be used in the hashing process.

    Returns:
        str: The hashed password.
    """

    password = password.encode('utf-8')
    salt = salt.encode('utf-8')
    hashed_password = hashlib.sha256(password + salt).hexdigest()
    return hashed_password


def verify_password(password, hashed_password, salt):
    """
    Verifies a password by comparing the hashed password to the provided password.

    Args:
        password (str): The password to be verified.
        hashed_password (str): The hashed password to be compared to.
        salt (str): The salt that was used to hash the password.

    Returns:
        bool: True if the passwords match, False otherwise.
    """

    password = password.encode('utf-8')
    salt = salt.encode('utf-8')
    hashed_password_to_check = hashlib.sha256(password + salt).hexdigest()
    return hashed_password == hashed_password_to_check

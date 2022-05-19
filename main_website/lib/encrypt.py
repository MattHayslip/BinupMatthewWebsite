from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64  # for encryption
import os

from .util import *

FORMAT = "utf-8"  # into bytes

def get_encryption_key(msg):  # generate encryption key to encrypt lol
    try:
        # stripping any white spaces
        password_provided = str(msg).strip()

        # encoding into a byte
        password = password_provided.encode(FORMAT)

        # salt used to encrypt
        # salt = b"\xb9\x1f|}'S\xa1\x96\xeb\x154\x04\x88\xf3\xdf\x05"
        salt = os.urandom(32)

        # generating said key
        kdf = PBKDF2HMAC(
            algorithm  = hashes.SHA256(),
            length     = 32,
            salt       = salt,
            iterations = 100000,
            backend    = default_backend()
        )

        # encrypt it?
        key = base64.urlsafe_b64encode(kdf.derive(password))

        return key  # this is the key that'll be used for encryption

    except Exception as e:
        print(f"{error} * Error: {str(e)}")


def Encrypt(data):  # encrypt
    try:
        # encrypt data
        fernet = Fernet(
            get_encryption_key(
                data.encode(FORMAT)
            )
        )
        return fernet.encrypt(
            data.encode(FORMAT)
        )
    except Exception as e:
        print(f"{error} * error: {str(e)}")


def Decrypt(data):  # decrypt
    try:
        # decrypt data
        fernet = Fernet(
            get_encryption_key(
                data.decode(FORMAT)
            )
        )
        return fernet.decrypt(
            data.decode(FORMAT)
        )
    except Exception as e:
        print(f"{error} * error: {str(e)}")
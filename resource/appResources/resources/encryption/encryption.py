"""
Encryption module for PWD Manager
"""
# Imports
from cryptography.fernet import Fernet
import os
import base64

# encypting 
password = 'Howimsiw' #for main()

KEY_PATH = os.path.expanduser(os.getenv('USERPROFILE')) + '\\AppData\\Local\\Programs\\Portal Password Manager\\resource\\appResources\\resources\\encryption\\key.key'

def encrypt(pswd):
    """
    Encrypts requested Password from user
    """
    file = open(KEY_PATH, 'rb')
    key = file.read()
    file.close()
    password_provided = pswd
    coded = password_provided.encode()
    f = Fernet(key)
    encrypt = f.encrypt(coded)
    return encrypt


def de_encrypt(encrypted_password):
    """
    De encrypts the password for user to see if requested
    """
    encrypt_msg = encrypted_password
    file = open(KEY_PATH, 'rb')
    key2 = file.read()
    file.close()
    f2 = Fernet(key2)
    decrypted = f2.decrypt(encrypt_msg)
    decrypted_msg = decrypted.decode('utf-8')
    return decrypted_msg

def main():
    encryption = encrypt(password)
    de_encrypt(encryption)
    
if __name__ == '__main__':
    main()
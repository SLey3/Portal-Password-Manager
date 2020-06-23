"""
Encryption module for PWD Manager
"""
# Imports
from cryptography.fernet import Fernet

# encypting 
password = 'Howimsiw' #TODO connect this with the user responce with wx

def encryption(pswd):
    """
    Encrypts requested Password from user
    """
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    password_provided = pswd
    coded = password_provided.encode()
    print(coded)
    f = Fernet(key)
    encrypt = f.encrypt(coded)
    print(encrypt)
    return encrypt


def de_encrypt():
    """
    De encrypts the password for user to see if requested
    """
    encrypt_msg = encryption(password)
    file = open('key.key', 'rb')
    key2 = file.read()
    file.close()
    f2 = Fernet(key2)
    decrypted = f2.decrypt(encrypt_msg)
    decrypted_msg = decrypted.decode('utf-8')
    print(decrypted_msg)
    
    return decrypted_msg

de_encrypt()
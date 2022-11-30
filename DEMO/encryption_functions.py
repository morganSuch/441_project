import random
from Crypto.Cipher import AES
import hashlib
import os
import struct

def encrypt_db(key, chunksize, db_name):
    if not os.path.exists(db_name):
        return # Database is already encrypted
    iv = os.urandom(16)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(db_name)
    with open(db_name, 'rb') as inDB:
        with open(db_name + ".enc", 'wb') as outDB:
            outDB.write(struct.pack('<Q', filesize))
            outDB.write(iv)
            while True:
                chunk = inDB.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)
                outDB.write(encryptor.encrypt(chunk))
    os.remove(db_name) # Deletes unencrypted database
    return

def decrypt_db(key, chunksize, db_name):
    if not os.path.exists(db_name + ".enc"):
        return # Database is not encrypted
    with open(db_name + ".enc", 'rb') as inDB:
        origsize = struct.unpack('<Q', inDB.read(struct.calcsize('Q')))[0]
        iv = inDB.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)
        with open(db_name, 'wb') as outDB:
            while True:
                chunk = inDB.read(chunksize)
                if len(chunk) == 0:
                    break
                outDB.write(decryptor.decrypt(chunk))

            outDB.truncate(origsize)
    os.remove(db_name + ".enc") # Deletes old encrypted database
    return
import random
from Crypto.Cipher import AES
import hashlib
import os
import struct

password = "1234" # Password will be changed to something more complicated
key = hashlib.sha256(password.encode('utf-8')).digest()
chunksize = 64*1024
in_db = "test.db.enc"
out_db = "test.db"

def encrypt(database, enc_database):
    iv = os.urandom(16)
    print (len(iv))
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(database)

    with open(database, 'rb') as inDB:
        with open(enc_database, 'wb') as outDB:
            outDB.write(struct.pack('<Q', filesize))
            outDB.write(iv)
            while True:
                chunk = inDB.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)
                outDB.write(encryptor.encrypt(chunk))

def decrypt(database, dec_database):
    with open(database, 'rb') as inDB:
        origsize = struct.unpack('<Q', inDB.read(struct.calcsize('Q')))[0]
        iv = inDB.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)
        with open(dec_database, 'wb') as outDB:
            while True:
                chunk = inDB.read(chunksize)
                if len(chunk) == 0:
                    break
                outDB.write(decryptor.decrypt(chunk))

            outDB.truncate(origsize)
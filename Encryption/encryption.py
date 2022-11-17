import random
from Crypto.Cipher import AES
import hashlib
import os
import struct


password = '1234' # Password will be changed to something more complicated
key = hashlib.sha256(password.encode('utf-8')).digest()
chunksize = 64*1024
in_db = "test.db"
out_db = "test.db.enc"
#iv = bytes(''.join(chr(random.randint(0, 0xFF)) for i in range(16)), 'utf-8')
iv = os.urandom(16)
print (len(iv))
encryptor = AES.new(key, AES.MODE_CBC, iv)
filesize = os.path.getsize(in_db)

with open(in_db, 'rb') as inDB:
    with open(out_db, 'wb') as outDB:
        outDB.write(struct.pack('<Q', filesize))
        outDB.write(iv)
        while True:
            chunk = inDB.read(chunksize)
            if len(chunk) == 0:
                break
            elif len(chunk) % 16 != 0:
                chunk += ' ' * (16 - len(chunk) % 16)
            outDB.write(encryptor.encrypt(chunk))
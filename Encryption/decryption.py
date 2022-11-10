from random import random
from Crypto.Cipher import AES
import hashlib
import os
import struct

password = "k@(HDFn20-fn_TRJDM_#(*mafsa"
key = hashlib.sha256(password).digest()
chunksize = 64*1024
in_db = "test.db.enc"
out_db = "test.db"

with open(in_db, 'rb') as inDB:
    origsize = struct.unpack('<Q', inDB.read(struct.calcsize('Q')))[0]
    iv = inDB.read(16)
    decryptor = AES.new(key, AES.MODE_CBC, iv)
    with open(out_db, 'wb') as outDB:
        while True:
            chunk = inDB.read(chunksize)
            if len(chunk) == 0:
                break
            outDB.write(decryptor.decrypt(chunk))

        outDB.truncate(origsize)
import face_recognition
import numpy as np
from picamera import PiCamera
from time import sleep
import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto import Random
from base64 import b64encode, b64decode

#camera = PiCamera()
extern_priv = """-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEApIi2HI7XMpNdOZYHSEnMBllQZUEtaXU33O1yCo1lPPh4k5Ou
OizGp2Bjk2iPHeCvlvbVLmHNciOKdXdUwCtNd+H+MMjGKnMo7ohFcUUtzLPqm2kr
IOQoP1rVJCRJNYx7K1edbJNFhujaXmGSLjP/tpzQrgh4GTrr4im7Kv0isfEDnwOJ
oxlZDP9I084496uc4NRvik0okJ5jajDHy/XetyX+fXtzI4tIby68xVPTYkEO6B+I
ZpZAHEddWBW/WvRUdy5qCQZ+mTyo9SLTkLk/v2gNGmv/DK/xd5P3NLWZM8q8KbV2
1wIPdcoVSj/dS2z7mBToJad7XafQOakAwpohMwIDAQABAoIBAEaRsHJNPbWeiRSi
6ZqytERg2F+ldeHOedhTK1+lR6+/7o91fvvKqqWtbOgTp5asAQPh+It9PU3gOomp
VftaV0686nZoFr6sR/kPD6HGhx9OZ6iikfH4id6qidKHkbLa/xUW7hlcjSyRAOAM
P1N70Ai197c9QK2pnPSS64lDqzbgNGreWgIuFhdn8WIFb6mPuhgDZSnKWXNwi2Da
lWRHw7S4jDpr46j1fBrCNnZrzCUFWxju8ah0Kt4z3bEfy60Gp/KUBx6HXihI6L5J
Ap7n7rAZFTi3sqD+iytYzpsPXx8Ru404ww6kcpaHjm531aRhmaJZW5EaX8JK+p6/
BzB6aeECgYEAtqvfeE4K4ZfTPN0yX29LdG4frV3oa/M+xKPSmvDGq/R2LQymRCIq
ldi3Ms0hsQl9FuxlA8+ykB2x9OUcQCFufaiPdRMgzyVEs9ZsG3VW+KgVgnIfDJzl
bLxRTUFlHgjFIKtYsyZeyf3qwr4ksNYbtO7e9KcdqiqtKMokNXPbjbECgYEA5pT2
nSBE5iwDELoQfbrot7ERsqvBgKmh0taY/RR6RU7PnM8xiC1mzt+GDdtuqnoMasCO
smMNOTGyYS522mQ0yI+duun69DnmME6l9AsmQ3v6wvYRxed/SjL+4xLDL+2DB2YG
RykpGkD7EF9nkx1tyDSEhX/+/onwYbY7V/LYYiMCgYB88kTxihghRHMlb3tUEdE/
u0+JivE+XWwynoegmU6bMaRfngZgFiqgwlJUukDwUjgwpNNXbwqJTvZ5NvlC2Fs2
MkSl5MaNScWbaPAbPACYJohH6H1aaDr5TDokKLXcfE0x0mHicD1n1nlsaRi5qEnd
UYJJP8Gnsncsrk9kDHJBkQKBgBWjSPk5u/11h9wb+cwyrAAA585Ce+gdAwiMBtNJ
BqhWWvk2IEnNKOak5ymJu/rXdS7XXwyyat1BIqIoABNCcAmaII0Xw+sDO+ywlLYw
Dakriz6cZNKThMhrvKuGaTaoLTGWi2RGIotKKcVBjrCphFHTS9RTTJSKUTp6JVt9
eHzNAoGBAI0PQ+VfzQAZGKhepcQ1b7paVlreiSEv/algHroUtIHwlYEhwFYAffM4
fuaMJcjIIfsjZA23Q8EGogWrJ61h7X29joFBX3AO22GTYrW9Mmj+zpTjPhKaAVIo
u/xa30s2VxE6vRllGrleWChYlj3tec2UrwSb3EynGOXRUynUdK3o
-----END RSA PRIVATE KEY-----"""

extern_pub = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApIi2HI7XMpNdOZYHSEnM
BllQZUEtaXU33O1yCo1lPPh4k5OuOizGp2Bjk2iPHeCvlvbVLmHNciOKdXdUwCtN
d+H+MMjGKnMo7ohFcUUtzLPqm2krIOQoP1rVJCRJNYx7K1edbJNFhujaXmGSLjP/
tpzQrgh4GTrr4im7Kv0isfEDnwOJoxlZDP9I084496uc4NRvik0okJ5jajDHy/Xe
tyX+fXtzI4tIby68xVPTYkEO6B+IZpZAHEddWBW/WvRUdy5qCQZ+mTyo9SLTkLk/
v2gNGmv/DK/xd5P3NLWZM8q8KbV21wIPdcoVSj/dS2z7mBToJad7XafQOakAwpoh
MwIDAQAB
-----END PUBLIC KEY-----"""

priv_rsa = RSA.import_key(extern_priv)
pub_rsa = RSA.import_key(extern_pub)

def add_face(camera, id, priv_rsa) -> bool:
    camera.start_preview()
    sleep(3)
    #file_name="morgan.jpg"
    file_name = "/home/pi/Faces/" + id + ".jpg"
    camera.capture(file_name) # Face to be recognized
    camera.stop_preview()

    image = face_recognition. load_image_file(file_name)
    try:
        image_encoding = face_recognition.face_encodings(image)[0]
    except IndexError:
        print("Unable to find face")
        os.remove(file_name)
        return False
    with open(file_name, 'rb') as file:
        contents = file.read()
    signer = PKCS1_v1_5.new(priv_rsa)
    digest = SHA256.new()
    digest.update(contents)
    signature = signer.sign(digest)
    sig_file = "/home/pi/Signatures/" + id + ".jpg.sig"
    with open(sig_file, 'wb') as s:
        s.write(signature)
    return True
    """file_name = "/home/pi/password_manager/441_project/Authentication/Faces/"+id+".txt"
    image_file = open(file_name, "w")
    print(image_encoding)
    image_file.writelines(str(image_encoding))
    image_file.close()"""
    return True
    #image_list.append(image_encoding)
    # Create arrays of known face encodings and their names
    # known_face_encodings = [
    #     image_encoding,
    # ]
    # known_face_names = [
    #     "id"
    # ]

def authenticate_face(camera, pub_rsa) -> bool:
    camera.start_preview()
    sleep(3)
    #file_name ="authorize.jpg"
    camera.capture("authorize.jpg") # Face to be recognized
    camera.stop_preview()
    
    # Load an image with an unknown face
    authorization_image = face_recognition.load_image_file("authorize.jpg")
    
    # Find all the faces and face encodings in the unknown image
    try:
        auth_encode = face_recognition.face_encodings(authorization_image)[0]
    except IndexError:
        print("Unable to find face")
        return False
    known_encodings = []
    face_path = "/home/pi/Faces/"
    sig_path = "/home/pi/Signatures/"
    signer = PKCS1_v1_5.new(pub_rsa)
    image_list = os.listdir(face_path)
    for file in image_list:
        with open(face_path + file, 'rb') as f:
            data = f.read()
        digest = SHA256.new()
        digest.update(data)
        try:
            with open(sig_path + file + ".sig", 'rb') as f:
                signature = f.read()
        except IOError:
            print("Signature not found")
            return False # Signature not found, attempt to add an unauthorized face detected.
        if signer.verify(digest, signature):
            image = face_recognition.load_image_file(face_path + file)
            print(file)
            encoding = face_recognition.face_encodings(image)[0]
            known_encodings.append(encoding)
        else:
            print("Unknown signature")
            return False # Signature did not match, attempt to add an unauthorized face detected.
    print(auth_encode)
    # Loop through each face found in the unknown image
    print(known_encodings)
    matches = face_recognition.compare_faces(known_encodings, auth_encode)
    print(matches)
    if True in matches:
        print("true")
        return True
    else:
        print("false")
        return False

camera = PiCamera()
#add_face(camera, "morgan", priv_rsa)
authenticate_face(camera, pub_rsa)
camera.close()



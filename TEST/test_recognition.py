import face_recognition
import numpy as np
from picamera import PiCamera
from time import sleep
import os

camera = PiCamera()

def add_face(camera, id) -> bool:
    camera.start_preview()
    sleep(3)
    #file_name="morgan.jpg"
    file_name = "Faces/" + id + ".jpg"
    camera.capture(file_name) # Face to be recognized
    camera.stop_preview()

    image = face_recognition. load_image_file(file_name)
    try:
        image_encoding = face_recognition.face_encodings(image)[0]
    except IndexError:
        print("Unable to find face")
        return False
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

def authenticate_face(camera) -> bool:
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
    image_list = os.listdir("/home/pi/password_manager/441_project/Authentication/Faces/")
    for file in image_list:
        image = face_recognition.load_image_file("Faces/" + file)
        print(file)
        encoding = face_recognition.face_encodings(image)[0]
        known_encodings.append(encoding)
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

# add_new_face(camera, "morgan")
# capture_face(camera)




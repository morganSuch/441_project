import face_recognition
from picamera import PiCamera
from time import sleep
import os

camera = PiCamera()

camera.start_preview()
sleep(5)
camera.capture("face.jpg") # Face to be recognized
camera.stop_preview()

known_faces = []
known_face_list = os.listdir("/faces/") # Needs faces from database in this directory

try:
    for i in known_face_list:
        image = face_recognition.load_image_file(i)
        known_faces.append(face_recognition.face_encodings(image)[0])
    image = face_recognition.load_image_file("face.jpg")
    unknown_face = face_recognition.face_encodings(image)[0]
    results = face_recognition.compare_faces(known_faces, unknown_face)
    for i in results:
        if i == True:
            print("Face recognized")
            #return True
    print("Face not recognized")
    #return False
except:
    print("An error occurred")
    #return False
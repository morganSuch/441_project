import face_recognition
import numpy as np
from picamera import PiCamera
from time import sleep
import os

def add_new_face(id):
    camera = PiCamera()
    camera.start_preview()
    sleep(5)
    file_name = id+".jpg"
    camera.capture(file_name) # Face to be recognized
    camera.stop_preview()

    image = face_recognition.load_image_file(file_name)
    image_encoding = face_recognition.face_encodings(file_name)[0]
    image_file = open("/home/pi/"+id+".txt", "w")
    image_file.writelines(image_encoding)
    image_file.close()
    #image_list.append(image_encoding)
    # Create arrays of known face encodings and their names
    # known_face_encodings = [
    #     image_encoding,
    # ]
    # known_face_names = [
    #     "id"
    # ]

def capture_face() -> bool:
    camera = PiCamera()
    camera.start_preview()
    sleep(5)
    #file_name ="authorize.jpg"
    camera.capture("authorize.jpg") # Face to be recognized
    camera.stop_preview()
    # Load an image with an unknown face
    authorization_image = face_recognition.load_image_file("authorize.jpg")

    # Find all the faces and face encodings in the unknown image
    face_locations = face_recognition.face_locations(authorization_image)
    face_encodings = face_recognition.face_encodings(authorization_image, face_locations)

    image_list = os.listdir("/home/pi/")
    # Loop through each face found in the unknown image
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(image_list, face_encoding)

        name = "Unknown"

        # If a match was found in known_face_encodings, just use the first one.
        # if True in matches:
        #     first_match_index = matches.index(True)
        #     name = known_face_names[first_match_index]

        # Or instead, use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(image_list, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = image_list[best_match_index]
            print("match found")
            return True
        else:
            print("match not found")
            return False

add_new_face("morgan")
capture_face()



# Adding this file that has different authentication functions
# so we can easily import into the client application script

import adafruit_fingerprint
import serial
import time

# Default variables
MAX_FAILED_ATTEMPTS = 3

# Serial connection to Adafruit Scanner
uart = serial.Serial("/dev/serial0", baudrate=57600, timeout=1)
scanner = adafruit_fingerprint.Adafruit_Fingerprint(uart)

# def testAuth() -> bool:
#     return True
# def testAuth2() -> bool:
#     return False

def countPrints() -> int:
    if scanner.count_templates() == adafruit_fingerprint.OK:
        return scanner.template_count
    
def removePrints() -> bool:
    if scanner.empty_library() == adafruit_fingerprint.OK:
        return True
    else:
        return False

def getPrints() -> list:
    if scanner.read_templates() == adafruit_fingerprint.OK:
        print_list = scanner.templates
        return print_list

def deletePrint(entry) -> bool:
    if scanner.delete_model(entry) == adafruit_fingerprint.OK:
        return True
    else:
        return False

def findFinger() -> bool:
     count = 0
     # Let user try authentication 3 times
     while (count < MAX_FAILED_ATTEMPTS):
         scanner.set_led(color=3, mode=3) # Sets led to purple
         while scanner.get_image() != adafruit_fingerprint.OK:
             pass
         if scanner.image_2_tz(1) != adafruit_fingerprint.OK:
             scanner.set_led(color=1, mode=2)
             print("An error occurred")
         elif scanner.finger_search() != adafruit_fingerprint.OK:
             scanner.set_led(color=1, mode=3)
             print("Finger not found")
             count +=1
             time.sleep(1)
         else:
             scanner.set_led(color=2, mode=3)
             print("Finger found")
             return True
     # If they fail after 3 let server know authnetication has failed
     return False

def addFinger(location) -> bool:
     # To be changed
     #location = 1 # Location the fingerprint is stored on the fingerprint scanner
     for img in range(1, 3):
         # Attempt to scan new finger, if image accepted break
         while True:
             i = scanner.get_image()
             # Finger found
             if i == adafruit_fingerprint.OK:
                 scanner.set_led(color=2, mode=2) # Sets led to flashing blue
                 print("got finger")
                 break
             # Finger not found
             if i == adafruit_fingerprint.NOFINGER:
                 scanner.set_led(color=3, mode=2) # Sets led to flashing purple
             else: # Error occurs
                 scanner.set_led(color=2, mode=2) # Sets led to flashing red
                 print("An error occurred")
                 #return False
         i = scanner.image_2_tz(img)
         if i == adafruit_fingerprint.OK:
             print("Fingerprint template made")
         else:
             scanner.set_led(color=2, mode=2)  # Sets led to flashing red
             print("Template not created")
             return False
         if img == 1:
             time.sleep(1)
             while i != adafruit_fingerprint.NOFINGER:
                 i = scanner.get_image()
         i = scanner.create_model()
         if i == adafruit_fingerprint.OK:
             print("Model created")
         else:
             scanner.set_led(color=2, mode=2)  # Sets led to flashing red
             print("An error occurred")
             return False
         if location < 1 or location > 199:
             print("Invalid storage location")
         i = scanner.store_model(location)
         if i != adafruit_fingerprint.OK:
             scanner.set_led(color=2, mode=2)  # Sets led to flashing red
             print("An error occurred storing the fingerprint")
             return False
         scanner.set_led(color=3, mode=4) # Turns led off
     return True

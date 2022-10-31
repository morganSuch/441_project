import time
import adafruit_fingerprint
import serial

uart = serial.Serial("/dev/serial0", baudrate=57600, timeout=1) # Configures the serial connection
scanner = adafruit_fingerprint.Adafruit_Fingerprint(uart)

location = 1 # Location the fingerprint is stored on the fingerprint scanner

for img in range(1,3):
    while True:
        i = scanner.get_image()
        if i == adafruit_fingerprint.OK:
            scanner.set_led(color=2, mode=2) # Sets led to flashing blue
            break
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
        print("An error occurred")
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
        #return False
    if location < 1 or location > 199:
        print("Invalid storage location")
    i = scanner.store_model(location)
    if i != adafruit_fingerprint.OK:
        scanner.set_led(color=2, mode=2)  # Sets led to flashing red
        print("An error occurred storing the fingerprint")
        #return False
    scanner.set_led(color=3, mode=4) # Turns led off
    #return True

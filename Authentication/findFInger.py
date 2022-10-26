import adafruit_fingerprint
import serial

uart = serial.Serial("/dev/serial0", baudrate=57600, timeout=1) # Configures the serial connection
scanner = adafruit_fingerprint.Adafruit_Fingerprint(uart)

scanner.set_led(color=3, mode=3) # Sets led to purple

while scanner.get_image() != adafruit_fingerprint.OK:
    pass
if scanner.image_2_tz(1) != adafruit_fingerprint.OK:
    scanner.set_led(color=1, mode=2)
    print("An error occurred")
    #return False
if scanner.finger_search() != adafruit_fingerprint.OK:
    scanner.set_led(color=1, mode=3)
    print("Finger not found")
scanner.set_led(color=2, mode=3)
print("Finger found")
#return True
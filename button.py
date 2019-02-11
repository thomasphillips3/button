import RPi.GPIO as GPIO
import time

inPin = 8
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(inPin, GPIO.IN)

while True:
    value = GPIO.input(inPin)
    if value:
        print("pressed")
    else:
        print ("not pressed")
    time.sleep(0.1)
GPIO.cleanup()

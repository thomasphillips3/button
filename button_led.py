import RPi.GPIO as GPIO
import time

inPin = 8
ledPin = 7

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(inPin, GPIO.IN)
GPIO.setup(ledPin, GPIO.OUT)

while True:
    value = GPIO.input(inPin)
    if value:
        print("pressed")
        GPIO.output(ledPin, GPIO.HIGH)
    else:
        GPIO.output(ledPin, GPIO.LOW)
    time.sleep(0.1)
GPIO.cleanup()

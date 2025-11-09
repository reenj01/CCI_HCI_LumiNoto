import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

redPin = 12
greenPin = 13
bluePin = 19

GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

redPin = 12
greenPin = 13
bluePin = 19

GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)

def turnOff():
  GPIO.output(redPin, GPIO.HIGH)
  GPIO.output(greenPin, GPIO.HIGH)
  GPIO.output(bluePin, GPIO.HIGH)

def white():
  GPIO.output(redPin, GPIO.LOW)
  GPIO.output(greenPin, GPIO.LOW)
  GPIO.output(bluePin, GPIO.LOW)

def red():
  GPIO.output(redPin, GPIO.LOW)
  GPIO.output(greenPin, GPIO.HIGH)
  GPIO.output(bluePin, GPIO.HIGH)

def green():
  GPIO.output(redPin, GPIO.HIGH)
  GPIO.output(greenPin, GPIO.LOW)
  GPIO.output(bluePin, GPIO.HIGH)

def blue():
  GPIO.output(redPin, GPIO.HIGH)
  GPIO.output(greenPin, GPIO.HIGH)
  GPIO.output(bluePin, GPIO.LOW)

while True:
  turnOff()
  sleep(1)
  white()
  sleep(1)
  red()
  sleep(1)
  green()
  sleep(1)
  blue()
  sleep(1)
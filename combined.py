from gpiozero import Button, RGBLED, DigitalInputDevice
from signal import pause
from time import sleep

tilt = Button(26)
ldr_ai = DigitalInputDevice(23)
ldr_lamp = DigitalInputDevice(24)

led = RGBLED(red=17, green=27, blue=22)

try:
  while True:
    led.red = 1
    print (f"Tilt: {0 if tilt.value else 1}") # 1 = tilt 0 = no tilt
    print(f"LDR AI: {1 if ldr_ai.value else 0}") # 1 = light 0 = no light
    print(f"LDR Lamp: {1 if ldr_lamp.value else 0}") # 1 = light 0 = no light
    sleep(0.5)
except KeyboardInterrupt:
  led.close()
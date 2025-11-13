from gpiozero import RGBLED
from time import sleep
import math

# Define your RGB pins (BCM numbering)
led = RGBLED(red=17, green=27, blue=22)  # common cathode

# Duration in seconds for a full pulsating cycle
duration = 20
# Number of steps for smoothness
steps = 100
# Time to sleep between steps
step_time = duration / steps

try:
    for i in range(steps):
        # Generate smooth sinusoidal RGB values (0-1)
        r = (math.sin(math.pi * i / steps) + 0.0)  # adjust phase if needed
        g = (math.sin(math.pi * i / steps + 2*math.pi/3) + 0.0)
        b = (math.sin(math.pi * i / steps + 4*math.pi/3) + 0.0)

        # Normalize to 0-1
        r = max(0, min(1, r))
        g = max(0, min(1, g))
        b = max(0, min(1, b))

        led.color = (r, g, b)
        sleep(step_time)
finally:
    led.close()
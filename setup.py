# Imports
from machine import Pin, freq
from neopixel import NeoPixel

# Set clock speed
freq(240000000)

# Neopixel setup
PIN=6
NUM_PIXELS = 18
np1 = Pin(PIN, Pin.OUT)
neo1 = NeoPixel(np1, NUM_PIXELS)

# User input setup
pinBTN01=18
btn01 = Pin(pinBTN01, Pin.IN, Pin.PULL_UP)
DEBOUNCE_MS = 50
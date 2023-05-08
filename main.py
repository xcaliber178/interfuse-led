from machine import Pin, freq
from neopixel import NeoPixel
from time import sleep
from setup import *

freq(240000000)

PIN=6
np1 = Pin(PIN, Pin.OUT)
neo1 = NeoPixel(np1, NUM_PIXELS)
BTN=18
from effects import *

def set_brightness(pot):
    global brightness
    brightness = pot / 65535.0
    
    brightness = min(1.0, max(0.0, brightness))

#BUTTON TEST
interrupt_flag=0
pin = Pin(BTN,Pin.IN,Pin.PULL_UP)

def test():
    chase(neo1, RED)
    chase_backward(neo1, RED)
    interrupt_flag=0

def callback(pin):
    global interrupt_flag
    interrupt_flag=1
    test()

pin.irq(trigger=Pin.IRQ_FALLING, handler=callback)

while (True):
    while (True):
        set_brightness(60000)
        print(brightness)
        
        rainbow(neo1, 0.03)
        
        set_brightness(40000)
        print(brightness)
        
        rainbow_move(neo1, 0.03)
        
        set_brightness(20000)
        print(brightness)
        
        rainbow(neo1, 0.03)
        
        set_brightness(10000)
        print(brightness)
        
        rainbow_move(neo1, 0.03)
        
        set_brightness(5000)
        print(brightness)
        
        rainbow(neo1, 0.03)

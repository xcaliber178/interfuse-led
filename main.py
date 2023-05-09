# Imports
from machine import Timer
from time import sleep
from setup import *
from colors import *
from effects import *


cycle = -1
def cycle_effect():
    global cycle
    cycle += 1
    effect()

def button01(pin):
    tim = Timer(-1)
    tim.init(period=DEBOUNCE_MS, mode=Timer.ONE_SHOT, callback=lambda t: None)
    state = pin.value()
    if state == 0:
        cycle_effect()

btn01.irq(trigger=Pin.IRQ_FALLING, handler=button01)

def effect():
    global cycle
    if cycle == 0:
        rainbow(neo1)
    elif cycle == 1:
        chase(neo1, RED)
    elif cycle == 2:
        chase_backward(neo1, BLUE)
    elif cycle == 3:
        color_wipe_backward(neo1, GREEN)
    elif cycle == 4:
        color_wipe(neo1, YELLOW)
    elif cycle == 5:
        rainbow_move(neo1, 0.02)
    elif cycle == 6:
        breath(neo1, BLUE)

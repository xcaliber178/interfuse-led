import math
from time import sleep
from setup import *

def chase(np, color, delay=DELAY):
    global brightness
    for i in range(NUM_PIXELS):
        np[i] = tuple(int(brightness * c) for c in color)
        np.write()
        sleep(delay)
        np[i] = (0, 0, 0)
        
def chase_backward(np, color, delay=DELAY):
    global brightness
    for i in range(NUM_PIXELS - 1, -1, -1):
        np[i] = tuple(int(brightness * c) for c in color)
        np.write()
        sleep(delay)
        np[i] = (0, 0, 0)

def color_wipe(np, color, delay=DELAY):
    global brightness
    for i in range(NUM_PIXELS):
        np[i] = tuple(int(brightness * c) for c in color)
        np.write()
        sleep(delay)

def color_wipe_backward(np, color, delay=DELAY):
    for i in range(NUM_PIXELS - 1, -1, -1):
        np[i] = tuple(int(brightness * c) for c in color)
        np.write()
        sleep(delay)

def breath(np, colors, delay=DELAY):
    global brightness
    for i in range(500):
        brightness = abs(math.sin(i / 500 * math.pi))
        for j in range(NUM_PIXELS):
            color = tuple(int(brightness * c) for c in colors[j % len(colors)])
            np[j] = color
        np.write()
        sleep(delay)

def rainbow_move(np, delay=DELAY):
    global brightness
    for j in range(255):
        for i in range(NUM_PIXELS):
            pixel_index = (i * 256 // NUM_PIXELS) + j
            np[i] = tuple(int(brightness * c) for c in wheel(pixel_index & 255))
        np.write()
        sleep(delay)

def rainbow(np, delay=DELAY):
    global brightness
    for i in range(255):
        for j in range(NUM_PIXELS):
            idx = (i + j) & 255
            np[j] = tuple(int(brightness * c) for c in wheel(idx))
        np.write()
        sleep(delay)

def wheel(pos):
    if pos < 85:
        return (pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return (0, pos * 3, 255 - pos * 3)

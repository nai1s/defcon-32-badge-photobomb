
from machine import Pin
import neopixel
import time
import machine

num_pixels = 9
np = neopixel.NeoPixel(machine.Pin(4), num_pixels)

def all_same_color(color):
    for i in range(num_pixels):
        np[i] = color
    np.write()

def init_lights():
    # Initial colors
    np[0] = (255, 0, 0)
    np[1] = (255, 0, 0)
    np[2] = (255, 0, 0)
    np[3] = (255, 0, 0)
    np[4] = (255, 0, 0)
    np[5] = (255, 0, 0)
    np[6] = (255, 0, 0)
    np[7] = (255, 0, 0)
    np[8] = (255, 0, 0)
    np.write()
"""
ST7789 example for DC32 badge
"""

from lights import *
from ir import *

def main():
    init_lights()
    all_same_color((0, 255, 0))
    while True:
        time.sleep_ms(500)
        all_same_color((0, 0, 125))
        uart.write('hello')
        time.sleep_ms(500)
        received = uart.read(5)
        #print(received)
        if (received != None):
            print(received)
            all_same_color((125, 0, 0))
        else:
            all_same_color((0, 0, 0))
            
   #while(True):
   #     rainbow_cycle(0)  # Increase the number to slow down the rainbow

main()

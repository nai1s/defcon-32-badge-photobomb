import machine
from machine import UART, Pin
from lights import all_same_color
import time

ir_rx = machine.Pin(27, machine.Pin.IN)
ir_tx = machine.Pin(26, machine.Pin.OUT)
ir_sd = machine.Pin(7, machine.Pin.OUT)

ir_sd.value(0)

uart = UART(1)                         
uart.init(9600, bits=3, parity=None, stop=1, tx=ir_tx, rx=ir_rx) 

# attempted RX Handler, doesn't seem to work consistently

#def rx_handler(uart_inst):
#    received = uart_inst.read(10)
    
    
#uart.irq(handler=rx_handler(uart),trigger=UART.IRQ_RXIDLE)
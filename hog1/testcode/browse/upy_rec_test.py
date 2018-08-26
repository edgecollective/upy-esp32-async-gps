from machine import Pin
from machine import SPI

from upy_rfm9x import RFM9x

import time

sck=Pin(5)
mosi=Pin(18)
miso=Pin(19)
cs = Pin(12, Pin.OUT)
#reset=Pin(13)
led = Pin(13,Pin.OUT)


def blink(duration):
    led.value(1)
    time.sleep(duration)
    led.value(0)
    time.sleep(duration)

spi=SPI(2,baudrate=5000000,sck=sck,mosi=mosi,miso=miso)

resetNum=15

rfm9x = RFM9x(spi, cs, resetNum, 915.0)

print('listening ...')
rfm9x.receive(timeout=5.0)
if rfm9x.packet is not None:
    packet_text = str(rfm9x.packet, 'ascii')
    print('Received: {0}'.format(packet_text))
    print("RSSI:",rfm9x.rssi)
    blink(.2)
spi.deinit()

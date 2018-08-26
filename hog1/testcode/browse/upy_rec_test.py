from machine import Pin
from machine import SPI

from upy_rfm9x_1 import RFM9x

sck=Pin(5)
mosi=Pin(18)
miso=Pin(19)
cs = Pin(12, Pin.OUT)
#reset=Pin(13)

spi=SPI(2,baudrate=5000000,sck=sck,mosi=mosi,miso=miso)

resetNum=13

rfm9x = RFM9x(spi, cs, resetNum, 915.0)

print('listening ...')
rfm9x.receive(timeout=5.0)
if rfm9x.packet is not None:
    packet_text = str(rfm9x.packet, 'ascii')
    print('Received: {0}'.format(packet_text))
    print("RSSI:",rfm9x.rssi)
spi.deinit()

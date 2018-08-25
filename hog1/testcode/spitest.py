import board
import busio
import digitalio
import adafruit_rfm9x
from micropython import const


spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.GPIO2)
reset = digitalio.DigitalInOut(board.GPIO0)
rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 915.0)


print(rfm9x.rssi)

#address=const(0x80)

#_RH_RF95_REG_11_IRQ_FLAGS_MASK                    = const(0x11)

address=const(0x01) #-- seems constant across widgets

#address= _RH_RF95_REG_11_IRQ_FLAGS_MASK
# simple
#print(rfm9x._read_u8(address))

# more complex
#rfm9x._read_into(address, rfm9x._BUFFER, length=1)

# raw spi

import adafruit_bus_device.spi_device as spi_device

baudrate=5000000

my_device=spi_device.SPIDevice(spi,cs,baudrate=baudrate,polarity=0,phase=0)

buffa = bytearray(10)

def read_into(address, buf, length=None):
    if length is None:
        length = len(buf)
    with my_device as device:
        buf[0] = address & 0x7F
        device.write(buf, end=1)
        device.readinto(buf,end=length)

read_into(address,buffa,length=1)
print(buffa[0])




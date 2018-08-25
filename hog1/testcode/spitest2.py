import board
import busio
import digitalio
import adafruit_rfm9x
from micropython import const


spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.GPIO2)
reset = digitalio.DigitalInOut(board.GPIO0)
#rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 915.0)


#sprint(rfm9x.rssi)

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

buffa = bytearray(1)

buf=buffa
with my_device as poo:
    length=1
    buf[0] = address & 0x7F
    poo.write(buf,end=1)
    poo.readinto(buf,end=length)

print(buffa[0])

#buf=bytearray(1)
#with my_device as poo:
#    length=1
#    buf = address & 0x7F
#    poo.write(buf)
#    poo.readinto(buf)







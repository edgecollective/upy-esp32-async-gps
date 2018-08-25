
from machine import Pin
from machine import SPI
from micropython import const

#sck=Pin(18)
#mosi=Pin(32)
#miso=Pin(21)
#cs = Pin(12, Pin.OUT)
#reset=Pin(13)


cs = Pin(2, Pin.OUT)
cs.value(1)

address=const(0x01) #-- seems constant across widgets

#spi=SPI(2,baudrate=12500000,sck=sck,mosi=mosi,miso=miso)

spi = machine.SPI(1, baudrate=5000000, polarity=0, phase=0)

buf= bytearray(1)

length=1

buf[0]=address & 0x7F

cs.value(0)

spi.write(buf)
spi.readinto(buf)
cs.value(1)


print(buf[0])



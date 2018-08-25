
from machine import Pin
from machine import SPI
from micropython import const

sck=Pin(5)
mosi=Pin(18)
miso=Pin(19)
cs = Pin(12, Pin.OUT)
reset=Pin(13)


#cs = Pin(2, Pin.OUT)
cs.value(1)

address=const(0x02) #-- seems constant across widgets

spi=SPI(2,baudrate=5000000,sck=sck,mosi=mosi,miso=miso)

#spi = machine.SPI(1, baudrate=5000000, polarity=0, phase=0)

baudrate=5000000

#my_device=spi_device.SPIDevice(spi,cs,baudrate=baudrate,polarity=0,phase=0)


buffa= bytearray(10)

length=1

buffa[0]=address & 0x7F


#with my_device as device:
#    device.poo()


def read_into_simple(address, buf, length=None):
    print("---simple---")
    if length is None:
        length = len(buf)
    buffa[0] = address & 0x7F
    print("before:\n",buffa)
    writebuf=bytearray([buffa[0]])
    spi.write(writebuf)
    print("middle:\n",buffa)
    #newbuf=bytearray([buf[0]])
    #device.write(newbuf)
    #device.readinto(buf[0:length])
    newbuf=buf[0:length]
    spi.readinto(newbuf)
    buf[0:len(newbuf)]=newbuf
    print("after:\n",buffa)
        

#cs.value(0)
#spi.write(buffa)
#spi.readinto(buffa)
#cs.value(1)
#print(buffa[0])

cs.value(0)
read_into_simple(address,buffa,length=1)
cs.value(1)
print(buffa[0])



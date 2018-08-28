import sdcard, os
from machine import Pin
from machine import SPI

from upy_rfm9x import RFM9x

sck=Pin(23)
mosi=Pin(21)
miso=Pin(17)
cs = Pin(14, Pin.OUT)
spi1=SPI(1,baudrate=5000000,sck=sck,mosi=mosi,miso=miso)

sd = sdcard.SDCard(spi1, cs)
os.mount(sd,'/sd')
output=os.listdir('/sd')
print(output)


spi1.deinit()


# works!
sck2=Pin(5)
mosi2=Pin(18)
miso2=Pin(19)
cs2 = Pin(12, Pin.OUT)
spi1=SPI(1,baudrate=5000000,sck=sck2,mosi=mosi2,miso=miso2)


resetNum=15
cs2 = Pin(12, Pin.OUT)
rfm9x = RFM9x(spi1, cs2, resetNum, 915.0)

rssi=str(rfm9x.rssi)
print(rssi)

led = Pin(13,Pin.OUT)

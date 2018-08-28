import sdcard, os
from machine import Pin
from machine import SPI

from upy_rfm9x import RFM9x


sck=Pin(23)
mosi=Pin(21)
miso=Pin(17)
cs = Pin(14, Pin.OUT)

sck2=Pin(5)
mosi2=Pin(18)
miso2=Pin(19)
cs2 = Pin(12, Pin.OUT)
resetNum=15

# sd card
spi1=SPI(2)
spi1.deinit()
spi1.init(baudrate=5000000,sck=sck,mosi=mosi,miso=miso)
sd = sdcard.SDCard(spi1, cs)
os.mount(sd,'/sd')
output=os.listdir('/sd')
print(output)
os.umount('/sd')
spi1.deinit()

# sd card
spi1=SPI(2)
spi1.deinit()
spi1.init(baudrate=5000000,sck=sck,mosi=mosi,miso=miso)
sd = sdcard.SDCard(spi1, cs)
os.mount(sd,'/sd')
output=os.listdir('/sd')
print(output)
os.umount('/sd')
spi1.deinit()

# sd card
spi1=SPI(2)
spi1.deinit()
spi1.init(baudrate=5000000,sck=sck,mosi=mosi,miso=miso)
sd = sdcard.SDCard(spi1, cs)
os.mount(sd,'/sd')
output=os.listdir('/sd')
print(output)
os.umount('/sd')
spi1.deinit()

# sd card
spi1=SPI(2)
spi1.deinit()
spi1.init(baudrate=5000000,sck=sck,mosi=mosi,miso=miso)
sd = sdcard.SDCard(spi1, cs)
os.mount(sd,'/sd')
output=os.listdir('/sd')
print(output)
os.umount('/sd')
spi1.deinit()

# lora
spi2=SPI(1)
spi2.deinit()
spi2.init(baudrate=5000000,sck=sck2,mosi=mosi2,miso=miso2)
rfm9x = RFM9x(spi2, cs2, resetNum, 915.0)
rssi=str(rfm9x.rssi)
print(rssi)
spi2.deinit()




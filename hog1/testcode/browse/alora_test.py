#
# This is a picoweb example showing a Server Side Events (SSE) aka
# EventSource handling. All connecting clients get the same events.
# This is achieved by running a "background service" (a coroutine)
# and "pushing" the same event to each connected client.
#
import uasyncio

import asyn

import time

from machine import Pin
from machine import SPI

from upy_arfm9x import RFM9x

sck=Pin(5)
mosi=Pin(18)
miso=Pin(19)
cs = Pin(12, Pin.OUT)
#reset=Pin(13)
resetNum=15

led = Pin(13,Pin.OUT)

spi=SPI(2,baudrate=5000000,sck=sck,mosi=mosi,miso=miso)



rfm9x = RFM9x(spi, cs, resetNum, 915.0)


event_sinks = set()

#
# Webapp part
#

def callback(timeout):
    rfm9x.receive(timeout=5.0)
    if rfm9x.packet is not None:
            packet_text = str(rfm9x.packet, 'ascii')
            rssi=str(rfm9x.rssi)
            print('Received: {0}'.format(packet_text))
            print("RSSI:",rssi)

def blink(duration):
    led.value(1)
    time.sleep(duration)
    led.value(0)
    time.sleep(duration)


async def grab_radio():
    try:
        #await rfm9x.receive(timeout=5.0)
        await rfm9x.receive(timeout=5.0)
        if rfm9x.packet is not None:
            packet_text = str(rfm9x.packet, 'ascii')
            rssi=str(rfm9x.rssi)
            print('Received: {0}'.format(packet_text))
            print("RSSI:",rssi)
    except uasyncio.TimeoutError:
        print('got timeout')

async def foo():
    while True:
        await uasyncio.wait_for(grab_radio(),3)
        await uasyncio.sleep(2)
    

barrier = asyn.Barrier(3,callback,('Synch',))

async def killer(duration):
    await uasyncio.sleep(duration)

def callback(text):
    await rfm9x.receive(timeout=5.0)
    if rfm9x.packet is not None:
        packet_text = str(rfm9x.packet, 'ascii')
        rssi=str(rfm9x.rssi)
        print('Received: {0}'.format(packet_text))
        print("RSSI:",rssi)

async def report(barrier):
    for i in range(5):
        print('{} '.format(i), end='')
        await barrier
        
print('test')

barrier = asyn.Barrier(3, callback, ('Synch',))
loop = uasyncio.get_event_loop()
for _ in range(3):
    loop.create_task(report(barrier))
loop.run_until_complete(killer(2))
loop.close()

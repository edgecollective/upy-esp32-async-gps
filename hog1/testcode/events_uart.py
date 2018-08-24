#
# This is a picoweb example showing a Server Side Events (SSE) aka
# EventSource handling. All connecting clients get the same events.
# This is achieved by running a "background service" (a coroutine)
# and "pushing" the same event to each connected client.
#
import uasyncio as asyncio
from machine import UART
import picoweb
import network
import aswitch
import random

ssid = "jpl"
password =  "mars-adventure"
 
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
    pass

ip = station.ifconfig()

event_sinks = set()

class DEVICE():
    def __init__(self, uart_no = 4):
        self.uart = UART(2,baudrate=9600,rx=16,tx=17)
        self.loop = asyncio.get_event_loop()
        self.swriter = asyncio.StreamWriter(self.uart, {})
        self.sreader = asyncio.StreamReader(self.uart)
        loop = asyncio.get_event_loop()
        loop.create_task(self._run())

    async def _run(self):
        responses = ['Line 1', 'Line 2', 'Line 3', 'Goodbye']
        while True:
            res = await self.sreader.readline()
            rcmd=str(res.decode('UTF8')).strip()
            #print("got command:"+rcmd)
            if rcmd=='Run':
                #print("got run")
                response='i will run'
                await self.swriter.awrite("{}\r\n".format(response))
                await asyncio.sleep_ms(300)
            if rcmd=='Poo':
                #print("got poo")
                response='i will poo'
                await self.swriter.awrite("{}\r\n".format(response))
                await asyncio.sleep_ms(300)
            if rcmd=='Zip':
                #print("got zip")
                response='i will zip'
                await self.swriter.awrite("{}\r\n".format(response))
                await asyncio.sleep_ms(300)
            #for response in responses:
                #await self.swriter.awrite("{}\r\n".format(response))
                # Demo the fact that the master tolerates slow response.
                #await asyncio.sleep_ms(300)

# The master's send_command() method sends a command and waits for a number of
# lines from the device. The end of the process is signified by a timeout, when
# a list of lines is returned. This allows line-by-line processing.
# A special test mode demonstrates the behaviour with a non-responding device. If
# None is passed, no commend is sent. The master waits for a response which never
# arrives and returns an empty list.
class MASTER():
    def __init__(self, uart_no = 2, timeout=4000):
        self.uart = UART(1,baudrate=9600,rx=12,tx=13)
        self.timeout = timeout
        self.loop = asyncio.get_event_loop()
        self.swriter = asyncio.StreamWriter(self.uart, {})
        self.sreader = asyncio.StreamReader(self.uart)
        self.delay = aswitch.Delay_ms()
        self.response = []
        loop = asyncio.get_event_loop()
        loop.create_task(self._recv())

    async def _recv(self):
        while True:
            res = await self.sreader.readline()
            self.response.append(res)  # Append to list of lines
            self.delay.trigger(self.timeout)  # Got something, retrigger timer

    async def send_command(self, command):
        self.response = []  # Discard any pending messages
        if command is None:
            print('Timeout test.')
        else:
            await self.swriter.awrite("{}\r\n".format(command))
            #print('Command sent:', command)
        self.delay.trigger(self.timeout)  # Re-initialise timer
        while self.delay.running():
            await asyncio.sleep(1)  # Wait for 4s after last msg received
        return self.response
#
# Webapp part
#

def index(req, resp):
    yield from picoweb.start_response(resp)
    yield from resp.awrite("""\
<!DOCTYPE html>
<html>
<head>
<script>
var source = new EventSource("events");
source.onmessage = function(event) {
    document.getElementById("result").innerHTML = event.data + "<br>";
}
source.onerror = function(error) {
    console.log(error);
    document.getElementById("result").innerHTML = "EventSource error:" + error + "<br>";
}
</script>
</head>
<body>
<div id="result"></div>
</body>
</html>
""")


def events(req, resp):
    global event_sinks
    print("Event source %r connected" % resp)
    yield from resp.awrite("HTTP/1.0 200 OK\r\n")
    yield from resp.awrite("Content-Type: text/event-stream\r\n")
    yield from resp.awrite("\r\n")
    event_sinks.add(resp)
    return False


ROUTES = [
    ("/", index),
    ("/events", events),
]

#
# Background service part
#

def push_event(ev):
    global event_sinks
    to_del = set()

    for resp in event_sinks:
        try:
            await resp.awrite("data: %s\n\n" % ev)
        except OSError as e:
            print("Event source %r disconnected (%r)" % (resp, e))
            await resp.aclose()
            # Can't remove item from set while iterating, have to have
            # second pass for that (not very efficient).
            to_del.add(resp)

    for resp in to_del:
        event_sinks.remove(resp)


def push_count():
    i = 0
    commands=['Run','Poo','Zip']
    while 1:
        pick=random.randint(0,len(commands)-1)
        cmd=commands[pick]
        await push_event("command %s is: %s" % (i,cmd))
        await asyncio.sleep(1)
        res = await master.send_command(cmd)
        if res:
            for line in res:
                rep=str(line.decode('UTF8')).strip()
                await push_event("response %s is: %s" % (i,rep))
                await asyncio.sleep(1)
        i += 1
        await asyncio.sleep(1)


#import logging
#logging.basicConfig(level=logging.INFO)
#logging.basicConfig(level=logging.DEBUG)

loop = asyncio.get_event_loop()
master = MASTER()
device = DEVICE()
loop.create_task(push_count())

#app = picoweb.WebApp(__name__, ROUTES)
app = picoweb.WebApp(None, ROUTES)
# debug values:
# -1 disable all logging
# 0 (False) normal logging: requests and errors
# 1 (True) debug logging
# 2 extra debug logging
print("host:"+ip[0])
app.run(debug=-1,host=ip[0])

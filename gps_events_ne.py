#
# This is a picoweb example showing a Server Side Events (SSE) aka
# EventSource handling. All connecting clients get the same events.
# This is achieved by running a "background service" (a coroutine)
# and "pushing" the same event to each connected client.
#
import uasyncio
import picoweb
import network
import as_GPS
from machine import UART

uart=UART(2,baudrate=9600,rx=16,tx=17,timeout=10)
sreader = uasyncio.StreamReader(uart)  # Create a
gps = as_GPS.AS_GPS(sreader)  # Instantiate GPS

#ssid = "jpl"
#password =  "mars-adventure"
 
#station = network.WLAN(network.STA_IF)
#station.active(True)
#station.connect(ssid, password)

essid = "bob"
password = "uncle"
ap=network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=essid,password=password)


#while ap.isconnected() == False:
#    pass

ip = ap.ifconfig()

event_sinks = set()

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
    document.getElementById("result").innerHTML = event.data;
}
source.onerror = function(error) {
    console.log(error);
    document.getElementById("result").innerHTML = "EventSource error:" + error;
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
    while 1:
        lat="0"
        lon="0"
        await gps.data_received(position=True, altitude=True)
        lat=gps.latitude()
        lon=gps.longitude()
        ev_str="reading %s: lat = %s, lon = %s" % (i,lat,lon)
        #await push_event("%s" % i)
        await push_event(ev_str)
        i += 1
        await uasyncio.sleep(1)


#import logging
#logging.basicConfig(level=logging.INFO)
#logging.basicConfig(level=logging.DEBUG)

loop = uasyncio.get_event_loop()
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

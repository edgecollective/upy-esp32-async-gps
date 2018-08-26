import network
ssid = "jpl"
password =  "mars-adventure"
 
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

import os
os.mkdir('/lib')

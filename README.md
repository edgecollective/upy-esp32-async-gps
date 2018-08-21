# upy-esp32-async-gps

Need to place 'lib' folder on ESP32 via ampy.

## GPS

https://github.com/peterhinch/micropython-async/blob/master/gps/README.md

When running on feather huzzah 32, connected the GPS RX,TX to feather huzzah 32's RX,TX (pins 16,17).

## UART

https://github.com/peterhinch/micropython-async/blob/master/auart_hd.py

When running on feather huzzah 32, connected:

feather RX (pin 16) --> pin 13 (defined in code as TX)
feather TX (pin 17) --> pin 12 (defined in code as RX)




import bme280
from machine import I2C
from machine import Pin
i2c = I2C(-1, Pin(16), Pin(4))
b=bme280.BME280(i2c=i2c)
print(b.values)

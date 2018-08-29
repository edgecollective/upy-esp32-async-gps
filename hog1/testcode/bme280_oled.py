import bme280
from machine import I2C
from machine import Pin
import ssd1306
import time

i2c = I2C(-1, Pin(16), Pin(4))

b=bme280.BME280(i2c=i2c)
values=b.values
print(values)

oled = ssd1306.SSD1306_I2C(128, 32, i2c)
oled.fill(0)
oled.text(str(values),0,10)
oled.show()
time.sleep(2)

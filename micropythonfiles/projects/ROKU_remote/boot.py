
import time
import machine
import network
import webrepl
from machine import Pin, I2C, SoftI2C
from ssd1306 import SSD1306_I2C
import ssd1306
import framebuf
import connect


BUTTON_PIN_1 = 5
BUTTON_PIN_2 = 2
BUTTON_PIN_3 = 3
BUTTON_PIN_6 = 6

button_1 = Pin(BUTTON_PIN_1, Pin.IN, Pin.PULL_UP)
button_2 = Pin(BUTTON_PIN_2, Pin.IN, Pin.PULL_UP)
prev_button_state_1 = 1
prev_button_state_2 = 1

webrepl.start()
i2c = SoftI2C(sda=Pin(8), scl=Pin(10))
display = ssd1306.SSD1306_I2C(128, 64, i2c)
display.rotate(2)
display.fill(0)
display.fill_rect(0, 0, 32, 32, 1)
display.fill_rect(2, 2, 28, 28, 0)
display.vline(9, 8, 22, 1)
display.vline(16, 2, 22, 1)
display.vline(23, 8, 22, 1)
display.fill_rect(26, 24, 2, 4, 1)
display.text('MicroPython', 40, 0, 1)
display.text('SSD1306', 40, 12, 1)
display.text('OLED 128x64', 40, 24, 1)
display.show()









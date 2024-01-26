import time
import machine
import network
import webrepl
from machine import Pin, I2C, SoftI2C
from ssd1306 import SSD1306_I2C
import ssd1306
import framebuf
import connect
#
#
#
#
#
#
#

def init_oled():
    i2c = I2C(0, scl=Pin(10), sda=Pin(8), freq=400000)
    oled = SSD1306_I2C(128, 64, i2c)
    return oled

def is_button_1_pressed():
    global prev_button_state_1
    button_state = button_1.value()
    pressed = button_state == 0 and prev_button_state_1 == 1
    prev_button_state_1 = button_state
    return pressed

def is_button_2_pressed():
    global prev_button_state_2
    button_state = button_2.value()
    pressed = button_state == 0 and prev_button_state_2 == 1
    prev_button_state_2 = button_state
    return pressed
#
#
#
#
def border():
    oled = init_oled()
    oled.fill(0)
    oled.rotate(2)
    text = "$h3LL0NTH3B0RD3R2023!!!"
    for i, char in enumerate(text):
        oled.text(char, i * 8, 0)
    oled.show()
#
def blink(iterations):
    i2c = SoftI2C(sda=Pin(8), scl=Pin(10))
    display = ssd1306.SSD1306_I2C(128, 64, i2c)

    for _ in range(iterations):
        # Rotate the display 180 degrees
        display.rotate(2)

        # Your existing code for the scene
        display.fill(0)
        display.rect(10, 10, 107, 43, 1)
        x_pos = [12, 38, 64, 90]
        percentages = [.25, .50, .75, 1.0]
        joke_texts = [
            "You",
            "Have",
            "Been",
            "Hacked!!"
        ]

        for ctr in range(4):
            display.fill_rect(x_pos[ctr], 11, 24, 40, 1)
            display.fill_rect(0, 56, 128, 40, 0)
            display.text("{:.0%} {}".format(percentages[ctr], joke_texts[ctr]), 11, 56)
            display.show()
            time.sleep_ms(1000)

        for ctr in range(4):
            display.fill_rect(x_pos[ctr], 11, 24, 40, 0)

        display.fill_rect(0, 56, 128, 40, 0)
        display.show()
        display.fill(0)

def button_click_handler(pin):
    print("Button on PIN {} clicked!".format(pin))

def configure_buttons():
    BUTTON_PIN_1 = 5
    BUTTON_PIN_2 = 2
    BUTTON_PIN_3 = 3
    BUTTON_PIN_0 = 6
    button_pins = [BUTTON_PIN_0, BUTTON_PIN_1, BUTTON_PIN_2, BUTTON_PIN_3]
    for pin in button_pins:
        machine.Pin(pin, machine.Pin.IN, machine.Pin.PULL_UP)

    # Attach interrupt handlers for button clicks
    for pin in button_pins:
        machine.Pin(pin, machine.Pin.IN, machine.Pin.PULL_UP).irq(trigger=machine.Pin.IRQ_FALLING, handler=lambda p: button_click_handler(p))

def run_button_click_detection():
    BUTTON_PIN_1 = 5
    BUTTON_PIN_2 = 2
    BUTTON_PIN_3 = 3
    BUTTON_PIN_0 = 6
    configure_buttons()

    # Keep the program running
    while True:
        time.sleep(1)


def display_command_list(commands, selected_index):
    def init_oled():
        i2c = I2C(0, scl=Pin(10), sda=Pin(8), freq=400000)
        oled = SSD1306_I2C(128, 64, i2c)
        return oled

    oled = init_oled()
    oled.fill(0)
    oled.rotate(2)

    for i, cmd in enumerate(commands):
        if i == selected_index:
            # Highlight the selected item
            oled.fill_rect(0, i * 10, 128, 10, 1)  # Assumes a 128x64 display
            oled.text(cmd, 0, i * 10, 0)
        else:
            oled.text(cmd, 0, i * 10)

    oled.show()

# Example usage with button control
commands = ["select", "up", "down", "left", "right"]
selected_index = 0  # Initial selected index (select command)
display_command_list(commands, selected_index)

while True:
    if Pin(5).value() == 0:  # Down button pressed
        selected_index = (selected_index + 1) % len(commands)
        display_command_list(commands, selected_index)
        break







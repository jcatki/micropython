from time import sleep_ms
from ssd1306 import SSD1306_I2C
from machine import Pin, I2C
import network


class OLED(SSD1306_I2C):
    def __init__(self, i2c=I2C(0, scl=Pin(15, Pin.OUT, Pin.PULL_UP), sda=Pin(4, Pin.OUT, Pin.PULL_UP), freq=1000000)):
        # turn on Vext
        Vext = Pin(21, Pin.OUT)
        Vext.off()
        sleep_ms(100)
        # reset OLED
        OLED_RST = Pin(16, Pin.OUT)
        OLED_RST.off()
        sleep_ms(50)
        OLED_RST.on()
        super().__init__(128, 64, i2c)

    def test(self):
        self.fill(0)
        self.fill_rect(0, 0, 32, 32, 1)
        self.fill_rect(2, 2, 28, 28, 0)
        self.vline(9, 8, 22, 1)
        self.vline(16, 2, 22, 1)
        self.vline(23, 8, 22, 1)
        self.fill_rect(26, 24, 2, 4, 1)
        self.text("MicroPython", 40, 0, 1)
        self.text("SSD1306", 40, 12, 1)
        self.text("OLED 128x64", 40, 24, 1)
        self.show()

    def display_wifi(self):
        self.fill(0)
        self.text("Scan...", 0, 0, 1)
        self.show()

        sta_if = network.WLAN(network.STA_IF)
        sta_if.active(True)
        _wifi = sta_if.scan()

        self.fill(0)
        self.text(str(len(_wifi)) + " Networks", 0, 0, 1)
        for i in range(min(5,len(_wifi))):
            self.text(str(_wifi[i][3]) + " " + (_wifi[i][0]).decode("utf-8"), 0, 12+12*i, 1)
        self.show()

import adafruit_ssd1306
import board
import busio
from digitalio import DigitalInOut
import time 

spi = busio.SPI (board.SCK, MOSI=board.MOSI, MISO=board.MISO)

dc_pin = DigitalInOut(board.D16)
reset_pin = DigitalInOut(board.D19)
cs_pin = DigitalInOut(board.D8)

oled = adafruit_ssd1306.SSD1306_SPI(128, 64, spi, dc_pin, reset_pin, cs_pin)

oled.fill(0)
oled.show()

oled.pixel (0,16,1)
oled.show()

oled.text ('Hello',0,10,0)
oled.show()
time.sleep (5)
oled.invert(True)


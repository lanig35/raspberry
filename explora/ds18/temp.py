from flask import Flask, render_template

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

app = Flask(__name__)

def getTemp ():
    sonde = open ('/sys/bus/w1/devices/28-00000ab5dfc6/temperature')
    valeur = sonde.read()
    sonde.close ()
    temp = round(float(valeur)/1000,2)
    oled.fill (0)
    oled.text (str(temp),0,10,1)
    oled.show ()
    return (temp)

@app.route('/temp')
def index():
    return render_template ('index.html', temp=getTemp())



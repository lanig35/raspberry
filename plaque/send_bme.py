import smbus
import time
import bme280

bus = smbus.SMBus (1)

DEVICE_ADDRESS = 0x10
BME_REGISTER = 0x04

while True:
    temperature,pressure,humidity = bme280.readBME280All()
    val = bytearray (str(temperature))
    bus.write_i2c_block_data (DEVICE_ADDRESS, BME_REGISTER, list(val)) 
    print (temperature)
    time.sleep (15)

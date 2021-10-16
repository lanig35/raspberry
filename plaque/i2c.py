import smbus
import time

bus = smbus.SMBus (1)

DEVICE_ADDRESS = 0x10
TEMP_REGISTER = 0x02
LUM_REGISTER = 0x03

while True:
    register = bus.read_i2c_block_data (DEVICE_ADDRESS, TEMP_REGISTER, 2)
    sensor = register[0]<<8 | register[1]
    tension = (sensor / 1024.0) * 3.3
    temperature = (tension - 0.5) * 100

    # pour faire clignoter la LED
    time.sleep (1)

    register = bus.read_i2c_block_data (DEVICE_ADDRESS, LUM_REGISTER, 2)
    lumiere = register[0]<<8 | register[1]
    print ('t: {} - l: {}'.format(round(temperature,2), lumiere))
    time.sleep (5)

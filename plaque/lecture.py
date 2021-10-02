import serial

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
ser.flush()

try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline()
            print(line)
except KeyboardInterrupt:
    ser.close ()

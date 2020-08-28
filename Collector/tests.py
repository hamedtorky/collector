from django.test import TestCase
import time
# Create your tests here.
import serial
import binascii

ser = serial.Serial('/dev/ttyACM1', 9600, timeout=1)
while True:
    ser.write('1'.encode())
    buff1 = ser.read(213)
    line= buff1.hex() 
    line = [line[i:i+2] for i in range(0, len(line), 2)]
    print (line)
    # if buff1.decode('UTF-8') == '1B3B1B':
    #     buff = ser.read(500)
    #     line = "{}{}".format(buff1.decode('utf-8'), buff.decode('utf-8'))
    #     n =2 
    #     line = [line[i:i+n] for i in range(0, len(line), n)]
    #     print(len(line))
    #     break

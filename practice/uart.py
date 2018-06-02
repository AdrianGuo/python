import serial
ser=serial.Serial("COM12",115200,timeout=0.5)
for i in range(0,100-1):
    ser.write('hello11111111111\r\n'.encode())
    print(ser.readline());
ser.close()

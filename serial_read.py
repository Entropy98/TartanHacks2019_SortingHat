import serial
ser = serial.Serial('/dev/ttyACM0')
print(ser.name)

timeout=0
while(timeout<19200):
  print(ser.readline())
  timeout+=1
  

import serial
ser = serial.Serial('/dev/ttyACM0')
print(ser.name)

timeout=0
while(timeout<19200):
  feed=[x.strip() for x in ser.readline().split(',')]
  delta=feed[1]
  theta=feed[2]
  lowalpha=feed[3]
  highalpha=feed[4]
  lowbeta=feed[5]
  highbeta=feed[6]
  lowgamma=feed[7]
  highgamma=feed[8]
  attention=feed[9]
  meditation=feed[10]
  print("delta: "+delta)
  print("theta: "+theta)
  print("low alpha: "+lowalpha)
  print("high alpha: "+highalpha)
  print("low beta: "+lowbeta)
  print("high beta: "+highbeta)
  print("low gamma: "+lowgamma)
  print("high gamma: "+highgamma)
  print("attention: "+attention)
  print("meditation: "+meditation)
  print("----------")
  timeout+=1
  

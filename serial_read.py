import serial
from threshold import *
from scipy.fftpack import fft, ifft
import numpy as np

def organize(feed):
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
    """
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
    print("----------")"""
    return (int(highgamma) + int(lowgamma))/(1+int(lowbeta) + int(highbeta)) + int(meditation)/(int(attention)+1) + int(lowalpha)

def read_data(ser, x):
    try:
        if x==1:
            return
        vals = []
        timeout = 0
        while(timeout<15):
          feed=[x.strip() for x in (str(ser.readline(), 'utf-8')).split(',')]
          vals.append(feed)
          timeout+= 1
        vals = [organize(feed) for feed in vals]
        vals = np.array(vals)
        #vals = fft(vals)
        vals = vals.tolist()
        place(vals)
        read_data(ser, x+1)
    except:
        read_data(ser, x)

def serial_date():
    #ser = serial.Serial('/dev/ttyACM0')
    ser = serial.Serial('COM8')
    print(ser.name)
    read_data(ser, 0)

if __name__ == '__main__':
    serial_date()

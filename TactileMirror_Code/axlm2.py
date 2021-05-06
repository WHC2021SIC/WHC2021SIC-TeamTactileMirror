# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# MMA8452Q
# This code is designed to work with the MMA8452Q_I2CS I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/content/Accelorometer?sku=MMA8452Q_I2CS#tabs-0-product_tabset-2

import smbus2
import time
import matplotlib.pyplot as plt
import math
from numpy.fft import fft, ifft
import numpy as np

fig = plt.figure()

xData = []
yData = []
zData = []
xAxis = [] # time

# Get I2C bus
bus = smbus2.SMBus(1)


# MMA8452Q address, 0x1D(28)

# Select Control register, 0x2A(42)
# 0x00(00) -->	StandBy mode (call standby mode before changing settings)
bus.write_byte_data(0x1D, 0x2A, 0x00)
# Select Control register, 0x2A(42)
# 0x01(01) -->	Active mode
bus.write_byte_data(0x1D, 0x2A, 0x01)

# Select Configuration register, 0x0E(14)
# 0x00(00)-->	Set range to +/- 2g; 0x01 --> +/- 4g; 0x10 +/- 8g
bus.write_byte_data(0x1D, 0x0E, 0x00)

time.sleep(0.5)

# MMA8452Q address, 0x1D(28)
# Read data back from 0x00(0), 7 bytes
# Status register, X-Axis MSB, X-Axis LSB, Y-Axis MSB, Y-Axis LSB, Z-Axis MSB, Z-Axis LSB

# 
# plt.plot(0, 0, 'ro')
# plt.plot(0, 0, 'go')
# plt.plot(0, 0, 'bo')

dataXPrev = 0
dataYPrev = 0
dataZPrev = 0
prevTime = 0

toc = 0
tic = time.time()
tic2 = time.time()
toc = time.time() -tic
toc2 = 0

rms = []
rms_window = []
while toc2 < 10.0:
    
    toc = time.time() -tic
    
    if toc > 0.001:

        data = bus.read_i2c_block_data(0x1D, 0x00, 7)

    # Convert the data
        xAccl = (data[1] * 256 + data[2]) / 16
        if xAccl > 2047 :
            xAccl -= 4096

        yAccl = (data[3] * 256 + data[4]) / 16
        if yAccl > 2047 :
            yAccl -= 4096

        zAccl = (data[5] * 256 + data[6]) / 16
        if zAccl > 2047 :
            zAccl -= 4096
     
        x_g =  (xAccl - (-1024)) * (1 - (-1)) / (1024 - (-1024)) + (-1) # convert to g
        y_g =  (yAccl - (-1024)) * (1 - (-1)) / (1024 - (-1024)) + (-1)
        z_g =  (zAccl - (-1024)) * (1 - (-1)) / (1024 - (-1024)) + (-1)
            

    
        
      #  plt.plot([prevTime, toc2], [dataXPrev, x_g], 'r-')
       # plt.plot([prevTime, toc2], [dataYPrev, y_g], 'g-')
      #  plt.plot([prevTime, toc2], [dataZPrev, z_g], 'b-')

        
        dataXPrev = x_g
        dataYPrev = y_g
        dataZPrev = z_g
        prevTime = toc2
        
        toc2 = time.time() - tic2
        #plt.xlim(0, 1+toc2)
        #plt.pause(0.001)
       
        #plt.tight_layout()
        
        xData.append(x_g)
        yData.append(y_g)
        zData.append(z_g)
        tic = time.time()

#         print (toc)


       # print(x_g, y_g, z_g)
        rms = math.sqrt(math.pow(x_g, 2) + math.pow(y_g, 2) + math.pow(z_g, 2))
        prevRMS = rms
       # print(rms)
        toc = (time.time() - tic)#*1000 elapsed time in ms
        plt.plot([prevTime, toc2], [prevRMS, rms], 'r')
        plt.xlim(0, 1+toc2)
        plt.pause(0.001)
#plt.show()
#print(xData)


# X = fft(xData)
# N = len(X)
# print(len(X))
# n = np.arange(N)
# sr = 500 # Hz
# T = N/sr
# frequency = n/T 

# plt.stem(frequency[1:2500], np.abs(X)[1:2500], 'b', \
#          markerfmt=" ", basefmt="-b")
# plt.xlabel('Freq (Hz)')
# plt.ylabel('FFT Amplitude |X(freq)|')

plt.show()
# Output data to screenpinout
#     print ("Acceleration in X-Axis : %d" %x_g)
#     print ("Acceleration in Y-Axis : %d" %y_g)
#     print ("Acceleration in Z-Axis : %d" %z_g)
#     toc = (time.time() - tic)*1000 # elapsed time in ms
#     print (toc)





     




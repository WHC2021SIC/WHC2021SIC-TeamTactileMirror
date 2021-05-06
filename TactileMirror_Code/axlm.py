# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# MMA8452Q
# This code is designed to work with the MMA8452Q_I2CS I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/content/Accelorometer?sku=MMA8452Q_I2CS#tabs-0-product_tabset-2

import smbus2
import time
import matplotlib.pyplot as plt
import math

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

tic = time.time()
# 
# plt.plot(0, 0, 'ro')
# plt.plot(0, 0, 'go')
# plt.plot(0, 0, 'bo')

dataXPrev = 0
dataYPrev = 0
dataZPrev = 0
prevTime = 0

while True:
    

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
        

    toc = (time.time() - tic)#*1000 elapsed time in ms
#     print (toc)
    
    plt.plot([prevTime, toc], [dataXPrev, x_g], 'r-')
    plt.plot([prevTime, toc], [dataYPrev, y_g], 'g-')
    plt.plot([prevTime, toc], [dataZPrev, z_g], 'b-')

    
    dataXPrev = x_g
    dataYPrev = y_g
    dataZPrev = z_g
    prevTime = toc
    
    plt.xlim(0, 1+toc)
    plt.pause(0.001)
   
    plt.tight_layout()


   # print(x_g, y_g, z_g)
    rms = math.sqrt(math.pow(x_g, 2) + math.pow(y_g, 2) + math.pow(z_g, 2))
    print(rms)
    
    
plt.show()
# Output data to screen
#     print ("Acceleration in X-Axis : %d" %x_g)
#     print ("Acceleration in Y-Axis : %d" %y_g)
#     print ("Acceleration in Z-Axis : %d" %z_g)
#     toc = (time.time() - tic)*1000 # elapsed time in ms
#     print (toc)





     



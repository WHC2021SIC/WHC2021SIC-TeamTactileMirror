import smbus2
import time
import math
import numpy as np
import RPi.GPIO as GPIO
import socket
import struct

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
UDP_PORT2 = 5006

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: Transmitting accelerometer data..")

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) #

sock2 = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) #

# set up the I2C accelerometer readings 
# Get I2C bus
bus = smbus2.SMBus(1)

# MMA8452Q address, 0x1D(28)
# Select Control register, 0x2A(42)
# 0x00(00) -->  StandBy mode (call standby mode before changing settings)
bus.write_byte_data(0x1D, 0x2A, 0x00)
# Select Control register, 0x2A(42)
# 0x01(01) -->  Active mode
bus.write_byte_data(0x1D, 0x2A, 0x01)

# Select Configuration register, 0x0E(14)
# 0x00(00)--> set range to +/- 2g (0x01 --> +/- 4g; 0x10 +/- 8g)
bus.write_byte_data(0x1D, 0x0E, 0x00)

time.sleep(0.5)

# read time to set condition for the readings
toc = 0
tic = time.time()

while True:
    
    toc = time.time() -tic
    
    if toc > 0.001:
        
        # read accelerometer data
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
            
        # map data to -1/1 g range
        x_g =  (xAccl - (-1024)) * (1 - (-1)) / (1024 - (-1024)) + (-1) 
        y_g =  (yAccl - (-1024)) * (1 - (-1)) / (1024 - (-1024)) + (-1)
        z_g =  (zAccl - (-1024)) * (1 - (-1)) / (1024 - (-1024)) + (-1)
        
        # compute rms
        rms = math.sqrt(math.pow(x_g, 2) + math.pow(y_g, 2) + math.pow(z_g, 2))
 
        # compute roll
        roll = math.atan(y_g / (math.sqrt(math.pow(x_g, 2) + math.pow(z_g, 2)))) * 180 / math.pi
    
        tic = time.time()
        
        rmsPacked = struct.pack('f', rms)
        rollPacked = struct.pack('f', roll)
        
        sock.sendto(rmsPacked, (UDP_IP, UDP_PORT))
        sock2.sendto(rollPacked, (UDP_IP, UDP_PORT2))
        #print(roll)


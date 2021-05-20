import smbus2
import time
import matplotlib.pyplot as plt
import math
from numpy.fft import fft, ifft
import numpy as np
from scipy import signal
from scipy.signal import find_peaks

import RPi.GPIO as GPIO
from time import sleep

ledpin = 12				# PWM pin connected to LED

GPIO.setwarnings(False)			#disable warnings
GPIO.setmode(GPIO.BOARD)		#set pin numbering system
GPIO.setup(ledpin,GPIO.OUT)

freq = 1
pi_pwm = GPIO.PWM(ledpin,freq)
#create PWM instance with frequency
pi_pwm.start(0)				#start PWM of required Duty Cycle 

import asyncio


fig = plt.figure()


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

xData = []
yData = []
zData = []
xAxis = [] # time

dataXPrev = 0
dataYPrev = 0
dataZPrev = 0
prevTime = []
prevRMS = []
prevFreq = []
mean = []
prevDuty=[]
toc = 0
tic = time.time()
toc = time.time() -tic

toc2 = 0
tic2 = time.time()

prevRMSr = []
arrayRMSr = []
peaksr = []

prev_dx = []
prevRMS = []

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        #print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(0.001)
        f *= i
    #print(f"Task {name}: factorial({number}) = {f}")
    return f



async def runGPIO():
	while toc2 < 5.0:


		for i in range(20):
  
			toc = time.time() -tic
			  
			if toc > 0.001:
			
				data = np.random.uniform(15,250,[7,1]) #bus.read_i2c_block_data(0x1D, 0x00, 7) 
				
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
				rms = math.sqrt(math.pow(x_g, 2) + math.pow(y_g, 2) + math.pow(z_g, 2))
				prevTime.append(toc2)
				toc2 = time.time() - tic2
				tic = time.time()
				toc = (time.time() - tic)#*1000 elapsed time in ms      
				prevRMS.append(rms)

            











async def main():
    # Schedule three calls *concurrently*:
    L = await asyncio.gather(
        runGPIO(),
        runGPIO(),
    )
    print(L[0])
    print(L[1])

asyncio.run(main())
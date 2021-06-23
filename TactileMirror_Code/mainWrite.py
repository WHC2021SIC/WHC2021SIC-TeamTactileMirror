import time
import math
import numpy as np
from scipy.signal import find_peaks
import RPi.GPIO as GPIO
import socket
import struct

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
UDP_PORT2 = 5006

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

sock2 = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock2.bind((UDP_IP, UDP_PORT2))


# set up PWM channels
vt_pin = 12             # PWM pin connected to LRA1 (left)
vt_pin2 = 32            # PWM pin connected to LRA2 (right)
freq = 10  # baseline frequency
duty = 45  # duty

GPIO.setwarnings(False)         #disable warnings
GPIO.setmode(GPIO.BOARD)        #set pin numbering system
GPIO.setup(vt_pin,GPIO.OUT)

pi_pwm = GPIO.PWM(vt_pin,freq) #create PWM instance first LRA (left)
pi_pwm.start(duty)             #start PWM 
pi_pwm.ChangeDutyCycle(duty)   #provide duty cycle 

GPIO.setwarnings(False)         #disable warnings
GPIO.setmode(GPIO.BOARD)        #set pin numbering system
GPIO.setup(vt_pin2,GPIO.OUT)

pi_pwm2 = GPIO.PWM(vt_pin2,freq) #create PWM instance for second LRA (right)
pi_pwm2.start(duty)              #start PWM 
pi_pwm2.ChangeDutyCycle(duty)    #provide duty cycle 
    
# read time to set condition for the readings
toc = 0
tic = time.time()

prevRMS = []
roll_out = []

while True:
    
    toc = time.time() -tic
    
    if toc > 0.001:
    
      rmsPacked, addr = sock.recvfrom(16) # buffer size is 16 bytes
      rollPacked, addr = sock2.recvfrom(16)
      
      rms = struct.unpack('f', rmsPacked)
      roll = struct.unpack('f', rollPacked)
    
      prevRMS.append(rms)
      roll_out = np.array(roll)
      
      if len(prevRMS) == 60: # every 60 readings (~120 ms)
        
         rms_out = [item for sublist in prevRMS for item in sublist]

         peaks, _ = find_peaks(rms_out, height=1.13)

         freq = len(peaks)/0.02

         if freq <= 99:
             freq = 10
         elif freq >= 800:
             freq = 800
     
         # print(freq) # uncomment to print out the output frequency
        
         if roll_out > 0:
             pi_pwm.ChangeFrequency(freq)
             time.sleep(0.05)
             pi_pwm2.ChangeFrequency(freq)
         elif roll_out < 0:
             
             pi_pwm2.ChangeFrequency(freq)
             time.sleep(0.05)
             pi_pwm.ChangeFrequency(freq)            
   
         prevRMS = []
         
         
      tic = time.time()


time_value = None
led = None

import pigpio
import time

time_value = 0.5
led = LED(2)
print("Tone Generator")

while True:
	led.on()
	print("Tone on")
	time.sleep(time_value)
	led.off()
	print("Tone off")
	time.sleep(time_value)
	
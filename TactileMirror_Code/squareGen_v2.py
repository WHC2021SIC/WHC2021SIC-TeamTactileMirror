import wave
import struct
import math 

SAMPLE_LEN=20000

wave_output = wave.open('sine.wav', 'wb')
wave_output.setparams((2, 2, 44100, 0, 'NONE', 'not compressed'))

for i in range(0, SAMPLE_LEN):
        #value = random.randint(-32767, 32767)
        value = math.sin(0.2*i) * 20000
        value=int(value)
        packed_value = struct.pack('h', value)
        wave_output.writeframes(packed_value)
        wave_output.writeframes(packed_value)
        print(i)
wave_output.close()
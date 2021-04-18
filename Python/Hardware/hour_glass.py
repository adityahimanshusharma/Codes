import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BOARD)
led={3,5,7,11,12,13,15,18}
for i in range (0,8):
    gpio.setup(led[i],gpio.OUT)
while(1):
    i=8
    j=0
    while(i<8):
        while(j<i+1):
            gpio.output(led[j],1)
            time.sleep(1)
            i=i+1
            j=j+1
    while(i<8):
        gpio.output(led[i],0)
    

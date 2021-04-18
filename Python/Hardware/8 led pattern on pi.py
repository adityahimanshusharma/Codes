led=(3,5,7,11,12,13,15,18)
import RPi.GPIO as gpio
from time import *
gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
i=0
for i in range(0,8):
    gpio.setup(led[i],gpio.OUT)
while(1):
    i=0
    j=7
    while(i<8 and j>=0):
        gpio.output(led[i],1)
        gpio.output(led[j],1)
        sleep(0.2)
        gpio.output(led[i],0)
        gpio.output(led[j],0)
        i=i+1
        j=j-1


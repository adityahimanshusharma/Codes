import RPi.GPIO as gpio
from time import *
gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
a=3
gpio.setup(a,gpio.OUT)
while(1):
    gpio.output(a,1)
    sleep(0.2)
    gpio.output(a,0)
    sleep(0.2)

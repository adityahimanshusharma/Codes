import RPi.GPIO as gpio
from time import *
gpio.setwarnings(0)
gpio.setmode(gpio.BOARD)
gpio.setup(3,gpio.IN)
gpio.setup(5,gpio.OUT)
while(1):
    while(gpio.input(3)==0):
        gpio.output(5,0)
    while(gpio.input(3)==1):
        gpio.output(5,1)

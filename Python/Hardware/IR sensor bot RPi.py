import RPi.GPIO as gpio
gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
gpio.setup(12,gpio.IN)
gpio.setup(13,gpio.IN)
gpio.setup(3,gpio.OUT)
gpio.setup(5,gpio.OUT)
gpio.setup(7,gpio.OUT)
gpio.setup(11,gpio.OUT)
while(1):
    while(gpio.input(12)==1 & gpio.input(13)==1):   #forward
        gpio.output(3,1)
        gpio.output(5,0)
        gpio.output(7,0)
        gpio.output(11,1)
    while(gpio.input(12)==1 & gpio.input(13)==0):   #right
        gpio.output(3,1)
        gpio.output(5,0)
        gpio.output(7,0)
        gpio.output(11,0)
    while(gpio.input(12)==0 & gpio.input(13)==1):   #left
        gpio.output(3,0)
        gpio.output(5,0)
        gpio.output(7,0)
        gpio.output(11,1)
    while(gpio.input(12)==0 & gpio.input(13)==0):   #stop
        gpio.output(3,0)
        gpio.output(5,0)
        gpio.output(7,0)
        gpio.output(11,0)
    

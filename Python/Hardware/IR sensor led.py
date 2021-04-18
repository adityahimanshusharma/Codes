import RPi.GPIO as gpio
gpio.warnings(0)
gpio.setup(3,gpio.OUT)
gpio.setup(5,gpio.IN)
while(1):
    if(gpio.input(5)==1):
        gpio.output(3,1)
    else:
        gpio.output(3,0)

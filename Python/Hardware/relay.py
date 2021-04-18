import RPi.GPIO as gpio
gpio.setmode(gpio.BOARD)
gpio.setup(7,gpio.OUT)
gpio.setwarnings(0)
while(1):
    gpio.output(7,1)
    time.sleep(2)
    gpio.output(7,0)
    time.sleep(2)

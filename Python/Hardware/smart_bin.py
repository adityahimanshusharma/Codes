import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
trig=3
echo=5
buzz=7
ir=13
motr=11
motor=12
gpio.setup(echo,gpio.IN)        #echo
gpio.setup(trig,gpio.OUT)       #trigger
gpio.setup(buzz,gpio.OUT)       #buzzer
gpio.setup(ir,gpio.IN)
gpio.setup(motr,gpio.OUT)#ir input
gpio.setup(motor,gpio.OUT)
while(1):
    gpio.output(trig,1)
    time.sleep(0.00001)
    gpio.output(trig,0)
    timei=time.time()
    while(gpio.input(echo)==1):
        timef=time.time()       #instant value of time get saved
        duration=timef-timei
        dist=duration*17050
    if(gpio.input(ir)==1):      #someone is near
        if(dist*100<500):       #garbage full
            gpio.output(buzz,1) #buzzer on
            time.sleep(2)
            gpio.output(buzz,0)
        else:
            gpio.output(motr,1) #lid open
            gpio.output(motr,0)
            #time.sleep(3)
            gpio.output(motor,1) #lid close
            gpio.output(motor,0)

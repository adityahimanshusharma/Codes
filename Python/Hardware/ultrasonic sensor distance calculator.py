import RPi.GPIO as gpio
gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
trig=5
echo=3
gpio.setup(echo,gpio.IN) #echo
gpio.setup(trig,gpio.OUT)#trigger
while(1):
    gpio.output(trig,1)
    time.sleep(0.00001)
    gpio.output(trig,0)
    timei=time.time()
    while(gpio.input(echo)==1):
        timef=time.time()#instant value of time get saved
        duration=timef-timei
        dist=duration*17050
        print(dist,' cm')

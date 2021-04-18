import RPi.GPIO as gpio
gpio.setmode(gpio.BOARD)
gpio.setwarnings(0)
ir1=3
ir2=5
lit=12
gpio.setup(lit,gpio.OUT)
gpio.setup(ir1,gpio.IN)
gpio.setup(ir2,gpio.IN)
cnt=0
print(cnt)
while(1):
    while((gpio.input(ir1)==1)&(gpio.input(ir2)==0)):     #Entry
        print(1)
        while((gpio.input(ir1)==1)&(gpio.input(ir2)==1)):
            print(2)
            while((gpio.input(ir1)==0)&(gpio.input(ir2)==1)):
                print(3)
                while((gpio.input(ir1)==0)&(gpio.input(ir2)==0)):
                    print(4)
                    cnt=cnt+1
                    print(cnt)
                    break
    while((gpio.input(ir1)==0)&(gpio.input(ir2)==1)):     #Exit
        print(4)
        while((gpio.input(ir1)==1)&(gpio.input(ir2)==1)):
            print(3)
            while((gpio.input(ir1)==1)&(gpio.input(ir2)==0)):
                print(2)
                while((gpio.input(ir1)==0)&(gpio.input(ir2)==0)):
                    print(1)
                    cnt=cnt-1
                    print(cnt)
                    break
    if(cnt>0):
        gpio.output(lit,1)
    else:
        gpio.output(lit,0)

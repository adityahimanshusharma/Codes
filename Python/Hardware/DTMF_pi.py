import RPi.GPIO as gpio
gpio.setmode(gpio.BOARD)
gpio.setwarnings(0)
dta=[3,5,7,8]
for i in range (0,4):
    gpio.setup(dta[i],gpio.IN)
while(1):
    a=gpio.input(3)
    b=gpio.input(5)<<1
    c=gpio.input(7)<<2
    d=gpio.input(8)<<3
    x=a+b+c+d
    if(x==1):
        print('1')
    if(x==2):
        print('2')
    if(x==3):
        print('3')
    if(x==4):
        print('4')
    if(x==5):
        print('5')
    if(x==6):
        print('6')
    if(x==7):
        print('7')
    if(x==8):
        print('8')
    if(x==9):
        print('9')
    if(x==11):
        print('*')
    if(x==10):
        print('0')
    if(x==12):
        print('#')
    

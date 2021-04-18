import RPi.GPIO as gpio
gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
rs=3
rw=5
en=7
d={11,12,13,15,18,19,21,22}
def strg(ch):
    for i in ch:
        lcd_data(i)
def lcd_port(num):
    a=1 #masking
    i=0 #list increment
    while a<129:
        if(num&a==a):
            gpio.output(d[i],1)
        else:
            gpio.output(d[i],0)
        a=a*2
        i=i+1
def lcd_data(x): #data function
    lcd_port(ord(x))
    gpio.output(rs,1)
    gpio.output(rw,0)
    gpio.output(en,1)
    time.sleep(0.001)
    gpio.output(en,0)
def lcd_cmd(x):  # command function
    lcd_port(x)
    gpio.output(rs,0)
    gpio.output(rw,0)
    gpio.output(en,1)
    time.sleep(0.001)
    gpio.output(en,0)
def lcd_init():
    lcd_cmd(0x01) #lcd clear
    lcd_cmd(0x80) #cursor 1st position
    lcd_cmd(0x38) #lcd 8 bit mode
    lcd_cmd(0x06) #auto increment
    lcd_cmd(0x0c) #cursor blinking off
i=0
while i<8:
    gpio.setup(d[i],gpio.OUT)
    i=i+1
gpio.setup(rs,gpio.OUT)
gpio.setup(rw,gpio.OUT)
gpio.setup(en,gpio.OUT)
lcd_init()
lcd_cmd(0x85)
strg("ADITYA :)")

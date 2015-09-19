import time
import random
import RPi.GPIO as GPIO

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT) #set up GPIO pins as outputs
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

i = 0

while i < 30: #allows to only run for a certain amount of time
    x = random.randint(11,15) #picks a random pattern
    y = random.randint(11,15)

    if(x != y and x != 14 and y != 14): #avoid pin 14 and similar LEDs
        GPIO.output(x, GPIO.HIGH) #turn random LED on
        GPIO.output(y, GPIO.HIGH)
        time.sleep(0.15) #pause
        GPIO.output(x,GPIO.LOW) #turn random LED off
        GPIO.output(y,GPIO.LOW)
        i=i+1

#HOW TO RUN FROM TERMINAL:   ~/Desktop $ sudo python blink.py 

import RPi.GPIO as GPIO

inPin = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(inPin, GPIO.IN)

while True:
    value = GPIO.input(inPin)
    if value:
        print "Not Pressed"
    else:
        print "Pressed"

GPIO.cleanup()
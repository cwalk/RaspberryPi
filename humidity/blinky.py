import RPi.GPIO as GPIO             ## Import GPIO Library
import time                         ## Import time library (for 'sleep')

pin = 7                             ## Work on pin 7
GPIO.setmode(GPIO.BOARD)            ## Use BOARD pin numbering
GPIO.setup(pin, GPIO.OUT)           ## Set pin 7 to OUTPUT

for i in range (0,20):
    GPIO.output(pin.GPIO.HIGH)      ## Turn on GPIO pin (HIGH)
        time.sleep(1)               ## Wait 1 second
        GPIO.output(pin.GPIO.LOW)   ## Turn off GPIO pin (LOW)
        time.sleep(1)               ## Wait 1 second

GPIO.cleanup()                      ## Cleanup
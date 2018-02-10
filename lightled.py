# Simple script to light LED on Elecrow stack board
# https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/

import time

import RPi.GPIO as GPIO

PIN = 25

GPIO.setmode(GPIO.BCM)

# Set pin 25 at OUTPUT
GPIO.setup(PIN, GPIO.OUT) 

for x in range(0, 10):
    print("turning LED on")
    GPIO.output(PIN, GPIO.HIGH) 
    time.sleep(2)

    print("turning LED off")
    GPIO.output(PIN, GPIO.LOW)
    time.sleep(2) 

GPIO.cleanup()

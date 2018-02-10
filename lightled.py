# Simple script to light LED on Elecrow stack board
# https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/

import time

import RPi.GPIO as GPIO

PIN_GREEN = 22
PIN_RED = 25

GPIO.setmode(GPIO.BCM)

# Set pins for as OUTPUT
GPIO.setup(PIN_GREEN, GPIO.OUT)
GPIO.setup(PIN_RED, GPIO.OUT)

for x in range(0, 10):
    if x % 2 == 0:
        pin = PIN_GREEN
        led = "green"
    else:
        pin = PIN_RED
        led = "red"

    print("turning %s LED on" % led)
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(2)

    print("turning %s LED off" % led)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(2)

GPIO.cleanup()

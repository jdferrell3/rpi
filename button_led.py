# Simple script to light LED when button is depressed
# on Elecrow stack board

# https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/

import time

import RPi.GPIO as GPIO

PIN_GREEN = 22
PIN_BUTTON = 21

GPIO.setmode(GPIO.BCM)

# Set pins for OUTPUT
GPIO.setup(PIN_GREEN, GPIO.OUT)

# Set pins for INPUT
GPIO.setup(PIN_BUTTON, GPIO.IN)

for x in range(0, 10):
    depressed = GPIO.input(PIN_BUTTON)
    print("depressed: %s" % depressed)
    if depressed:
        pin = PIN_GREEN
        led = "green"

        print("turning %s LED on" % led)
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(2)

        print("turning %s LED off" % led)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(2)
    time.sleep(2)
GPIO.cleanup()

import RPi.GPIO as GPIO
import time

# set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

# set up GPIO pin
relay_pin = 17  # change this to the GPIO pin you connected the relay to
GPIO.setup(relay_pin, GPIO.OUT)

# turn on the relay
GPIO.output(relay_pin, GPIO.HIGH)

# wait for 1 second
time.sleep(1)

# turn off the relay
GPIO.output(relay_pin, GPIO.LOW)

# clean up GPIO
GPIO.cleanup()

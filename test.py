import RPi.GPIO as GPIO
import time

PIN = 10   # pin fisico 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Test button started")

try:
    while True:
        state = GPIO.input(PIN)

        if state == 0:
            print("PRESSED")
        else:
            print("RELEASED")

        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()

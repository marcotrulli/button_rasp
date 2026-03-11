import RPi.GPIO as GPIO
import time
from config import BUTTON_PIN, BOUNCE_TIME

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

last_state = GPIO.input(BUTTON_PIN)

print("Button reader started")

try:
    while True:
        state = GPIO.input(BUTTON_PIN)

        if state != last_state:
            time.sleep(BOUNCE_TIME)
            state = GPIO.input(BUTTON_PIN)

            if state == GPIO.LOW:
                print("BUTTON PRESSED")
            else:
                print("BUTTON RELEASED")

            last_state = state

        time.sleep(0.01)

except KeyboardInterrupt:
    print("Stopping program")

finally:
    GPIO.cleanup()

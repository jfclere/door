# External module imports
import RPi.GPIO as GPIO
import time

# relays
out1 = 21
out2 = 20

# switch input (zero when pushed)
up = 26
down = 16

# Pin Setup:
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(up, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Switch up
GPIO.setup(down, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Switch down

GPIO.setup(out1, GPIO.OUT) # Relay 1 pin set as outout
GPIO.setup(out2, GPIO.OUT) # Relay 2 pin set as output

# When press go to zero (should be 1).
while True:
    action = False
    time.sleep(0.1)
    rup = GPIO.input(up)
    rdown = GPIO.input(down)
    # default to up
    if rup == 0:
       # up is pressed Switch up and action.
       GPIO.output(out1, GPIO.HIGH)
       GPIO.output(out2, GPIO.LOW) 
       action = True
    if rdown == 0:
       # down is pressed Switch down and action.
       GPIO.output(out1, GPIO.LOW)
       GPIO.output(out2, GPIO.LOW) 
       action = True
    if action == False:
       GPIO.output(out2, GPIO.HIGH) 

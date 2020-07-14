# External module imports
import RPi.GPIO as GPIO
import time

# relays
out1 = 21
out2 = 21

# switch
up = 26
down = 16

# Pin Setup:
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(up, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Switch up
GPIO.setup(down, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Switch down

GPIO.setup(out1, GPIO.OUT) # Relay 1 pin set as outout
GPIO.setup(out2, GPIO.OUT) # Relay 2 pin set as output

while True:
    rup = GPIO.input(up)
    rdown = GPIO.input(down)
    time.sleep(1)
    print("up : ", rup, " down: ", rdown);

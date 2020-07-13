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
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(in1, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Switch 1
GPIO.setup(in2, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Switch 2

GPIO.setup(ledPin, GPIO.OUT) # LED pin set as output
GPIO.setup(pwmPin, GPIO.OUT) # PWM pin set as output

while true:
    rup = GPIO.input(up)
    rdown = PIO.input(down)
    time.sleep(1)
    print("up : ", rup, " down: ", rdown);

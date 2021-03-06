# External module imports
import RPi.GPIO as GPIO
import time
import pwd
import grp
import os

# relays
out1 = 20
out2 = 21

# switch input (zero when pushed)
up = 26
down = 16

# Write the button status in the status file.
def write_status(status):
    filename = "/tmp/status.txt"
    try:
        os.remove(filename)
    except OSError as error:
        print("Error: ", error)
    f = open(filename,"w+")
    f.write(status)
    f.close()
    uid = pwd.getpwnam("apache").pw_uid
    gid = grp.getgrnam("apache").gr_gid
    os.chown(filename, uid, gid)

# the command from httpd
def read_cmd():
    try:
        f = open("/tmp/cmd.txt","r")
        data = f.read()
        f.close()
        os.remove("/tmp/cmd.txt")
        return data.strip('\n')
    except:
        return "NONE"

# put blinds up
def do_up():    
    # Switch up and action.
    GPIO.output(out1, GPIO.HIGH)
    GPIO.output(out2, GPIO.HIGH) 

# put blinds down
def do_down():    
    # Switch down and action.
    GPIO.output(out1, GPIO.HIGH)
    GPIO.output(out2, GPIO.LOW) 

# Pin Setup:
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(up, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Switch up
GPIO.setup(down, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Switch down

GPIO.setup(out1, GPIO.OUT) # Relay 1 pin set as outout
GPIO.setup(out2, GPIO.OUT) # Relay 2 pin set as output

# When press go to zero (should be 1).
status = "NONE"
while True:
    action = False
    time.sleep(0.1)
    rup = GPIO.input(up)
    rdown = GPIO.input(down)
    # default to up
    if rup == 0:
       # up is pressed
       action = True
       newstatus = "UP"
    if rdown == 0:
       # down is pressed
       action = True
       newstatus = "DOWN"
    if action == False:
       GPIO.output(out1, GPIO.LOW) 
       newstatus = "NONE"
    if newstatus != status:
       status = newstatus
       write_status(status)
       if status == "UP":
          do_up()
       elif status == "DOWN":
          do_down()
    else:
       # nothing from the buttom (unchanged)
       cmd = read_cmd()
       if cmd == "UP":
          do_up()
          time.sleep(90)
       elif cmd == "DOWN":
          do_down()
          time.sleep(90)
       elif cmd == "LIGHT":
          do_up()
          time.sleep(0.2)
          GPIO.output(out1, GPIO.LOW)
       elif cmd == "DARK":
          do_down()
          time.sleep(0.2)
          GPIO.output(out1, GPIO.LOW)

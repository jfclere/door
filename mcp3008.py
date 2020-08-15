#!/usr/bin/python3
 
import spidev
import time
import os
import pycurl
from io import BytesIO 

# get user/password from env
auth=os.environ.get('AUTH')

def SendBlindsUp():
  b_obj = BytesIO() 
  crl = pycurl.Curl() 

  # Set URL value
  crl.setopt(crl.URL, 'https://jfclere.ddns.net/cgi-bin/blinds.cgi?UP')
  crl.setopt(pycurl.HTTPAUTH, pycurl.HTTPAUTH_BASIC)
  crl.setopt(pycurl.USERPWD, auth)

  # Write bytes that are utf-8 encoded
  crl.setopt(crl.WRITEDATA, b_obj)

  # Perform a file transfer 
  crl.perform() 

  # End curl session
  crl.close()

  # Get the content stored in the BytesIO object (in byte characters) 
  get_body = b_obj.getvalue()

  # Decode the bytes stored in get_body to HTML and check for 'Doing UP be patient'.
  body_string = get_body.decode('utf8')
  if (body_string.find('Doing UP be patient') == -1):
    print("Error: ", body_string)
 
# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000
 
# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data
 
# Function to convert data to voltage level,
# rounded to specified number of decimal places.
def ConvertVolts(data,places):
  volts = (data * 3.3) / float(1023)
  volts = round(volts,places)
  return volts

# Convert the volts into meter per second
# Copied from https://gitlab.com/fkumro/ex_windspeed.git (./lib/ex_windspeed/conversions.ex)
def ConvertVoltsTomMS(volts):
  return (volts - 0.4) / 1.6 * 32.4
 
# Define sensor channels
wind_channel = 0
 
# Define delay between readings
delay = 5
 
while True:
 
  # Read the wind sensor data
  wind_level = ReadChannel(wind_channel)
  wind_volts = ConvertVolts(wind_level,2)
  wind_ms = ConvertVoltsTomMS(wind_volts)
 
  # Print out results
  print("Wind: {} ({}V) ({}ms)".format(wind_level,wind_volts,wind_ms))

  #value to send the blinds up (probably 20 ms = 75 km/h)
  if wind_ms > 20:
     SendBlindsUp()
 
  # Wait before repeating loop
  time.sleep(delay)

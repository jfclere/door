#!/usr/bin/python
 
import spidev
import time
import os
 
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
ref_channel  = 1
 
# Define delay between readings
delay = 5
 
while True:
 
  # Read the wind sensor data
  wind_level = ReadChannel(wind_channel)
  wind_volts = ConvertVolts(wind_level,2)
  wind_ms = ConvertVoltsTomMS(wind_volts)
 
  # Read the reference sensor data
  ref_level = ReadChannel(ref_channel)
  ref_volts = ConvertVolts(ref_level,2)
 
  # Print out results
  print "--------------------------------------------"
  print("Wind: {} ({}V) ({}ms)".format(wind_level,wind_volts,wind_ms))
  print("Ref : {} ({}V)".format(ref_level,ref_volts))

  #value to send the blinds up (probably 20 ms = 75 km/h)
 
  # Wait before repeating loop
  time.sleep(delay)

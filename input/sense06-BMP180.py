#!/usr/bin/python
# -*- coding: utf-8 -*-

## by Konrad Keck

import Adafruit_BMP.BMP085 as BMP085
#from envirophat import weather
#import datetime
from datetime import datetime
from datetime import timedelta 
import sqlite3 as lite
import sys

#################################################
#################################################

## Source & 
source_name = 'FreyrTST 1'
source_description = 'Test RPi3 - Freyr - Longterm Test'

## location
loc_lat = 53.304130
loc_long = 9.706472
loc_description = 'test indoor'

## Periphery
periphery_name = 'BMP180'
periphery_type = 'sensor'
periphery_description = 'Temperature & Pressure'
periphery_device_description = 'tst'

## measure target
measure_target_type = 'climate' ## general type
measure_target_name = 'weather' ## 'yes' 'none' 'other'
measure_target_description = 'picking up weather data about climate' 

## Other Qualities
outdoors_name = 'no'  ## 'yes' 'none' 'other'
provider_type = 'RPi3'   ## 'REST API' 
data_quality = 99

#################################################
#################################################

def roundTime(dt=None, roundTo=60):
   """Round a datetime object to any time laps in seconds
   dt : datetime object, default now.
   roundTo : Closest number of seconds to round to, default 1 minute.
   Author: Thierry Husson 2012 - Use it as you want but don't blame me.
   """
   if dt == None : dt = datetime.now()
   seconds = (dt - dt.min).seconds
   # // is a floor division, not a comment on following line:
   rounding = (seconds+roundTo/2) // roundTo * roundTo
   return dt + timedelta(0,rounding-seconds,-dt.microsecond)

#################################################
#################################################

# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola

# Default constructor will pick a default I2C bus.
#
# For the Raspberry Pi this means you should hook up to the only exposed I2C bus
# from the main GPIO header and the library will figure out the bus number based
# on the Pi's revision.
#
# For the Beaglebone Black the library will assume bus 1 by default, which is
# exposed with SCL = P9_19 and SDA = P9_20.
pin = 0x77
# sensor = BMP085.BMP085(address=pin)
# sensor = BMP085.BMP085()

# Optionally you can override the bus number:
#sensor = BMP085.BMP085(busnum=2)
# You can also optionally change the BMP085 mode to one of BMP085_ULTRALOWPOWER,
# BMP085_STANDARD, BMP085_HIGHRES, or BMP085_ULTRAHIGHRES.  See the BMP085
# datasheet for more details on the meanings of each mode (accuracy and power
# consumption are primarily the differences).  The default mode is STANDARD.
# sensor = BMP085.BMP085(mode=BMP085.BMP085_ULTRALOWPOWER, address=pin)
# sensor = BMP085.BMP085(mode=BMP085_STANDARD, address=pin)
# sensor = BMP085.BMP085(mode=BMP085.BMP085_HIGHRES, address=pin)
# sensor = BMP085.BMP085(mode=BMP085.BMP085_ULTRAHIGHRES, address=pin)

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
now1 = datetime.now()
utc1 = datetime.utcnow()
# raw_temp = sensor.read_raw_temp()
# raw_press = sensor.read_raw_pressure()
temp = sensor.read_temperature()
press = sensor.read_pressure()
# alt = sensor.read_altitude()
# sl_press = sensor.read_sealevel_pressure()
utc2 = datetime.utcnow()
offset_utc = str(roundTime(now1,roundTo=30*60) - roundTime(utc1,roundTo=30*60))
duration = (utc2-utc1)
duration2 = (float(duration.microseconds) / 10**6) + duration.seconds + (((duration.days * 24) * 60) * 60)

# print raw_temp
# print raw_press
# print str(temp) + '/ {0:0.10f}'.format(temp)
# print str(press) + '/ {0:0.11f}'.format(press)
# print str(alt) + '/ {0:0.12f}'.format(alt)
# print str(sl_press) + '/ {0:0.13f}'.format(sl_press)
#
# print
# print weather.temperature()
# print weather.pressure()
# print weather.altitude()

sys.exit(duration2)

#################################################
#################################################

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!

try:

    connection = lite.connect('freyr.db', isolation_level=None)
    cursor = connection.cursor()
    
    #################################################
    # Outdoors
    ## ID (auto)
    ## name (none, outdoor, indoor, other)  
    cursor.execute("CREATE TABLE IF NOT EXISTS outdoors(id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("SELECT max(id) FROM outdoors WHERE name LIKE ?", ([outdoors_name]))
    outdoors_id = cursor.fetchone()[0]
    if outdoors_id is None:
        cursor.execute("INSERT INTO outdoors(name) VALUES (?)", ([outdoors_name]))
        cursor.execute('SELECT max(id) FROM outdoors')
        outdoors_id = cursor.fetchone()[0]
    
    #################################################
    # Data Quality
    ## ID (auto)
    ## name (none, fine, maverick, invalid)  
    cursor.execute("CREATE TABLE IF NOT EXISTS data_quality(id INTEGER PRIMARY KEY, name TEXT)")
    
    #################################################
    # Provider Types
    ## ID (auto)
    ## Type (REST API, RPi3, RPi0)  
    cursor.execute("CREATE TABLE IF NOT EXISTS provider_types(id INTEGER PRIMARY KEY, type TEXT)")
    cursor.execute("SELECT max(id) FROM provider_types WHERE type LIKE ?", ([provider_type]))
    provider_type_id = cursor.fetchone()[0]
    if provider_type_id is None:
        cursor.execute("INSERT INTO provider_types(type) VALUES (?)", ([provider_type]))
        cursor.execute('SELECT max(id) FROM provider_types')
        provider_type_id = cursor.fetchone()[0]
    
    #################################################
    # Periphery Types
    ## ID (auto)
    ## Type (Sensor, Motor, LED, ...)   
    cursor.execute("CREATE TABLE IF NOT EXISTS periphery_types(id INTEGER PRIMARY KEY, type TEXT)")
    cursor.execute("SELECT max(id) FROM periphery_types WHERE type LIKE ?", ([periphery_type]))
    periphery_type_id = cursor.fetchone()[0]
    if periphery_type_id is None:
        cursor.execute("INSERT INTO periphery_types(type) VALUES (?)", ([periphery_type]))
        cursor.execute('SELECT max(id) FROM periphery_types')
        periphery_type_id = cursor.fetchone()[0]
    
    #################################################
    # Location
    ## ID (auto)
    ## lat
    ## long
    ## outdoors (ID)
    ## description (in/out, garden, etc.)
    #location_id
    cursor.execute("CREATE TABLE IF NOT EXISTS location(id INTEGER PRIMARY KEY, lat REAL, long REAL, outdoors INTEGER, description TEXT)")
    cursor.execute("SELECT max(id) FROM location WHERE lat = ? AND long = ? AND outdoors = ? AND description LIKE ?", ([loc_lat, loc_long, outdoors_id, loc_description]))
    location_id = cursor.fetchone()[0]
    if location_id is None:
        cursor.execute("INSERT INTO location(lat, long, outdoors, description) VALUES (?, ?, ?, ?)", ([loc_lat, loc_long, outdoors_id, loc_description]))
        cursor.execute('SELECT max(id) FROM location')
        location_id = cursor.fetchone()[0]
    
    #################################################
    # Source
    ## ID (auto)
    ## name
    ## location (id)
    ## provider (device / api)
    ## description
    cursor.execute("CREATE TABLE IF NOT EXISTS source(id INTEGER PRIMARY KEY, name TEXT, location INTEGER, provider_type INTEGER, description TEXT)")
    cursor.execute("SELECT max(id) FROM source WHERE name = ? AND location = ? AND provider_type LIKE ? AND description LIKE ?", ([source_name, location_id, provider_type_id, source_description]))
    source_id = cursor.fetchone()[0]
    if source_id is None:
        cursor.execute("INSERT INTO source(name, location, provider_type, description) VALUES (?, ?, ?, ?)", ([source_name, location_id, provider_type_id, source_description]))
        cursor.execute('SELECT max(id) FROM source')
        source_id = cursor.fetchone()[0]
    
    #################################################
    # Peripheries
    ## ID (auto)
    ## name 
    ## type 
    ## description (i.e. readings)
    #periphery_id
    cursor.execute("CREATE TABLE IF NOT EXISTS periphery(id INTEGER PRIMARY KEY, name TEXT, periphery_type INTEGER, description TEXT, gpio TEXT)") 
    cursor.execute("SELECT max(id) FROM periphery WHERE name = ? AND periphery_type = ? AND description LIKE ? AND gpio = ?", ([periphery_name, periphery_type_id, periphery_description, pin]))
    periphery_id = cursor.fetchone()[0]
    if periphery_id is None:
        cursor.execute("INSERT INTO periphery(name, periphery_type, description, gpio) VALUES (?, ?, ?, ?)", ([periphery_name, periphery_type_id, periphery_description, pin]))
        cursor.execute('SELECT max(id) FROM periphery')
        periphery_id = cursor.fetchone()[0]
    
    #################################################
    # Periphery Device
    ## ID (auto)
    ## Periphery Type (ID)
    ## description (i.e. readings)
    #sensor_id
    cursor.execute("CREATE TABLE IF NOT EXISTS periphery_device(id INTEGER PRIMARY KEY, periphery INTEGER, description TEXT)")    
    cursor.execute("SELECT max(id) FROM periphery_device WHERE periphery = ? AND description LIKE ?", ([periphery_id, periphery_device_description]))
    sensor_id = cursor.fetchone()[0]
    if sensor_id is None:
        cursor.execute("INSERT INTO periphery_device (periphery, description) VALUES (?, ?)", ([periphery_id, periphery_device_description]))
        cursor.execute('SELECT max(id) FROM periphery_device')
        sensor_id = cursor.fetchone()[0]
    
    #################################################
    # Measures
    ## ID (auto)
    ## absolute_min
    ## absolute_max
    ## name (i.e Celsious)
    ## symbol (i.e. °C)
    ## type_full (i.e. temperature)
    ## type_abbr (i.e. temp)
    #measure_id
    cursor.execute("CREATE TABLE IF NOT EXISTS measures(id INTEGER PRIMARY KEY, name TEXT, sign INTEGER, type_full TEXT, type_abbr TEXT, absolute_min REAL, absolute_max REAL)")    
    
    measure_name = 'celsius'
    measure_sign = u'\u2103' #.encode('utf8')  #'°C'
    measure_type_full = 'temperature'
    measure_type_abbr = 'temp'
    measure_absolute_min = (273.15 * (-1))
    measure_absolute_max = None
    cursor.execute("SELECT max(id) FROM measures WHERE (name LIKE ? OR sign LIKE ?) AND type_full LIKE ? AND (type_abbr LIKE ? OR absolute_min = ? OR absolute_max = ?)", ([measure_name, measure_sign, measure_type_full, measure_type_abbr, measure_absolute_min, measure_absolute_max]))
    temp_measure_id = cursor.fetchone()[0]
    if temp_measure_id is None:
        cursor.execute("INSERT INTO measures(name, sign, type_full, type_abbr, absolute_min, absolute_max) VALUES (?, ?, ?, ?, ?, ?)", ([measure_name, measure_sign, measure_type_full, measure_type_abbr, measure_absolute_min, measure_absolute_max]))
        cursor.execute('SELECT max(id) FROM measures WHERE type_abbr LIKE ?', ([measure_type_abbr]))
        temp_measure_id = cursor.fetchone()[0]
    
    measure_name = 'pascal'
    measure_sign = 'Pa'
    measure_type_full = 'pressure'
    measure_type_abbr = 'press'
    measure_absolute_min = None
    measure_absolute_max = None
    cursor.execute("SELECT max(id) FROM measures WHERE (name LIKE ? OR sign LIKE ?) AND type_full LIKE ? AND (type_abbr LIKE ? OR absolute_min = ? OR absolute_max = ?)", (measure_name, measure_sign, measure_type_full, measure_type_abbr, measure_absolute_min, measure_absolute_max))
    press_measure_id = cursor.fetchone()[0]
    if press_measure_id is None:
        cursor.execute("INSERT INTO measures(name, sign, type_full, type_abbr, absolute_min, absolute_max) VALUES (?, ?, ?, ?, ?, ?)", (measure_name, measure_sign, measure_type_full, measure_type_abbr, measure_absolute_min, measure_absolute_max))
        cursor.execute('SELECT max(id) FROM measures WHERE type_abbr LIKE ?', ([measure_type_abbr]))
        press_measure_id = cursor.fetchone()[0]
    
    #################################################
    # read_log
    ## ID (auto)
    ## sensor (ID)
    ## source (ID)
    ## utc_start
    ## utc_end
    ## timezone
    ## duration2 (secs)    
    cursor.execute("CREATE TABLE IF NOT EXISTS read_log(id INTEGER PRIMARY KEY, sensor INTEGER, source INTEGER, utc_start TIMESTAMP, utc_end TIMESTAMP, offset_utc TIMESTAMP, duration_sec REAL)")
    if press is not None or temp is not None:
        cursor.execute("INSERT INTO read_log(sensor, source, utc_start, utc_end, offset_utc, duration_sec) VALUES (?, ?, ?, ?, ?, ?)", (sensor_id, source_id, utc1, utc2, offset_utc, duration2))
        cursor.execute('SELECT max(id) FROM read_log')
        new_log = cursor.fetchone()[0]
	
    #################################################
    # measure_target_types
    ## ID (auto)
    ## measure_target_type
    cursor.execute("CREATE TABLE IF NOT EXISTS measure_target_types(id INTEGER PRIMARY KEY, measure_target_type TEXT)")
    cursor.execute("SELECT max(id) FROM measure_target_types WHERE measure_target_type LIKE ?", ([measure_target_type]))
    measure_target_type_id = cursor.fetchone()[0]
    if measure_target_type_id is None:
        cursor.execute("INSERT INTO measure_target_types(measure_target_type) VALUES (?)", ([measure_target_type]))
        cursor.execute('SELECT max(id) FROM measure_target_types')
        measure_target_type_id = cursor.fetchone()[0]
    
    #################################################
    # measure_target
    ## ID (auto)
    ## name
    ## description (additional information)
    cursor.execute("CREATE TABLE IF NOT EXISTS measure_targets(id INTEGER PRIMARY KEY, measure_target_name TEXT, measure_target_type INTEGER, measure_target_description TEXT)")
    cursor.execute("SELECT max(id) FROM measure_targets WHERE measure_target_name = ? AND measure_target_type = ? AND measure_target_description = ?", ([measure_target_name, measure_target_type_id, measure_target_description]))
    measure_target_id = cursor.fetchone()[0]
    if measure_target_id is None:
        cursor.execute("INSERT INTO measure_targets(measure_target_name, measure_target_type, measure_target_description) VALUES (?, ?, ?)", ([measure_target_name, measure_target_type_id, measure_target_description]))
        cursor.execute('SELECT max(id) FROM measure_targets')
        measure_target_id = cursor.fetchone()[0]
    
    #################################################
    # Readings
    ## ID (auto)
    ## measure (ID)
    ## reading (from sensor)
    ## read_log (ID)
    cursor.execute("CREATE TABLE IF NOT EXISTS readings(id INTEGER PRIMARY KEY, measure INTEGER, reading REAL, read_log INTEGER, data_quality INTEGER, measure_target INTEGER)")
    if temp is not None:
        cursor.execute("INSERT INTO readings(measure, reading, read_log, data_quality, measure_target) VALUES (?, ?, ?, ?, ?)", (temp_measure_id, temp, new_log, data_quality, measure_target_id))
    if press is not None:
        cursor.execute("INSERT INTO readings(measure, reading, read_log, data_quality, measure_target) VALUES (?, ?, ?, ?, ?)", (humid_measure_id, press, new_log, data_quality, measure_target_id))

except lite.Error, e:    
    
    ##print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if connection:
        connection.close() 

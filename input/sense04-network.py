#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division
import re
import os 
import subprocess
#import psutil
import sys
#import Adafruit_DHT
#import datetime
from datetime import datetime
from datetime import timedelta 
import time
import sqlite3 as lite
from random import *

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
periphery_name = 'Raspberry Pi 3'
periphery_type = 'Internet'
periphery_description = 'Internet Speed Test via speedtest-cli'
periphery_device_description = 'tst'

## measure target
#measure_target_type = '' ## general type
ping_measure_target_type = 'Disk' 
upload_measure_target_type = 'CPU'
download_measure_target_type = 'RAM'
measure_target_name = 'Network' ## 'yes' 'none' 'other'
measure_target_description = 'Monitoring Internet Speed' 

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

## setup rnd test cycle
_threshold = 1.0/int(sys.argv[1])
_rnd = random()

threshold = _rnd <= _threshold

pin = ''

# Try to grab a sensor reading.  Use the read_retry method which will retry up
now1 = datetime.now()
utc1 = datetime.utcnow()

#try:
response = subprocess.Popen('ifconfig', shell=True, stdout=subprocess.PIPE).stdout.read()
##ERROR: <urlopen error [Errno -3] Temporary failure in name resolution>
#finally:

ifconfig = re.findall('^(\S*?)\:.*?\n', response, re.MULTILINE)

response = []

for i in range(0, len(ifconfig)):
    response.append(subprocess.Popen('iwconfig ' + ifconfig[i], shell=True, stdout=subprocess.PIPE).stdout.read())
    print response[i]
	
utc2 = datetime.utcnow()
offset_utc = str(roundTime(now1,roundTo=30*60) - roundTime(utc1,roundTo=30*60))
duration = (utc2-utc1)
duration2 = (float(duration.microseconds) / 10**6) + duration.seconds + (((duration.days * 24) * 60) * 60)



#print tmp[i]
#print tmp[i]
#print ifconfig[i]
essid = []
bitrate = []
bitrate_measure = []
linkqi = []
linkqj = []
signallevel = []
signallevel_measure = []
#tmp = []

for i in range(0, len(response)):
    if response[i].find("no wireless extension") is not -1:
        essid.append(None)
        bitrate.append(None)
        bitrate_measure.append(None)
        linkqi.append(None)
        linkqj.append(None)
        signallevel.append(None)
        signallevel_measure.append(None)
    else:
        essid.append(re.findall('ESSID\:\"(.*?)\"', response[i], re.MULTILINE))
        bitrate.append(re.findall('Bit\sRate\=(.*?)\s', response[i], re.MULTILINE))
        bitrate_measure.append(re.findall('Bit\sRate\=.*?\s(.*?)\s', response[i], re.MULTILINE))
        linkqi.append(re.findall('Link\sQuality\=(.*?)\/', response[i], re.MULTILINE))
        linkqj.append(re.findall('Link\sQuality\=.*?\/(.*?)\s', response[i], re.MULTILINE))
        signallevel.append(re.findall('Signal\slevel\=(.*?)\s', response[i], re.MULTILINE))
        signallevel_measure.append(re.findall('Signal\slevel\=.*?\s(.*?)\s', response[i], re.MULTILINE))
        print essid[i]
        print bitrate[i]
        print bitrate_measure[i]
        print linkqi[i]
        print linkqj[i]
        print signallevel[i]
        print signallevel_measure[i]

# Change result to data

## try:
#provider = re.findall('Testing from\s(.*?)\s\(', response, re.MULTILINE)
#provider = str(provider[0].replace(',', '.'))
## except lite.Error, e:
## finally:
#provider = re.findall('Testing from\s(.*?)\s\(', response, re.MULTILINE)
#provider = str(provider[0].replace(',', '.'))
#ip = re.findall('\s\((.*?)\)\.\.\.', response, re.MULTILINE)
#ip = str(ip[0].replace(',', '.'))
#distance = re.findall('\s\[(.*?)\s', response, re.MULTILINE)
#distance = float(distance[0].replace(',', '.'))
#distance_measure = re.findall('Hosted by.*?\d\s(.*?)\]\:', response, re.MULTILINE)
#distance_measure = str(distance_measure[0].replace(',', '.'))
#host = re.findall('Hosted by\s(.*?)\s\[', response, re.MULTILINE)
#host = str(host[0].replace(',', '.'))
#ping = re.findall(']:\s(.*?)\s', response, re.MULTILINE)
#ping = float(ping[0].replace(',', '.'))
#ping_measure = re.findall('\]\:.*?\d\s(.*?)\n', response, re.MULTILINE)
#ping_measure = str(ping_measure[0].replace(',', '.'))
#download = re.findall('Download:\s(.*?)\s', response, re.MULTILINE)
#download = float(download[0].replace(',', '.'))
#download_measure = re.findall('Download\:.*?\d\s(.*?)\n', response, re.MULTILINE)
#download_measure = str(download_measure[0].replace(',', '.'))
#upload = re.findall('Upload:\s(.*?)\s', response, re.MULTILINE)
#upload = float(upload[0].replace(',', '.'))
#upload_measure = re.findall('Upload\:.*?\d\s(.*?)\n', response, re.MULTILINE)
#upload_measure = str(upload_measure[0].replace(',', '.'))

### exit before entering database

print _rnd
print _threshold
print threshold

#print response

#print provider
#print ip
#print host
#print distance
#print distance_measure
#print ping
#print ping_measure
#print download
#print download_measure
#print upload
#print upload_measure

sys.exit(duration2)

#################################################
#################################################

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!

try:
    connection = lite.connect('freyr_tst.db', isolation_level=None)
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
    # print '|' + str(outdoors_id) + 'out'
    
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
    # print '|' + str(provider_type_id) + 'provider_type_id'

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
    # print '|' + str(periphery_type_id) + 'periphery_type'

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
    # print '|' + str(location_id) + 'location'

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
    # print '|' + str(source_id) + 'source'
	
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
    # print '|' + str(periphery_id) + 'periphery'
	
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
    # print '|' + str(sensor_id) + 'sensor'
	
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
    # print '|' + str(temp_measure_id) + '°C'
	
    measure_name = 'percent'
    measure_sign = '%'
    measure_type_full = 'Used Capacity'
    measure_type_abbr = 'usage'
    measure_absolute_min = 0.0
    measure_absolute_max = 100.0
    cursor.execute("SELECT max(id) FROM measures WHERE (name LIKE ? OR sign LIKE ?) AND type_full LIKE ? AND (type_abbr LIKE ? OR absolute_min = ? OR absolute_max = ?)", (measure_name, measure_sign, measure_type_full, measure_type_abbr, measure_absolute_min, measure_absolute_max))
    percent_measure_id = cursor.fetchone()[0]
    if percent_measure_id is None:
        cursor.execute("INSERT INTO measures(name, sign, type_full, type_abbr, absolute_min, absolute_max) VALUES (?, ?, ?, ?, ?, ?)", (measure_name, measure_sign, measure_type_full, measure_type_abbr, measure_absolute_min, measure_absolute_max))
        cursor.execute('SELECT max(id) FROM measures WHERE type_abbr LIKE ?', ([measure_type_abbr]))
        percent_measure_id = cursor.fetchone()[0]
    # print '|' + str(percent_measure_id) + '%'
	
    measure_name = 'Mega Byte'
    measure_sign = 'MB'
    measure_type_full = 'Memory'
    measure_type_abbr = 'mem'
    measure_absolute_min = 0.0
    measure_absolute_max = ram_total
    cursor.execute("SELECT max(id) FROM measures WHERE (name LIKE ? OR sign LIKE ?) AND type_full LIKE ? AND (type_abbr LIKE ? OR absolute_min = ? OR absolute_max = ?)", (measure_name, measure_sign, measure_type_full, measure_type_abbr, measure_absolute_min, measure_absolute_max))
    mb_measure_id = cursor.fetchone()[0]
    if mb_measure_id is None:
        cursor.execute("INSERT INTO measures(name, sign, type_full, type_abbr, absolute_min, absolute_max) VALUES (?, ?, ?, ?, ?, ?)", (measure_name, measure_sign, measure_type_full, measure_type_abbr, measure_absolute_min, measure_absolute_max))
        cursor.execute('SELECT max(id) FROM measures WHERE type_abbr LIKE ?', ([measure_type_abbr]))
        mb_measure_id = cursor.fetchone()[0]
    # print '|' + str(mb_measure_id) + 'MB'
	
    measure_name = 'Giga Byte'
    measure_sign = 'GB'
    measure_type_full = 'Memory'
    measure_type_abbr = 'mem'
    measure_absolute_min = 0.0
    measure_absolute_max = disk_total
    cursor.execute("SELECT max(id) FROM measures WHERE (name LIKE ? OR sign LIKE ?) AND type_full LIKE ? AND (type_abbr LIKE ? OR absolute_min = ? OR absolute_max = ?)", (measure_name, measure_sign, measure_type_full, measure_type_abbr, measure_absolute_min, measure_absolute_max))
    gb_measure_id = cursor.fetchone()[0]
    if gb_measure_id is None:
        cursor.execute("INSERT INTO measures(name, sign, type_full, type_abbr, absolute_min, absolute_max) VALUES (?, ?, ?, ?, ?, ?)", (measure_name, measure_sign, measure_type_full, measure_type_abbr, measure_absolute_min, measure_absolute_max))
        cursor.execute('SELECT max(id) FROM measures WHERE type_abbr LIKE ?', ([measure_type_abbr]))
        gb_measure_id = cursor.fetchone()[0]
    # print '|' + str(gb_measure_id) + 'GB'
	
    #################################################
    # measure_target_types
    ## ID (auto)
    ## measure_target_type
    cursor.execute("CREATE TABLE IF NOT EXISTS measure_target_types(id INTEGER PRIMARY KEY, measure_target_type TEXT)")
    cursor.execute("SELECT max(id) FROM measure_target_types WHERE measure_target_type LIKE ?", ([CPU_measure_target_type]))
    CPU_target_id = cursor.fetchone()[0]
    if CPU_target_id is None:
        cursor.execute("INSERT INTO measure_target_types(measure_target_type) VALUES (?)", ([CPU_measure_target_type]))
        cursor.execute('SELECT max(id) FROM measure_target_types')
        CPU_target_id = cursor.fetchone()[0]
    # print '|' + str(CPU_target_id) + 'CPU'
	
    cursor.execute("SELECT max(id) FROM measure_target_types WHERE measure_target_type LIKE ?", ([RAM_measure_target_type]))
    RAM_target_id = cursor.fetchone()[0]
    if RAM_target_id is None:
        cursor.execute("INSERT INTO measure_target_types(measure_target_type) VALUES (?)", ([RAM_measure_target_type]))
        cursor.execute('SELECT max(id) FROM measure_target_types')
        RAM_target_id = cursor.fetchone()[0]
    #print '|' + str(RAM_target_id) + 'RAM'
	
    cursor.execute("SELECT max(id) FROM measure_target_types WHERE measure_target_type LIKE ?", ([Disk_measure_target_type]))
    Disk_target_id = cursor.fetchone()[0] 
    if Disk_target_id is None:
        cursor.execute("INSERT INTO measure_target_types(measure_target_type) VALUES (?)", ([Disk_measure_target_type]))
        cursor.execute('SELECT max(id) FROM measure_target_types')
        Disk_target_id = cursor.fetchone()[0]
    # print '|' + str(Disk_target_id) + 'DISK'
	
    #################################################
    # measure_target
    ## ID (auto)
    ## name
    ## description (additional information)
    cursor.execute("CREATE TABLE IF NOT EXISTS measure_targets(id INTEGER PRIMARY KEY, measure_target_name TEXT, measure_target_type INTEGER, measure_target_description TEXT)")

    cursor.execute("SELECT max(id) FROM measure_targets WHERE measure_target_name = ? AND measure_target_type = ? AND measure_target_description = ?", ([measure_target_name, CPU_target_id, measure_target_description]))
    CPU_measure_target_id = cursor.fetchone()[0]
    if CPU_measure_target_id is None:
        cursor.execute("INSERT INTO measure_targets(measure_target_name, measure_target_type, measure_target_description) VALUES (?, ?, ?)", ([measure_target_name, CPU_target_id, measure_target_description]))
        cursor.execute('SELECT max(id) FROM measure_targets')
        CPU_measure_target_id = cursor.fetchone()[0]
    # print '|' + str(CPU_measure_target_id) + 'CPU'
	
    cursor.execute("SELECT max(id) FROM measure_targets WHERE measure_target_name = ? AND measure_target_type = ? AND measure_target_description = ?", ([measure_target_name, RAM_target_id, measure_target_description]))
    RAM_measure_target_id = cursor.fetchone()[0]
    if RAM_measure_target_id is None:
        cursor.execute("INSERT INTO measure_targets(measure_target_name, measure_target_type, measure_target_description) VALUES (?, ?, ?)", ([measure_target_name, RAM_target_id, measure_target_description]))
        cursor.execute('SELECT max(id) FROM measure_targets')
        RAM_measure_target_id = cursor.fetchone()[0]
    # print '|' + str(RAM_measure_target_id) + 'RAM'
	
    cursor.execute("SELECT max(id) FROM measure_targets WHERE measure_target_name = ? AND measure_target_type = ? AND measure_target_description = ?", ([measure_target_name, Disk_target_id, measure_target_description]))
    Disk_measure_target_id = cursor.fetchone()[0]
    if Disk_measure_target_id is None:
        cursor.execute("INSERT INTO measure_targets(measure_target_name, measure_target_type, measure_target_description) VALUES (?, ?, ?)", ([measure_target_name, Disk_target_id, measure_target_description]))
        cursor.execute('SELECT max(id) FROM measure_targets')
        Disk_measure_target_id = cursor.fetchone()[0]
    # print '|' + str(Disk_measure_target_id) + 'Disk'
	
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
    if cpu_tempA is not None or cpu_tempB is not None or cpu_use is not None or disk_percentage is not None or ram_used is not None or disk_used is not None or ram_percent_used is not None:
        cursor.execute("INSERT INTO read_log(sensor, source, utc_start, utc_end, offset_utc, duration_sec) VALUES (?, ?, ?, ?, ?, ?)", (sensor_id, source_id, utc1, utc2, offset_utc, duration2))
        cursor.execute('SELECT max(id) FROM read_log')
        new_log = cursor.fetchone()[0]
    # print str(new_log) + 'log'
	
    #################################################
    # Readings
    ## ID (auto)
    ## measure (ID)
    ## reading (from sensor)
    ## read_log (ID)
    cursor.execute("CREATE TABLE IF NOT EXISTS readings(id INTEGER PRIMARY KEY, measure INTEGER, reading REAL, read_log INTEGER, data_quality INTEGER, measure_target_id INTEGER)")
	
    if cpu_temp is not None:
        cursor.execute("INSERT INTO readings(measure, reading, read_log, data_quality, measure_target) VALUES (?, ?, ?, ?, ?)", (temp_measure_id, cpu_temp, new_log, data_quality, CPU_measure_target_id))
    # print str(cpu_tempA) + 'cpu_tempA'
	
    if cpu_use is not None:
        cursor.execute("INSERT INTO readings(measure, reading, read_log, data_quality, measure_target) VALUES (?, ?, ?, ?, ?)", (percent_measure_id, cpu_use, new_log, data_quality, CPU_measure_target_id))
    # print str(cpu_use) + 'cpu_use'
	
    if disk_percentage is not None:
        cursor.execute("INSERT INTO readings(measure, reading, read_log, data_quality, measure_target) VALUES (?, ?, ?, ?, ?)", (percent_measure_id, disk_percentage, new_log, data_quality, Disk_measure_target_id))
    # print str(disk_percentage) + 'disk_percentage'
	
    if ram_used is not None:
        cursor.execute("INSERT INTO readings(measure, reading, read_log, data_quality, measure_target) VALUES (?, ?, ?, ?, ?)", (mb_measure_id, ram_used, new_log, data_quality, RAM_measure_target_id))
    # print str(ram_used) + 'ram_used'

    if ram_percent_used is not None:
        cursor.execute("INSERT INTO readings(measure, reading, read_log, data_quality, measure_target) VALUES (?, ?, ?, ?, ?)", (percent_measure_id, ram_percent_used, new_log, data_quality, RAM_measure_target_id))
    # print str(ram_used) + 'ram_used'
	
    if disk_used is not None:
        cursor.execute("INSERT INTO readings(measure, reading, read_log, data_quality, measure_target) VALUES (?, ?, ?, ?, ?)", (gb_measure_id, disk_used, new_log, data_quality, Disk_measure_target_id))
    # print str(disk_used) + 'disk_used'
		
except lite.Error, e:    
    
    ##print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if connection:
        connection.close() 

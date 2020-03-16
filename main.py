# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 20:18:39 2020

@author: Xiaolan Rong
"""

import csv
import time
from datetime import datetime
import dateutil.parser

starttime = time.time()
fn = 'trip_data_12.csv'
#fn = 'subset_data_12.csv'

f2 = open('subset_data_12.csv','w')
f2.write("")
f2.close()

f = open(fn, "r")
reader = csv.reader(f)
f2 = open('subset_data_12.csv','a')
writer = csv.writer(f2, delimiter=',', lineterminator='\n')

n = 0
fdt_pickup = None
fdt_dropoff = None

min_rate_code = None
max_rate_code = None

min_pickup_datetime = None
max_dropoff_datetime = None

min_passenger_count = None
max_passenger_count = None

min_trip_time_in_secs = None
max_trip_time_in_secs = None

min_trip_distance = None
max_trip_distance = None

min_pickup_longitude = None
max_pickup_longitude = None

min_pickup_latitude = None
max_pickup_latitude = None

min_dropoff_longitude = None
max_dropoff_longitude = None

min_dropoff_latitude = None
max_dropoff_latitude = None


#Define a list to contain no of values recorded per hour
hours_no_values = [[0 for i in range(24)] for j in range(2)]

#Define a list to contain mean passenger count stats per hour
mean_pc_stats = [[0 for i in range(24)] for j in range(2)]

#Define lists to contain the distinct values for vendor_id, rate_code and 
# passenger_count.
vendor_id, rate_code, passenger_count = [], [], []

for row in reader:
    if n > 0:
        
        fdt_pickup = datetime.strptime(row[5], '%Y-%m-%d %H:%M:%S')
        fdt_dropoff = datetime.strptime(row[6], '%Y-%m-%d %H:%M:%S')
        
        if row[2] not in vendor_id:
            vendor_id.append(row[2])
        if row[3] not in rate_code:
            rate_code.append(row[3])
        if row[7] not in passenger_count:
            passenger_count.append(row[7])
        
        if fdt_pickup.hour not in hours_no_values[0]:
            hours_no_values[0][fdt_pickup.hour] = fdt_pickup.hour
            mean_pc_stats[0][fdt_pickup.hour] = fdt_pickup.hour
            
        mean_pc_stats[1][fdt_pickup.hour] += int(row[7])
        hours_no_values[1][fdt_pickup.hour] += 1
        
        if n == 1:
            min_rate_code = int(row[3])
            max_rate_code = int(row[3])
    
            min_pickup_datetime = dateutil.parser.parse(str(fdt_pickup))
            max_dropoff_datetime = dateutil.parser.parse(str(fdt_dropoff))
            
            min_passenger_count = int(row[7])
            max_passenger_count = int(row[7])
            
            min_trip_time_in_secs = int(row[8])
            max_trip_time_in_secs = int(row[8])
            
            min_trip_distance = float(row[9])
            max_trip_distance = float(row[9])
            
            min_pickup_longitude = float(row[10])
            max_pickup_longitude = float(row[10])
            
            min_pickup_latitude = float(row[11])
            max_pickup_latitude = float(row[11])
            
            min_dropoff_longitude = float(row[12])
            max_dropoff_longitude = float(row[12])
            
            min_dropoff_latitude = float(row[13])
            max_dropoff_latitude = float(row[13])
            
        else:
            if int(row[3]) > max_rate_code:
                max_rate_code = int(row[3])
            if int(row[3]) < min_rate_code:
                min_rate_code = int(row[3])
                
            if dateutil.parser.parse(str(fdt_dropoff)) > max_dropoff_datetime:
                max_dropoff_datetime = dateutil.parser.parse(str(fdt_dropoff))
            if dateutil.parser.parse(str(fdt_pickup)) < min_pickup_datetime:
                min_pickup_datetime = dateutil.parser.parse(str(fdt_pickup))
                
            if int(row[7]) > max_passenger_count:
                max_passenger_count = int(row[7])
            if int(row[7]) < min_passenger_count:
                min_passenger_count = int(row[7])
                
            if int(row[8]) > max_trip_time_in_secs:
                max_trip_time_in_secs = int(row[8])
            if int(row[8]) < min_trip_time_in_secs:
                min_trip_time_in_secs = int(row[8])
                
            if float(row[9]) > max_trip_distance:
                max_trip_distance = float(row[9])
            if float(row[9]) < min_trip_distance:
                min_trip_distance = float(row[9])

#Lat-long coordinates for New York city area are in range: Latitude from 40.5 to
#41.5 and longitude from -75 to -72, use them to filter outliers.

            try:
                pickup_longitude = float(row[10])
            except ValueError:
                print(row[10] + ' is not a valid longitude!')
                pickup_longitude = min_pickup_longitude
                
            if pickup_longitude > -75 and pickup_longitude < -72:
                if pickup_longitude > max_pickup_longitude:
                    max_pickup_longitude = pickup_longitude
                if pickup_longitude < min_pickup_longitude:
                    min_pickup_longitude = pickup_longitude
#            else:
#                print(str(pickup_longitude) + ' is out of the range!')
            
            try:
                pickup_latitude = float(row[11])
            except ValueError:
                print(row[11] + ' is not a valid latitude!')
                pickup_latitude = min_pickup_latitude
                
            if pickup_latitude > 40.5 and pickup_latitude < 41.5:
                if min_pickup_latitude > max_pickup_latitude:
                    max_pickup_latitude = pickup_latitude
                if min_pickup_latitude < min_pickup_latitude:
                    min_pickup_latitude = pickup_latitude
#            else:
#                print(str(pickup_latitude) + ' is out of the range!')
            
            try:
                dropoff_longitude = float(row[12])
            except ValueError:
                print(row[12] + ' is not a valid longitude!')
                dropoff_longitude = min_dropoff_longitude
                
            if dropoff_longitude > -75 and dropoff_longitude < -72:
                if dropoff_longitude > max_dropoff_longitude:
                    max_dropoff_longitude = dropoff_longitude
                if dropoff_longitude < min_dropoff_longitude:
                    min_dropoff_longitude = dropoff_longitude
#            else:
#                print(str(dropoff_longitude) + ' is out of the range!')
             
            try:
                dropoff_latitude = float(row[13])
            except ValueError:
                print(row[13] + ' is not a valid latitude!')
                dropoff_latitude = min_dropoff_latitude
                
            if dropoff_latitude > 40.5 and dropoff_latitude < 41.5:
                if dropoff_latitude > max_dropoff_latitude:
                    max_dropoff_latitude = dropoff_latitude
                if dropoff_latitude < min_dropoff_latitude:
                    min_dropoff_latitude = dropoff_latitude
#            else:
#                print(str(dropoff_latitude) + ' is out of the range!')
            
    if n % 1000 == 0:
        writer.writerow(row)
        print(n)
        
    n+=1

print("\nPassenger count per hour:")
for i in range(0, 24):
    if(hours_no_values[1][i] != 0):
        mean_pc_stats[1][i] = mean_pc_stats[1][i]/hours_no_values[1][i]    
    else:
        mean_pc_stats[1][i] = 0
    
    print("hour %2d: %2.3f" % (i, mean_pc_stats[1][i]))

print("\nTime range:")
print("Min datetime: " + str(min_pickup_datetime))
print("Max datetime: " + str(max_dropoff_datetime))
print("\nTotal row number: " + str(n-1))
print("\nGeographic range:")

if min_pickup_latitude < min_dropoff_latitude:
    min_latitude = min_pickup_latitude
else:
    min_latitude = min_dropoff_latitude

if min_pickup_longitude < min_dropoff_longitude:
    min_longitude = min_pickup_longitude
else:
    min_longitude = min_dropoff_longitude
    
if max_pickup_latitude > max_dropoff_latitude:
    max_latitude = max_pickup_latitude
else:
    max_latitude = max_dropoff_latitude

if max_pickup_longitude > max_dropoff_longitude:
    max_longitude = max_pickup_longitude
else:
    max_longitude = max_dropoff_longitude
    
print("Min latitude: " + str(min_latitude))
print("Max latitude: " + str(max_latitude))
print("Min longitude: " + str(min_longitude))
print("Max longitude: " + str(max_longitude))

print("\nMin rate_code: " + str(min_rate_code))
print("Max rate_code: " + str(max_rate_code))
print("\nMin passenger_count: " + str(min_passenger_count))
print("Max passenger_count: " + str(max_passenger_count))
print("\nMin trip_time_in_secs: " + str(min_trip_time_in_secs))
print("Max trip_time_in_secs: " + str(max_trip_time_in_secs))
print("\nMin trip_distance: " + str(min_trip_distance))
print("Max trip_distance: " + str(max_trip_distance))

print("\nDistinct values for vendor_id:")
print(vendor_id)
print("\nDistinct values for rate_code:")
print(rate_code)
print("\nDistinct values for passenger_count:")
print(passenger_count)

f.close()
f2.close()  

print(time.time() - starttime)     
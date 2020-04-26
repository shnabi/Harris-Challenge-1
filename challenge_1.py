# CHALLENGE PROBLEMS
# YOU MAY NOT USE ANY ADDITIONAL LIBRARIES OR PACKAGES TO COMPLETE THIS CHALLENGE

# Divvy is Chicago's bike share system, which consists of almost 600 stations scattered
# around the city with blue bikes available for anyone to rent. Users begin a ride by removing
# a bike from a dock, and then they can end their ride by returning the bike to a dock at any Divvy 
# station in the city. You are going to use real data from Divvy collected at 1:30pm on 4/7/2020 
# to analyze supply and demand for bikes in the system. 

# NOTE ** if you aren't able to run this, type "pip install json" into your command line
import json

# do not delete; this is the data you'll be working with
divvy_stations = json.loads(open(r'C:\Users\Shehryar\Dropbox\UChicago\Classes\Spring 2020\Data and Programming\Harris-Challenge_1\divvy_stations.txt').read())

# PROBLEM 1
# find average number of empty docks (num_docks_available) and 
# available bikes (num_bikes_available) at all stations in the system

mean_empty_docks = sum([i['num_docks_available'] for i in divvy_stations])/595
print(mean_empty_docks)

mean_avail_bikes = sum([i['num_bikes_available'] for i in divvy_stations])/595
print(mean_avail_bikes)

# PROBLEM 2
# find ratio of bikes that are currently rented to total bikes in the system (ignore ebikes)

empty_docks = sum([i['num_docks_available'] for i in divvy_stations])
bikes_system = (sum([i['num_docks_available'] for i in divvy_stations]) + 
                sum([i['num_bikes_available'] for i in divvy_stations]))
ratio = empty_docks/bikes_system
print(ratio)   

# PROBLEM 3 
# Add a new variable for each divvy station's entry, "percent_bikes_remaining", that shows 
# the percentage of bikes available at each individual station (again ignore ebikes). 
# This variable should be formatted as a percentage rounded to 2 decimal places, e.g. 66.67%
# percent_bikes_remaining = ((i['num_bikes_available'])/(i['num_bikes_available'] + i['num_docks_available']))*100) for i in divvy_stations]

def pct(i):
      percent = str(
          round(
              (
                  i['num_bikes_available']/(i['num_bikes_available'] + 
                                            i['num_docks_available'])
               )
              *100, 2)
      ) + '%'
      return percent

for d in divvy_stations:
    d.update({'percent_bikes_remaining': pct(d)})
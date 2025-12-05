#! /bin/bash

# Historical Weather Forecast Comparison Project
# This script downloads weather data for Casablanca and logs it for comparison

# Set the city
city=Casablanca

# Set the timezone for Casablanca
TZ='Morocco/Casablanca'

# Download weather report
curl -s wttr.in/$city?T --output weather_report

# Extract current temperature
obs_temp=$(curl -s wttr.in/$city?T | grep -m 1 '°.' | grep -Eo -e '-?[[:digit:]].*')
echo "The current Temperature of $city: $obs_temp"

# Extract forecast temperature for noon tomorrow
fc_temp=$(curl -s wttr.in/$city?T | head -23 | tail -1 | grep '°.' | cut -d 'C' -f2 | grep -Eo -e '-?[[:digit:]].*')
echo "The forecasted temperature for noon tomorrow for $city: $fc_temp C"

# Get current day, month, and year
day=$(TZ='Morocco/Casablanca' date -u +%d) 
month=$(TZ='Morocco/Casablanca' date +%m)
year=$(TZ='Morocco/Casablanca' date +%Y)

# Create record with tab-separated values
record=$(echo -e "$year\t$month\t$day\t$obs_temp\t$fc_temp C")

# Append record to log file
echo $record>>rx_poc.log

echo "Weather data logged successfully!"
echo "Record: $record"

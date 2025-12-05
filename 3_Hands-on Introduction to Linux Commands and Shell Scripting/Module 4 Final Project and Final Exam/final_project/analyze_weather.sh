#! /bin/bash

# Weather Report Analysis Script
# This script analyzes the historical weather data and generates statistics

LOG_FILE="rx_poc.log"

echo "=================================================="
echo "  WEATHER FORECAST ACCURACY ANALYSIS REPORT"
echo "=================================================="
echo ""

# Check if log file exists
if [ ! -f "$LOG_FILE" ]; then
    echo "Error: Log file $LOG_FILE not found!"
    exit 1
fi

# Count total records (excluding header)
total_records=$(($(wc -l < $LOG_FILE) - 1))

if [ $total_records -eq 0 ]; then
    echo "No data found in log file. Please run rx_poc.sh first."
    exit 1
fi

echo "📊 Summary Statistics:"
echo "---------------------"
echo "Total records: $total_records"
echo ""

# Display the log file in a formatted table
echo "📋 Weather Data Records:"
echo "------------------------"
column -t -s $'\t' $LOG_FILE
echo ""

# Calculate some basic statistics if there are at least 2 records
if [ $total_records -ge 2 ]; then
    echo "📈 Additional Analysis:"
    echo "----------------------"
    
    # Get the date range
    first_date=$(tail -n +2 $LOG_FILE | head -1 | cut -f1-3)
    last_date=$(tail -1 $LOG_FILE | cut -f1-3)
    
    echo "First record: $first_date"
    echo "Last record: $last_date"
    echo ""
    
    # Show most recent forecast vs actual
    echo "🔍 Most Recent Data:"
    echo "--------------------"
    tail -1 $LOG_FILE | awk -F'\t' '{
        print "Date: " $1 "/" $2 "/" $3
        print "Observed Temperature: " $4 "°C"
        print "Forecasted Temperature: " $5
    }'
    echo ""
fi

echo "=================================================="
echo "Analysis complete! Generated on: $(date)"
echo "=================================================="

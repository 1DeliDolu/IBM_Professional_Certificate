# 🧪 Testing Guide - Weather Forecast Project

## ✅ Test Checklist

### 1. Initial Setup Test

```bash
cd /mnt/d/CODE/IBM_Back-End_Development_Professional_Certificate/3_Hands-on\ Introduction\ to\ Linux\ Commands\ and\ Shell\ Scripting/Module\ 4\ Final\ Project\ and\ Final\ Exam/final_project

# Check all files exist
ls -la

# Verify scripts are executable
ls -l *.sh
```

**Expected Output:**

- rx_poc.sh (executable)
- analyze_weather.sh (executable)
- rx_poc.log (with header line)
- README.md
- crontab.txt

---

### 2. Weather Data Collection Test

```bash
# Run the main script
./rx_poc.sh
```

**Expected Output:**

```
The current Temperature of Casablanca: XX °C
The forecasted temperature for noon tomorrow for Casablanca: XX ° C
Weather data logged successfully!
Record: YYYY    MM      DD      XX °C           XX ° C
```

**What to Check:**

- ✅ Current temperature is displayed
- ✅ Forecast temperature is displayed
- ✅ Success message appears
- ✅ Record shows current date and both temperatures

---

### 3. Log File Test

```bash
# View the log file
cat rx_poc.log

# Or view in formatted table
column -t -s $'\t' rx_poc.log
```

**Expected Output:**

```
year    month   day     obs_temp        fc_temp
2025    12      05      20 °C           19 ° C
```

**What to Check:**

- ✅ Header row exists (year, month, day, obs_temp, fc_temp)
- ✅ Data row contains current date
- ✅ Both temperature values are present
- ✅ Columns are tab-separated

---

### 4. Multiple Runs Test

```bash
# Run the script multiple times
./rx_poc.sh
./rx_poc.sh
./rx_poc.sh

# Check that multiple records are added
wc -l rx_poc.log
cat rx_poc.log
```

**Expected Output:**

- Line count increases with each run
- Each run adds a new data row
- Header remains at the top

---

### 5. Analysis Script Test

```bash
# Run the analysis script
./analyze_weather.sh
```

**Expected Output:**

```
==================================================
  WEATHER FORECAST ACCURACY ANALYSIS REPORT
==================================================

📊 Summary Statistics:
---------------------
Total records: X

📋 Weather Data Records:
------------------------
year  month  day  obs_temp  fc_temp
...data rows...

==================================================
Analysis complete! Generated on: [timestamp]
==================================================
```

**What to Check:**

- ✅ Report displays correctly
- ✅ Total records count is accurate
- ✅ All data rows are shown in formatted table
- ✅ Timestamp is correct

---

### 6. Weather Report File Test

```bash
# Check the raw weather report
head -30 weather_report
```

**Expected Output:**

- ASCII art weather display
- Current conditions
- Forecast for next 2-3 days
- Temperature in Celsius

---

### 7. Error Handling Test

#### Test 1: Missing log file

```bash
# Backup the log file
mv rx_poc.log rx_poc.log.backup

# Try to run analysis
./analyze_weather.sh

# Restore log file
mv rx_poc.log.backup rx_poc.log
```

**Expected Output:**

```
Error: Log file rx_poc.log not found!
```

#### Test 2: Empty log file (only header)

```bash
# Create a new log with only header
echo -e "year\tmonth\tday\tobs_temp\tfc_temp" > rx_poc.log

# Run analysis
./analyze_weather.sh
```

**Expected Output:**

```
No data found in log file. Please run rx_poc.sh first.
```

---

### 8. Cron Job Test (Optional)

```bash
# Edit crontab
crontab -e

# Add the line from crontab.txt (adjust path)
# Example: 0 12 * * * cd /path/to/final_project && ./rx_poc.sh >> cron.log 2>&1

# Save and verify
crontab -l
```

**To Test Cron:**

```bash
# Wait for scheduled time or set a test time (e.g., 2 minutes from now)
# Check if cron.log is created and contains output
cat cron.log
```

---

## 🔍 Common Issues and Solutions

### Issue 1: Permission Denied

```bash
# Solution: Make scripts executable
chmod u+x rx_poc.sh analyze_weather.sh
```

### Issue 2: curl command not found

```bash
# Solution: Install curl
sudo apt-get update
sudo apt-get install curl
```

### Issue 3: No data in log file

```bash
# Solution: Check internet connection and run script
ping wttr.in
./rx_poc.sh
```

### Issue 4: Incorrect date/time

```bash
# Solution: Verify timezone is set correctly in script
# Check: TZ='Morocco/Casablanca'
grep TZ rx_poc.sh
```

### Issue 5: Column command not found (for formatted output)

```bash
# Alternative: Use cat to view tab-separated data
cat rx_poc.log
```

---

## 📊 Validation Criteria

The project is successful if:

1. ✅ **rx_poc.sh runs without errors**

   - Downloads weather data from wttr.in
   - Extracts current and forecast temperatures
   - Logs data with correct date

2. ✅ **rx_poc.log is properly formatted**

   - Contains header row
   - Each data row has 5 tab-separated columns
   - Dates are in YYYY MM DD format
   - Temperatures include units (°C)

3. ✅ **analyze_weather.sh generates report**

   - Displays total record count
   - Shows formatted data table
   - Handles missing/empty log file gracefully

4. ✅ **Scripts are executable**

   - Have proper shebang (#!/bin/bash)
   - Have execute permissions (chmod u+x)

5. ✅ **Documentation is complete**
   - README.md explains project
   - TESTING.md (this file) provides test procedures
   - crontab.txt shows how to schedule

---

## 🎯 Success Metrics

After running for several days:

- Log file contains multiple entries (one per day)
- Can compare forecast accuracy by looking at previous day's forecast vs. actual
- Analysis script provides clear summary of collected data

---

## 📝 Test Results Log

Record your test results:

| Test            | Date       | Status            | Notes |
| --------------- | ---------- | ----------------- | ----- |
| Initial Setup   | YYYY-MM-DD | ✅ Pass / ❌ Fail |       |
| Data Collection | YYYY-MM-DD | ✅ Pass / ❌ Fail |       |
| Log File        | YYYY-MM-DD | ✅ Pass / ❌ Fail |       |
| Multiple Runs   | YYYY-MM-DD | ✅ Pass / ❌ Fail |       |
| Analysis Script | YYYY-MM-DD | ✅ Pass / ❌ Fail |       |
| Error Handling  | YYYY-MM-DD | ✅ Pass / ❌ Fail |       |
| Cron Job        | YYYY-MM-DD | ✅ Pass / ❌ Fail |       |

---

## 🎓 Learning Outcomes Verified

- [x] Bash scripting fundamentals
- [x] Data extraction with curl, grep, cut
- [x] Text processing with pipes
- [x] Date/time manipulation
- [x] Log file creation and management
- [x] Error handling in scripts
- [x] Cron job scheduling
- [x] Documentation and testing

---

**Project Status: ✅ COMPLETED AND TESTED**

Last Updated: December 5, 2025

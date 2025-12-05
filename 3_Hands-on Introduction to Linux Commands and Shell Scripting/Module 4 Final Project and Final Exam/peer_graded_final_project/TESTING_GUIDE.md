# 🧪 Testing Guide for backup.sh

## 📋 Overview

This guide provides comprehensive testing procedures to verify your backup.sh script works correctly before submission.

---

## 🚀 Quick Test

### Method 1: Using test_backup.sh (Automated)

```bash
# Make test script executable
chmod +x test_backup.sh

# Run automated tests
./test_backup.sh
```

The automated test script will:

- Verify backup.sh exists and is executable
- Create test directories and files
- Run backup.sh with test data
- Verify backup file creation
- Check backup contents
- Provide detailed results

---

### Method 2: Manual Testing

#### Step 1: Download Test Files

```bash
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/Final%20Project/important-documents.zip
```

#### Step 2: Extract Files

```bash
unzip -DDo important-documents.zip
```

**Note:** `-DDo` flag:

- `-D` - Do not restore timestamps
- `-o` - Overwrite existing files
- Result: All files get current timestamp

#### Step 3: Update Modification Times

```bash
touch important-documents/*
```

This ensures all files are considered "recent" (modified in last 24 hours).

#### Step 4: Make Script Executable

```bash
chmod +x backup.sh
```

#### Step 5: Verify Permissions

```bash
ls -l backup.sh
```

Expected output:

```
-rwxr-xr-x 1 user user 1234 Dec  5 10:00 backup.sh
```

The `x` indicates executable permission.

#### Step 6: Run Backup Script

```bash
./backup.sh important-documents .
```

**Arguments:**

- `important-documents` - Source directory
- `.` - Current directory (destination)

Expected output:

```
Target directory: important-documents
Destination directory: .
file1.txt
file2.txt
config.ini
...
```

#### Step 7: Verify Backup Created

```bash
ls -l backup-*.tar.gz
```

Expected output:

```
-rw-r--r-- 1 user user 12345 Dec  5 10:00 backup-1733399200.tar.gz
```

#### Step 8: Verify Backup Contents

```bash
tar -tzf backup-*.tar.gz
```

This lists all files in the backup without extracting them.

---

## 🔍 Detailed Verification Tests

### Test 1: Argument Validation

#### Test 1.1: No Arguments

```bash
./backup.sh
```

**Expected Result:**

```
backup.sh target_directory_name destination_directory_name
```

#### Test 1.2: One Argument

```bash
./backup.sh test_dir
```

**Expected Result:**

```
backup.sh target_directory_name destination_directory_name
```

#### Test 1.3: Invalid Directory

```bash
./backup.sh nonexistent_dir another_dir
```

**Expected Result:**

```
Invalid directory path provided
```

**✅ Pass Criteria:** Script exits with error message in all cases

---

### Test 2: Directory Variables

Create test script to verify variables:

```bash
# Add these lines after [TASK 2] in backup.sh temporarily
echo "DEBUG: targetDirectory = $targetDirectory"
echo "DEBUG: destinationDirectory = $destinationDirectory"
echo "DEBUG: currentTS = $currentTS"
echo "DEBUG: backupFileName = $backupFileName"
```

Then run:

```bash
./backup.sh test_source test_dest
```

**Expected Output:**

```
DEBUG: targetDirectory = test_source
DEBUG: destinationDirectory = test_dest
DEBUG: currentTS = 1733399200
DEBUG: backupFileName = backup-1733399200.tar.gz
```

**✅ Pass Criteria:** All variables contain expected values

---

### Test 3: Timestamp Calculations

Verify timestamp is reasonable:

```bash
# Get current timestamp
date +%s
# Should be close to currentTS in script

# Verify 24-hour calculation
# yesterdayTS should be 86400 seconds less than currentTS
```

**✅ Pass Criteria:**

- currentTS matches current time (±few seconds)
- yesterdayTS = currentTS - 86400

---

### Test 4: File Selection by Date

#### Test 4.1: Create Mixed-Age Files

```bash
mkdir test_mixed
cd test_mixed

# Create old files (25 hours ago)
echo "old" > old_file.txt
touch -d "25 hours ago" old_file.txt

# Create recent files (1 hour ago)
echo "recent" > recent_file.txt
touch -d "1 hour ago" recent_file.txt

# Create very recent files (now)
echo "very recent" > new_file.txt

cd ..
```

#### Test 4.2: Run Backup

```bash
./backup.sh test_mixed .
```

#### Test 4.3: Verify Contents

```bash
tar -tzf backup-*.tar.gz
```

**Expected Result:**

- Should contain: `recent_file.txt`, `new_file.txt`
- Should NOT contain: `old_file.txt`

**✅ Pass Criteria:** Only files modified in last 24 hours are included

---

### Test 5: Multiple Runs

Test that multiple backups don't interfere:

```bash
# Run 1
./backup.sh test_source test_dest
sleep 2

# Run 2
./backup.sh test_source test_dest
sleep 2

# Run 3
./backup.sh test_source test_dest

# List all backups
ls -l test_dest/backup-*.tar.gz
```

**Expected Result:**

- 3 different backup files
- Each with unique timestamp
- No files overwritten

**✅ Pass Criteria:** Each run creates a new backup file

---

### Test 6: Subdirectories

Test if script handles subdirectories:

```bash
mkdir -p test_nested/subdir1/subdir2
echo "nested" > test_nested/subdir1/subdir2/nested_file.txt
touch test_nested/subdir1/subdir2/nested_file.txt

./backup.sh test_nested .
tar -tzf backup-*.tar.gz
```

**Expected Result:**
Backup should contain:

```
subdir1/
subdir1/subdir2/
subdir1/subdir2/nested_file.txt
```

**✅ Pass Criteria:** Subdirectories and their contents are included

---

### Test 7: Special Characters in Filenames

```bash
mkdir test_special
cd test_special
touch "file with spaces.txt"
touch "file'with'quotes.txt"
touch "file-with-dashes.txt"
cd ..

./backup.sh test_special .
tar -tzf backup-*.tar.gz
```

**Expected Result:**
All files should be backed up correctly, including those with:

- Spaces
- Quotes
- Special characters

**✅ Pass Criteria:** All files backed up without errors

---

### Test 8: Empty Directory

```bash
mkdir test_empty
./backup.sh test_empty .
```

**Expected Result:**

- Script should run without errors
- Backup file may be empty or very small
- No crashes or error messages

**✅ Pass Criteria:** Script handles empty directory gracefully

---

### Test 9: Large Number of Files

```bash
mkdir test_many
cd test_many
for i in {1..100}; do
    echo "file $i" > "file_$i.txt"
done
cd ..

./backup.sh test_many .
tar -tzf backup-*.tar.gz | wc -l
```

**Expected Result:**

- Backup contains all 100 files
- No errors or memory issues

**✅ Pass Criteria:** All files are backed up successfully

---

### Test 10: Permissions After Backup

```bash
./backup.sh test_source test_dest
ls -l test_dest/backup-*.tar.gz
```

**Expected Permissions:**

- Read/write for owner
- Read for group and others
- Format: `-rw-r--r--`

**✅ Pass Criteria:** Backup file has appropriate permissions

---

## 📊 Test Results Checklist

Mark each test as you complete it:

- [ ] Test 1: Argument Validation

  - [ ] 1.1: No arguments
  - [ ] 1.2: One argument
  - [ ] 1.3: Invalid directory

- [ ] Test 2: Directory Variables
- [ ] Test 3: Timestamp Calculations
- [ ] Test 4: File Selection by Date

  - [ ] 4.1: Create mixed-age files
  - [ ] 4.2: Run backup
  - [ ] 4.3: Verify contents

- [ ] Test 5: Multiple Runs
- [ ] Test 6: Subdirectories
- [ ] Test 7: Special Characters
- [ ] Test 8: Empty Directory
- [ ] Test 9: Large Number of Files
- [ ] Test 10: Permissions

---

## 🎯 Integration Tests

### Complete Workflow Test

```bash
#!/bin/bash

# Full integration test
echo "Starting integration test..."

# Setup
mkdir -p integration_test/{source,destination}
cd integration_test/source
echo "content" > file1.txt
echo "content" > file2.txt
echo "content" > file3.txt
cd ../..

# Run backup
./backup.sh integration_test/source integration_test/destination

# Verify
if [ -f integration_test/destination/backup-*.tar.gz ]; then
    echo "✅ Integration test PASSED"
    echo "Backup file created successfully"
    tar -tzf integration_test/destination/backup-*.tar.gz
else
    echo "❌ Integration test FAILED"
    echo "No backup file found"
fi

# Cleanup
rm -rf integration_test
```

---

## 🐛 Debugging Tips

### Enable Verbose Mode

Add to top of backup.sh:

```bash
set -x  # Print commands as they execute
set -e  # Exit on first error
```

Remove after debugging.

### Check Individual Components

Test each part separately:

```bash
# Test timestamp
date +%s

# Test date arithmetic
currentTS=$(date +%s)
yesterdayTS=$(($currentTS - 24 * 60 * 60))
echo "Current: $currentTS"
echo "Yesterday: $yesterdayTS"
echo "Difference: $(($currentTS - $yesterdayTS))"

# Test file modification time
touch test_file.txt
date -r test_file.txt +%s

# Test tar
tar -czvf test.tar.gz test_file.txt
tar -tzf test.tar.gz
```

### Common Issues and Solutions

| Issue                    | Possible Cause         | Solution                      |
| ------------------------ | ---------------------- | ----------------------------- |
| No backup created        | Script not executable  | `chmod +x backup.sh`          |
| Empty backup             | Files too old          | Use `touch` to update times   |
| Backup in wrong location | Path issues            | Use absolute paths            |
| Permission denied        | Directory not writable | Check destination permissions |
| Command not found        | Missing tools          | Install tar, date, etc.       |

---

## 🔄 Cron Testing

### Test Cron Job (Safely)

```bash
# Create test cron job (runs every minute)
echo "*/1 * * * * cd $PWD && ./backup.sh test_source test_dest >> cron.log 2>&1" | crontab -

# Wait 2 minutes
sleep 120

# Check if backups were created
ls -l test_dest/backup-*.tar.gz

# Check cron log
cat cron.log

# Remove test cron job
crontab -r
```

**✅ Pass Criteria:**

- Multiple backup files created
- cron.log shows successful execution
- No errors in log

---

## 📈 Performance Testing

### Time Execution

```bash
time ./backup.sh large_directory destination
```

Monitor:

- Real time (wall clock)
- User time (CPU in user mode)
- System time (CPU in kernel mode)

### Resource Usage

```bash
# While script runs, in another terminal:
top
# Look for backup.sh process
```

Monitor:

- CPU usage
- Memory usage
- Disk I/O

---

## ✅ Final Verification Checklist

Before submission, verify:

- [ ] Script is executable (`chmod +x`)
- [ ] Script accepts exactly 2 arguments
- [ ] Script validates directory paths
- [ ] Variables are set correctly (Tasks 1-8)
- [ ] Loop iterates through files (Task 9)
- [ ] Timestamp comparison works (Task 10)
- [ ] Files added to array (Task 11)
- [ ] Tar archive created (Task 12)
- [ ] Backup moved to destination (Task 13)
- [ ] Backup file has timestamp in name
- [ ] Only recent files are included
- [ ] Cron job configured correctly
- [ ] All 16 screenshots taken
- [ ] backup.sh file saved

---

## 🎉 Success Criteria

Your backup.sh script is ready for submission when:

✅ All tests pass
✅ Script handles edge cases
✅ Error messages are clear
✅ Backup files created successfully
✅ Only recent files are included
✅ Cron job runs without errors
✅ All screenshots captured
✅ Documentation is complete

---

**Testing Complete! Ready for Peer Grading! 🚀**

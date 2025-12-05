# 📚 Complete Solution Guide

## 🎯 Detailed Explanation of Each Task

This guide provides in-depth explanations for every task in the backup.sh script.

---

## Task 1: Set Variables from Command-Line Arguments

### Code:

```bash
# [TASK 1]
targetDirectory=$1
destinationDirectory=$2
```

### Explanation:

- `$1` represents the first command-line argument
- `$2` represents the second command-line argument
- These assignments make the code more readable by using descriptive variable names

### Why This Matters:

Using meaningful variable names instead of positional parameters ($1, $2) throughout the script improves code maintainability and readability.

### Example Usage:

```bash
./backup.sh /path/to/source /path/to/destination
# $1 = /path/to/source
# $2 = /path/to/destination
```

---

## Task 2: Display Variable Values

### Code:

```bash
# [TASK 2]
echo "Target directory: $targetDirectory"
echo "Destination directory: $destinationDirectory"
```

### Explanation:

- `echo` command prints text to terminal
- `$targetDirectory` and `$destinationDirectory` are interpolated (replaced with their values)
- Provides user feedback about what directories will be processed

### Why This Matters:

User feedback helps with debugging and confirms the script received correct arguments.

### Example Output:

```
Target directory: /home/user/important-documents
Destination directory: /home/user/backups
```

---

## Task 3: Get Current Timestamp

### Code:

```bash
# [TASK 3]
currentTS=$(date +%s)
```

### Explanation:

- `date +%s` returns current Unix timestamp (seconds since Jan 1, 1970)
- `$(...)` is command substitution - captures command output
- Timestamp is used to create unique backup filename

### Why This Matters:

Unix timestamps ensure each backup has a unique, sortable identifier.

### Example:

```bash
$ date +%s
1733399200
# This represents: Thu Dec  5 12:00:00 2025
```

---

## Task 4: Create Backup Filename

### Code:

```bash
# [TASK 4]
backupFileName="backup-$currentTS.tar.gz"
```

### Explanation:

- Creates filename in format: `backup-[TIMESTAMP].tar.gz`
- `$currentTS` is interpolated into the string
- `.tar.gz` indicates compressed tar archive

### Why This Matters:

Unique filenames prevent overwriting previous backups and make identification easy.

### Example:

```bash
# If currentTS=1733399200
# Then backupFileName="backup-1733399200.tar.gz"
```

---

## Task 5: Save Original Directory Path

### Code:

```bash
# [TASK 5]
origAbsPath=$(pwd)
```

### Explanation:

- `pwd` prints current working directory (absolute path)
- Saves current location so we can return to it later
- Essential for navigating between directories

### Why This Matters:

We'll change directories multiple times; saving the original path lets us return.

### Example:

```bash
$ pwd
/home/user/projects
# origAbsPath="/home/user/projects"
```

---

## Task 6: Get Destination Directory Absolute Path

### Code:

```bash
# [TASK 6]
cd "$destinationDirectory" || exit
destAbsPath=$(pwd)
```

### Explanation:

- `cd "$destinationDirectory"` changes to destination directory
- `|| exit` means: if cd fails, exit the script immediately
- `pwd` gets absolute path of destination
- Quotes around `$destinationDirectory` handle spaces in paths

### Why This Matters:

Converting relative paths to absolute paths ensures consistency regardless of where the script is run from.

### Example:

```bash
# If user provided: ./backups
# And current dir is: /home/user
# Then destAbsPath="/home/user/backups"
```

---

## Task 7: Navigate to Target Directory

### Code:

```bash
# [TASK 7]
cd "$origAbsPath" || exit
cd "$targetDirectory" || exit
```

### Explanation:

- First cd: Return to original directory
- Second cd: Go to target directory (where files to backup are)
- Both use `|| exit` for error handling
- Quotes handle spaces in directory names

### Why This Matters:

We need to be in the target directory to iterate through files and check modification times.

### Example:

```bash
# Start: /home/user/projects
# After line 1: /home/user/projects (original)
# After line 2: /home/user/important-documents (target)
```

---

## Task 8: Calculate Yesterday's Timestamp

### Code:

```bash
# [TASK 8]
yesterdayTS=$(($currentTS - 24 * 60 * 60))
```

### Explanation:

- `$((...))` is arithmetic expansion
- `24 * 60 * 60` = seconds in 24 hours
  - 24 hours × 60 minutes × 60 seconds = 86,400 seconds
- Subtracts from current timestamp to get 24 hours ago

### Why This Matters:

Comparing file modification times against this timestamp identifies recently changed files.

### Example:

```bash
# If currentTS=1733399200
# Then yesterdayTS=1733312800 (86400 seconds earlier)
```

---

## Task 9: Loop Through All Files

### Code:

```bash
for file in * # [TASK 9]
do
```

### Explanation:

- `for` loop iterates through items
- `*` is a wildcard matching all files/directories in current directory
- `file` variable holds each item's name during iteration

### Why This Matters:

We need to check every file to determine if it was modified recently.

### Example:

```bash
# If directory contains: doc1.txt, doc2.txt, config/
# Loop runs 3 times with file equal to:
#   1. doc1.txt
#   2. doc2.txt
#   3. config
```

---

## Task 10: Check If File Was Recently Modified

### Code:

```bash
# [TASK 10]
if [[ $(date -r "$file" +%s) -gt $yesterdayTS ]]
then
```

### Explanation:

- `date -r "$file" +%s` gets file's last modification timestamp
- `-gt` means "greater than" (numerical comparison)
- `[[...]]` is enhanced test command with better error handling
- Compares file's timestamp with yesterday's timestamp

### Why This Matters:

Only files modified in last 24 hours should be backed up.

### Example:

```bash
# If file modified at: 1733399000 (recent)
# And yesterdayTS: 1733312800
# Then 1733399000 > 1733312800 → TRUE → backup this file
```

---

## Task 11: Add File to Backup Array

### Code:

```bash
# [TASK 11]
toBackup+=("$file")
fi
done
```

### Explanation:

- `toBackup+=()` appends to array
- Parentheses create array element
- Quotes preserve filenames with spaces
- `fi` ends if statement
- `done` ends for loop

### Why This Matters:

Collecting files in an array allows us to backup them all at once with tar.

### Example:

```bash
# Initially: toBackup=()
# After loop: toBackup=("doc1.txt" "doc2.txt" "config.ini")
```

---

## Task 12: Create Compressed Backup Archive

### Code:

```bash
# [TASK 12]
tar -czvf "$backupFileName" "${toBackup[@]}"
```

### Explanation:

- `tar` - tape archive utility
- `-c` - create new archive
- `-z` - compress with gzip
- `-v` - verbose (show files being added)
- `-f` - specify filename
- `${toBackup[@]}` - expand array to all elements

### Why This Matters:

Creates a single compressed file containing all recently modified files.

### Example:

```bash
# Creates: backup-1733399200.tar.gz
# Containing: doc1.txt, doc2.txt, config.ini (compressed)
```

---

## Task 13: Move Backup to Destination

### Code:

```bash
# [TASK 13]
mv "$backupFileName" "$destAbsPath"
```

### Explanation:

- `mv` moves (or renames) files
- Moves backup file from current directory to destination
- Uses absolute path to ensure correct location

### Why This Matters:

Backup file needs to be in the specified destination directory, not left in the source.

### Example:

```bash
# Moves:
# From: /home/user/important-documents/backup-1733399200.tar.gz
# To: /home/user/backups/backup-1733399200.tar.gz
```

---

## Task 14: Save and Submit Script

### Instructions:

1. Save backup.sh file (Ctrl+S or Cmd+S)
2. Download file from IDE (File → Download)
3. Submit file for peer grading

### Why This Matters:

Peers need your complete script to evaluate your work.

---

## Task 15: Make Script Executable

### Commands:

```bash
chmod +x backup.sh
ls -l backup.sh
```

### Explanation:

- `chmod +x` adds execute permission
- `ls -l` lists file with permissions
- Output should show `x` in permissions: `-rwxr-xr-x`

### Why This Matters:

Scripts need execute permission to run as programs.

### Example Output:

```
-rwxr-xr-x 1 user user 1234 Dec  5 10:00 backup.sh
  ^^^
  Owner can execute
```

---

## Task 16: Test Backup Creation

### Commands:

```bash
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-LX0117EN-SkillsNetwork/labs/Final%20Project/important-documents.zip
unzip -DDo important-documents.zip
touch important-documents/*
./backup.sh important-documents .
ls -l backup-*.tar.gz
```

### Explanation:

1. Download test files
2. Extract without preserving timestamps
3. Update modification times to now
4. Run backup script
5. Verify backup file exists

### Why This Matters:

Proves the script works correctly end-to-end.

### Example Output:

```
-rw-r--r-- 1 user user 12345 Dec  5 10:00 backup-1733399200.tar.gz
```

---

## Task 17: Schedule with Cron

### Commands:

```bash
sudo cp backup.sh /usr/local/bin/
crontab -e
# Add line:
0 0 * * * /usr/local/bin/backup.sh /home/project/important-documents /home/project
crontab -l
```

### Explanation:

- Copy script to system directory
- Edit crontab (cron table)
- `0 0 * * *` means daily at midnight
- Full paths required in cron

### Cron Format:

```
* * * * * command
│ │ │ │ │
│ │ │ │ └─── Day of week (0-7, 0 and 7 are Sunday)
│ │ │ └───── Month (1-12)
│ │ └─────── Day of month (1-31)
│ └───────── Hour (0-23)
└─────────── Minute (0-59)
```

### Example Schedules:

```bash
# Every day at midnight
0 0 * * * /usr/local/bin/backup.sh /path/to/source /path/to/dest

# Every day at 2:30 AM
30 2 * * * /usr/local/bin/backup.sh /path/to/source /path/to/dest

# Every hour
0 * * * * /usr/local/bin/backup.sh /path/to/source /path/to/dest

# Every minute (testing only!)
* * * * * /usr/local/bin/backup.sh /path/to/source /path/to/dest
```

---

## 🔧 Complete Script Flow

### Step-by-Step Execution:

1. **Validate Arguments**

   - Check exactly 2 arguments provided
   - Verify both are valid directories

2. **Initialize Variables**

   - Set directory variables (Tasks 1-2)
   - Get current timestamp (Task 3)
   - Create backup filename (Task 4)

3. **Prepare Paths**

   - Save original path (Task 5)
   - Get destination absolute path (Task 6)
   - Navigate to target directory (Task 7)

4. **Find Recent Files**

   - Calculate yesterday's timestamp (Task 8)
   - Loop through all files (Task 9)
   - Check modification time (Task 10)
   - Add to backup array (Task 11)

5. **Create and Move Backup**

   - Create tar.gz archive (Task 12)
   - Move to destination (Task 13)

6. **Deployment**
   - Make executable (Task 15)
   - Test functionality (Task 16)
   - Schedule with cron (Task 17)

---

## 💡 Key Bash Concepts Used

### Command Substitution

```bash
variable=$(command)
# Captures command output
```

### Arithmetic Expansion

```bash
result=$(($a + $b * $c))
# Performs calculations
```

### Arrays

```bash
declare -a myArray
myArray+=("item")
echo "${myArray[@]}"
```

### Conditional Execution

```bash
command || action
# If command fails, execute action
```

### Test Commands

```bash
[[ condition ]]
# Enhanced test with better error handling
```

### Wildcards

```bash
*         # Matches any characters
?         # Matches one character
[abc]     # Matches a, b, or c
```

---

## 🎓 Learning Outcomes

After completing this project, you can:

✅ Write robust bash scripts with error handling
✅ Process command-line arguments
✅ Manipulate timestamps and dates
✅ Use arrays for data collection
✅ Create compressed archives with tar
✅ Schedule automated tasks with cron
✅ Handle file permissions
✅ Validate user input
✅ Navigate filesystem programmatically

---

## 📚 Additional Resources

- **Bash Guide:** https://www.gnu.org/software/bash/manual/
- **Tar Manual:** `man tar`
- **Cron Tutorial:** `man crontab`, `man 5 crontab`
- **Date Command:** `man date`
- **Test Expressions:** `man test`, `help [[`

---

## 🔍 Common Pitfalls and Solutions

### Issue: Script doesn't find files

**Solution:** Ensure you're in correct directory (cd to target)

### Issue: Backup contains no files

**Solution:** Use `touch` to update modification times for testing

### Issue: Permission denied

**Solution:** Use `chmod +x` to make script executable

### Issue: Cron doesn't run

**Solution:** Use absolute paths, check cron service is running

### Issue: Variables don't expand in cron

**Solution:** Use full paths, don't rely on environment variables

---

## 🎉 Congratulations!

You've completed a comprehensive backup automation project demonstrating professional-level bash scripting skills!

**Skills Demonstrated:**

- System administration
- Task automation
- Error handling
- File system operations
- Process scheduling

These skills are essential for:

- DevOps engineers
- System administrators
- Backend developers
- Linux specialists
- Site reliability engineers (SRE)

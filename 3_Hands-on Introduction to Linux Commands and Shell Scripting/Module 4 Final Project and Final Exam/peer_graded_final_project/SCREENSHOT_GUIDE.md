# 📸 Screenshot Guide - All Tasks

This guide provides detailed instructions for taking screenshots for each task in the peer-graded final project.

---

## 📋 General Screenshot Guidelines

1. **Format:** JPEG or PNG only
2. **Quality:** Clear and readable
3. **Content:** Show both code AND relevant context
4. **Naming:** Use exact filenames as specified
5. **Size:** Keep file size reasonable (< 5MB per image)

---

## 🖼️ Task-by-Task Screenshot Instructions

### 📸 Task 1: Set Variables

**Filename:** `01-Set_Variables.jpg` or `.png`

**What to capture:**

```bash
# [TASK 1]
targetDirectory=$1
destinationDirectory=$2
```

**Screenshot should show:**

- The comment `# [TASK 1]`
- Both variable assignments
- Line numbers (if visible in editor)

**Example description for screenshot:**

```
Lines showing:
targetDirectory=$1
destinationDirectory=$2
```

---

### 📸 Task 2: Display Values

**Filename:** `02-Display_Values.jpg` or `.png`

**What to capture:**

```bash
# [TASK 2]
echo "Target directory: $targetDirectory"
echo "Destination directory: $destinationDirectory"
```

**Screenshot should show:**

- The comment `# [TASK 2]`
- Both echo statements
- Variable interpolation with $

**Example description for screenshot:**

```
Lines showing:
echo "Target directory: $targetDirectory"
echo "Destination directory: $destinationDirectory"
```

---

### 📸 Task 3: Current Timestamp

**Filename:** `03-CurrentTS.jpg` or `.png`

**What to capture:**

```bash
# [TASK 3]
currentTS=$(date +%s)
```

**Screenshot should show:**

- The comment `# [TASK 3]`
- Command substitution with $(...)
- date command with +%s format

**Example description for screenshot:**

```
Line showing:
currentTS=$(date +%s)
```

---

### 📸 Task 4: Set Backup Filename

**Filename:** `04-Set_Value.jpg` or `.png`

**What to capture:**

```bash
# [TASK 4]
backupFileName="backup-$currentTS.tar.gz"
```

**Screenshot should show:**

- The comment `# [TASK 4]`
- Variable assignment with string interpolation
- .tar.gz extension

**Example description for screenshot:**

```
Line showing:
backupFileName="backup-$currentTS.tar.gz"
```

---

### 📸 Task 5: Define Original Path Variable

**Filename:** `05-Define_Variable.jpg` or `.png`

**What to capture:**

```bash
# [TASK 5]
origAbsPath=$(pwd)
```

**Screenshot should show:**

- The comment `# [TASK 5]`
- Command substitution with pwd
- Variable assignment

**Example description for screenshot:**

```
Line showing:
origAbsPath=$(pwd)
```

---

### 📸 Task 6: Define Destination Path Variable

**Filename:** `06-Define_Variable.jpg` or `.png`

**What to capture:**

```bash
# [TASK 6]
cd "$destinationDirectory" || exit
destAbsPath=$(pwd)
```

**Screenshot should show:**

- The comment `# [TASK 6]`
- cd command with error handling
- pwd command in command substitution
- Quoted variable

**Example description for screenshot:**

```
Lines showing:
cd "$destinationDirectory" || exit
destAbsPath=$(pwd)
```

---

### 📸 Task 7: Change Directory

**Filename:** `07-Change_Directory.jpg` or `.png`

**What to capture:**

```bash
# [TASK 7]
cd "$origAbsPath" || exit
cd "$targetDirectory" || exit
```

**Screenshot should show:**

- The comment `# [TASK 7]`
- Two cd commands with error handling
- Quoted variables

**Example description for screenshot:**

```
Lines showing:
cd "$origAbsPath" || exit
cd "$targetDirectory" || exit
```

---

### 📸 Task 8: Calculate Yesterday's Timestamp

**Filename:** `08-YesterdayTS.jpg` or `.png`

**What to capture:**

```bash
# [TASK 8]
yesterdayTS=$(($currentTS - 24 * 60 * 60))
```

**Screenshot should show:**

- The comment `# [TASK 8]`
- Arithmetic expansion $((...))
- Calculation: 24 _ 60 _ 60 seconds

**Example description for screenshot:**

```
Line showing:
yesterdayTS=$(($currentTS - 24 * 60 * 60))
```

---

### 📸 Task 9: List All Files and Directories

**Filename:** `09-List_AllFilesandDirectories.jpg` or `.png`

**What to capture:**

```bash
for file in * # [TASK 9]
do
```

**Screenshot should show:**

- The for loop with wildcard \*
- The comment `# [TASK 9]`
- The do keyword

**Example description for screenshot:**

```
Lines showing:
for file in * # [TASK 9]
do
```

---

### 📸 Task 10: IF Statement to Check Modified Date

**Filename:** `10-IF_Statement.jpg` or `.png`

**What to capture:**

```bash
  # [TASK 10]
  if [[ $(date -r "$file" +%s) -gt $yesterdayTS ]]
  then
```

**Screenshot should show:**

- The comment `# [TASK 10]`
- if statement with double brackets [[]]
- date -r command for file modification time
- Greater than comparison -gt
- then keyword

**Example description for screenshot:**

```
Lines showing:
if [[ $(date -r "$file" +%s) -gt $yesterdayTS ]]
then
```

---

### 📸 Task 11: Add File to Array

**Filename:** `11-Add_File.jpg` or `.png`

**What to capture:**

```bash
    # [TASK 11]
    toBackup+=("$file")
  fi
done
```

**Screenshot should show:**

- The comment `# [TASK 11]`
- Array append operation +=()
- Quoted variable
- fi and done keywords

**Example description for screenshot:**

```
Lines showing:
toBackup+=("$file")
fi
done
```

---

### 📸 Task 12: Create Backup Archive

**Filename:** `12-Create_Backup.jpg` or `.png`

**What to capture:**

```bash
# [TASK 12]
tar -czvf "$backupFileName" "${toBackup[@]}"
```

**Screenshot should show:**

- The comment `# [TASK 12]`
- tar command with flags: -czvf
- Quoted variables
- Array expansion ${toBackup[@]}

**Example description for screenshot:**

```
Line showing:
tar -czvf "$backupFileName" "${toBackup[@]}"
```

---

### 📸 Task 13: Move Backup to Destination

**Filename:** `13-Move_Backup.jpg` or `.png`

**What to capture:**

```bash
# [TASK 13]
mv "$backupFileName" "$destAbsPath"
```

**Screenshot should show:**

- The comment `# [TASK 13]`
- mv command
- Both quoted variables

**Example description for screenshot:**

```
Line showing:
mv "$backupFileName" "$destAbsPath"
```

---

### 📸 Task 15: Executable Permissions

**Filename:** `15-executable.jpg` or `.png`

**What to capture:**
Terminal output of:

```bash
ls -l backup.sh
```

**Screenshot should show:**

- Terminal prompt
- The command: `ls -l backup.sh`
- Output showing executable permissions: `-rwxr-xr-x` or similar
- The x (execute) permission bit should be visible

**Example output:**

```
$ ls -l backup.sh
-rwxr-xr-x 1 user user 1234 Dec  5 10:00 backup.sh
```

**Key indicators:**

- First character: `-` (regular file)
- Characters 2-4: `rwx` (owner can read, write, execute)
- The presence of 'x' indicates executable

---

### 📸 Task 16: Backup File Created

**Filename:** `16-backup-complete.jpg` or `.png`

**What to capture:**
Terminal output of:

```bash
ls -l backup-*.tar.gz
```

**Screenshot should show:**

- Terminal prompt
- The ls command
- Output showing backup file(s) with timestamp in name
- File size
- Date/time created

**Example output:**

```
$ ls -l backup-*.tar.gz
-rw-r--r-- 1 user user 12345 Dec  5 10:00 backup-1733399200.tar.gz
```

**Key indicators:**

- Filename format: `backup-[TIMESTAMP].tar.gz`
- File exists and has size > 0

---

### 📸 Task 17: Crontab Schedule

**Filename:** `17-crontab.jpg` or `.png`

**What to capture:**
Terminal output of:

```bash
crontab -l
```

**Screenshot should show:**

- Terminal prompt
- The command: `crontab -l`
- Cron entry for daily backup
- Full path to backup.sh script
- Directory arguments

**Example output:**

```
$ crontab -l
0 0 * * * /usr/local/bin/backup.sh /home/project/important-documents /home/project
```

**Key components of cron entry:**

- `0 0 * * *` - Daily at midnight
- `/usr/local/bin/backup.sh` - Full path to script
- Two directory arguments

**Alternative schedules:**

```bash
# Every minute (for testing)
*/1 * * * * /usr/local/bin/backup.sh /home/project/important-documents /home/project

# Daily at 2:30 AM
30 2 * * * /usr/local/bin/backup.sh /home/project/important-documents /home/project
```

---

## 🎨 Screenshot Taking Tips

### Using Terminal/IDE:

1. **Clear your terminal** before taking screenshots

   ```bash
   clear
   ```

2. **Use appropriate zoom level** - Make text readable

3. **Include context** - Show a few lines above/below the relevant code

4. **Avoid clutter** - Close unnecessary windows/tabs

5. **Use consistent formatting** - Keep your editor settings consistent

### Tools for Screenshots:

**Windows:**

- Snipping Tool (Win + Shift + S)
- Print Screen (PrtScn)

**macOS:**

- Cmd + Shift + 4 (select area)
- Cmd + Shift + 3 (full screen)

**Linux:**

- gnome-screenshot
- Spectacle (KDE)
- Flameshot

---

## ✅ Screenshot Checklist

Before submitting, verify each screenshot:

- [ ] Filename matches exactly (case-sensitive)
- [ ] File format is JPEG or PNG
- [ ] Image is clear and readable
- [ ] Shows the correct task code
- [ ] Includes task comment marker
- [ ] No sensitive information visible
- [ ] File size is reasonable (<5MB)

---

## 📊 Screenshot Summary Table

| Task | Screenshot Name                        | Content              | Points |
| ---- | -------------------------------------- | -------------------- | ------ |
| 1    | 01-Set_Variables.jpg/png               | Variable assignments | 1      |
| 2    | 02-Display_Values.jpg/png              | Echo statements      | 1      |
| 3    | 03-CurrentTS.jpg/png                   | Current timestamp    | 1      |
| 4    | 04-Set_Value.jpg/png                   | Backup filename      | 1      |
| 5    | 05-Define_Variable.jpg/png             | Original path        | 1      |
| 6    | 06-Define_Variable.jpg/png             | Destination path     | 1      |
| 7    | 07-Change_Directory.jpg/png            | Directory changes    | 1      |
| 8    | 08-YesterdayTS.jpg/png                 | Yesterday timestamp  | 1      |
| 9    | 09-List_AllFilesandDirectories.jpg/png | For loop             | 1      |
| 10   | 10-IF_Statement.jpg/png                | If condition         | 1      |
| 11   | 11-Add_File.jpg/png                    | Array append         | 1      |
| 12   | 12-Create_Backup.jpg/png               | Tar command          | 1      |
| 13   | 13-Move_Backup.jpg/png                 | Move command         | 1      |
| 14   | backup.sh (file)                       | Complete script      | 1      |
| 15   | 15-executable.jpg/png                  | ls -l output         | 2      |
| 16   | 16-backup-complete.jpg/png             | Backup file listed   | 2      |
| 17   | 17-crontab.jpg/png                     | Crontab entry        | 2      |

**Total: 20 points**

---

## 🚨 Common Screenshot Mistakes

### ❌ Don't:

- Take blurry or unreadable screenshots
- Include personal/sensitive information
- Use wrong file formats (e.g., .gif, .bmp)
- Crop out task comment markers
- Show incomplete code sections
- Use wrong filenames

### ✅ Do:

- Ensure text is crisp and clear
- Include task markers in code screenshots
- Use exact filenames as specified
- Show complete relevant code sections
- Include command prompts in terminal screenshots
- Verify file format before submitting

---

## 💾 Organizing Your Screenshots

Create a dedicated folder structure:

```
peer_graded_final_project/
├── screenshots/
│   ├── 01-Set_Variables.png
│   ├── 02-Display_Values.png
│   ├── 03-CurrentTS.png
│   ├── 04-Set_Value.png
│   ├── 05-Define_Variable.png
│   ├── 06-Define_Variable.png
│   ├── 07-Change_Directory.png
│   ├── 08-YesterdayTS.png
│   ├── 09-List_AllFilesandDirectories.png
│   ├── 10-IF_Statement.png
│   ├── 11-Add_File.png
│   ├── 12-Create_Backup.png
│   ├── 13-Move_Backup.png
│   ├── 15-executable.png
│   ├── 16-backup-complete.png
│   └── 17-crontab.png
└── backup.sh
```

---

## 🎉 Final Checklist

Before submission:

- [ ] All 16 screenshots taken
- [ ] backup.sh file saved
- [ ] All filenames are correct
- [ ] All images are in JPEG/PNG format
- [ ] Images are clear and readable
- [ ] Organized in submission folder
- [ ] Ready for peer grading upload

---

**Good luck with your submission! 🚀**

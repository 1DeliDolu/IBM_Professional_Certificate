#!/bin/bash

# Testing Guide for backup.sh Script
# This script helps verify that backup.sh works correctly

echo "=================================================="
echo "  BACKUP.SH TESTING GUIDE"
echo "=================================================="
echo ""

# Check if backup.sh exists
if [ ! -f "backup.sh" ]; then
    echo "❌ ERROR: backup.sh not found in current directory"
    echo "Please ensure backup.sh is in the same directory as this test script"
    exit 1
fi

echo "✅ backup.sh found"
echo ""

# Check if backup.sh is executable
if [ -x "backup.sh" ]; then
    echo "✅ backup.sh is executable"
else
    echo "⚠️  backup.sh is not executable"
    echo "Running: chmod +x backup.sh"
    chmod +x backup.sh
    echo "✅ Made backup.sh executable"
fi
echo ""

# Create test directories
echo "📁 Setting up test environment..."
mkdir -p test_source test_destination 2>/dev/null
echo "✅ Created test_source and test_destination directories"
echo ""

# Create test files with different timestamps
echo "📝 Creating test files..."
cd test_source || exit

# Create old files (should NOT be backed up)
echo "old content 1" > old_file1.txt
echo "old content 2" > old_file2.txt
touch -t 202312010000 old_file1.txt old_file2.txt

# Create recent files (SHOULD be backed up)
echo "recent content 1" > recent_file1.txt
echo "recent content 2" > recent_file2.txt
echo "recent content 3" > recent_file3.txt
touch recent_file*.txt

cd ..
echo "✅ Created test files (3 recent, 2 old)"
echo ""

# Display test file timestamps
echo "📅 Test file timestamps:"
ls -lt test_source/
echo ""

# Run the backup script
echo "🚀 Running backup.sh..."
echo "Command: ./backup.sh test_source test_destination"
echo ""
./backup.sh test_source test_destination
echo ""

# Check if backup was created
echo "🔍 Checking backup results..."
backup_files=$(ls test_destination/backup-*.tar.gz 2>/dev/null | wc -l)

if [ "$backup_files" -gt 0 ]; then
    echo "✅ Backup file(s) created successfully!"
    echo ""
    echo "Backup file(s) in test_destination:"
    ls -lh test_destination/backup-*.tar.gz
    echo ""
    
    # Extract and verify backup contents
    latest_backup=$(ls -t test_destination/backup-*.tar.gz | head -1)
    echo "🔍 Verifying backup contents..."
    echo "Latest backup: $latest_backup"
    echo ""
    echo "Files in backup:"
    tar -tzf "$latest_backup"
    echo ""
    
    # Count files in backup
    file_count=$(tar -tzf "$latest_backup" | wc -l)
    echo "📊 Backup contains $file_count file(s)"
    
    # Check if only recent files were backed up
    if tar -tzf "$latest_backup" | grep -q "old_file"; then
        echo "⚠️  WARNING: Backup contains old files (>24 hours old)"
        echo "This may indicate an issue with the timestamp check"
    else
        echo "✅ Backup correctly excludes old files"
    fi
    
    if tar -tzf "$latest_backup" | grep -q "recent_file"; then
        echo "✅ Backup contains recent files"
    else
        echo "⚠️  WARNING: Backup does not contain recent files"
    fi
else
    echo "❌ ERROR: No backup file created"
    echo "Please check the script for errors"
    exit 1
fi

echo ""
echo "=================================================="
echo "  TEST SUMMARY"
echo "=================================================="
echo ""
echo "✅ Script execution: SUCCESS"
echo "✅ Backup file created: YES"
echo "✅ Files backed up: $file_count"
echo ""
echo "📁 Test directories created:"
echo "   - test_source/ (contains test files)"
echo "   - test_destination/ (contains backup)"
echo ""
echo "🧹 To clean up test files, run:"
echo "   rm -rf test_source test_destination"
echo ""
echo "=================================================="
echo "  TESTING COMPLETE"
echo "=================================================="

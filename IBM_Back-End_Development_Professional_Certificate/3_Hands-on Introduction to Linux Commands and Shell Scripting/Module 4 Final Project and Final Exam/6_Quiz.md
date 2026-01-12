### 1.

Question 1

What is Linux?


[ ]

Linux is a programming language for developing web applications

[X]

Linux is a family of Unix-like operating systems

[ ]

Linux is a proprietary operating system developed by Microsoft

[ ]

Linux is a type of computer hardware that can run graphical applications

Correct

Correct! Linux is a family of operating systems that function like the UNIX operating system It is an open-source operating system that allows multiple users to access the system simultaneously.

1 / 1 point

### 2.

Question 2

Which layer of the Linux system enables you to interact with the Linux operating system?


[X]

User Interface (UI)

[ ]

Operating system

[ ]

Hardware

[ ]

Application

Correct

Correct! The User Interface allows users to interact with the system and is responsive to keyboard and mouse input.

1 / 1 point

### 3.

Question 3

Which shell command can you use to change the current working directory to your home directory?


[ ]

cd !

[ ]

cd ..

[ ]

cd /

[X]

cd ~

Correct

Correct! The tilde ( ~ ) is a shortcut for specifying the path to your home directory.

1 / 1 point

### 4.

Question 4

Which mode do you use in Vim to enter text?


[ ]

Edit

[ ]

Command

[X]

Insert

[ ]

Enter

Correct

Correct! You can enter Insert mode in Vim by pressing ‘i’. This will allow you to enter text.

1 / 1 point

### 5.

Question 5

Which shell command can you use to display information about mounted file systems?


[ ]

ps

[ ]

head

[ ]

cat

[X]

df

Correct

Correct! The df command is a common shell command that displays information about mounted file systems.

1 / 1 point

### 6.

Question 6

Assume your present working directory is folder1, which contains a file named file1.txt and a folder named folder2. Also assume folder2 contains a file named file2.txt. Which of the following commands would successfully remove file2.txt?


[ ]

rmdir folder2/file2.txt

[ ]

rm folder2/file2.txt

[X]

rmdir -r folder2/file2.txt

[ ]

rm file2.txt

Incorrect

Incorrect. Please review the video File and Directory Management Commands.

1 point

### 7.

Question 7

Assume you run the command wc contract.txt and receive the following output: 40 185 1302 contract.txt

What does the number “40” indicate about contract.txt?


[ ]

Number of words

[X]

Number of lines

[ ]

Number of characters

[ ]

Number of spaces

Correct

Correct! The wc command will return, in order, the number of lines, words, and characters in a file. In this example, the output of wc document.txt indicates that contract.txt contains 40 lines, 185 words, and 1,302 characters.

1 / 1 point

### 8.

Question 8

Which command prints all lines in the file contract.txt that contain the word “will” and ignores the case of the text while matching?


[ ]

cut -n will contract.txt

[X]

grep -i will contract.txt

[ ]

uniq -c will contract.txt

[ ]

sort -v will contract.txt

Correct

Correct! The grep command allows you to specify a pattern and search for lines from the input text that contain a match to the pattern. Add the -i option to the command to ignore the case of the text while matching.

1 / 1 point

### 9.

Question 9

Which command displays the hardware specification of a Wi-Fi adapter wifi0?


[ ]

hostname wifi0

[ ]

ping wifi0

[ ]

netstat wifi0

[X]

ip addr show wifi0

Correct

Correct! The ip addr show wifi0 command displays detailed information about the specific network device wifi0, such as its IP address, status, and hardware specifications. To view information about all installed network devices, you can use the command ip addr show without specifying a device name.

The ip addr show wifi0 command can display information, including hardware specifications, about network devices such as Wi-Fi adapters. To display information about all installed network devices, enter ip a with no options. To display information about a specific network device, specify the device name after ip addr show in your command.

1 / 1 point

### 10.

Question 10

Which command creates an archive of the /etc directory and names this archive etc.tar?


[ ]

tar -xf /etc etc.tar

[X]

tar -cf etc.tar /etc

[ ]

tar -lf etc.tar /etc

[ ]

tar -tf /etc etc.tar

Correct

Correct! To create a new archive file, you must include the -c option. After listing the -c option, you must list the name for the new archive file and then the file’s destination path.

1 / 1 point

### 11.

Question 11

How can you change the permissions of a shell script to make it executable for all users?


[ ]

chmod +w script_name.sh

[X]

chmod +x script_name.sh

[ ]

chmod +r script_name.sh

[ ]

chmod +s script_name.sh

Correct

Correct! You can use the chmod command to change permissions on a file. The +x option allows all users to execute the file.

1 / 1 point

### 12.

Question 12

Which command can you use to extend a shell variable to an environment variable?


[ ]

set

[ ]

grep

[ ]

env

[X]

export

Correct

Correct! The export command extends a shell variable to an environment variable, that persists in any child processes spawned by the shell in which the variable originates.

1 / 1 point

### 13.

Question 13

Assume you have a file named shoppinglist.txt. In the terminal, you want to print each line of shoppinglist.txt in alphabetical order, but you want to omit consecutively repeated lines from the output. Which of the following Bash inputs should you use?


[ ]

sort shoppinglist.txt \\> uniq

[ ]

uniq shoppinglist.txt | sort

[X]

sort shoppinglist.txt | uniq

[ ]

uniq shoppinglist.txt \\> sort

Correct

Correct! The sort command prints each line of a file; by default, the sort command will print each line in alphabetical order. The uniq command prints each line of a file while omitting consecutively repeated lines from the output. In this example, first use the sort command on shoppinglist.txt. Next, use the pipe operator (|) followed by the uniq command to print the output from sort shoppinglist.txt while omitting consecutively repeated lines.

1 / 1 point

### 14.

Question 14

Which input can you use to run the pwd command and ls command in parallel?


[X]

pwd & ls

[ ]

psd; ls

[ ]

pwd \\>\\> ls

[ ]

pwd = ls

Correct

Correct! You can use the ampersand (&) operator to make two Bash commands run in parallel.

1 / 1 point

### 15.

Question 15

Which cron command removes the current crontab?


[ ]

crontab -u

[ ]

crontab -l

[X]

crontab -r

[ ]

crontab -e

Correct

Correct! Entering crontab -r on the command line removes the current crontab.ntering crontab -l on the command line lists all the scheduled jobs in the current crontab.



### 1.

Question 1

What is an operating system?


[ ]

The process of running multiple instances of a program on a computer system

[X]

The software that manages computer hardware and resources

[ ]

The physical components of a computer system, such as the keyboard, mouse, and monitor

[ ]

The collection of files and programs that a user interacts with on a computer system

Correct

Correct! An operating system is a software that manages a computer’s hardware and its resources It enables interaction with hardware to perform useful tasks.

1 / 1 point

### 2.

Question 2

Which layer of the Linux system enables you to interact with the Linux operating system?


[ ]

Operating system

[ ]

Hardware

[ ]

Application

[X]

User Interface (UI)

Correct

Correct! The User Interface allows users to interact with the system and is responsive to keyboard and mouse input.

1 / 1 point

### 3.

Question 3

Which shell command can you use to change the current working directory to the root directory?


[ ]

cd !

[X]

cd /

[ ]

cd ~

[ ]

cd ..

Correct

Correct! The slash ( / )  is a shortcut for specifying the path to your root directory.

1 / 1 point

### 4.

Question 4

Which mode do you use in Vim to enter text?


[X]

Insert

[ ]

Command

[ ]

Edit

[ ]

Enter

Correct

Correct! You can enter Insert mode in Vim by pressing ‘i’. This will allow you to enter text.

1 / 1 point

### 5.

Question 5

Which shell command can you use to print the contents of a file?


[ ]

touch

[ ]

wget

[X]

cat

[ ]

man

Correct

Correct! There are some common commands for printing file contents or strings. The cat command prints the entire content of a file.

1 / 1 point

### 6.

Question 6

You can use the touch command for which of the following purposes?


[ ]

To add a string to a file

[ ]

To change a file’s permissions

[X]

To create a new file

[ ]

To display a file’s contents

Correct

Correct! You can use the touch command to create a new file or update an existing file’s timestamp.

1 / 1 point

### 7.

Question 7

Assume you run the command wc contract.txt and receive the following output: 40 185 1302 contract.txt

What does the number “40” indicate about contract.txt?


[X]

Number of lines

[ ]

Number of words

[ ]

Number of spaces

[ ]

Number of characters

Correct

Correct! The wc command will return, in order, the number of lines, words, and characters in a file. In this example, the output of wc document.txt indicates that contract.txt contains 40 lines, 185 words, and 1,302 characters.

1 / 1 point

### 8.

Question 8

Which command prints all lines from the file test.txt that contain the word “evaluate”?


[X]

grep evaluate test.txt

[ ]

tail evaluate test.txt

[ ]

cat evaluate test.txt

[ ]

paste evaluate test.txt

Correct

Correct! The grep command allows you to specify a pattern and search for lines from the input text that contain a match to the pattern.

1 / 1 point

### 9.

Question 9

What does the ip a command do?


[ ]

Sends Internet Control Message Protocol requests to a server

[ ]

Transfers data to or from a server

[X]

Displays information on all the system’s network devices

[ ]

Shows or sets the system’s host name

Correct

Correct! The ip a command stands for Interface configuration. It displays information regarding all your device’s communication devices.

1 / 1 point

### 10.

Question 10

Which command creates an archive of the /etc directory and names this archive etc.tar?


[ ]

tar -tf /etc etc.tar

[ ]

tar -lf etc.tar /etc

[X]

tar -cf etc.tar /etc

[ ]

tar -xf /etc etc.tar

Correct

Correct! To create a new archive file, you must include the -c option. After listing the -c option, you must list the name for the new archive file and then the file’s destination path.

1 / 1 point

### 11.

Question 11

Which extension is used to indicate a file is a shell script?


[X]

.sh

[ ]

.ss

[ ]

.script

[ ]

.shebang

Correct

Correct! The .sh extension is used to indicate that a file is a shell script.

1 / 1 point

### 12.

Question 12

Which command can you use to extend a shell variable to an environment variable?


[ ]

set

[X]

export

[ ]

grep

[ ]

env

Correct

Correct! The export command extends a shell variable to an environment variable, that persists in any child processes spawned by the shell in which the variable originates.

1 / 1 point

### 13.

Question 13

Assume you have a file named storelist.txt. In the terminal, you want to display only the last 10 lines of the file. From this list of 10 lines, you also want to omit any consecutively repeated lines from the output. Which of the following Bash inputs should you use?


[ ]

uniq storelist.txt > tail

[ ]

uniq storelist.txt | tail

[ ]

tail storelist.txt > uniq

[X]

tail storelist.txt | uniq

Correct

Correct! The tail command prints the last ten lines of a file. The uniq command prints each line of a file while omitting consecutively repeated lines from the output. In this example, first run the tail command on storelist.txt. Next, use the pipe operator (|) followed by the uniq command to print the output from tail storelist.txt while omitting consecutively repeated lines.

1 / 1 point

### 14.

Question 14

Which input can you use to run the pwd command and ls command in parallel?


[ ]

pwd = ls

[X]

pwd & ls

[ ]

psd; ls

[ ]

pwd \\>\\> ls

Correct

Correct! You can use the ampersand (&) operator to make two Bash commands run in parallel.

1 / 1 point

### 15.

Question 15

Which cron command returns the current crontab?


[ ]

crontab -e

[ ]

crontab -u

[ ]

crontab -r

[X]

crontab -l

Correct

Correct! Entering crontab -l on the command line lists all the scheduled jobs in the current crontab.

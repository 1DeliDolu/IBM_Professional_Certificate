### 1.

Question 1

Why is the implementation of code practices necessary?


[X]Establishes secure coding standards

[ ]Validates data from untrusted sources

[ ]Allows developers to follow the same process

[ ]Reduces exposed threats on source code

Correct! Implementing code practices is an essential part of developing secure software. Implementing code practices helps mitigate vulnerabilities and attacks. It’s cost-effective, too. Correcting unsecure code later in development or after production is very expensive. Implement code practices early in development.


### 2.

Question 2

If you plan to allow malicious characters as part of input data, what must you do to make their use more secure?


[ ]Log input tampering events

[X]Input scrubbing

[ ]Use dependencies to handle malicious characters

[ ]Establish general code practices

Correct! Malicious characters must be scrubbed or removed if allowed as input data. Also, if malicious characters are permitted, implement controls such as output encoding, secure task-specific APIs, and accounting for all data throughout an entire application.

### 3.

Question 3

If you wish to translate special characters into an equivalent but safe version, what must you use?


[ ]Flask

[X]Output encoding

[ ]Secure input

[ ]A reusable code library

Correct! Output encoding is the translation of input code to safe output code.

### 4.

Question 4

Attackers try to target insecure code at which layer in the OSI model?


[X]Application layer

[ ]Session layer

[ ]Network layer

[ ]Transport layer

Correct! Attackers target insecure code in the application layer.

### 5.

Question 5

You are tasked with implementing secure coding standards in your organization’s software development life cycle. Which of the following is a good practice to implement?


[X]Develop with tested and approved managed code

[ ]Always implement error logging

[ ]Maintain a list of malicious characters

[ ]Only write code on high-end developer machines

Correct! Develop with tested and approved managed code to reduce the risk of vulnerabilities entering into your code base.

### 6.

Question 6

What is a dependency?


[X]Is needed when a piece of software or code relies on another to function

[ ]A well-designed API

[ ]A framework based on Python

[ ]An open-source package manager

Correct! A dependency is reusable code found in a library, package, or module. It’s frequently used to add features and functionality to a software application that currently doesn’t exist. It eliminates the need to write the feature or functionality code from scratch, thus saving time and money.

### 7.

Question 7

You are developing a software application and are considering the use of dependencies to add extra functionalities not native to the platform being used. Before you implement, what should you do?


[ ]Only use third-party dependencies

[ ]Build a reusable object library to reduce risk

[X]Check dependency’s issue tracker for bugs

[ ]Talk to your colleagues about dependencies they’ve used in the past

Correct! Check dependency's issue tracker for open issues and bug reports.

### 8.

Question 8

Why should you avoid using a dependency that hasn’t been updated for a year or more?


[ ]The dependency is part of a reusable library that is up-to-date

[ ]The dependency has its own dependency, which receives all the updates

[X]The dependency was likely abandoned

[ ]The dependency is stable and hasn’t required any updates or fixes

Correct! Review the dependency’s commit history for bug fixes and ongoing improvements. Dependencies that haven’t been updated in a long time are likely abandoned and no longer maintained. Avoid using dependencies that haven't been updated for a year or more.

### 9.

Question 9

You are making progress in developing your software application. You can save time by implementing dependencies in your code instead of writing it from scratch. You’ve noticed that some of these dependencies are updated regularly. What should you do?


[ ]Only use dependencies whose APIs are well-designed and well-documented

[ ]Try reducing the number of dependencies in your code

[X]Use a dependency management tool

[ ]Check the quality of the code for indicators that frequent updates are needed

Correct! Use a dependency management tool to manage downloads and track version updates.

### 10.

Question 10

You are developing an application that needs to send data to an untrusted environment and get it back later, ensuring that no one has tampered with it during transit. Which dependency can provide this functionality?


[ ]Werkzeug

[ ]Flask

[X]ItsDangerous

[ ]MarkupSafe


Correct! You can call the dependency, ItsDangerous, to generate a token for transmitting account information between web requests.

### 1.

Question 1

There were no critical vulnerabilities in the code.


[ ]True

[X]False

Incorrect

Correct! The code has critical vulnerabilities.

1 point

### 2.

Question 2

In the code, which version of the node was used by the developers?


[ ]node:bullseye

[ ]node:bookworm-slim

[X]node:hydrogen-buster

[ ]node:alpine

Correct

Correct! The developers used ‘node:hydrogen-buster’ to code. Hydrogen-buster is a tag for the node build from docker, which has a lot of vulnerabilities.

1 / 1 point

### 3.

Question 3

What does the CSRF (Cross-Site Request Forgery) package in the code fix do?


[ ]Allows developers to test cross-site request forgery in code

[ ]Creates a secret code for cross-site request forgery

[X]Addresses cross-site request forgery

[ ]Triggers a cross-site request forgery attack

Correct

Correct! CSRF attacks target functionality that causes a state change on the server, such as changing the victim's email address or password or purchasing something.

1 / 1 point

### 4.

Question 4

What is the right sequence of actions to address the vulnerabilities in the code?


[ ]Add project to Snyk, Fork, Scan, Fix

[ ]Add project to Snyk, Scan, Fork, Fix

[X]Fork, Add project to Snyk, Scan, Fix

[ ]Scan, Add project to Snyk, Fork, Fix

Correct

Correct! To address the vulnerabilities in the code, first, you fork the code, then you add the project or code to Snyk, then you scan for vulnerabilities, and finally, you fix them.

1 / 1 point

### 5.

Question 5

What are the four categories of errors you can scan using Snyk?


[ ]Critical, High, Average, Small

[ ]Critical, Very High, Medium, Low

[X]Critical, High, Medium, Low

[ ]Critical, High, Average, Low

Correct

Correct! Severity levels help you with application vulnerability assessment. The risk levels are indicated by severity levels such as **C**ritical, **H**igh, **M**edium, or **L**ow.

1 / 1 point

### 6.

Question 6

What action should you take after editing the **Dockerfile **to fix the vulnerabilities?


[ ]Delete the old repository and fork again

[X]Re-run the Snyk scan to verify if the issues are resolved

[ ]Push the code to a new GitHub repository

[ ]Change the project name on Snyk

Correct

Correct! Re-running the scan helps confirm that the applied changes effectively fix the identified vulnerabilities.

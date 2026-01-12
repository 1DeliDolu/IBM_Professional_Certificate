### 1.

Question 1

What is the Open Web Application Security Project (OWASP)?

[ ]OWASP is a list of current security vulnerabilities

[X]OWASP is a foundation that focuses on software security

[ ]OWASP is a foundation that focuses on application development

[ ]OWASP is a core team of security analysts, security organizations, and other security experts

Correct

Correct! OWASP is a foundation that focuses on improving software security.

### 2.

Question 2

Which OWASP Top 10 vulnerability covers password issues, automated attacks like credential stuffing, and session identifier issues?


[ ]Software and data integrity failures

[ ]Server-side request forgery

[X]Identification and authentication failures

[ ]Logging and monitoring failures

Correct! In 2022, the number seven vulnerability was in identification and authentication failures to confirm the user's identity and authenticate the user.

### 3.

Question 3

An attack that combines two unrelated queries to grab data from different tables is an example of which type of injection.


[ ]Code function

[ ]Stored

[ ]Reflected

[X]Manipulation

Correct! An SQL manipulation attack can use a UNION SELECT statement to combine two unrelated SELECT queries to grab data from different tables.

### 4.

Question 4

How does using a parameter prevent SQL injection?


[ ]The SQL releases the placeholder to production

[ ]The SQL restricts user access to read-only

[X]The SQL treats the input as a string

[ ]The SQL treats the input as a set statement

Correct! The SQL will treat the input as a string, and the string will not get executed as a statement.

### 5.

Question 5

To monitor and track who is accessing which resources, what must you address in development?


[ ]Communicating with decoupled applications

[ ]Authentication and validation

[X]Auditing and logging

[ ]Encrypting the written data that is stored

Correct! Auditing and logging are essential to monitor and track who is accessing which resources.

### 6.

Question 6

Which type of cross-site scripting is also referred to as persistent?


[ ]Code

[ ]Reflective

[ ]Blind

[X]Stored

Correct! Stored cross-site scripting is also referred to as persistent because this type of attack injects a script that becomes permanently stored in a database or a targeted server.

### 7.

Question 7

What is the best way to prevent a cryptographic failure?


[ ]Use FTP or SMTP

[ ]Encrypt only data stored in the database

[ ]Encrypt only data that is being currently transmitted

[X]Use authenticated encryption

Correct! The best strategy to prevent cryptographic failures is to encrypt all sensitive data stored in the database using authenticated encryption instead of traditional encryption methods. Encrypt data that is at rest and also data in transit. Use HTTPS over HTTP to ensure that all data transmitted is encrypted. Finally, avoid using older protocols such as SMTP and FTP, which are prone to man-in-the-middle attacks.

### 8.

Question 8

Which strategy is best for preventing injection attacks?


[X]Use a secure API that avoids using the interpreter

[ ]Use traditional encryption methods

[ ]Perform regular access control checks

[ ]Disable directory listings in URLs

Correct! The best way to eliminate injection attacks is to use a secure API that avoids using the interpreter or offers a parameterized interface.

### 9.

Question 9

Error messages are an essential part of app development and troubleshooting. Sometimes, error messages reveal too much information and expose vulnerabilities in your app. Which best practice should you follow to handle errors correctly?


[X]Use a secure error handler

[ ]Remove framework and features not needed to reduce vulnerabilities

[ ]Handle sensitive UI errors as “An unknown error has occurred.”

[ ]Avoid using outdated dependencies to reduce vulnerabilities


Correct! The best way to address error-handling is to use a secure error handler. Write user-friendly error messages in the UI for users that reveal no factual information and write more detailed errors in a log file that is useful for troubleshooting. Keeping specific information out of UI messages reduces the exposure to vulnerabilities.

### 10.

Question 10

What strategy can you use to help stop brute-force, credential-stuffing, and stolen credential reuse attacks?


[ ]Only use dependencies from the past 12 months

[X]Implement multifactor authentication where possible

[ ]Enable auto-updates to verify application integrity

[ ]Include session header information inside URLs

Correct! Multifactor authentication can help stop brute-force, credential-stuffing, and stolen credential reuse attacks.

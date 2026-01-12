### 1.

Question 1

What is a dependency?


[ ]A framework based on Python

[ ]A well-designed API

[X]Reusable code found in a library

[ ]An open-source package manager

Correct! A dependency is a reusable code found in a library, package, or module. It’s often used to add features and functionality to a software application that currently doesn’t exist. It eliminates the need to write the feature or functionality code from scratch, thus saving time and money.

### 2.

Question 2

What can you do to protect an API key in your code?


[ ]Store the key in a database since the data is always encrypted.

[X]Implement a secrets management solution.

[ ]Only store certificates and passwords in your code.

[ ]Encrypt the key in your code so it doesn’t appear in plaintext.

Correct! You must store passwords, certificates, and API encryption keys using a secrets management solution to manage and integrate it with your applications and databases. A tool like Vault, developed by Hashicorp, can help. It is a token-based storage solution for managing secrets.

### 3.

Question 3

You are assigned to review an extremely large codebase in a short period of time. You are also required to be able to make any necessary changes immediately. What is the best way to achieve this?


[ ]Use static analysis security testing.

[ ]Use a validation checker.

[X]Use automated code review.

[ ]Use manual code review.

Correct! If you have a large number of files and lengthy codes, an automated code review is the best choice of action. Large codebases are evaluated quickly and efficiently. When used while writing code, changes can be made right away.

### 4.

Question 4

Your company’s database was the target of a SQL injection attack. You’re not sure how it happened since you were hired long after the database was put into production. What steps can you take to secure your web application?


[ ]Use custom functions in SQL statements.

[ ]Substitute variables and values.

[ ]Use SQL manipulation.

[X]Use server-side validation.

Correct! Protect your application against SQL injection attacks by using server-side validation to identify untrusted data inputs.

### 5.

Question 5

You wrote the code for a web application. No vulnerabilities were found before it went live last month. Is it safe to assume that your application is still free of vulnerabilities today?


[ ]Yes, it’s a safe to assume that no new vulnerabilities were discovered in the past 30 days.

[ ]Yes, it’s a safe assumption. Our web app uses SSL to encrypt all connections. Encrypted apps can’t be attacked.

[ ]Yes, it’s a safe assumption. Our IT Department always keeps our servers and databases updated and uses powerful firewall technology to prevent intrusions.

[X]No. It’s never safe to make that assumption. I have no idea what vulnerabilities could be lurking around in my code.

Correct! Code that was secure last month could be vulnerable today. Implement security early in the software development lifecycle. Use vulnerability analysis tools during testing before your app goes live. Perform regular vulnerability scans after the go-live date. Keep informed of the latest vulnerabilities by checking vulnerability reports which are published daily.

### 6.

Question 6

You are tasked with keeping your data safe from unauthorized changes by outside forces with malicious intent. What process can you use to achieve that goal?


[ ]Data encryption

[ ]Data quality

[ ]Data security

[X]Data integrity

Correct! Data integrity is the process of ensuring stored data hasn’t been changed by an unauthenticated source. It means you can trust the data you’re reading.

### 7.

Question 7

You are working on a software application and need to find a way to analyze your code to check its correctness. Which method will help you accomplish this task?


[X]Static analysis

[ ]Data analysis

[ ]Interface analysis

[ ]Fault or failure analysis

Correct! Static analysis is a debugging method that automatically checks your source or object code or runtime binaries for correctness without executing the code. It covers more avenues of code execution, verifies the code as you work on the build, and indicates where potential problems may exist in your code.

### 8.

Question 8

You have been given access to an application that needs to be checked for flaws, memory issues, and crashes during runtime. Choose the appropriate analysis method for this task.


[ ]Interface analysis

[X]Dynamic analysis

[ ]Memory analysis

[ ]Data analysis

Correct! Dynamic analysis is the process of testing and evaluating an application during runtime. Use it to analyze fully built applications in production. Scan to diagnose and fix flaws, memory issues, and crashes.

### 9.

Question 9

Cross-site scripting attacks are listed as one of the OWASP top 10 most critical types of security risks for web applications. What action can you take to prevent them?


[ ]Turn off HTTPS TRACE support on a web server.

[X]Escape suspect lists.

[ ]Use unsafe sinks by refactoring code to use textContext or values.

[ ]Look for suspicious HTTPS requests or keywords.

Correct! Escaping suspect lists and keywords and blocking special characters can help prevent cross-site scripting attacks. Looking for suspicious HTTP requests or keywords, disabling HTTP TRACE support on web servers, and avoiding the use of unsafe sinks by refactoring or using text content or values can also help.

### 10.

Question 10

At what point should threat modeling be implemented in the software development lifecycle (SDLC)?


[ ]Test phase

[ ]Requirements phase

[X]Design phase

[ ]Development phase

Correct! The best time to implement threat modeling is during the design phase. By developing threat models early, you can lessen the potential for software vulnerabilities and eliminate weaknesses in the application.

### 11.

Question 11

Your organization is building software and, at the same time, battling security issues. The issues are causing significant time delays at the testing level. What type of solution should you look for?


[ ]Use an updated TLS version to avoid security vulnerabilities.

[ ]Hire teams to resolve coding and security flaws.

[X]Use DevSecOps to reduce time spent on fixing security vulnerabilities.

[ ]Use vulnerability analysis tools to improve security.

Correct! Security issues can cause significant time delays when software is built in a non-DevSecOps environment. DevSecOps helps reduce time spent on fixing security vulnerabilities by reducing the need to repeat a procedure to minimize development costs.

### 12.

Question 12

You are working on an application that requires data delivery in the same order in which they were received. Which of the following OSI layers helps you achieve this?


[X]Transport layer

[ ]Application layer

[ ]Data link layer

[ ]Network layer

Correct! The transport layer, which is the fourth layer of the OSI model, accepts transmissions or data from the session layer and then chops them into smaller units or packets for passing to the network layer. In addition, the transport layer assures that all the units arrive correctly from end to end. This layer provides an error-free point-to-point channel that delivers data in the same order in which they were received.

### 13.

Question 13

As an application developer, you have implemented cloud sources for developing applications. What must you configure for securing the cloud assets according to the needs and roles?


[ ]GitHub

[X]Identification and access management (IAM)

[ ]Network tool called Nmap

[ ]Network tool called snort

Correct! If cloud sources are implemented for developing applications, you must configure identification and access management (IAM) for securing cloud assets according to the needs and roles when developing. IAM roles are an important security mechanism to grant permissions to applications and systems within cloud infrastructures.

### 14.

Question 14

Your company has started a video streaming platform with secure TLS to give in-house live training to its employees. Some employees bring their own laptops to work. Few of these employees cannot connect their applications to the server. Considering there is no network problem, what could be the reason for this communication failure?


[ ]The application has bugs that are causing network problems.

[ ]The server and laptops are not generating session keys.

[ ]The application in laptops has encrypted data.

[X]The application in laptops may not have updated or supported TLS protocol version.

Correct! For two computers to communicate using a secure TLS protocol, they must first agree on a TLS version to use. Both must choose the highest supported version. The process will fail if the two computers don’t have the supported version.

### 15.

Question 15

Your organization has assigned you to develop an application for their new products and services division. How will you ensure that all code testing meets multiple valid testing criteria?


[ ]Use application monitoring techniques and tools during development.

[ ]Audit security issues throughout the development.

[ ]View system logs to track and fix the issues before testing.

[X]Implement static application security testing (SAST) and software composition analysis (SCA).

Correct! To ensure that all code testing meets multiple valid testing criteria, you must implement static application security testing (SAST) and software composition analysis (SCA) in addition to continuous security analysis.

### 16.

Question 16

You oversee a software development team at a tech firm. The security posture of your apps is a priority for your team. You’ve heard of the interactive application security testing (IAST) method for security testing. Which of the following is a feature of IAST in software development?


[ ]Detects and prevents attacks with great precision

[ ]Capable of monitoring and self-protecting application behavior

[X]Detects vulnerabilities and fixes them early in the SDLC

[ ]Protects against exploitation

Correct! IAST enables earlier and less expensive fixes. It gives you an edge in detecting and fixing vulnerabilities early in the development lifecycle when you work closely with your code. That’s when fixing errors and vulnerabilities will be the least expensive in terms of resources and security risk.

### 17.

Question 17

Which of the following is the number one vulnerability or is one of a web application’s most encountered vulnerabilities in the 2021 OWASP Top 10?


[ ]Injection vulnerabilities

[ ]Security misconfiguration

[X]Broken access control

[ ]Cryptographic failures

Correct! Broken access control is the number one vulnerability in the 2022 OWASP Top 10. It’s one of a web application’s most encountered vulnerabilities, which happens when attackers can access, modify, delete, or perform actions outside an application or system’s intended permissions.

### 18.

Question 18

Tech Giant Inc. is worried about potential identification and authentication failures that could damage their web application process. They are planning to implement some measures to improve their security. Which is the first step they should take following the guidelines of OWASP Top 7–10?


[ ]Avoid transmitting unencrypted sensitive data to untrusted sources.

[ ]Use multifactor authentication.

[X]Start with the software supply chain.

[ ]Perform regular checks and reviews on configuration changes.

1 point

### 19.

Question 19

An SQL injection is an attack where the attacker modifies an SQL statement by using set operations and altering the WHERE clause to return alternate results. Which of the following is the most common type of SQL injection?

[ ]Buffer overflows

[ ]Code injection

[X]SQL manipulation

[ ]Function call injection

Correct! SQL manipulation is one of the most common types of SQL injection. An SQL manipulation is an attack that modifies an SQL statement of set operations. Two common forms of SQL manipulation attacks use a WHERE clause or a UNION statement. Often, an SQL manipulation attack modifies a WHERE clause of user authentication to always result in TRUE.

### 20.

Question 20

You are working in an organization as a network administrator who wants to implement some best practices to secure the development environment. Which method will you recommend to your developers to ensure all ports are closed to the outside by default?


[ ]Provide additional security to developers who need to access production systems from their developer machines.

[X]Develop in Docker containers.

[ ]Regularly check for open ports and close unnecessary ports.

[ ]Implement multifactor authentication.

Correct! Developing in Docker containers is really helpful to ensure that only allowed access is granted. This is because the containers are on a separate isolated network from their development computer, and all ports are closed to the outside by default.

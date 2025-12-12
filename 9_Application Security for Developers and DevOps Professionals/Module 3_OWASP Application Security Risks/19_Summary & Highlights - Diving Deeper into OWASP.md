### 1.

Question 1

An attacker has injected your website with malicious scripts. These scripts are intended to run in another user’s browser. This script tries to steal the session cookies from users who visit your site. What type of attack has occurred?


[ ]An SQL manipulation attack

[ ]A function call injection attack

[X]Cross-site scripting

That’s correct! Cross-site scripting occurs when an application takes untrusted data and then sends it to a web browser without proper validation or escaping. Attackers use cross-site scripting to execute scripts in the victim’s browser to steal critical user data.

[ ]A server-side request forgery attack

1 / 1 point

### 2.

Question 2

An attacker has modified the WHERE clause of user authentication to always result in TRUE. What type of attack has occurred?


[ ]A credential stuffing attack

[ ]A local file inclusion attack

[X]An SQL manipulation attack

That’s correct! SQL manipulation is one of the most common types of SQL injection attacks. The attacker modifies an SQL statement of set operations. Two common forms of SQL manipulation attacks use a WHERE clause or a UNION statement.

[ ]A path traversal attack

1 / 1 point

### 3.

Question 3

An attacker has inserted an additional SQL statement into another SQL statement so that two will execute as one. What type of attack has occurred?


[ ]A buffer overflow attack

[X]A code injection attack

That’s correct! A code injection is an attack that inserts new SQL statements or database commands into another SQL statement. In code injection, typically the attacker will execute the two statements as one.

[ ]A cross-site scripting attack

[ ]A function call injection attack

1 / 1 point

### 4.

Question 4

An attacker has infiltrated your organization and has stolen your application programming interface (or API) encryption keys. What could you have implemented to prevent this from occurring?


[ ]A software component analysis solution

[X]A secrets management solution

That’s correct! Use a secrets management solution, such as Vault, to safely store, manage, and integrate passwords, certifications, and encryption keys with your applications and databases.

[ ]A continuous security analysis solution

[ ]A vulnerability analysis solution

1 / 1 point

### 5.

Question 5

Recently, there has been an increase in the number of times your application has crashed. Log analysis indicates tz_offset, a function that returns the time zone offset, was used to cause a buffer overflow. How could you have prevented this type of attack?


[ ]Use query parameters as placeholders

[ ]Use lists to escape or block suspicious keywords

[X]Look for suspicious HTTP requests and keywords

Not quite right. Looking for suspicious HTTP requests and keywords that can trigger a scripting engine is a preventative measure for blocking cross-site scripting attacks.

[ ]Avoid or remove references to unsafe sinks

1 point

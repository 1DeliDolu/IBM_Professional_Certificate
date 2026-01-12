### 1.

Question 1

Which feature of Flask provides the ability to redirect client requests?

[ ]Session management

[X]Routing

[ ]Static asset support

[ ]Error-handling

Correct

Correct! You can create routes for different HTTP methods and provide redirection in your application.

1 / 1 point

### 2.

Question 2

Which Flask package helps write command line interfaces?

[ ]ItsDangerous

[ ]Werkzeug

[X]Click

[ ]Jinja

Correct

Correct! Click is a framework for writing command-line applications.

1 / 1 point

### 3.

Question 3

Which Flask run command argument enables automatic restarts when source files are changed?

[X]--reload

[ ]@app.route

[ ]-name-

[ ]--app

Correct

Correct! The reload argument enables automatic restarts when source files are changed.

1 / 1 point

### 4.

Question 4

 Which configuration enables you to correct exceptions and errors?

[ ]ENV

[X]DEBUG

[ ]TESTING

[ ]SECRET_KEY

Correct

Correct! DEBUG indicates that the debug mode is enabled, and an interactive debugger is shown for exceptions and errors.

1 / 1 point

### 5.

Question 5

Which Flask application directory structure is considered good practice?

[ ]Store the main source in the configuration’s directory

[ ]Place all test files in a module directory

[ ]Store all static assets like image, JavaScript, and CSS files in one file

[X]Store all dynamic content in the directory that contains templates

Correct

Correct! You should store all dynamic content in the directory that contains all the templates.

1 / 1 point

### 6.

Question 6

Which Request attribute gives information about the IP addresses for requests that were forwarded multiple times?

[ ]headers

[ ]is_secure

[X]access_route

[ ]Accept

Correct

Correct! The access_route attribute lists all the IP addresses for requests that are forwarded multiple times.

1 / 1 point

### 7.

Question 7

Which Response Object method returns 302 and changes the URL of the client?

[ ]Abort

[ ]JSONify

[X]redirect

[ ]make_response

Correct

Correct! Flask provides a special redirect method to return a 302 and redirects the client to another URL.

1 / 1 point

### 8.

Question 8

 Which is the correct way to enable a dynamic route parameter called ‘isbn’?

[ ]D: app.route(“/book/{isbn})

[ ]*C: app.route(“/book/[int:isbn](int:isbn))

[X]app.route(“/book/isbn)

[ ]B: app.route(“/isbn)

Incorrect

Incorrect. Review the More on Routes video.

1 point

### 9.

Question 9

Which method is used to explicitly set the status code?

[ ]search_response

[ ]fetch_from_database

[ ]server_error

[X]make_response

Correct

Correct! You can use the make_response() method to explicitly set the status code.

1 / 1 point

### 10.

Question 10

Which error code indicates a server error?

[ ]404

[X]500

[ ]403

[ ]400

Correct

Correct! The error code 500 is used when there is an error on the server.

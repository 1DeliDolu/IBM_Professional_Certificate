
### 1.

Question 1

What command do you use to run migrations?

[ ]python manage.py runserver

[ ]python migrate

[ ]python manage.py makemigrations

[X]python manage.py migrate

Correct

Correct! This command is used to run migrations.

1 / 1 point

### 2.

Question 2

What is the correct format to write a URL in a Django application?


[X]path(URL path, view function, name)

[ ]

path(name, URL path, view function)

[ ]path(name, view function, URL path)

[ ]path(class name, view function, name)

Correct

Correct! The path() function takes two required arguments: the URL path and the view function to be called when the path is accessed. The name argument is an optional parameter.

1 / 1 point

### 3.

Question 3

Which utility function do you use to generate a URL from a view name and optional parameters?

[ ]get_urlconf (“index”)

[X]reverse(“index”)

[ ]resolve(“index”)

[ ]translate_url (“index”)

Correct

Correct! The reverse() function returns a string representing the URL pattern associated with the index view.

1 / 1 point

### 4.

Question 4

 Which function do you use to redirect the user to the index page after they log into the application?

[ ]HttpResponsePermanentRedirect

[ ]HttpResponseNotFound

[ ]HttpResponseNotModified

[X]HttpResponseRedirect

Correct

Correct! The HttpResponseRedirect function is used in Django views to handle form submissions or other POST requests.

1 / 1 point

### 5.

Question 5

Which function do you use to return an HTML page to the user?

[X]render()

[ ]return()

[ ]respond()

[ ]redirect()

Correct

Correct! The render() function is a shortcut function that is used to render a Django template with a context dictionary and return an HttpResponse object with the result.

1 / 1 point

### 6.

Question 6

Which model class field do you use to store concert_name with a maximum of 255 characters?

[ ]concert_name = models.TextField(max_length=255)

[X]concert_name = models.CharField(max_length=255)

[ ]concert_name = models.Field(max_length=255)

[ ]concert_name = models.Long_Text(max_length=255)

Correct

Correct! CharField is used to store character data.

1 / 1 point

### 7.

Question 7

Which model class field do you use to store event_date with the default date of now?

[X]event_date = models.DateField(default=datetime.now)

[ ]event_date = models.Date(default=datetime.now)

[ ]

event_date = models.Today(default=datetime.now)

[ ]event_date = models.MMDDYY(default=datetime.now)

Correct

Correct! The DateField is a model field class that is used to store date data.

1 / 1 point

### 8.

Question 8

How do you register the Concert model with the Django admin?

[ ]admin.site.add(Concert)

[X]admin.site.register(Concert)

[ ]admin.site.signup(Concert)

[ ]admin.register(Concert)

Correct

Correct! With this code, Django automatically adds an interface for managing instances of the Concert model.

1 / 1 point

### 9.

Question 9

How is re_path different from the path method in urls.py?

[ ]There is no method called re_path.

[ ]re_path and path are the same.

[X]re_path allows you to use regular expressions to define more complex URL patterns.

[ ]re_path automatically redirects the user to a different URL.

Correct

Correct! You can use the make_response() method to explicitly set the status code.

1 / 1 point

### 10.

Question 10

Which utility function do you use to securely hash a plaintext password when creating a new user?

[ ]password=hash_password(password))

[ ]password=django_password(password))

[X]password=make_password(password))

[ ]password=secure_password(password))

Correct

Correct! make_password is used to securely hash a plaintext password.

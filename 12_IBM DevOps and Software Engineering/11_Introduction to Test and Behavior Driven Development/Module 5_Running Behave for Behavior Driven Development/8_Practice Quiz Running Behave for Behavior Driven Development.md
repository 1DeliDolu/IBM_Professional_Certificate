### 1.

Question 1

You want to run the Behave tool for the first time against your feature file that does not have any steps. How will the Behave tool help you?

[X]Give a set of suggested steps

Correct! If you haven’t written any steps, then the first time you run Behave, all of the steps are missing. If this is the case, Behave will seed your development efforts with a set of suggested steps.

[ ]Behave will fail because there are no steps

[ ]Will show a blank screen

[ ]Will only validate your steps

1 / 1 point

### 2.

Question 2

What happens when you run Behave on a steps file created from the generated steps the first time?

[ ]The steps are shown in yellow

[X]An exception is raised

Correct! The first step fails, and it raises an exception.

[ ]All the steps pass

[ ]All of the steps are shown in blue

1 / 1 point

### 3.

Question 3

While implementing the first step to open the Home Page, which code will get the contents of the Home Page?

[ ]base_url

[ ]import getenv

[X]context.driver.get(context.base_url)

Correct! This code tells the web driver to issue an HTTP GET method on the URL of the Home Page to get the page’s contents.

[ ]HTTP GET

1 / 1 point

### 4.

Question 4

Which characteristic is true for the context variable?

[ ]The context variable argument can be passed only to one step.

[ ]Every step called from the feature file will share a different context.

[X]It exists for the duration of the entire feature file.

Correct! The context variable exists for the duration of the entire feature file and all of the steps.

[ ]The context information cannot be used for other steps.

1 / 1 point

### 5.

Question 5

What is the benefit of variable substitution?

[ ]To use different names for different variables

[X]To make the steps generic and reusable

Correct! Variable substitution is used to make steps as generic as possible for maximum reuse.

[ ]To make one sentence in your feature file match a single unique step

[ ]To make the steps specific and clear

1 / 1 point

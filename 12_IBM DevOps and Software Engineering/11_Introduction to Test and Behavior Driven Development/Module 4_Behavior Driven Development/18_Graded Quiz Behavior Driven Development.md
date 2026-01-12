
### 1.

Question 1

Which characteristic does behavior driven development (BDD) have in common with test driven development (TDD)?

[X]Emphasis on a test-first approach

[ ]Value for testing individual units of software

[ ]Focus on the system from the inside out

[ ]Goal of building the application correctly

Correct

Correct! Like TDD, BDD is a test-first approach to development; the tests drive code development.

1 / 1 point

### 2.

Question 2

With most behavior driven development (BDD) tools, which items can you automatically generate from your specifications?

[ ]Testing factories

[X]Technical documents

[ ]Project schedules

[ ]Kanban boards

Correct

Correct! With most BDD tools, you can draw from specifications to automatically generate technical documentation.

1 / 1 point

### 3.

Question 3

In Gherkin syntax, what do steps beginning with the When keyword describe?

[X]Actions that the user takes to interact with the system under test

[ ]Outcome expected from the actions that the user performs

[ ]Conditions needed to put the system into the required state for testing

[ ]Feature of the system and each of its related scenarios

Correct

Correct! Steps that begin with the When keyword describe actions that the user takes to interact with the system under test.

1 / 1 point

### 4.

Question 4

Which part of a behavior driven development (BDD) specification represents a complete user story?

[ ]Scenario

[ ]Example

[ ]Background

[X]Feature

Correct

Correct! A feature represents a user story, and you write a feature using the standard user-story syntax from Agile development.

1 / 1 point

### 5.

Question 5

How must you order the steps in a steps file to ensure that Behave locates them and executes them correctly?

[ ]By the guidelines dictated in the environment.py file

[X]By any order you choose, as the order does not matter

[ ]By the same order as the steps in the feature file

[ ]By listing steps with a Given decorator, then steps with a When decorator, and then steps with a Then decorator

Correct

Correct! The Python steps in a steps file do not have to be in any specific order. Behave will find them regardless of the order in which they appear.

1 / 1 point

### 6.

Question 6

What is one ideal use for the before_all() and after_all() test fixtures in Behave?

[ ]Checking specific parts of your feature set

[ ]Modifying the environment before and after each step

[ ]Establishing a clean environment before and after each feature

[X]Setting up web drivers for tools like Selenium

Correct

Correct! The before_all() and after_all() test fixtures are ideal for setting up web drivers for tools like Selenium. Multiple steps across multiple features may require these drivers. Thus, it’s helpful that you can use just one test fixture set to grant and later remove driver access for all steps.

1 / 1 point

### 7.

Question 7

You should always write features as if you are explaining which of its aspects?

[ ]What the underlying code will be

[ ]When you created the feature

[X]How to use the feature as a client

[ ]Where to place it in the folder structure

Correct

Correct! One essential tip for writing features is to consider the user experience. You should always write a feature as if you are explaining how to use it, not what it does internally in the code.

1 / 1 point

### 8.

Question 8

Which action must you perform to initialize Selenium for use in Behave?

[ ]Reference the browser in each feature.

[X]Instantiate the appropriate driver.

[ ]Add parameters to Python step functions.

[ ]Specify the HTML element to find.

Correct

Correct! To initialize Selenium, you must instantiate a driver of the same type as the browser that you will test.

1 / 1 point

### 9.

Question 9

In a Gherkin feature, you have the following Gherkin statement:

When I visit the “FAQs Page”

What is the complete code needed in the first line of the corresponding Python step?

[ ]@when

[X]@when(‘I visit the “FAQs Page”’)

[ ]When I visit the “FAQs Page”

[ ]when(‘I visit the %’)

Correct

Correct! In the first line of a Python step, you must include a decorator corresponding to the Gherkin statement’s keyword. You must also include a text string that matches the rest of the statement.

1 / 1 point

### 10.

Question 10

When Behave loads data from a Gherkin table, it converts each row into which type of Python collection?

[ ]List

[ ]Tuple

[ ]Set

[X]Dictionary

Correct

Correct! When Behave loads data from a Gherkin table, it converts each row into a Python dictionary.

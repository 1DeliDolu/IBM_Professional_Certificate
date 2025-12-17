### 1.

Question 1

Which of the following statements is a key principle of testing?

[ ]You should prefer manual tests over automated tests.

[ ]You can only test for the factors that you know.

[ ]You should run as few software tests as possible.

[ ]You can save testing for the beta stage onward.

1 point

### 2.

Question 2

Testing has which of the following benefits for development?

[ ]Increases code readability

[ ]Produces file backups

[ ]Reduces project spending

[ ]Improves code quality

1 point

### 3.

Question 3

At which level of the software testing process do developers test the entire software process?

[ ]Unit testing

[ ]System testing

[ ]Integration testing

[ ]Acceptance testing

1 point

### 4.

Question 4

What is the purpose of integration testing?

[ ]Validate that each unit performs as designed

[ ]Assess the system’s acceptability for delivery

[ ]Expose flaws in the interaction between components

[ ]Evaluate compliance with specific technical requirements

1 point

### 5.

Question 5

Behavior driven development (BDD) ensures which of the following for developers?

[ ]Writing concise code

[ ]Bolstering customer service

[ ]Building correct software

[ ]Identifying the code’s purpose

1 point

### 6.

Question 6

In the basic workflow for test driven development (TDD), what happens in the third step?

[ ]Write the program code.

[ ]Improve the code’s quality.

[ ]Create the test case.

[ ]Describe the system’s behavior.

1 point

### 7.

Question 7

In which Python testing framework can you use nearly an infinite number of setup and teardown levels?

[ ]Pytest

[ ]PyUnit

[ ]RSpec

[ ]Doctest

1 point

### 8.

Question 8

Assume you are using Python and have installed PyUnit, Nose, and Pinocchio. Which of the following commands can you use to perform unit tests and receive color-coded output?

[ ]nosetests --with-spec –cover-tests

[ ]unittest --with-spec --spec-color

[ ]unittest --with-spec –cover-tests

[ ]nosetests --with-spec --spec-color

1 point

### 9.

Question 9

Which of the following PyUnit assertions is useful for determining if an object is in a result set?

[ ]assertLogs()

[ ]assertIn()

[ ]assertIsInstance()

[ ]assertRegex()

1 point

### 10.

Question 10

PyUnit provides six test fixtures. Assume you include all six in a test module. Which of the following sequences shows the order in which the test runner will execute the final three test fixtures?

[ ]setUpModule, tearDownModule, tearDown

[ ]tearDown, tearDownClass, tearDownModule

[ ]tearDownClass, tearDownModule, tearDown

[ ]tearDownModule, setUpModule, tearDownClass

1 point

### 11.

Question 11

How does a missing test coverage report help developers improve their testing?

[ ]Reveals lines of code that need test cases

[ ]Lists functions that respond to exceptions appropriately

[ ]Shows the lines of code that have coverage

[ ]Announces when no bugs remain in the code

1 point

### 12.

Question 12

When generating fakes in Python, what is one advantage of using the Faker class to generate fake data?

[ ]Arranges the test results in a logical order

[ ]Uses a small amount of code

[ ]Decreases the number of attributes to test

[ ]Creates a diverse set of test data

1 point

### 13.

Question 13

Developers should use mocking for which of the following purposes?

[ ]Avoid calls of untested code

[ ]Isolate their tests from a remote component

[ ]Include internal systems in their testing

[ ]Ensure that database transactions actually work

1 point

### 14.

Question 14

For which of the following purposes is it useful to patch return values with data?

[ ]Controlling data returned from a function call

[ ]Testing mocks

[ ]Testing objects that call other objects

[ ]Testing objects with method calls

1 point

### 15.

Question 15

Developers use mock objects for which of the following purposes?

[ ]Mimicking a real object

[ ]Change a function call’s parameters

[ ]Identifying a sad path

[ ]Generating a data set

1 point

### 16.

Question 16

Which of the following characteristics is common to both behavior driven development (BDD) and test driven development (TDD)?

[ ]Emphasis on a test-first approach

[ ]Focus on the system from the inside out

[ ]Value for testing individual units of software

[ ]Goal of building the application correctly

1 point

### 17.

Question 17

Using your specifications which item can you generate automatically with most behavior driven development (BDD) tools?

[ ]Project schedules

[ ]Technical documents

[ ]Kanban boards

[ ]Testing factories

1 point

### 18.

Question 18

What does the ‘When’ keyword specify at the beginning of a step in Gherkin syntax?

[ ]Feature of the system and each of its related scenarios

[ ]Outcome expected from the actions that the user performs

[ ]Conditions needed to put the system into the required state for testing

[ ]Actions taken by the user to interact with the system under test

1 point

### 19.

Question 19

Which keyword displays first in a Gherkin document?

[ ]Feature

[ ]Scenario

[ ]Background

[ ]Given

1 point

### 20.

Question 20

If your step files are written in Ruby, which BDD tool will you use?

[ ]Gherkin

[ ]Cucumber

[ ]Behave

[ ]Concordion

1 point

### 21.

Question 21

Which folder is used to store all Python files that contain step functions while using Behave?

[ ]matches

[ ]python

[ ]functions

[ ]steps

1 point

### 22.

Question 22

What are the before_feature() and after_feature() test fixtures ideally used for in Behave?

[ ]Checking specific parts of your feature set

[ ]Setting up web drivers for tools like Selenium

[ ]Declaring the context values that all steps can access

[ ]Establishing a clean environment before and after each feature

1 point

### 23.

Question 23

What is the purpose of the background section in a feature?

[ ]Execute a scenario two or more times

[ ]Represent a business rule to implement

[ ]Check parts of the feature set selectively

[ ]Specify the context shared by all scenarios

1 point

### 24.

Question 24

Which Selenium function can you use to type input into an HTML input field?

[ ]clear()

[ ]submit()

[ ]send_keys()

[ ]

text()

1 point

### 25.

Question 25

In a Gherkin feature, you have the following Gherkin statement:

When I visit the “FAQs Page”

What is the complete code needed in the first line of the corresponding Python step?

[ ]When I visit the “FAQs Page.”

[ ]@when

[ ]@when(‘I visit the “FAQs Page”’)

[ ]when(‘I visit the %’)

1 point

### 26.

Question 26

When Behave loads data from a Gherkin table, it converts each row into which type of Python collection?

[ ]Tuple

[ ]List

[ ]Set

[ ]Dictionary

1 point

### 27.

Question 27

When you run the Behave tool the first time against your feature file with no steps, what will the Behave tool do for you?

[ ]Will show a blank screen

[ ]Will only validate your steps

[ ]Give you only the missing steps

[ ]Give a set of suggested steps

1 point

### 28.

Question 28

Which steps show the NotImplementedError exception?

[ ]Missing steps

[ ]Failed steps

[ ]Passed steps

[ ]Default steps

1 point

### 29.

Question 29

How can you pass information from one step to another?

[ ]Store the information in data and call the string function

[ ]Store information in the context variable of one step and call the variable in another step

[ ]Store the information in the get method and call it from another step

[ ]Store the information in import and call it from another step

1 point

### 30.

Question 30

What is the benefit of variable substitution?

[ ]To use different names for different variables

[ ]To make one sentence in your feature file match a single unique step

[ ]To make the steps specific and clear

[ ]To make the steps generic and reusable

1 point




1. **You can only test for the factors that you know.**
2. **Improves code quality**
3. **System testing**
4. **Expose flaws in the interaction between components**
5. **Building correct software**
6. **Improve the code’s quality.**
7. **Pytest**
8. **nosetests --with-spec --spec-color**
9. **assertIn()**
10. **tearDown, tearDownClass, tearDownModule**


11. **Reveals lines of code that need test cases**
12. **Creates a diverse set of test data**
13. **Isolate their tests from a remote component**
14. **Controlling data returned from a function call**
15. **Mimicking a real object**
16. **Emphasis on a test-first approach**
17. **Technical documents**
18. **Actions taken by the user to interact with the system under test**
19. **Feature**
20. **Cucumber**

21. **steps**
22. **Establishing a clean environment before and after each feature**
23. **Specify the context shared by all scenarios**
24. **send_keys()**
25. **@when(‘I visit the “FAQs Page”’)**
26. **Dictionary**
27. **Give a set of suggested steps**
28. **Default steps**
29. **Store information in the context variable of one step and call the variable in another step**
30. **To make the steps generic and reusable**

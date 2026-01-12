### 1.

Question 1

In the basic workflow for test driven development (TDD), what happens in the second step?

[X]Write the program code.

[ ]Improve the code’s quality.

[ ]Describe the system’s behavior.

[ ]Create the test case.

Incorrect

Correct. In the second step in the basic TDD workflow, developers write just enough code to make the unit test pass.

1 point

### 2.

Question 2

To create a DevOps pipeline, which type of testing must developers use for all testing?

[ ]Manual testing

[ ]Smoke testing

[ ]Exploratory testing

[X]Automated testing

Correct

Correct. To create a DevOps pipeline, developers must automate all testing. That way, they can easily identify bugs well before the bugs would otherwise reach production.

1 / 1 point

### 3.

Question 3

Which of the following testing frameworks supports multiple programming languages?

[ ]Roundup

[ ]Fakeit

[X]xUnit

[ ]Beantest

Correct

Correct. The xUnit testing framework supports multiple programming languages, such as Python, Java, C, and C++.

1 / 1 point

### 4.

Question 4

Which of the following commands can developers use to invoke Python with the unittest module and to run all the tests in the test folder?

[ ]python -m unittest pattern

[ ]python -m unittest catch

[X]python -m unittest discover

[ ]python -m unittest locals

Correct

Correct. The command python -m unittest discover will invoke Python with the unittest module and run all the tests in the test folder.

1 / 1 point

### 5.

Question 5

Which of the following features is available in Nose but missing in unittest?

[ ]Reporting the number of tests run

[ ]Displaying the length of time for running tests

[ ]Indicating whether any tests failed

[X]Adding color coding to test output

Correct

Correct. With Nose, developers can add color coding and other formatting features to test output. This feature is not available in unittest.

1 / 1 point

### 6.

Question 6

In which of the following ways do testing frameworks help developers build assertions?

[X]Testing frameworks provide tools that simplify testing conditions.

[ ]Testing frameworks identify potential sad paths to test.

[ ]Testing frameworks set up the required file structure automatically.

[ ]Testing frameworks generate fakes to test against a model.

Correct

Correct. Testing frameworks provide tools, such as the TestCase class in unittest, that simplify testing conditions.

1 / 1 point

### 7.

Question 7

What purpose do assertions serve in testing?

[ ]Establishing a known initial state for testing

[ ]Reporting how many lines of code execute during testing

[ ]Providing tools to simplify testing conditions

[X]Determining if tests have passed or failed

Correct

Correct. Developers use assertions as checks to determine if the results of a test have passed or failed.

1 / 1 point

### 8.

Question 8

What is the purpose of using sad paths in testing?

[ ]Ensure that code produces only the expected output.

[ ]Guarantee that tests execute in the correct initial state.

[ ]Check that test resources are cleaned up after execution.

[X]Verify that functions respond to exceptions appropriately.

Correct

Correct. Developers use sad paths to verify that a function responds to exceptions appropriately and without breaking.

1 / 1 point

### 9.

Question 9

Test fixtures provide which of the following benefits for testing?

[ ]Shorter code

[ ]Organized output

[X]Repeatable results

[ ]Improved communication

Correct

Correct. With test fixtures, developers can ensure that the system resets after each test. In turn, this reset ensures repeatable results because every test runs from the same initial state.

1 / 1 point

### 10.

Question 10

PyUnit provides six test fixtures. Assume you include all six in a test module. Which of the following sequences shows the order in which the test runner will execute the first three test fixtures?

[ ]setUpModule, tearDownModule, setUpClass

[ ]setUpClass, setUp, setUpModule

[X]setUpModule, setUpClass, setUp

[ ]tearDownModule, setUpModule, setUpClass

Correct

Correct. The first three test fixtures that the test runner will execute, in order, are setUpModule, setUpClass, and then setUp.

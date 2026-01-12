### 1.

Question 1

The output from Behave does something like Red/Green/Refactor of TDD. What does it indicate when the steps are yellow in color?

[ ]The steps have failed.

[ ]The steps have passed.

[ ]The steps are skipped.

[ ]The steps are undefined.

1 point

### 2.

Question 2

How does Behave differentiate the type of step when it gives you snippets of code for the undefined steps?

[ ]By giving a proper decorator keyword indicating the type of step: Given, When, or Then

[ ]By coloring the step red to show a failed step

[ ]By coloring the step green to indicate passing of the step

[ ]By showing None

1 point

### 3.

Question 3

Which is the first line of code for creating a generic web steps file that works across web applications?

[ ]@then(u'I should see the message "Success"')

[ ]from behave import given, when, then

[ ]@given(u'I am on the "Home Page"')

[ ]from behave import

1 point

### 4.

Question 4

Why does Behave skip certain steps and show them as blue?

[ ]The steps belong to another scenario

[ ]To show they are skipped when the current scenario has failed

[ ]Behave cannot find them in the feature file

[ ]The steps are the default steps

1 point

### 5.

Question 5

In the Behave workflow, which step should you implement after the first step passes?

[ ]Implement a step

[ ]Implement the next step that fails

[ ]After the first step passes, all steps turn green

[ ]Repeat the process until all steps pass

1 point

### 6.

Question 6

Which steps show the NotImplementedError exception?

[ ]Default steps

[ ]Missing steps

[ ]Passed steps

[ ]Failed steps

1 point

### 7.

Question 7

In the following code, which element has the message string?

*assert message in str(context.response.data)*

[ ]context.response.data

[ ]str

[ ]context.response

[ ]context

1 point

### 8.

Question 8

How does context act as a container in your feature file?

[ ]It contains description of the steps.

[ ]It stores whatever data you need to make available to all of your steps.

[ ]It stores data of other feature files.

[ ]It contains different data for each step.

1 point

### 9.

Question 9

How can you pass information from one step to another?

[ ]Store information in the context variable of one step and call the variable in another step

[ ]Store the information in data and call the string function

[ ]Store the information in import and call it from another step

[ ]Store the information in the get method and call it from another step

1 point

### 10.

Question 10

What are rules to substitute variables in your steps? Select two.

[ ]Replace data in the decorator with variables preceded by an underscore

[ ]Substitute the variable names in place of the strings passed in from the feature file

[ ]Add step implementation parameters with different names from the variables

[ ]Replace data in the decorator string with variables enclosed by curly braces

1 point



1. **The steps are undefined.**
2. **By giving a proper decorator keyword indicating the type of step: Given, When, or Then**
3. **from behave import given, when, then**
4. **To show they are skipped when the current scenario has failed**
5. **Implement the next step that fails**
6. **Missing steps**
7. **context.response.data**
8. **It stores whatever data you need to make available to all of your steps.**
9. **Store information in the context variable of one step and call the variable in another step**
10. (Select two)

* **Substitute the variable names in place of the strings passed in from the feature file**
* **Replace data in the decorator string with variables enclosed by curly braces**

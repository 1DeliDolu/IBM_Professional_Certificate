
### 1.

Question 1

What hook can you use to manage a form's state in React?

[ ]useEffect

[X]useState

[ ]useForm

[ ]useContext

Correct

Correct! In React, you can use the useState to handle a form's state.

1 / 1 point

### 2.

Question 2

Which hook should you use to handle asynchronous logic in functional components?

[X]useEffect

[ ]useAsync

[ ]useCallback

[ ]useState

Correct

Correct! While the useEffect hook itself is not specifically designed for handling asynchronous code, you can use it to create side effects functionalities such as data fetching, which often involves asynchronous operations.

1 / 1 point

### 3.

Question 3

How can you trigger an effect to run only once after the initial render in a functional component?

[ ]With the useState hook to track the component's initial render

[ ]With the useEffect hook and a non-empty dependency array

[X]With the useEffect hook and an empty dependency array

[ ]With the useEffect hook and no dependencies

Correct

Correct! By providing an empty dependency array to the useEffect hook, you ensure that the effect runs only once after the initial render of the component.

1 / 1 point

### 4.

Question 4

How can you handle form submission in React?

[ ]With the onChange event handler

[ ]With the onKeyDown event handler

[ ]With the onClick event

[X]With the onSubmit event

Correct

Correct! You can use the onSubmit event to handle an event whenever the user submits the form.

1 / 1 point

### 5.

Question 5

How can you handle user input in a controlled component in React?

[ ]With controlled data

[ ]By directly modifying the DOM elements

[ ]By relying on the default behavior of form elements

[X]With the onChange event handler to update the state

Correct

Correct! onChange event handler is used to capture changes to form elements. This event handler is used to update the component's state, ensuring that the input value is controlled by React state.

1 / 1 point

### 6.

Question 6

What is an advantage of using Redux Thunk middleware?

[X]Thunk enables async operations without boilerplate code.

[ ]Thunk works well with complex applications.

[ ]Thunk scales well.

[ ]Thunk handles concurrency problems efficiently.

Correct

Correct! Redux Thunk middleware enables asynchronous operations without requiring excessive boilerplate code.

1 / 1 point

### 7.

Question 7

What is Redux Toolkit primarily used for?

[ ]Managing HTTP requests and responses

[X]Reducing boilerplate code

[ ]Creating complex UI components

[ ]Implementing authentication and authorization

Correct

Correct! The Redux Toolkit provides utilities to streamline common Redux tasks, minimizing the amount of boilerplate code.

1 / 1 point

### 8.

Question 8

Which function from the Redux Toolkit consolidates Redux setup logic into a single function call?

[ ]createReducer()

[ ]createSlice()

[ ]createStore()

[X]configureStore()

Correct

Correct! The configureStore() function consolidates Redux setup logic, such as setting up middleware and enabling the Redux DevTools Extension into a single function call.

1 / 1 point

### 9.

Question 9

What is the purpose of a Redux slice?

[ ]To handle asynchronous operations

[ ]To create reusable UI components

[X]To divide the application states into several parts and manage their updates

[ ]To manage HTTP requests and responses

Correct

Correct! A Redux slice divides the application states into individual parts and manages the logic to update them. It typically consists of a reducer function, action creators, and an initial state.

1 / 1 point

### 10.

Question 10

Which middleware is commonly used with Redux to handle asynchronous actions and side effects?

[ ]Redux Saga

[ ]Redux DevTools Extension

[ ]Redux Logger

[X]Redux Thunk

Correct

Correct! Thunk is middleware commonly used with Redux to handle asynchronous actions and side effects. It allows action creators to return functions, enabling asynchronous behavior in Redux applications.

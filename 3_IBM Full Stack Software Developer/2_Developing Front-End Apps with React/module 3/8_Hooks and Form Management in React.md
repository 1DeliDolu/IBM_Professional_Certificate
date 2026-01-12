
### 1.

Question 1

When using the useEffect hook, what happens if you pass an empty array ([]) as the dependency list?

[ ]The effect runs only when the state changes.

[ ]The effect runs after every render of the component.

[X]The effect runs only once, when the component first mounts.

Correct! Passing an empty array ([]) to useEffect makes the effect run only once, when the component first mounts.

[ ]The effect does not run at all.

1 / 1 point

### 2.

Question 2

Which hook would you recommend to manage side effects?

[ ]useContext

[ ]useReducer

[ ]useState

[X]useEffect

Correct! In React, the useEffect hook helps to run side effects like getting data, subscribing to something, or changing the DOM by hand in functional components.

1 / 1 point

### 3.

Question 3

Why would you need to create a custom hook?

[ ]To perform side effects in functional components

[X]To share reusable stateful logic across components

Correct! With React's custom hooks, you can take stateful logic out of components and put it into functions for sharing and using them again and again.

[ ]To manage dependencies

[ ] To manage a functional component's state

1 / 1 point

### 4.

Question 4

Which hook would you recommend for making HTTP requests within React functional components?

[ ]useFetch

[ ]useState

[ ]useContext

[X]useEffect

Correct. The useEffect hook manages side effects such as HTTP requests within React functional components.

1 / 1 point

### 5.

Question 5

Which of the following is a standard method used to fetch data from an external API?

[ ]Axios

[ ]JSON.stringify

[X]Fetch API

Correct!  This is a standard method used to fetch data from an external API.

[ ] XMLHttpRequest

1 / 1 point

### 1.

**Doğru seçenek:** The effect runs only once, when the component first mounts.

### 2.

**Doğru seçenek:** useEffect

### 3.

**Doğru seçenek:** To share reusable stateful logic across components

### 4.

**Doğru seçenek:** useEffect

### 5.

**Doğru seçenek:** Fetch API

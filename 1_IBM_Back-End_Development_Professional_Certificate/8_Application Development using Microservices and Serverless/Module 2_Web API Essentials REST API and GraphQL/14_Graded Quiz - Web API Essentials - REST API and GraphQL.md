### 1.

Question 1

What are the key characteristics of a RESTful API? Select two answers.

[X]Stateless communication between client and server

Correct

Correct. The REST architecture is designed so that the client state is not maintained on the server.

[X]It works on HTTP

Correct

Correct. Communication between a REST client and the REST server is in the form of an HTTP request using methods like GET, POST, and DELETE.

[ ]Unique interface for each component

[ ]One API to access all resources

1 / 1 point

### 2.

Question 2

What does an API Gateway act as?

[X]An API management tool

[ ]A streaming service

[ ]A firewall to protect your microservices

[ ]A load balancer for your hosted services

Correct

Correct. An API Gateway decouples clients from your services, hiding their complexity, interconnection, and implementation details.

1 / 1 point

### 3.

Question 3

Which syntax is used to make an update request to a product REST API?

[ ]GET /products/114?updatedName=Calendar2023

[ ]POST /products (product data in the body)

[ ]PUT /products/114/name/Calendar2023

[X]PUT /products/114 (product data in the body)

Correct

Correct. A PUT method with submitted data in the body is the standard for updating a resource.

1 / 1 point

### 4.

Question 4

Which type of framework is Flask?

[ ]REST API

[ ]Frontend

[ ]Database

[X]Micro web

Correct

Correct. Flask is classified as a micro web framework as it does not require particular tools or libraries.

1 / 1 point

### 5.

Question 5

Which one of the following statements is true about communication in a RESTful API?

[ ]Session state is kept entirely on the REST API.

[ ]Each request does not contain all information.

[ ]A request can take advantage of any stored context on the server.

[X]Resources are uniquely identified at individual endpoints.

Correct

Correct. The REST API should ensure that the same piece of data belongs to only one uniform resource identifier (or URI).

1 / 1 point

### 6.

Question 6

What are the potential drawbacks of an API Gateway? Select two answers.

[X]Bottleneck in scalability

Correct

Correct. An API Gateway can become a scalability bottleneck if it is not designed in a resilient and highly available fashion.

[X]Single point of failure

Correct

Correct. If you ensure the gateway is properly designed to meet your application's availability requirements, then it won’t become a single point of failure.

[ ]Increases requests to the backend

[ ]Exposes the implementation details

1 / 1 point

### 7.

Question 7

Which specification is followed by Swagger?

[X]OpenAPI

[ ]WebAPI

[ ]GraphQL

[ ]SOA

Correct

Correct. OpenAPI is a specification implemented by Swagger.

1 / 1 point

### 8.

Question 8

Which cURL command should be used to query a list of products?

[X]curl -X 'GET' \

 'http://127.0.0.1:5000/products' \

 -H 'accept: application/json'

[ ]curl -X 'PUT' \

 'http://127.0.0.1:5000/products' \

 -H 'accept: application/json'

[ ]curl -X 'POST' \

 'http://127.0.0.1:5000/products' \

 -H 'accept: application/json'

[ ]curl -X 'PATCH' \

 'http://127.0.0.1:5000/products' \

 -H 'accept: application/json'

Correct

Correct. This cURL command with the -X flag specifies a GET operation.

1 / 1 point

### 9.

Question 9

Which HTTP method is used to create new data in a REST API?

[ ]PATCH

[X]POST

[ ]PUT

[ ]UPDATE

Correct

Correct. You can use POST to create a new resource. A POST request requires a body in which you define the data of the entity to be created.

1 / 1 point

### 10.

Question 10

What is the purpose of Postman?

[X]Tests APIs

[ ]Uniform interface for different components

[ ]Transfers applications

[ ] Command line tool to get data

Correct

Correct. Postman is a popular tool for testing APIs.

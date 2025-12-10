### 1.

Question 1

Which phase of the Twelve-Factor Methodology contains Port binding?

Status: [object Object]

1 / 1 point

[ ] Deploy

[ ] Configure

[ ] Operate

[ ] Code

Correct

Correct. Deploy phase of the delivery lifecycle contains: Config, Backing services, Processes, and Port binding.

### 2.

Question 2

What makes an application concurrent?

Status: [object Object]

1 / 1 point

[ ] It should contain the same backend services across environments

[ ] It should be stateless

[ ] It should store config in environment variables

[ ] It should have a minimal process start time

Correct

Correct. If processes are stateless and share nothing, an application can start additional processes to scale horizontally and handle the additional workload without creating interdependencies among processes.

### 3.

Question 3

In a microservice architecture, you can

Status: [object Object]

1 / 1 point

[ ] Scale all services together

[ ] Use a different technology stack for each service

[ ] Deploy all services together

[ ] Create interdependency among services

Correct

Correct. Teams can choose even different programming languages for different components as they are dependent on each other via an API endpoint.

### 4.

Question 4

Select the correct answer that completes this sentence:

Monolith application has __________ components.

Status: [object Object]

1 / 1 point

[ ] Independent

[ ] Reusable

[ ] Interconnected

[ ] Scalable

Correct

Correct. A monolithic application has all or most of its functionality within a single process. Making them tightly connected and dependent on each other.

### 5.

Question 5

Which component of services design in an SOA architecture defines how the service provider and service consumer should interact?

Status: [object Object]

1 / 1 point

[ ]  Interface

[ ] Contract

[ ] Implementation

[ ] Own storage

Correct

Correct. A contract defines how the service provider and service consumer should interact.

### 6.

Question 6

What is the purpose of Backend For Frontend?

Status: [object Object]

1 / 1 point

[ ] Loading one interface that never reloads

[ ] Refactoring in stages

[ ] Customized user experiences

[ ] Service discovery

Correct

Correct. The BFF pattern allows developers to create and support one backend type per user interface using the best options for that interface rather than trying to support a generic backend that works with any interface but may negatively impact frontend performance.

### 7.

Question 7

What is the purpose of the Strangler pattern?

Status: [object Object]

1 / 1 point

[ ] Helps with third-party API integrations

[ ] Supports refactoring in stages

[ ] Simplifies the front-end experience

[ ] Combine functional domains

Correct

Correct. With the Strangler pattern, you use the structure of a web application to split an application into multiple functional domains and replace those domains with a new microservices-based implementation for one domain at a time.

### 8.

Question 8

Larger services should be broken into smaller services when:

Status: [object Object]

1 / 1 point

[ ] Refactoring is required

[ ] Automation is required

[ ] Functional reusability is required

[ ] Common data model becomes overly complex

Correct

Correct. If your data model becomes too broad, it is time to split the service and functionally segregate them.

### 9.

Question 9

What is the requirement of Microservices?

Status: [object Object]

0 / 1 point

[ ] Independent storage

[ ] Its own implementation of auxiliary services like loggings, security, throttling, and so on

[ ] Coarse-grained functionality

[ ] Manual deployment process

Incorrect

Incorrect. Review the Microservices Anti-Patterns video.

### 10.

Question 10

What is the requirement of a development and production environment?

Status: [object Object]

1 / 1 point

[ ] Different dependencies

[ ] Different source control

[ ] Similar backing services across the environments.

[ ] Embedded access details in code

Correct

Correct. If you use a MySQL database in production, you should use the same version of MySQL database in your development environments.

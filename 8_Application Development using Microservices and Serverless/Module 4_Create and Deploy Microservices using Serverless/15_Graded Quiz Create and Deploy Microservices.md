### 1.

Question 1

What is the main benefit of using PaaS, such as IBM Cloud Code Engine, to deploy your microservices?


[ ]Enables handling of the full deployment process by a single user

[ ]Provides a design to run a single type of workload

[ ]Scales your microservices manually based on predefined rules and configurations

[X]Provides fully managed deployment services to help your deployment process with minimal efforts

Correct

Correct. Most PaaS are fully managed so that you can build and deploy your microservices with minimal effort.

1 / 1 point

### 2.

Question 2

What are the three deployment modes of IBM Cloud Code Engine?


[X](1) Build and deploy applications from source code. (2) Deploy container image-based applications, and (3) Run Jobs

[ ](1) Build and deploy applications from source code. (2) Deploy container image-based applications and (3) REST APIs

[ ](1) Run REST APIs, (2) Build and Run Source Code, and (3) Run Jobs

[ ](1) SCP. (2) TCP, and (3) HTTP

Correct

Correct. IBM Cloud Code Engine can deploy a built container image or build your application from source code or run your executable code as jobs.

1 / 1 point

### 3.

Question 3

Which of the following statement is correct about Code Engine project and application?


[ ]A project in IBM Cloud Code Engine acts like a namespace so that you can only create one project under your account.

[X]A project in IBM Cloud Code Engine acts like a namespace so that you can create and deploy multiple applications even with the same name across projects.

[ ]You can have two applications sharing the same name in the same project.

[ ]A project can only contain one application.

Correct

Correct. A project in IBM Cloud Code Engine acts like a namespace or a container so that you can create and deploy multiple applications.

1 / 1 point

### 4.

Question 4

What are the two main application-building methods supported in IBM Cloud Code Engine?


[ ]Building container image with Github Action and DockerHuB:

[X]Building container image with Dockerfile and Buildpack.

[ ]Building container image with DockerHub and Buildpack.

[ ]Building container image with Dockerpack and Buildpack.

Correct

Correct. Dockerfile and Cloud Native Buildpack are currently supported in IBM Cloud Code Engine to build the container image.

1 / 1 point

### 5.

Question 5

What is the role of docker in container technology?


[ ]A cloud tool to scan your container images for security vulnerabilities

[ ]An application development and testing IDE

[ ]A container orchestration platform

[X]A software platform for building and running applications as containers

Correct

Correct. Docker is a software platform for building and running applications as docker containers.

1 / 1 point

### 6.

Question 6

What is normally the first command of a Dockerfile?


[ ]COPY

[ ]CMD

[X]FROM

[ ]EXPOSE

Correct

Correct. FROM is normally the first line or command of a Dockerfile to import a base image.

1 / 1 point

### 7.

Question 7

What is a container registry?


[ ]A cloud platform to deploy container images.

[X]A container repository where your pushed container images are curated

[ ]A cloud IDE to develop container

[ ]A software platform to build a container image

Correct

Correct. A container registry is a repository where you can push your built container images to. After the container images are pushed, your container images will be managed and curated there.

1 / 1 point

### 8.

Question 8

Once your microservice or web application is deployed, how can you test it?


[ ]You can only verify your application’s running status via log files.

[X]IBM Cloud Code Engine will provide a URL for you to run or test your service or application.

[ ]IBM Cloud Code Engine will provide a URL to download your microservice, and then you can unzip and run it.

[ ]IBM Cloud Code Engine will provide a container image reference for you to test your application.

Correct

Correct. IBM Cloud Code Engine provides a URL as the entry point to your deployed microservice or web application.

1 / 1 point

### 9.

Question 9

What is the correct IBM Cloud CLI command to create and deploy an application?


[ ]“ibmcloud ce app create –image us.icr.io/mynamespace/hello_repo --registry-secret myregistry.”

[X]“ibmcloud ce app create --name helloworldapp --image us.icr.io/mynamespace/hello_repo --registry-secret myregistry”

[ ]“ ibmcloud ce createapp --n helloworldapp --i us.icr.io/mynamespace/hello_repo”

[ ]“app create --name helloworldapp --image us.icr.io/mynamespace/hello_repo --registry-secret myregistry”

Correct

Correct. “ibmcloud ce app create” is the correct command with three main arguments: --name, --image, and --registry-secret.

1 / 1 point

### 10.

Question 10

Which method is used by the IBM Cloud Code Engine to access your container image?


[ ]From the Private container registry only

[ ]From the source code

[ ]From the public container registry only

[X]From both public and private container registry

Correct

Correct. The Code Engine can access your container image from either a private or a public container registry. For non-public container registries, you will need to provide a registry access to the Code Engine.

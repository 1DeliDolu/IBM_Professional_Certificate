### 1.

Question 1

What Kubernetes object adds or deletes pods for scaling and redundancy?


[X]  A ReplicaSet

[ ] A Secret

[ ] A Config Map

[ ] A DaemonSet

Correct

Correct! A ReplicaSet ensures the right number of pods are always up and running.

1 / 1 point

### 2.

Question 2

What are the three required steps to bind the IBM Cloud Service to your Cluster?


[X]  Bind the Service to your Cluster to create credentials.

Correct

Correct! The required steps to bind an IBM Cloud Service to your Cluster are: Provision an instance of the service, Bind the Service to your Cluster to create credentials, Store the credentials, and Configure your app to access the credentials.

[X] Provision an instance of the Service.

Correct

Correct! The required steps to bind an IBM Cloud Service to your Cluster are: Provision an instance of the service, Bind the Service to your Cluster to create credentials, Store the credentials, and Configure your app to access the credentials.

[ ] Erase the credential configuration file after credential setup.

[X] Configure your app to access the credentials.

Correct

Correct! The required steps to bind an IBM Cloud Service to your Cluster are: Provision an instance of the service, Bind the Service to your Cluster to create credentials, Store the credentials, and Configure your app to access the credentials.

1 / 1 point

### 3.

Question 3

Which rolling update types ensure 100% app availability?


[ ]  One-at-a-time updates and rollbacks ensure 100% app availability.

[ ] Both all-at-once and one-at-a-time updates and rollbacks ensure 100% app availability.

[X] No rolling update types can ensure 100% app availability.

[ ] All-at-once updates and rollbacks ensure 100% app availability.

Incorrect

Incorrect. Please review the Rolling Updates video.

1 point

### 4.

Question 4

What are three ways to create a ConfigMap?


[ ] By adding another environment to the deployment descriptor

[X] By providing a ConfigMap YAML descriptor file

Correct

Correct! A ConfigMap is created using string literals, using an existing property or ‘key’ = ‘value’ file, or by providing a ConfigMap YAML descriptor file.

[X]  By using an existing property or ‘key’ = ‘value’ file

Correct

Correct! A ConfigMap is created using string literals, using an existing property or ‘key’ = ‘value’ file, or by providing a ConfigMap YAML descriptor file.

[X] By using string literals

Correct

Correct! A ConfigMap is created using string literals, using an existing property or ‘key’ = ‘value’ file, or by providing a ConfigMap YAML descriptor file.

1 / 1 point

### 5.

Question 5

What does a ConfigMap do?


[ ] Verifies that a Secret was created

[X] Provides sensitive information to your application

[ ] Mounts a file using the volumes plugin

[ ] Provides variables for your application

Incorrect

Incorrect. Please review the ConfigMaps and Secrets video.

1 point

### 6.

Question 6

Which Kubernetes autoscaler type scales the Cluster?


[ ] You cannot autoscale a Kubernetes Cluster.

[ ] Vertical Pod Autoscaler (VPA)

[X] Cluster Autoscaler (CA)

[ ] Horizontal Pod Autoscaler (HPA)

Correct

Correct! The Cluster Autoscaler (CA) scales the Cluster in Kubernetes.

1 / 1 point

### 7.

Question 7

How do you create a ReplicaSet from scratch?


[ ] Apply a JSON file that includes the number of desired replicas.

[ ] Use the ‘get pods’ command.

[X] Apply a YAML file with the ‘kind’ attribute set to ‘ReplicaSet’.

[ ] Use the ‘scale’ command to scale the deployment.

Correct

Correct! To create a ReplicaSet from scratch, apply a YAML file with the ‘kind’ attribute set to ‘ReplicaSet’.

1 / 1 point

### 8.

Question 8

What does Service binding do?


[X] Manages configuration and credentials for back-end Services while protecting sensitive data

[ ] Calls the service without using binding credentials.

[ ] Makes Service credentials hidden.

[ ] Provides variables for your application

Correct

Correct! Service binding manages configuration and credentials for back-end Services while protecting sensitive data.

1 / 1 point

### 9.

Question 9

How do you prepare your application to enable rolling updates?


[ ] Set the maxSurge to 100%.

[ ] Set the maxSurge to 50%.

[X] Add liveness and readiness probes to deployments.

[ ] Use autoscaling.

Correct

Correct! Add liveness and readiness probes to deployments to enable rolling updates for an application.

1 / 1 point

### 10.

Question 10

What are three ways to create a Secret?

[X] By using environment variables

Correct

Correct! You create a Secret by using a string literal, by using environment variables, or by using volume mounts.

[ ] By providing a ConfigMap YAML descriptor file

[X] By using volume mounts

Correct

Correct! You create a Secret by using a string literal, by using environment variables, or by using volume mounts.

[X] By using a string literal

Correct

Correct! You create a Secret by using a string literal, by using environment variables, or by using volume mounts.

### 1.

Question 1

What is a benefit of Continuous Delivery (CD)?

[ ]Reduces deployment time

[ ]Refactors unit code

[ ]Decreases project size

[ ]Increases development budget

1 point

### 2.

Question 2

According to the key principles of Continuous Delivery (CD), what should you do if a build breaks?

[ ]Extend the project’s deadlines.

[ ]Save the problem for quality assurance.

[ ]Assign blame to a developer.

[ ]Determine how the system failed.

1 point

### 3.

Question 3

What is a best practice for Continuous Delivery (CD)?

[ ]Use long-lived repository branches when possible.

[ ]Deploy software updates to production continually.

[ ]Ensure ample downtime between releases.

[ ]Include user documentation for each change.

1 point

### 4.

Question 4

Which scanning capability should you have within your Continuous Delivery (CD) pipeline?

[ ]Compatibility

[ ]Plagiarism

[ ]Deployment

[ ]Secret

1 point

### 5.

Question 5

In Tekton, what does TaskRun do?

[ ]Defines locations for the inputs and outputs of steps

[ ]Creates a Kubernetes pod for each task

[ ]Instantiates a pipeline with parameters

[ ]Stores data for sharing between tasks

1 point

### 6.

Question 6

In a Tekton task manifest, what syntax must you use to pass a parameter into a step?

[ ]$~`<variable-name>`~

[ ][`<variable-name>`]

[ ]"`<variable-name>`"

[ ]$(`<variable-name>`)

1 point

### 7.

Question 7

Which subfield must you include within the spec field of a Tekton EventListener definition?

[ ]podTemplate

[ ]generateName

[ ]serviceAccountName

[ ]description

1 point

### 8.

Question 8

Assume you want to use the git-clone task from the Tekton Catalog. You have a Tekton PersistentVolumeClaim named pipelinerun-vc and a PipelineRun defined as follows:

apiVersion: tekton.dev/v1beta1kind: PipelineRun

metadata: generateName: pipeline-mn-

spec: pipelineRef: name: ab-pipeline

 workspaces: - name: pipeline-xy persistentVolumeClaim: claimName: pipelinerun-vc

 params: - name: repo-url value: "$(tt.params.repo)"

In the pipeline’s spec section, what name must you give the workspace so that any tasks that need it can use it?

[ ]pipeline-xy

[ ]ab-pipeline

[ ]pipeline-mn-

[ ]pipelinerun-vc

1 point

### 9.

Question 9

Where should you define an environment property that you want to add to a Tekton task?

[ ]Pipeline’s results field

[ ]Task’s steps field

[ ]Pipeline’s params field

[ ]Task’s workspaces field

1 point

### 10.

Question 10

How can you deploy an application to an environment when using Tekton?

[ ]Use the 'tkn resource describe' command.

[ ]Apply manifests in YAML format.

[ ]Use the 'odo service create' command.

[ ]Apply manifests in CSV format.

1 point



1. **Reduces deployment time**
2. **Determine how the system failed**
3. Include user documentation for each change.
4. **Secret**
5. **Creates a Kubernetes pod for each task**
6. **$(`<variable-name>`)**
7. **serviceAccountName**
8. **pipeline-xy**
9. **Task’s steps field**
10. **Apply manifests in YAML format**

### 1.

Question 1

In Tekton, what does a TriggerTemplate create when triggered by an event?

[ ]Interceptor

[ ]EventListener

[ ]Container

[X]PipelineRun

Correct. When triggered by an event, a TriggerTemplate creates a PipelineRun, passing along any parameters from the triggered event, or persistent storage, that the pipeline might need.

1 / 1 point

### 2.

Question 2

Which field must you include in every Tekton manifest?

[ ]volumes

[X]apiVersion

Correct. Every Tekton manifest must define an API version to use, such as tekton.dev/v1beta1.

[ ]finally

[ ]results

1 / 1 point

### 3.

Question 3

What syntax must you use in a TriggerTemplate’s resourceTemplates section to reference a value from the TriggerTemplate’s params section?

[ ]$(params.`<name>`.tt)

[ ]$(params.`<name>`)

[ ]$(`<name>`.params.)

[X]$(tt.params.`<name>`)

Correct. In a TriggerTemplate’s resourceTemplates section, you must use the '$(tt.params.`<name>`)' syntax to reference a value from the TriggerTemplate’s params section.

1 / 1 point

### 4.

Question 4

Which command can you use to install tasks from the Tekton Catalog?

[ ]kubectl create job

[X]tkn hub install

Correct. You can use the 'tkn hub install task' command followed by the task’s name to install a task from the Tekton Catalog.

[ ]kubectl get services

[ ]tkn hub get

1 / 1 point

### 5.

Question 5

How can you ensure that a Tekton task called task-x runs after two parallel tasks in the pipeline?

[ ]Specify task-x in the from fields of both parallel tasks.

[X]Specify the parallel tasks in the runAfter field of task-x.

Correct. To run a task after parallel tasks, you must specify all the parallel tasks in the runAfter field of that task.

[ ]Specify the parallel tasks in the retries field of task-x.

[ ]Specify task-x in the runAfter fields of both parallel tasks.

1 / 1 point

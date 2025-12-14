### 1.

Question 1

What does the following CRUD operation in Python do?

customers.insert_many(customers_list)

[ ]Allows you to insert a customer from your ‘customers_list’ in the database

[ ]Allows you to insert the column ‘customers_list’ in the database.

[X]Allows you to do a bulk insert of customers listed in the ‘customers_list’

Correct! The insert.many function allows you to do bulk inserts in the database.

[ ]Updates the customer list with customer information in the ‘customers_list’ field

1 / 1 point

### 2.

Question 2

True or False: Replication can save you from disasters, such as accidentally deleting your database.

[X]False

[ ]True

Correct. Replication cannot save you from disasters. For disaster recovery scenarios, you have backup and restore options.

1 point

### 3.

Question 3

Aggregation Framework is a series of operations that you apply on your data to get a desired outcome. What outcome does the operation “$merge” produce?

[ ]Projects out certain fields from the document

[ ]Counts and assigns an outcome to a specified field

[ ]Filters out documents based on specified value

[X]Takes the outcome from the previous stage and stores it in a target collection

Correct! “$merge” takes the outcome from the previous stage and stores it in a target collection.

1 / 1 point

### 4.

Question 4

MongoDB uses compound indexing. Which one of the following is a distinguishing characteristic of a compound index?

[X]When a single index structure holds reference to more than one field, that is referred to as a compound index.

Correct! MongoDB stores data being indexed on the index entry and a location of the document on disk.

[ ]When the index is stored in a particular order, it is known as a compound index.

[ ]When you create an index for the most frequent queries, that is known as compound indexing.

[ ]When an index helps you to quickly locate data without looking for it everywhere, that is called a compound index.

1 / 1 point

### 5.

Question 5

True or False: The read operation db.students.findOne({"firstName": Lisa"}) will read all documents in the database in which the student’s first name is Lisa.

[X]False

Correct! This read operation will read only the first document, which matches the criteria since we’re using the ‘findOne’ function.

[ ]True

1 / 1 point

### 1.

Question 1

How do you specify a change set to update the song object in the HTTP PUT "/song/[int:id](int:id)" using the update_one () method?

[X]{"$set": song_in}

[ ]{"$new_set": song_in}

[ ]{"$change_set": song_in}

[ ]{"$new_set": [song_in]}

Correct

Correct! This is the correct syntax for updating an existing document in MongoDB using the update_one() method.

1 / 1 point

### 2.

Question 2

How do you test the **count **endpoint for the **songs** microservice?

[ ]wget -X GET -i -w '\n' localhost:5000/count

[ ]curl -X GET -i -w '\n' localhost:5000/health

[X]curl -X GET -i -w '\n' localhost:5000/count

[ ]tar -X GET -i -w '\n' localhost:5000/file

Correct

Correct! The curl command is used to test the endpoint of /count.

1 / 1 point

### 3.

Question 3

How do you **GET** all the songs from the collection?

[ ]db.songs.find_all({})

[ ]db.songs.get_all({})

[ ]db.songs.find({“all”})

[X]db.songs.find({})

Correct

Correct! The find method with an empty JSON object as input will return all documents in a collection.

1 / 1 point

### 4.

Question 4

Which HTTP method do you use to create a new song in the MongoDB collection?

[ ]methods=["NONE"]

[ ]methods=["POST,” “PUT”]

[ ]methods=["GET"]

[X]methods=["POST"]

Correct

Correct! The POST method is used to create a new resource.

1 / 1 point

### 5.

Question 5

Which PyMongo method do you use to delete a song from the songs collection with song id as input?

[ ]db.songs.delete_one_by_id(id)

[ ]db.songs.drop_song(id)

[X]db.songs.delete_one(id)

[ ]db.songs.remove_one()

Correct

Correct! The delete_one method inputs the song id and deletes the song from the collection.

1 / 1 point

### 6.

Question 6

How do you switch to database songs in Mongo shell?

[ ]work with songs

[X]use songs

[ ]access songs

[ ]switch songs

Correct

Correct! The use songs command is used to switch to database songs in Mongo shell.

1 / 1 point

### 7.

Question 7

What is the right way to connect to MongoDB using the PyMongo module?

[ ]client = MongoClient.connect('mongodb://mongouser:password')

[ ]client = MongoClient(mongo://%s:%s@127.0.0.1' % ('mongouser', 'password'))

[ ]client = MongoClient.connect(‘mongouser', 'password')

[X]client = MongoClient('mongodb://%s:%s@127.0.0.1' % ('mongouser', 'password'))

Correct

Correct! The MongoClient method requires a string of this specific format with username, password, and the database host to connect to MongoDB using the PyMongo module.

1 / 1 point

### 8.

Question 8

What is the correct way to insert multiple documents in a mongodb collection called “todo” in a database called **tododb**?

[X]client.tododb.todo.insert_many([])

[ ]client.tododb.todo.insert_all([])

[ ]client.tododb.todo.insert_many(data=[])

[ ]client.todo.insert_many([])

Correct

Correct! Insert_many() is a method of the collection object that is used to insert multiple documents into the collection.

1 / 1 point

### 9.

Question 9

What method do you use to convert BSON objects to JSON?

[ ]json_util(list(result))

[X]json_util.dumps(list(result))

[ ]json_util.convert(list(result))

[ ]json.dumps(list(result))

Correct

Correct! The json_util.dumps() method is used to serialize MongoDB documents that are returned by PyMongo methods so that they can be stored or transmitted as text.

1 / 1 point

### 10.

Question 10

How will you find a todo with a low priority in the todo collection inside a tododb database using PyMongo client?

[ ]client.tododb.todo.search(priority="low")

[ ]client.tododb.todo.find(“low")

[X]client.tododb.todo.find({"priority": "low"})

[ ]client.tododb.todo.find(priority="low")

Correct

Correct! You can find a todo with a low priority in the 'todo' collection inside a 'tododb' database using PyMongo.

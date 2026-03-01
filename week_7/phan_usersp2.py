"""
Christopher Phan
Date: 3/1/26
Assignment: Hands-On 5.2: Python with MongoDB, Part 2
"""
# Import the MongoClient
from pymongo import MongoClient
from datetime import datetime, UTC

# Build a connection string to connect to
client = MongoClient("mongodb+srv://web335_user:s3cret@cluster0.lujih.mongodb.net/web335DBretryWrites=true&w=majority")

# Configure a variable to access web335DB
db = client['web335DB']

# Create a new user document
franz = {
    'firstName': 'Franz',
    'lastName': 'Liszt',
    'employeeId': '2525',
    'email': 'fliszt@me.com',
    'dateCreated': datetime.now(UTC),
}

#Insert the document
franz_user_id = db.users.insert_one(franz).inserted_id
print(franz_user_id)

#Prove that the insert succeeded
print(db.users.find_one({'employeeId': '2525'}))

#Update the email of the new user
db.users.update_one({'employeeId': '2525'}, {'$set': {'email': 'Liszt@me.com'}})

#Prove that the email was updated
print(db.users.find_one({'employeeId': '2525'}))

#Delete the new user
db.users.delete_one({'employeeId': '2525'})

#Prove that it was deleted
print(db.users.find_one({'employeeId': '2525'}))
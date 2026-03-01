# Import the MongoClient
from pymongo import MongoClient
from datetime import datetime, UTC

# Build a connection string to connect to
client = MongoClient("mongodb+srv://web335_user:s3cret@cluster0.lujih.mongodb.net/web335DBretryWrites=true&w=majority")

# Configure a variable to access web335DB
db = client['web335DB']

db.users.delete_one({'employeeId': '2525'})

print(db.users.find_one({'employeeId': '2525'}))
"""
Christopher Phan
Date: 2/22/26
Assignment: Hands-On 4.2: Python with MongoDB, Part 1
"""

from pymongo import MongoClient

client = MongoClient("mongodb+srv://web335_user:s3cret@cluster0.lujih.mongodb.net/web335DBretryWrites=true&w=majority")

print(client)

import datetime

db = client['web335DB']
for user in db.users.find({}, {"_id": 0, "firstName": 1, "lastName": 1}):
    print(user)

print(db.users.find_one({"employeeId": "1007"}, {"_id": 0, "firstName": 1, "lastName": 1, "employeeId": 1}))

print(db.users.find_one({"lastName": "Mozart"}, {"_id": 0, "firstName": 1, "lastName": 1}))
/*
Christopher Phan
Date: 2/22/26
Assignment: Solutions for Assignment 6.2 Aggregate Queries
*/

/*
Query 1: Display all students
*/

Db.students.find();

/*
Query 2: Add a new student + find() to prove student was added
*/

db.students.insertOne({firstName: 'Ron', lastName: 'Weasley', studentId: 's1019', houseId: 'h1007', dateCreated: new Date()});
db.students.find({firstName: 'Ron'});

/*
Query 3: Update one of the properties of the added student + find() to prove property was updated
*/

db.students.updateOne({firstName: 'Ron'}, {$set: {houseId: '1009'}});
db.students.find({firstName: 'Ron'});

/*
Query 4: Delete the added student + find() to prove that student no longer exists in the file
*/

db.students.deleteOne({firstName: 'Ron'});
db.students.find({firstName: 'Ron'});

/*
Query 5: Display all students by house
*/

db.houses.aggregate([{$lookup: {from: 'students', localField: 'houseId', foreignField: 'houseId', as: 'Houses_docs'}}, {$project: {mascot: 1, founder: 1, 'Houses_docs.firstName': 1, 'Houses_docs.lastName': 1}}]);

/*
Query 6: Display all students in house Gryffindor
*/

db.houses.aggregate([{$match: {founder: 'Godric Gryffindor'}}, {$lookup: {from: 'students', localField: 'houseId', foreignField: 'houseId', as: 'Houses_docs'}}, {$project: {mascot: 1, founder: 1, 'Houses_docs.firstName': 1, 'Houses_docs.lastName': 1}}]);

/*
Query 7: Display all students in the house with an eagle mascot
*/

db.houses.aggregate([{$match: {mascot: 'Eagle'}}, {$lookup: {from: 'students', localField: 'houseId', foreignField: 'houseId', as: 'Houses_docs'}}, {$project: {mascot: 1, founder: 1, 'Houses_docs.firstName': 1, 'Houses_docs.lastName': 1}}]);
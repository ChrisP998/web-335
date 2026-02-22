/*
Christopher Phan
Date: 2/21/26
Query solutions
*/

/*
Query 1: Add a new user to the collection
*/

Db.users.insertOne({firstName: 'Franz', lastName: 'Liszt', employeeId: '1013', email: 'fliszt@me.com', dateCreated: newDate()});

/*
Query 2: Update Mozart's email to mozart@m1.com
*/

Db.users.updateOne({employeeId: '1009'}, {$set: {email: 'mozart@me.com'}});

/*
Query 3: Display the whole collection showing only the first name, last name, and email
*/

Db.users.find({}, {_id: 0, firstName: 1, lastName: 1, email: 1});
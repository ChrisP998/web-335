/*
Query list for assignment 4.3 MongoDBShell
*/

/*
Query 1: Display all users in collection
*/

Db.users.find();

/*
Query 2: Display user with email jbach@me.com
*/

Db.users.findOne({email: 'jbach@me.com'});

/*
Query 3: Display users with last name Mozart
*/

Db.users.findOne({lastName: 'Mozart'});

/*
Query 4: Display users with first name Richard
*/

Db.users.findOne({firstName: 'Richard'});

/*
Query 5: Display user with employee id 1010
*/

Db.users.findOne({employeeId: '1010'});
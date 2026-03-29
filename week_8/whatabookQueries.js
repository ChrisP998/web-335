/*
Query 1: Write a query to display a list of books
*/

db.books.find();

/*
Query 2: Write a query to display a list of books by genre.
*/

db.books.find({genre: 'Fantasy'});

/*
Query 3: Write a query to display a list of books by author.
*/

db.books.find({author: 'Michael Crichton'});

/*
Query 4: Write a query to display a book by bookId.
*/

db.books.find({bookId: 'b1005'});
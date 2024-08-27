MyBooks: Book Management Application
Description
MyBooks is a terminal-based book management application that helps users manage their personal book collection. Users can create a "To Be Read" (TBR) list, track books they have read, mark books as favorites, and get book suggestions based on the favorite books of other users.

The application uses SQLite as the database and Peewee as the ORM for managing the data. You can add, view, and manage books and users, all within the terminal.

Features
User Management: Add users to the system.
To-Be-Read (TBR) List: Keep track of books you plan to read.
Bookshelf: View the list of books you have read, with ratings and the year you completed them.
Favorites: Mark books as your favorites and manage them.
Suggestions: View book suggestions based on favorite books from other users.
Table of Contents
Installation
Usage
File Structure
Commands
Contributing
License
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/mybooks.git
cd mybooks
Install dependencies: This project requires Python and the Peewee ORM.

You can install the required dependencies by running:
bash
Copy code
pip install peewee tabulate
Initialize the database:

The project uses SQLite, so no further configuration is required. The database my_books.db will be created automatically if it doesn't already exist.
Run the application:

bash
Copy code
python main.py
Usage
Once you start the application, you can begin by adding users and managing their book lists. The interface provides options to view and manage your TBR list, bookshelf, favorites, and get suggestions.

Main Menu Options
A: Add a new user.
E: Exit the application.
Once a user is selected, you can:

View and manage your TBR list.
View your bookshelf (books you've read).
Manage your favorites list.
Get book suggestions from the favorites of other users.
Book Operations
Add a book: Enter the book's name, author, and genre.
Mark a book as read: Input the year of completion and give it a rating.
Favorite a book: Optionally mark a book as your favorite after reading it.
Manage favorites: Remove books from your favorites list.
File Structure
bash
Copy code
mybooks/
├── app.py          # Application logic
├── main.py         # Entry point to run the app
├── models.py       # Database models and setup
├── my_books.db     # SQLite database file
└── README.md       # Documentation (this file)
app.py: Contains the logic for user interaction and database operations such as adding books, marking them as read, and handling TBR lists and favorites.
main.py: The entry point to run the app, displaying the menu and handling user input.
models.py: Defines the data models using Peewee ORM.
my_books.db: The SQLite database that stores user and book information.
Commands
Within the app, you will be able to:

List users: See all users in the system.
Add user: Add a new user to the database.
Manage TBR: Add books to your TBR and mark them as read.
See bookshelf: View books you've already read.
Favorite management: Add or remove books from your favorites list.
Book suggestions: See book suggestions based on the favorites of other users.

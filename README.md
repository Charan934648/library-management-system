# library-management-system
# Library Management System

## Overview
The Library Management System is a Python-based application designed to manage books in a library. It allows users to add, remove, search for books, manage user accounts, and issue/return books. The project also includes a graphical user interface (GUI) built using Tkinter.

## Features
- Add, remove, and search for books
- Add and manage user accounts
- Issue and return books
- Search for books by title
- Simple and user-friendly GUI

## Project Structure

library-management-system/
│
├── library.db                # SQLite database file
├── database.py               # Script to create database tables
├── library.py                # Core functions for library management
├── app.py                    # Tkinter GUI application
├── README.md                 # Project documentation
└── requirements.txt          # Project dependencies


## Getting Started

### Prerequisites
- Python 3.x
- Tkinter (usually comes with Python)

### Installation

1. *Clone the repository*:
   sh
   git clone https://github.com/your-username/library-management-system.git
   cd library-management-system
   

2. *Set up a virtual environment*:
   sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   

3. *Install required packages*:
   sh
   pip install -r requirements.txt
   

4. *Create the database tables*:
   sh
   python database.py
   

### Running the Application

Run the GUI application:
sh
python app.py

This will start the Tkinter-based GUI for the Library Management System.

## Core Functions

### Add Book
Adds a book to the library.
python
add_book(title, author)


### Remove Book
Removes a book from the library by its ID.
python
remove_book(book_id)


### Search Book
Searches for books by title.
python
search_book(title)


### Add User
Adds a new user to the library system.
python
add_user(name)


### Issue Book
Issues a book to a user.
python
issue_book(book_id, user_id)


### Return Book
Returns a book from a user.
python
return_book(book_id, user_id)


## GUI Components

### Add Book Frame
Allows users to add a new book by entering the title and author.

### Add User Frame
Allows users to add a new user by entering the user's name.

### Issue Book Frame
Allows users to issue a book to a user by entering the book ID and user ID.

### Return Book Frame
Allows users to return a book by entering the book ID and user ID.

### Search Book Frame
Allows users to search for books by entering the title. Displays the search results.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or suggestions, please open an issue or contact the project maintainer.

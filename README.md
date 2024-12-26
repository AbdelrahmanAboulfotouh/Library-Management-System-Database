# Library Management System

## Project Description

The Library Management System is designed to manage book inventories, member registrations, borrowing and returning of books, and overdue fines. It includes a graphical user interface (GUI) for easy interaction and a robust database for secure and efficient data management.

---

## Features

- **Book Management:** Add, view, and update book records including title, author, genre, ISBN, publication year, and availability.
- **Member Management:** Register and maintain member details such as full name, email, phone number, and address.
- **Borrowing and Returning:** Track borrowing and returning activities with automatic updates to book availability.
- **Fine Management:** Calculate and track overdue fines, with records of payment status.

---

## Project Structure

### 1. Database
The database manages all data related to books, members, borrowing, and fines. It uses the following schema:

- **Books Table:** Stores book information and availability.
- **Members Table:** Stores member details and registration information.
- **Borrowing Table:** Tracks book borrow and return dates.
- **Fines Table:** Records overdue fines and payment status.

#### Triggers:
- **`AfterBorrow`:** Decrements the available copies of a book after it is borrowed.
- **`AfterReturn`:** Increments the available copies of a book when it is returned.

### 2. GUI Application
The GUI is built with Python's `tkinter` module and provides an intuitive interface for library operations.

#### Main Components:
- **Book Management Frame:** Allows adding new books and viewing the current list of books.
- **Book List View:** Displays all books in a tabular format using a `Treeview` widget.
- **Interactivity:** Includes error handling and notifications for database operations.

---

## Technologies Used

- **Programming Language:** Python (GUI)
- **Database:** MySQL
- **GUI Library:** `tkinter`
- **Database Connector:** `mysql-connector-python`

---
## Future Enhancements

- Add member and fine management features in the GUI.
- Implement borrowing and returning workflows with due date notifications.
- Enhance user experience with advanced search and sorting options.
- Add support for user authentication.

## Getting Started

### Prerequisites

1. Install Python 3.x and ensure `pip` is available.
2. Install MySQL and create the database schema using the provided SQL script.
3. Install the required Python library:
   ```bash
   pip install mysql-connector-python

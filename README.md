Airbnb Clone Project
This project aims to create a simplified version of the popular Airbnb platform. It allows users to list and book accommodations, manage reservations, and explore available properties.

Description
The Airbnb clone is a web application built using Python and Flask. It provides a user-friendly interface for property owners to list their spaces and for travelers to find suitable accommodations. The project includes features such as user authentication, property search, booking management, and reviews.

Command Interpreter
The command interpreter is a crucial part of the project. It allows users to interact with the application via the command line. Here’s how to use it:

Starting the Command Interpreter:
Run the following command in your terminal:
./console.py

This will launch the interactive command-line interface.
Using the Command Interpreter:
The command interpreter supports various commands, including:
create: Create a new object (e.g., user, property).
show: Display details of a specific object.
update: Modify object attributes.
all: List all available objects.
destroy: Delete an object.
Example usage:
(hbnb) create User email="john@example.com" password="secret"
(hbnb) show User 12345
(hbnb) update Property 9876 name="Cozy Cabin" price=100

Examples:
To create a new user:
(hbnb) create User email="alice@example.com" password="secure123"

To list all available properties:
(hbnb) all Property

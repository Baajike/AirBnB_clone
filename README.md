# AirBnB Clone - Command Interpreter

## Description

This project is an implementation of a command-line interpreter for managing AirBnB objects. The command interpreter allows users to create, retrieve, update, and delete various objects related to AirBnB, such as Users, States, Cities, and Places.

## Command Interpreter

### How to Start

To start the command interpreter, run the `console.py` script.

$ ./console.py

How to Use
The command interpreter provides a set of commands for interacting with AirBnB objects. Here are some examples:

Creating a new object:

(hbnb) create User

Retrieving objects:

(hbnb) show User 1234-5678

Updating attributes of an object:

(hbnb) update Place 8765-4321 name "New Place Name"

Destroying an object:

(hbnb) destroy State 9876-5432

Exiting the interpreter:

(hbnb) quit

Examples
Here are some examples of using the command interpreter:

$ ./console.py
(hbnb) create State name="California"
(hbnb) show State
(hbnb) all
(hbnb) update State 1234-5678 name "New California"
(hbnb) destroy State 1234-5678
(hbnb) quit

Authors
Immanuella Adwoa Baajike

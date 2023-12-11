# Bus Reservation System Documentation
This documentation is for a bus reservation system that includes both server-side and client-side code.

# System Overview
This system allows users to book bus seats online.

# Server-side:
  The server listens for client connections on port 8888.
  Handles client requests for displaying the seat matrix, booking seats, and generating tickets.
  Uses threading to handle multiple clients concurrently.
  Uses a mutex to ensure thread-safe access to the shared seat matrix.
  Simulates a payment process by generating a random transaction ID.

  Socket Programming: The server utilizes Python's socket library to establish network connections and communicate with        clients. This leverages the operating system's networking capabilities to facilitate communication across the network.

  Threading: The threading library allows the server to handle multiple client requests concurrently. This utilizes the        operating system's ability to manage multiple threads of execution, improving responsiveness and scalability.

  Mutex: A threading.Semaphore object is used as a mutex to ensure thread-safe access to the shared seat matrix. This          prevents race conditions and ensures data consistency when multiple clients attempt to access the same resource           
  simultaneously.

  File I/O: The server stores user credentials and booking information in text files. This leverages the operating system's    file system capabilities for persistent data storage.

# Client-side:
  The client connects to the server on port 8888.
  Allows users to register, login, and perform various actions such as displaying the seat matrix, booking seats, and making   payments.
  Simulates a payment process by sending a "dummy_payment" message to the server.
  Displays the ticket details or payment failure message.

  Socket Programming: Similar to the server, the client uses the socket library to connect to the server and exchange          messages. This relies on the operating system's networking functionalities to establish and maintain the connection.

  User Management: The client utilizes file I/O to store user credentials locally. This leverages the operating system's       file system capabilities for user data persistence.

  Process Management: The client employs the operating system's process management features to run the program and interact    with the system resources.

# System Components

Server-side
  Main Function:
    Initializes the server socket and listens for client connections.
    Creates a new thread for each client connection.
  Client Handling Thread:
    Receives and processes client requests.
    Handles display, book, dummy_payment, and exit actions.
    Uses a mutex to ensure thread-safe access to the shared seat matrix.
  Display Seat Matrix Function:
    Generates a string representation of the seat matrix.
  Book Seat Function:
    Verifies the seat number and checks availability.
    Updates the seat matrix and generates a transaction ID.
    Stores the booking information in a user session.
  Dummy Payment and Generate Ticket Function:
    Simulates a payment process and generates a ticket.
    Checks if a user session exists and retrieves booking information.
    Sends the ticket details to the client.
    
Client-side
  Main Function:
    Connects to the server and establishes a communication channel.
    Provides a menu for user interaction.
    Handles user input and sends messages to the server.
    Receives and displays server responses.
  User Registration Function:
    Allows users to register with a username and password.
    Stores the user credentials in a file.
  User Login Function:
    Verifies user credentials against stored data.
    Allows access to booking functionality upon successful login.
  Dummy Payment Function:
    Sends a "dummy_payment" message to the server.
    Displays the ticket details or payment failure message received from the server.
    
# System Dependencies
  Python 3.x
  socket
  threading
  hashlib
  random

#Deployment
This code can be deployed on any server that supports Python 3.x and has the required libraries installed.

# Usage
  Start the server-side code.
  Run the client-side code.
  Choose an option from the client menu to proceed.

Additional Resources
Python socket documentation: https://docs.python.org/3/library/socket.html
Threading documentation: https://docs.python.org/3/library/threading.html
hashlib documentation: https://docs.python.org/3/library/hashlib.html

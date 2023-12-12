# BookBus Reservation System Documentation

## Server-Side Code

### Constants and Initialization
- `NUM_SEATS = 40`: Defines the total number of bus seats.
- `seat_matrix`: A list representing the availability status of each seat. Initialized to all seats being available.

### Semaphore
- `seat_mutex = threading.Semaphore(1)`: A semaphore to control access to the seat_matrix, preventing race conditions during concurrent updates.

### Displaying Seat Matrix
- `display_seat_matrix()`: Function to generate a formatted display of the current seat matrix. Each seat is represented by a unique identifier.

### Generating Tickets
- `generate_ticket(price, seat_number)`: Function to generate a ticket with a random serial number for a given seat and price. The ticket includes a congratulatory message and relevant details.

### Handling Client Communication
- `handle_client(client_socket)`: Function to manage communication with a client.
  - Calculates dynamic pricing based on the number of active clients.
  - Receives and responds to client actions (display, book, exit).
  - Controls seat booking, generates tickets, and sends responses.
  - Runs in a loop until the client chooses to exit.

### Main Server Function
- `main()`: Function to set up the server socket, listen for client connections, and handle each client in a separate thread.
  - Accepts client connections and starts a new thread for each client.
  - Monitors the server continuously for incoming connections.

## Client-Side Code

### User Registration and Login
- `register_user()`: Function to register a new user by entering a username and password. Passwords are hashed for security.
- `login_user()`: Function to authenticate and login a user by entering a username and password. Passwords are hashed for comparison.

### Main Client Function
- `main()`: 
  - Connects to the server using the server's IP address and port number.
  - Displays a menu for user registration, login, or exit.
  - Calls functions for user registration and login based on user input.
  - Establishes a connection to the server for seat booking.
  - Sends user actions (display, book, exit) to the server.
  - Receives and displays server responses, including seat prices and booking confirmations.
  - Closes the client socket when done.

**Note:** Replace `<common_network's_IP_address>` with the actual IP address for proper communication between the client and server.

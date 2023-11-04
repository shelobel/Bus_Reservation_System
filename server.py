import socket
import threading


NUM_SEATS = 10

seat_matrix = [True] * NUM_SEATS


seat_mutex = threading.Semaphore(1)

def display_seat_matrix():
    matrix = "Seat Matrix:\n"
    for i, seat in enumerate(seat_matrix, start=1):
        status = "Available" if seat else "Booked"
        matrix += f"Seat {i}: {status}\n"
    return matrix

def handle_client(client_socket):
    while True:
        action = client_socket.recv(1024).decode()

        if action == "display":
            response = display_seat_matrix()
            client_socket.send(response.encode())
        elif action.startswith("book"):
            try:
                seat_choice = int(action.split(" ")[1])
            except ValueError:
                client_socket.send(b"Invalid input. Please enter a valid seat number.")
                continue

            if seat_choice < 1 or seat_choice > NUM_SEATS:
                client_socket.send(f"Invalid seat number. Please choose a seat between 1 and {NUM_SEATS}.".encode())
                continue

            seat_mutex.acquire()

            if seat_matrix[seat_choice - 1]:
                seat_matrix[seat_choice - 1] = False
                client_socket.send(f"\n\nSeat {seat_choice} booked successfully.\n\n".encode())
                seat_mutex.release()
            else:
                client_socket.send(f"\n\nSeat {seat_choice} is already booked. Please choose another seat.\n\n".encode())
                seat_mutex.release()
        elif action == "exit":
            client_socket.send(b"        ***** THANK YOU FOR AVAILING OUR SERVICE. PLEASE PROVIDE YOUR VALUABLE FEEDBACK FOR BOOKBUS! ***** ")
            break
        else:
            client_socket.send(b"\n\nInvalid action. Please choose 'display', 'book <seat_number>', or 'exit'.\n\n")

    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 8888))
    server.listen(5)
    print("[*] Server listening on 0.0.0.0:8888")
    
    
    while True:
        client, addr = server.accept()
        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client,))
        
        client_handler.start()

if __name__ == "__main__":
    main()

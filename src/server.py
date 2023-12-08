import socket
import threading
import random


NUM_SEATS = 40
seat_matrix = [True] * NUM_SEATS


seat_mutex = threading.Semaphore(1)

def display_seat_matrix():
    matrix = "\nSeat Matrix:\n\n"
    matrix += "| D  |\n"
    matrix+="\n"
    for i, seat in enumerate(seat_matrix, start=1):
        if i/10 < 1 and seat:
            status = f" 0{i} "
        elif i/10 > 0 and seat:
            status = f" {i} "
        else:
            status = " X  "
        # status = f" 0{i} " if seat and if i%10 === 0 else " X "
        matrix += f"|{status}|"
        if((i+2)%4)==0:
            matrix+=" "
        if i%4==0:
            matrix+="\n"
    return matrix

   
def generate_ticket(price,seat_number):
    serial_number = random.randint(1000, 9999)
    ticket = "Congratulations! Your transaction was successful. Your ticket has been generated. You may print it for future reference\n\n"
    ticket += f"+------------------+\n|    BUS TICKET    |\n+------------------+\n| Serial Number:   |\n|                  |\n|       {serial_number}       |\n|                  |\n| Seat Number:     |\n|                  |\n|       {seat_number}         |\n|                  |\n| Price: ₹         |\n|                  |\n|      {price:.2f}      |\n+------------------+"
    return ticket


def handle_client(client_socket):
    while True:
        num_client = threading.activeCount() - 1
        price_int = (num_client*0.05*200 + 200) if num_client > 2 else 200
        action = client_socket.recv(1024).decode()
        price = str(price_int)
        client_socket.send(price.encode())

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
                ticket = generate_ticket(price_int,seat_choice)
                client_socket.send(ticket.encode())
                seat_mutex.release()
            else:
                client_socket.send(f"\n\nSeat {seat_choice} is already booked. Please choose another seat.\n\n".encode())
                seat_mutex.release()
        elif action == "exit":
            client_socket.send(b"\n\n        ***** THANK YOU FOR AVAILING OUR SERVICE. PLEASE PROVIDE YOUR VALUABLE FEEDBACK FOR BOOKBUS! ***** ")
            break
        else:
            client_socket.send(b"\n\nInvalid action. Please choose 'display', 'book <seat_number>', or 'exit'.\n\n")

    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("<common_network's_IP_address>", 8888))
   # server.bind(("0.0.0.0", 8888))
    server.listen(5)
    print("[*] Server listening on <common_network's_IP_address>:8888")
    
    
    while True:
        client, addr = server.accept()
        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client,))
        
        client_handler.start()

if __name__ == "__main__":
    main()

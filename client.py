import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 8888))

    while True:
        action = input("Choose action ('display', 'book <seat_number>', 'exit'): ")
        client.send(action.encode())

        response = client.recv(1024).decode()
        print(response)

        if "booked successfully" in response:
            continue
        elif action == "exit":
            break

    client.close()

if __name__ == "__main__":
    main()


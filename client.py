import socket
import hashlib

def register_user():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    with open("users.txt", "a") as file:
        file.write(f"{username}:{hashed_password}\n")
    print("Registration successful. You can now login.")

def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    with open("users.txt", "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(":")
            if username == stored_username and hashed_password == stored_password:
                return True
    return False

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 8888))

    while True:
        print("Choose an option:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            if login_user():
                print("Login successful.")
                break
            else:
                print("Invalid username or password. Please try again.")
        elif choice == "3":
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

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

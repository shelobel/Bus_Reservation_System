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
        print("\n                 ****** WELCOME TO BOOKBUS ****** \n")
        print("Choose an option:")
        print("\n\n1. Register")
        print("\n\n2. Login")
        print("\n\n3. Exit")
        choice = input("\n\nEnter your choice: ")

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
        action = input("\n                 ****** WELCOME TO BOOKBUS ****** \n 1) Type \"display\" if you would like to display the seat matrix \n\n 2) Type \"book <seat_number>\" to book your desired seat \n\n 3) Type \"exit\" to exit from terminal\n")
        client.send(action.encode())
        
        price = client.recv(1024).decode()
       
        
        response = client.recv(1024).decode()
        print(response)
        print(f"\n\nPrice of a seat is: Rs {price}\n\n")
        if "booked successfully" in response:
            continue
        elif action == "exit":
            break

    client.close()

if __name__ == "__main__":
    main()
